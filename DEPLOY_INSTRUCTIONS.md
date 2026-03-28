# Bazar da Thaís - Deploy Configuration

## 1. GitHub Repository Setup

1. Create a new GitHub repository:
   - Go to https://github.com/new
   - Repository name: `bazar-da-thais`
   - Set to Public (required for Streamlit Community Cloud free tier)
   - Initialize with README: No (we'll upload our files)

2. Upload files to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Bazar da Thaís Dashboard"
   git branch -M main
   git remote add origin https://github.com/[YOUR_USERNAME]/bazar-da-thais.git
   git push -u origin main
   ```

3. Files to upload:
   - `app_bazar.py` (main Streamlit app)
   - `requirements.txt` (dependencies)
   - `produtos_bazar.json` (initial demo data)
   - `.gitignore` (exclude local files)
   - `.streamlit/config.toml` (theme configuration)
   - `README.md` (documentation)

## 2. Streamlit Community Cloud Deployment

1. Go to https://share.streamlit.io/
2. Sign in with GitHub account
3. Click "New app"
4. Configure:
   - Repository: `[YOUR_USERNAME]/bazar-da-thais`
   - Branch: `main`
   - Main file path: `app_bazar.py`
5. Click "Deploy!"

## 3. Public URL

After deployment, you'll get a public URL like:
`https://[your-username]-bazar-da-thais-app-bazar-main-[hash].streamlit.app/`

Share this URL with anyone to access the dashboard.

## 4. Updates

To update the dashboard:
1. Push changes to GitHub repository
2. Streamlit automatically redeploys within 2-3 minutes

## 5. Security Notes

- Dashboard is read-only (safe for public access)  
- No sensitive data exposed
- Fallback demo data if JSON file missing
- Auto-refresh every 5 seconds for real-time updates

## 6. Features Included

- 📊 Real-time product catalog
- 📈 KPI dashboard with sales analytics
- 🔍 Product filtering by brand/type
- 📱 Mobile-friendly responsive design
- 🎨 Branded theme in pink/beauty colors
- ⚡ Auto-refresh for live updates