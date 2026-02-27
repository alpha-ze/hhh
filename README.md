# Kerala Government Schemes - AI-Powered Application Assistant

An intelligent system to check eligibility for Kerala government welfare schemes and get AI-guided assistance for filling online application forms.

## 🌟 Features

- **Eligibility Checker**: Input your details to find schemes you qualify for
- **AI Form Assistant**: Real-time guidance while filling government forms
- **Screen Analysis**: AI agent analyzes the webpage and provides step-by-step instructions
- **Field Mapping**: Intelligent field detection and auto-fill suggestions
- **Document Guidance**: Alerts for required documents at each step
- **Multi-Scheme Support**: Works for both online and offline application processes

## 🚀 Quick Start (Local Development)

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Start the main API server**:
```bash
uvicorn main:app --reload --port 8000
```

3. **Start the AI agent server** (in a new terminal):
```bash
uvicorn agent:agent_app --reload --port 8001
```

4. **Open the frontend**:
   - Simply open `index.html` in your browser
   - Or use a local server: `python -m http.server 3000`

## 📦 Deployment

### Easiest Method (7 minutes total)

#### 1. Deploy Backend on Render (Free)
```bash
# Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_URL
git push -u origin main

# Then:
# 1. Go to https://render.com
# 2. Click "New" → "Blueprint"
# 3. Connect your GitHub repo
# 4. Render auto-deploys both APIs
```

#### 2. Deploy Frontend on Netlify (Free)
```bash
# Update API URLs in script.js and assistant-simple.html first!
# Then drag and drop these files to Netlify:
# - index.html
# - style.css
# - script.js
# - assistant-simple.html
# - agent-assistant.html
```

### Other Deployment Options

- **Heroku**: `heroku create && git push heroku main`
- **Railway**: `railway init && railway up`
- **Docker**: `docker-compose up -d`
- **AWS/GCP**: See `DEPLOYMENT.md`

**📖 Full deployment guide**: See [DEPLOYMENT.md](DEPLOYMENT.md)

### Quick Deploy Scripts

**Windows**:
```bash
deploy.bat
```

**Linux/Mac**:
```bash
chmod +x deploy.sh
./deploy.sh
```

## 🏗️ Project Structure

```
kerala-schemes/
├── main.py                    # Main API (eligibility checker)
├── agent.py                   # AI agent API (form guidance)
├── kerala_schemes.json        # Schemes database
├── index.html                 # Main frontend
├── style.css                  # Styling
├── script.js                  # Frontend logic
├── assistant-simple.html      # AI assistant interface
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Multi-container setup
├── render.yaml               # Render deployment config
├── Procfile                  # Heroku deployment config
├── netlify.toml              # Netlify deployment config
├── DEPLOYMENT.md             # Detailed deployment guide
└── README.md                 # This file
```

## 🎯 How It Works

1. **Check Eligibility**: User fills form with personal details
2. **View Results**: System shows all eligible schemes
3. **AI-Guided Application**: 
   - Click "AI-Guided Application" button
   - Opens AI assistant with step-by-step guidance
   - For online schemes: Opens official website
   - For offline schemes: Provides office visit instructions
4. **Follow Guidance**: AI provides real-time help for each step

## 📋 Supported Schemes

| Scheme | Type | AI Guidance |
|--------|------|-------------|
| Sthree Suraksha Pension | Online | ✅ Full |
| Kerala Social Security Pension | Offline | ✅ Full |
| Chief Minister's Connect to Work | Online | ✅ Full |
| Life Mission Housing | Online | ✅ Full |
| Snehasparsham (Unwed Mothers) | Offline | ✅ Full |

## 🔧 API Endpoints

### Main API (Port 8000)
- `GET /` - Health check
- `POST /check-eligibility` - Check scheme eligibility
- `GET /roadmap/{scheme_id}` - Get application roadmap

### Agent API (Port 8001)
- `GET /` - Agent health check
- `POST /analyze-form` - Analyze form and provide guidance

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Agent**: Python (ready for GPT-4 Vision integration)
- **Deployment**: Render, Netlify, Docker, Heroku, Railway

## 🔮 Future Enhancements

- [ ] Integrate GPT-4 Vision for real screenshot analysis
- [ ] Auto-fill forms using browser extensions
- [ ] Document OCR for data extraction
- [ ] Voice guidance (text-to-speech)
- [ ] Multi-language support (Malayalam, Tamil, etc.)
- [ ] Mobile app (React Native/Flutter)
- [ ] SMS notifications for application status
- [ ] Integration with government APIs

## 📊 Environment Variables

Create `.env` file for production:
```env
ENVIRONMENT=production
API_URL=https://your-api-url.com
AGENT_URL=https://your-agent-url.com
ALLOWED_ORIGINS=https://your-frontend-url.com
```

## 🐛 Troubleshooting

### CORS Issues
Update `main.py` to add your frontend domain:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.com"],
    ...
)
```

### API Connection Failed
1. Check if both servers are running
2. Verify URLs in `script.js` and `assistant-simple.html`
3. Check browser console for errors

### Deployment Issues
See [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific troubleshooting

## 📝 License

MIT License - Feel free to use for any purpose

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues or questions:
- Check [DEPLOYMENT.md](DEPLOYMENT.md)
- Review API logs
- Test endpoints with curl/Postman
- Open an issue on GitHub

## 🎉 Credits

Built for Kerala State Government Schemes
Powered by FastAPI and AI
