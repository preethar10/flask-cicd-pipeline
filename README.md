# 🚀 Flask CI/CD Pipeline

Automated REST API built with Python & Flask, with a full CI/CD pipeline using GitHub Actions.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Framework:** Flask
- **CI/CD:** GitHub Actions
- **Version Control:** Git & GitHub

## 📡 API Endpoints
| Endpoint | Description |
|----------|-------------|
| `/` | Home - returns API status |
| `/health` | Health check |
| `/about` | Project info |
| `/counter` | Counts API visits |
| `/time` | Returns current date & time |

## ⚙️ How CI/CD Works
1. Code is pushed to GitHub
2. GitHub Actions automatically triggers
3. Pipeline installs dependencies
4. Pipeline tests the app
5. All done automatically!

## 🚀 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/preethar10/flask-cicd-pipeline.git

# Go into the folder
cd flask-cicd-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
