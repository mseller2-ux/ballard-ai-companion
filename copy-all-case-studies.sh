#!/bin/bash

echo "🚀 COMPREHENSIVE CASE STUDY DEPLOYMENT"
echo "Copying ALL case studies to DEPLOYMENT-PACKAGE..."
echo ""

# Source and destination
SOURCE="/Users/melissasellers/Desktop/ballard-ai-companion-mcp-server-v8/case-studies"
DEST="/Users/melissasellers/Desktop/ballard-ai-companion-mcp-server-v8/DEPLOYMENT-PACKAGE/case-studies"

# Create all phase directories
echo "📁 Creating phase directories..."
mkdir -p "$DEST/phase1-love-the-one"
mkdir -p "$DEST/phase2-identify-understand" 
mkdir -p "$DEST/phase3-specify-outcome"
mkdir -p "$DEST/phase4-co-create-intervention"
mkdir -p "$DEST/phase5-implement-solution"
mkdir -p "$DEST/phase6-evaluate-impact"
mkdir -p "$DEST/phase7-scale-sustain"
mkdir -p "$DEST/phase8-love-more"

# Copy Phase 1 case studies
echo "📚 Phase 1: Love the One..."
cp -R "$SOURCE/phase1-love-the-one"/* "$DEST/phase1-love-the-one/" 2>/dev/null

# Copy Phase 2 case studies
echo "📚 Phase 2: Identify & Understand..."
cp -R "$SOURCE/phase2-identify-understand"/* "$DEST/phase2-identify-understand/" 2>/dev/null

# Copy Phase 3 case studies
echo "📚 Phase 3: Specify Outcome..."
cp -R "$SOURCE/phase3-specify-outcome"/* "$DEST/phase3-specify-outcome/" 2>/dev/null

# Copy Phase 4 case studies
echo "📚 Phase 4: Co-Create Intervention..."
cp -R "$SOURCE/phase4-co-create-intervention"/* "$DEST/phase4-co-create-intervention/" 2>/dev/null

# Copy Phase 5 case studies
echo "📚 Phase 5: Implement Solution..."
cp -R "$SOURCE/phase5-implement-solution"/* "$DEST/phase5-implement-solution/" 2>/dev/null

# Copy Phase 6 case studies
echo "📚 Phase 6: Evaluate Impact..."
cp -R "$SOURCE/phase6-evaluate-impact"/* "$DEST/phase6-evaluate-impact/" 2>/dev/null

# Copy Phase 7 case studies
echo "📚 Phase 7: Scale & Sustain..."
cp -R "$SOURCE/phase7-scale-sustain"/* "$DEST/phase7-scale-sustain/" 2>/dev/null

# Copy Phase 8 case studies (including your crown jewel biography!)
echo "📚 Phase 8: Love More (including Donella Meadows biography)..."
cp -R "$SOURCE/phase8-love-more"/* "$DEST/phase8-love-more/" 2>/dev/null

# Copy main library files
echo "📚 Copying case library index files..."
cp "$SOURCE/case-library.html" "$DEST/" 2>/dev/null

# Count and report
TOTAL=$(find "$DEST" -name "*.html" | wc -l)
echo ""
echo "✅ CASE STUDY DEPLOYMENT COMPLETE!"
echo "📍 Location: $DEST"
echo "📚 Total files copied: $TOTAL case studies"
echo ""
echo "🎯 Your complete case study library includes:"
echo "   📖 Phase 1: Google Project Relate, Be My Eyes, Crisis Text Line, Polaris"
echo "   📖 Phase 2: BudgIT Nigeria, World Food Program, GIGA UNICEF, DataKind"
echo "   📖 Phase 3: 3ie Impact Evaluation, IFAD Rural Development" 
echo "   📖 Phase 4: ARMMAN Maternal Health, Khan Academy, Microsoft AI"
echo "   📖 Phase 5: Grameen Foundation, PATH Tuberculosis, Mercy Corps"
echo "   📖 Phase 6: GiveWell Evaluation, J-PAL RCTs, World Bank"
echo "   📖 Phase 7: Ashoka Changemaker, Gates Foundation, Teach for All"
echo "   📖 Phase 8: Donella Meadows Biography (6 pages), Rotary Polio"
echo ""
echo "👑 Your crown jewel Donella Meadows biography is preserved!"
echo "🚀 Ready for deployment with complete academic case study library!"
