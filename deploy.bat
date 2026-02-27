@echo off
echo 🚀 Kerala Schemes Deployment Script
echo ====================================
echo.

REM Check if git is initialized
if not exist .git (
    echo 📦 Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit - Kerala Schemes AI Assistant"
    echo ✅ Git initialized
) else (
    echo ✅ Git already initialized
)

echo.
echo Choose deployment option:
echo 1. Deploy to Render (Recommended - Free)
echo 2. Deploy to Heroku
echo 3. Deploy with Docker
echo 4. Deploy to Railway
echo 5. Setup for manual deployment
echo.
set /p option="Enter option (1-5): "

if "%option%"=="1" (
    echo.
    echo 📋 Render Deployment Steps:
    echo 1. Push code to GitHub:
    echo    git remote add origin YOUR_GITHUB_URL
    echo    git push -u origin main
    echo.
    echo 2. Go to https://render.com
    echo 3. Click 'New' → 'Blueprint'
    echo 4. Connect your GitHub repository
    echo 5. Render will auto-deploy using render.yaml
    echo.
    echo 6. After deployment, update these files with your URLs:
    echo    - script.js (line 1^): const API_BASE_URL = 'YOUR_RENDER_API_URL'
    echo    - assistant-simple.html: Update fetch URLs
    echo.
    echo 7. Deploy frontend to Netlify:
    echo    - Go to https://netlify.com
    echo    - Drag and drop frontend files
    echo.
) else if "%option%"=="2" (
    echo.
    echo 📋 Heroku Deployment:
    where heroku >nul 2>nul
    if errorlevel 1 (
        echo ❌ Heroku CLI not found. Install from: https://devcenter.heroku.com/articles/heroku-cli
        exit /b 1
    )
    
    echo Creating Heroku apps...
    heroku create kerala-schemes-api
    heroku create kerala-schemes-agent
    
    echo.
    echo Deploy with:
    echo   git push heroku main
) else if "%option%"=="3" (
    echo.
    echo 🐳 Docker Deployment:
    where docker >nul 2>nul
    if errorlevel 1 (
        echo ❌ Docker not found. Install from: https://docker.com
        exit /b 1
    )
    
    echo Building and starting containers...
    docker-compose up -d
    
    echo.
    echo ✅ Services started!
    echo    - API: http://localhost:8000
    echo    - Agent: http://localhost:8001
    echo    - Frontend: http://localhost:80
) else if "%option%"=="4" (
    echo.
    echo 📋 Railway Deployment:
    where railway >nul 2>nul
    if errorlevel 1 (
        echo Installing Railway CLI...
        npm i -g @railway/cli
    )
    
    echo Initializing Railway...
    railway login
    railway init
    
    echo.
    echo Deploy with:
    echo   railway up
) else if "%option%"=="5" (
    echo.
    echo 📋 Manual Deployment Checklist:
    echo.
    echo ✅ Files created:
    echo    - Dockerfile
    echo    - docker-compose.yml
    echo    - Procfile (Heroku^)
    echo    - render.yaml (Render^)
    echo    - netlify.toml (Netlify^)
    echo    - vercel.json (Vercel^)
    echo.
    echo 📖 Read DEPLOYMENT.md for detailed instructions
) else (
    echo ❌ Invalid option
    exit /b 1
)

echo.
echo ✅ Setup complete!
echo 📖 See DEPLOYMENT.md for detailed instructions
pause
