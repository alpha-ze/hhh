#!/bin/bash

echo "🚀 Vercel Deployment Script - Kerala Schemes"
echo "============================================"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - Kerala Schemes"
    echo "✅ Git initialized"
    echo ""
    echo "⚠️  Next steps:"
    echo "1. Create a repository on GitHub"
    echo "2. Run: git remote add origin YOUR_GITHUB_URL"
    echo "3. Run: git push -u origin main"
    echo "4. Then run this script again"
    exit 0
fi

echo "✅ Git repository found"
echo ""

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm i -g vercel
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Vercel CLI"
        echo "Please install Node.js first: https://nodejs.org"
        exit 1
    fi
fi

echo "✅ Vercel CLI found"
echo ""

echo "Choose deployment option:"
echo "1. Deploy to Vercel (Production)"
echo "2. Deploy Preview"
echo "3. Run Local Development Server"
echo "4. View Deployment Logs"
echo "5. Open Vercel Dashboard"
echo ""
read -p "Enter option (1-5): " option

case $option in
    1)
        echo ""
        echo "🚀 Deploying to Vercel Production..."
        vercel --prod
        echo ""
        echo "✅ Deployment complete!"
        echo "📱 Your app is live!"
        echo ""
        echo "Test your deployment:"
        echo "- Frontend: Check the URL provided above"
        echo "- API: https://your-url.vercel.app/api"
        echo "- Agent: https://your-url.vercel.app/agent"
        ;;
    2)
        echo ""
        echo "🚀 Deploying Preview..."
        vercel
        echo ""
        echo "✅ Preview deployment complete!"
        ;;
    3)
        echo ""
        echo "🔧 Starting local development server..."
        echo "This simulates Vercel environment locally"
        echo ""
        vercel dev
        ;;
    4)
        echo ""
        echo "📊 Fetching deployment logs..."
        vercel logs
        ;;
    5)
        echo ""
        echo "🌐 Opening Vercel Dashboard..."
        if command -v xdg-open &> /dev/null; then
            xdg-open https://vercel.com/dashboard
        elif command -v open &> /dev/null; then
            open https://vercel.com/dashboard
        else
            echo "Please visit: https://vercel.com/dashboard"
        fi
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac

echo ""
echo "📖 For detailed instructions, see VERCEL_DEPLOYMENT.md"
