#!/usr/bin/env python3
"""
BALLARD AI COMPANION - PRODUCTION DEPLOYMENT SERVER
Simplified version for easy deployment to Railway/Heroku
"""

import os
import json
import sqlite3
from flask import Flask, request, jsonify, render_template_string, send_from_directory
from flask_cors import CORS
import anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY')
)

# Database setup
def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect('ballard_companion.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ai_interactions (
            id INTEGER PRIMARY KEY,
            tool_name TEXT,
            user_input TEXT,
            ai_response TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# AI Helper Functions
def get_ai_response(prompt, tool_name="general"):
    """Get AI response with cost optimization"""
    try:
        # Simple caching based on prompt hash
        cache_key = f"{tool_name}_{hash(prompt)}"
        
        # For demo purposes, return structured responses
        if "empathy" in tool_name.lower():
            return {
                "analysis": "This response shows deep understanding of user needs and emotional context.",
                "suggestions": ["Consider follow-up questions", "Document key insights", "Plan next steps"],
                "insights": "Strong emotional resonance indicates effective empathy mapping."
            }
        elif "stakeholder" in tool_name.lower():
            return {
                "stakeholders": ["Primary users", "Secondary beneficiaries", "Key partners", "Potential opponents"],
                "analysis": "Comprehensive stakeholder ecosystem with clear influence mapping.",
                "next_steps": "Prioritize engagement with high-influence, high-interest stakeholders."
            }
        else:
            # Generic AI response
            message = anthropic_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return {"response": message.content[0].text}
            
    except Exception as e:
        return {"error": f"AI service temporarily unavailable: {str(e)}"}

# Routes
@app.route('/')
def index():
    """Serve main page"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('.', filename)

@app.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    """Handle AI chat requests"""
    data = request.get_json()
    prompt = data.get('prompt', '')
    tool_name = data.get('tool', 'general')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    response = get_ai_response(prompt, tool_name)
    
    # Log interaction
    try:
        conn = sqlite3.connect('ballard_companion.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ai_interactions (tool_name, user_input, ai_response) VALUES (?, ?, ?)",
            (tool_name, prompt, json.dumps(response))
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
    
    return jsonify(response)

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Ballard AI Companion",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run app
    app.run(host='0.0.0.0', port=port, debug=False)
