from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def flip_image(image, flip_code):
    return cv2.flip(image, flip_code)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        # Lấy các thông tin từ request
        angle = int(request.form['rotation'])
        flip_option = request.form['flip']
        image_file = request.files['image']

        # Kiểm tra xem người dùng đã chọn tệp hình ảnh chưa
        if not image_file:
            return jsonify({'error': 'No image provided'})

        # Đọc hình ảnh từ file
        image_data = image_file.read()
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Xử lý hình ảnh
        if angle != 0:
            image = rotate_image(image, angle)

        # Xử lý flip_option
        flip_code = 0
        if 'Lật' in flip_option:
            flip_code += 1
        if 'Xoay' in flip_option:
            flip_code += 0

        image = flip_image(image, flip_code)

        # Chuyển đổi hình ảnh sang định dạng base64 để hiển thị trên HTML
        _, img_encoded = cv2.imencode('.jpg', image)
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')

        return jsonify({'image': img_base64})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
