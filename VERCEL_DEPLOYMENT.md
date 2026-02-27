# Vercel Deployment Guide - Kerala Schemes

## 🚀 Quick Deploy to Vercel (5 minutes)

### Prerequisites
- GitHub account
- Vercel account (free at https://vercel.com)

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Kerala Schemes"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/kerala-schemes.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Vercel

#### Option A: Using Vercel Dashboard (Easiest)

1. Go to https://vercel.com
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration
5. Click "Deploy"
6. Wait 2-3 minutes for deployment
7. Your site is live! 🎉

#### Option B: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? kerala-schemes
# - Directory? ./
# - Override settings? No

# Deploy to production
vercel --prod
```

### Step 3: Test Your Deployment

Your app will be live at: `https://your-project-name.vercel.app`

Test the endpoints:
- Frontend: `https://your-project-name.vercel.app`
- Main API: `https://your-project-name.vercel.app/api`
- Agent API: `https://your-project-name.vercel.app/agent`

## 📁 Project Structure for Vercel

```
kerala-schemes/
├── api/
│   ├── main.py          # Main API (auto-deployed to /api)
│   └── agent.py         # Agent API (auto-deployed to /agent)
├── index.html           # Frontend (root)
├── style.css
├── script.js
├── assistant-simple.html
├── kerala_schemes.json  # Data file
├── requirements.txt     # Python dependencies
└── vercel.json         # Vercel configuration
```

## ⚙️ Configuration Details

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    },
    {
      "src": "agent.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "main.py"
    },
    {
      "src": "/agent/(.*)",
      "dest": "agent.py"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

### API Routes
- `/api` → Main API (eligibility checker)
- `/api/check-eligibility` → POST endpoint
- `/api/roadmap/{scheme_id}` → GET endpoint
- `/agent` → Agent API
- `/agent/analyze-form` → POST endpoint

## 🔧 Environment Variables (Optional)

If you need environment variables:

1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add variables:
   - `ENVIRONMENT=production`
   - `ALLOWED_ORIGINS=https://your-domain.com`

## 🌐 Custom Domain (Optional)

1. Go to Vercel Dashboard → Your Project → Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions
4. SSL certificate is automatically provisioned

## 🔄 Automatic Deployments

Every push to your GitHub repository will automatically deploy:
- Push to `main` branch → Production deployment
- Push to other branches → Preview deployment

## 📊 Monitoring

Vercel provides:
- Real-time logs
- Analytics
- Performance metrics
- Error tracking

Access from: Dashboard → Your Project → Analytics/Logs

## 🐛 Troubleshooting

### Build Fails
- Check `requirements.txt` has all dependencies
- Verify Python version compatibility
- Check Vercel build logs

### API Not Working
- Ensure `api/` folder structure is correct
- Check that `handler = app` is at the end of Python files
- Verify routes in `vercel.json`

### CORS Issues
- CORS is already configured to allow all origins
- For production, update `allow_origins` in `api/main.py`

### Frontend Can't Connect to API
- URLs are auto-configured to use relative paths
- Check browser console for errors
- Verify API endpoints are accessible

## 📱 Testing Locally Before Deploy

```bash
# Install Vercel CLI
npm i -g vercel

# Run local development server
vercel dev

# This will:
# - Start frontend on http://localhost:3000
# - Start APIs on /api and /agent routes
# - Simulate Vercel environment
```

## 🚀 Deployment Checklist

- [x] Code pushed to GitHub
- [x] Vercel account created
- [x] Project imported to Vercel
- [x] Deployment successful
- [x] Frontend loads correctly
- [x] API endpoints working
- [x] Agent API working
- [x] Test eligibility checker
- [x] Test AI assistant
- [x] Check all schemes

## 💰 Pricing

Vercel Free Tier includes:
- ✅ Unlimited deployments
- ✅ 100GB bandwidth/month
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Serverless functions
- ✅ Custom domains

Perfect for this project! 🎉

## 🔗 Useful Links

- Vercel Dashboard: https://vercel.com/dashboard
- Vercel Docs: https://vercel.com/docs
- Python on Vercel: https://vercel.com/docs/functions/serverless-functions/runtimes/python
- Support: https://vercel.com/support

## 📞 Need Help?

1. Check Vercel build logs
2. Review function logs in dashboard
3. Test API endpoints with curl/Postman
4. Check GitHub Actions (if configured)
5. Contact Vercel support

---

## Quick Commands Reference

```bash
# Deploy to production
vercel --prod

# Deploy preview
vercel

# Check deployment status
vercel ls

# View logs
vercel logs

# Remove deployment
vercel rm project-name

# Link local project to Vercel
vercel link
```

---

Your Kerala Schemes app is now live on Vercel! 🎊
