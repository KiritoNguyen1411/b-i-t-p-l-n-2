import cv2

def flip_image_horizontal(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Lật ngang ảnh
    flipped_image = cv2.flip(image, 1)  # 1 là giá trị cho lật ngang, 0 cho lật dọc

    # Hiển thị ảnh gốc và ảnh sau khi lật
    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Image', flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đường dẫn của ảnh cần lật ngang
image_path = 'path/to/your/image.jpg'

# Gọi hàm để lật ngang ảnh và hiển thị kết quả
flip_image_horizontal(image_path)
