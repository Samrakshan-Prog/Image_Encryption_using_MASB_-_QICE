import cv2
import sys
import os
import json
import numpy as np

def calculate_psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

if len(sys.argv) != 3:
    print(json.dumps({"error": "Invalid arguments"}))
    sys.exit(1)

original_path = sys.argv[1]
decrypted_path = sys.argv[2]

original = cv2.imread(original_path)
decrypted = cv2.imread(decrypted_path)

if original is None or decrypted is None:
    print(json.dumps({"error": "Could not read one or both images"}))
    sys.exit(1)

if original.shape != decrypted.shape:
    print(json.dumps({"error": "Image dimensions do not match"}))
    sys.exit(1)

psnr_value = calculate_psnr(original, decrypted)

result = {
    "original_size": os.path.getsize(original_path),
    "decrypted_size": os.path.getsize(decrypted_path),
    "psnr": round(psnr_value, 2)
}

print(json.dumps(result))
