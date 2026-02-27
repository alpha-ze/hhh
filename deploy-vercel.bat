@echo off
echo 🚀 Vercel Deployment Script - Kerala Schemes
echo ============================================
echo.

REM Check if git is initialized
if not exist .git (
    echo 📦 Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit - Kerala Schemes"
    echo ✅ Git initialized
    echo.
    echo ⚠️  Next steps:
    echo 1. Create a repository on GitHub
    echo 2. Run: git remote add origin YOUR_GITHUB_URL
    echo 3. Run: git push -u origin main
    echo 4. Then run this script again
    pause
    exit /b 0
)

echo ✅ Git repository found
echo.

REM Check if Vercel CLI is installed
where vercel >nul 2>nul
if errorlevel 1 (
    echo 📦 Installing Vercel CLI...
    npm i -g vercel
    if errorlevel 1 (
        echo ❌ Failed to install Vercel CLI
        echo Please install Node.js first: https://nodejs.org
        pause
        exit /b 1
    )
)

echo ✅ Vercel CLI found
echo.

echo Choose deployment option:
echo 1. Deploy to Vercel (Production)
echo 2. Deploy Preview
echo 3. Run Local Development Server
echo 4. View Deployment Logs
echo 5. Open Vercel Dashboard
echo.
set /p option="Enter option (1-5): "

if "%option%"=="1" (
    echo.
    echo 🚀 Deploying to Vercel Production...
    vercel --prod
    echo.
    echo ✅ Deployment complete!
    echo 📱 Your app is live!
    echo.
    echo Test your deployment:
    echo - Frontend: Check the URL provided above
    echo - API: https://your-url.vercel.app/api
    echo - Agent: https://your-url.vercel.app/agent
) else if "%option%"=="2" (
    echo.
    echo 🚀 Deploying Preview...
    vercel
    echo.
    echo ✅ Preview deployment complete!
) else if "%option%"=="3" (
    echo.
    echo 🔧 Starting local development server...
    echo This simulates Vercel environment locally
    echo.
    vercel dev
) else if "%option%"=="4" (
    echo.
    echo 📊 Fetching deployment logs...
    vercel logs
) else if "%option%"=="5" (
    echo.
    echo 🌐 Opening Vercel Dashboard...
    start https://vercel.com/dashboard
) else (
    echo ❌ Invalid option
    exit /b 1
)

echo.
echo 📖 For detailed instructions, see VERCEL_DEPLOYMENT.md
pause
