# Image Security using Multi-Agent Swarm Behavior (MASB) and Quantum-Inspired Chaotic Encoding (QICE)

## Overview
This project implements a secure image encryption and decryption system using Multi-Agent Swarm Behavior (MASB) combined with Quantum-Inspired Chaotic Encoding (QICE). It ensures robust image protection with high randomness and resistance to brute-force or statistical attacks.

The system is built with:
- **Frontend**: AngularJS
- **Backend**: Flask (Python)
- **Algorithms**: MASB + QICE
- **Database**: Oracle SQL (optional for storage)
- **Image Types Supported**: JPG, PNG

---

## Features
- Encrypts images with MASB and QICE for high security.
- Decrypts images to recover the original without loss.
- Single image encryption and decryption per process.
- Cross-platform (Windows/Linux/Mac).
- Web interface with modern animations and background effects.

---

## Project Structure
```
project/
│
├── app.py                 # Flask backend
├── encryptor.py           # MASB + QICE encryption
├── decryptor.py           # MASB + QICE decryption
├── verify.py 
├── templates/
│   └── index.html         # AngularJS frontend
├── static/
│   └── image8.png
├── sample images/
│   └── images
├── input/
├── output/
├── decrypted/
└── README.md              # Project documentation
```

---

## Installation

### Prerequisites
- Python 3.8+
- pip
- Node.js (optional if modifying AngularJS frontend)
- Oracle SQL (optional for storage)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Samrakshan-Prog/Image_Encryption_using_MASB_&_QICE.git
   cd Image_Encryption_using_MASB_-_QICE
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## How It Works
### MASB (Multi-Agent Swarm Behavior)
- Mimics the swarm intelligence found in nature (e.g., birds, fish).
- Shuffles and scrambles pixel positions based on swarm dynamics.

### QICE (Quantum-Inspired Chaotic Encoding)
- Uses chaotic maps and quantum key principles to generate encryption keys.
- Enhances unpredictability and security in pixel value transformation.

---

## Usage
1. Select **Encrypt** or **Decrypt** from the web interface.
2. Upload your image file.
3. Wait for the process to complete.
4. Download the processed image.

---

## Deployment
This project can be deployed on:
- **Heroku** (Flask-ready)
- **Render**
- **PythonAnywhere**
- **Self-hosted servers**

Note: Vercel does not natively support Flask. You can create a Node.js wrapper or use serverless functions for deployment.

---

## License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Author
Srisamrakshan Parthiban  
[LinkedIn Profile](www.linkedin.com/in/srisamrakshan)
