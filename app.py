from flask import Flask, request, jsonify, render_template
import os
import subprocess
import uuid
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files:
        return jsonify({'message': 'No image uploaded'})

    image = request.files['image']
    filename = image.filename
    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    os.makedirs('input', exist_ok=True)
    os.makedirs('output', exist_ok=True)

    input_path = os.path.join('input', filename)
    image.save(input_path)

    subprocess.run(['python', 'encryptor.py', input_path])

    if ext in ['.jpg', '.jpeg']:
        return jsonify({'message': f'📸 JPG was converted to PNG to avoid quality loss. Encrypted as encrypted_{name}.png'})
    else:
        return jsonify({'message': f'Encrypted image and key saved as encrypted_{name}{ext} and key_{name}.json'})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    if 'image' not in request.files or 'key' not in request.files:
        return jsonify({'message': 'Encrypted image and key (.json) are required'})

    image = request.files['image']
    key = request.files['key']
    img_name = image.filename
    key_name = key.filename

    enc_path = os.path.join('output', img_name)
    key_path = os.path.join('output', key_name)

    os.makedirs('output', exist_ok=True)
    os.makedirs('decrypted', exist_ok=True)

    image.save(enc_path)
    key.save(key_path)

    subprocess.run(['python', 'decryptor.py', enc_path, key_path])

    # Derive original name from encrypted name
    original_name = img_name.replace("encrypted_", "")
    original_path = os.path.join('input', original_name)
    decrypted_path = os.path.join('decrypted', 'decrypted_' + os.path.splitext(original_name)[0] + '.png')

    # Run verify.py to get PSNR and sizes
    result = subprocess.run(
        ['python', 'verify.py', original_path, decrypted_path],
        capture_output=True,
        text=True
    )

    try:
        metrics = json.loads(result.stdout)
        return jsonify({
            'message': 'Decrypted image saved successfully.',
            'original_size': metrics.get('original_size'),
            'decrypted_size': metrics.get('decrypted_size'),
            'psnr': f"{metrics.get('psnr', 0)} dB"
        })
    except:
        return jsonify({'message': 'Decryption done but failed to verify PSNR.'})

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
DECRYPTED_FOLDER = os.path.join(BASE_DIR, "decrypted")


@app.route("/open-output")
def open_output_folder():
    try:
        print("Opening folder:", OUTPUT_FOLDER)
        os.startfile(OUTPUT_FOLDER)
        return "Output folder opened successfully!"
    except Exception as e:
        print("Error:", str(e))
        return f"Error opening output folder: {str(e)}"


@app.route("/open-decrypted")
def open_decrypted_folder():
    try:
        os.startfile(DECRYPTED_FOLDER)  # Windows only
        return "Decrypted folder opened successfully!"
    except Exception as e:
        return f"Error opening decrypted folder: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
