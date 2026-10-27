
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/seminar')
def seminar():
    return render_template('seminar.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/api/posts', methods=['POST'])
def create_post():
    username = request.form.get('username', 'Flow Member')
    content = request.form.get('content', '')
    audio_file = request.files.get('audio')
    
    audio_url = None
    if audio_file:
        filename = secure_filename(f"{username}_{audio_file.filename}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)
        audio_url = f"/static/uploads/{filename}"

    return jsonify({
        "success": True,
        "message": "Post created successfully!",
        "post": {
            "username": username,
            "content": content,
            "audio_url": audio_url
        }
    }), 200

if __name__ == "__main__":
    app.run(debug=True)