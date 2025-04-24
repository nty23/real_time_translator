🌐 Real-Time Translator

A simple, elegant web app that translates text in real-time using Python, Flask, and the Deep Translator API. Built with a beautiful, feminine-themed UI using HTML, CSS, and JavaScript.

✨ Features

Real-time translation with a single click
Supports multiple languages (English, French, Spanish, Hindi, German, etc.)
Clean and responsive design
Built using Flask (Python backend) and vanilla JS (frontend)
🚀 Tech Stack

Python 3.10+
Flask
Deep Translator
HTML5 / CSS3 / JavaScript
Hosted locally via Flask server
📦 Setup Instructions

Clone the repo:
git clone https://github.com/nty23/real-time-translator.git
cd real-time-translator
Create a virtual environment:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Run the app:
flask run
Or:

python app.py
Open your browser and go to http://127.0.0.1:5000
📁 File Structure

real-time-translator/
│
├── app.py
├── translator.py
├── config.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── (optional CSS/JS files)
│
└── README.md
💡 Future Ideas

Add more languages
Text-to-speech for outputs
Deployment on Heroku or Render
