from flask import Flask, request, jsonify
from flask_cors import CORS  # For handling Cross-Origin Resource Sharing
import os
from style_transfer import apply_style  # Your function to apply style using a pre-trained model

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/apply_style', methods=['POST'])
def apply_style_route():
    # Check if the post request has the file part
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    file = request.files['image']

    # If the user does not select a file, the browser sends an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        # Save the uploaded image
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Get the selected style from the request
        style = request.form.get('style', 'default_style')

        # Apply style using your function (replace this with your actual style transfer logic)
        styled_image_path = apply_style(file_path, style)

        return jsonify({'styledImage': styled_image_path})

    return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
