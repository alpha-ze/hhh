# Deployment Guide - Kerala Schemes AI Assistant

## Deployment Options

### Option 1: Deploy on Render (Recommended - Free Tier Available)

#### Backend Deployment

1. **Create a Render account** at https://render.com

2. **Create `render.yaml`** (already provided in the project)

3. **Push code to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

4. **Deploy on Render**:
   - Go to Render Dashboard
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` and deploy both services
   - Note the URLs provided (e.g., https://your-app.onrender.com)

5. **Update Frontend URLs**:
   - Edit `script.js` and `assistant-simple.html`
   - Replace `http://localhost:8000` with your main API URL
   - Replace `http://localhost:8001` with your agent API URL

#### Frontend Deployment

**Option A: Netlify (Easiest)**
1. Go to https://netlify.com
2. Drag and drop your frontend files (index.html, style.css, script.js, etc.)
3. Site is live instantly!

**Option B: Vercel**
1. Go to https://vercel.com
2. Import your GitHub repository
3. Deploy with one click

**Option C: GitHub Pages**
1. Push code to GitHub
2. Go to Settings → Pages
3. Select branch and folder
4. Site will be live at https://username.github.io/repo-name

---

### Option 2: Deploy on Railway

1. **Create account** at https://railway.app

2. **Deploy Backend**:
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

3. **Add environment variables** in Railway dashboard

4. **Deploy Frontend** on Netlify/Vercel (same as above)

---

### Option 3: Deploy on Heroku

1. **Install Heroku CLI**:
```bash
# Windows
winget install Heroku.HerokuCLI

# Or download from https://devcenter.heroku.com/articles/heroku-cli
```

2. **Create Heroku apps**:
```bash
heroku login
heroku create kerala-schemes-api
heroku create kerala-schemes-agent
```

3. **Deploy Main API**:
```bash
git subtree push --prefix . heroku main
```

4. **Set up Procfile** (already provided)

5. **Deploy Frontend** on Netlify/Vercel

---

### Option 4: Deploy on AWS (Production-Ready)

#### Backend on AWS Elastic Beanstalk

1. **Install AWS CLI and EB CLI**:
```bash
pip install awsebcli
```

2. **Initialize EB**:
```bash
eb init -p python-3.11 kerala-schemes
```

3. **Create environment**:
```bash
eb create kerala-schemes-env
```

4. **Deploy**:
```bash
eb deploy
```

#### Frontend on AWS S3 + CloudFront

1. **Create S3 bucket**:
```bash
aws s3 mb s3://kerala-schemes-frontend
```

2. **Upload files**:
```bash
aws s3 sync . s3://kerala-schemes-frontend --exclude "*.py" --exclude "*.json"
```

3. **Enable static website hosting** in S3 console

4. **Set up CloudFront** for HTTPS and CDN

---

### Option 5: Deploy on Google Cloud Platform

#### Backend on Cloud Run

1. **Install Google Cloud SDK**

2. **Build and deploy**:
```bash
gcloud run deploy kerala-schemes-api --source .
gcloud run deploy kerala-schemes-agent --source .
```

#### Frontend on Firebase Hosting

1. **Install Firebase CLI**:
```bash
npm install -g firebase-tools
```

2. **Initialize and deploy**:
```bash
firebase init hosting
firebase deploy
```

---

### Option 6: Deploy on DigitalOcean

#### Using App Platform

1. Go to DigitalOcean App Platform
2. Connect GitHub repository
3. Configure build settings
4. Deploy with one click

#### Using Droplet (VPS)

1. **Create Ubuntu droplet**

2. **SSH into server**:
```bash
ssh root@your_droplet_ip
```

3. **Install dependencies**:
```bash
apt update
apt install python3-pip nginx
pip3 install -r requirements.txt
```

4. **Set up systemd services** (see systemd section below)

5. **Configure Nginx** (see nginx section below)

---

## Production Configuration

### Environment Variables

Create `.env` file:
```env
# Production
ENVIRONMENT=production
API_URL=https://your-api-url.com
AGENT_URL=https://your-agent-url.com

# CORS
ALLOWED_ORIGINS=https://your-frontend-url.com

# Optional: Database
DATABASE_URL=postgresql://user:pass@host:5432/db
```

### Update Frontend URLs

**script.js**:
```javascript
const API_BASE_URL = 'https://your-api-url.com';
```

**assistant-simple.html**:
```javascript
const response = await fetch('https://your-api-url.com/roadmap/${schemeId}');
const response = await fetch('https://your-agent-url.com/analyze-form', {
```

---

## Server Configuration

### Systemd Service (Linux)

Create `/etc/systemd/system/kerala-schemes-api.service`:
```ini
[Unit]
Description=Kerala Schemes API
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/kerala-schemes
Environment="PATH=/usr/local/bin"
ExecStart=/usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Create `/etc/systemd/system/kerala-schemes-agent.service`:
```ini
[Unit]
Description=Kerala Schemes Agent
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/kerala-schemes
Environment="PATH=/usr/local/bin"
ExecStart=/usr/local/bin/uvicorn agent:agent_app --host 0.0.0.0 --port 8001
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
systemctl enable kerala-schemes-api
systemctl enable kerala-schemes-agent
systemctl start kerala-schemes-api
systemctl start kerala-schemes-agent
```

### Nginx Configuration

Create `/etc/nginx/sites-available/kerala-schemes`:
```nginx
# Main API
server {
    listen 80;
    server_name api.yoursite.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# Agent API
server {
    listen 80;
    server_name agent.yoursite.com;

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# Frontend
server {
    listen 80;
    server_name yoursite.com www.yoursite.com;
    root /var/www/kerala-schemes/frontend;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Enable site:
```bash
ln -s /etc/nginx/sites-available/kerala-schemes /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

---

## SSL/HTTPS Setup

### Using Let's Encrypt (Free)

```bash
# Install certbot
apt install certbot python3-certbot-nginx

# Get certificates
certbot --nginx -d yoursite.com -d www.yoursite.com
certbot --nginx -d api.yoursite.com
certbot --nginx -d agent.yoursite.com

# Auto-renewal
certbot renew --dry-run
```

---

## Docker Deployment (Optional)

### Docker Compose

Already provided in `docker-compose.yml`. Deploy with:

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## Monitoring & Maintenance

### Health Checks

Add to `main.py` and `agent.py`:
```python
@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```

### Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Monitoring Tools

- **Uptime monitoring**: UptimeRobot, Pingdom
- **Error tracking**: Sentry
- **Analytics**: Google Analytics, Plausible

---

## Quick Start (Easiest Method)

### 1. Deploy Backend on Render (5 minutes)

1. Push code to GitHub
2. Go to Render.com → New Blueprint
3. Connect repository
4. Wait for deployment
5. Copy API URLs

### 2. Deploy Frontend on Netlify (2 minutes)

1. Update `script.js` with Render URLs
2. Drag frontend files to Netlify
3. Done!

**Total time: ~7 minutes** ✅

---

## Cost Estimates

| Platform | Backend | Frontend | Total/Month |
|----------|---------|----------|-------------|
| Render + Netlify | Free | Free | $0 |
| Railway + Vercel | $5 | Free | $5 |
| Heroku | $7 | Free | $7 |
| DigitalOcean | $6 | $0 | $6 |
| AWS | $10-20 | $1-5 | $11-25 |

---

## Troubleshooting

### CORS Issues
- Add your frontend domain to CORS allowed origins
- Check browser console for specific errors

### API Not Responding
- Check if services are running: `systemctl status kerala-schemes-api`
- Check logs: `journalctl -u kerala-schemes-api -f`

### Frontend Can't Connect
- Verify API URLs in script.js
- Check if APIs are accessible from browser
- Ensure HTTPS if frontend is HTTPS

---

## Support

For issues or questions:
- Check logs first
- Verify all URLs are updated
- Test APIs with curl or Postman
- Check firewall/security group settings
