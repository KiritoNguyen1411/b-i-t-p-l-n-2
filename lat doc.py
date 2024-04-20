import cv2

def flip_image_vertical(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Lật dọc ảnh
    flipped_image = cv2.flip(image, 0)  # 0 là giá trị cho lật dọc, 1 cho lật ngang

    # Hiển thị ảnh gốc và ảnh sau khi lật
    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Image', flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đường dẫn của ảnh cần lật dọc
image_path = 'path/to/your/image.jpg'

# Gọi hàm để lật dọc ảnh và hiển thị kết quả
flip_image_vertical(image_path)
