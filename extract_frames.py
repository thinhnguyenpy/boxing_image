import cv2
import os
import glob  # Thư viện mới để tìm tệp

# --- Cấu hình của bạn ---
# Đổi tên video này thành video bạn muốn trích xuất
VIDEO_PATH = 'video/my_video2.mp4'  
SAVE_DIR = 'frame1'
FRAME_SKIP = 30
# --------------------------

# Hàm tìm số thứ tự của frame cuối cùng đã lưu
def get_last_frame_number(save_dir):
    # Tìm tất cả các tệp .jpg trong thư mục
    list_of_files = glob.glob(os.path.join(save_dir, '*.jpg'))
    
    if not list_of_files:
        # Nếu không có tệp nào, bắt đầu từ 0
        return 0
    
    # Tìm tệp có tên lớn nhất (ví dụ: 'frame_00191.jpg')
    latest_file = max(list_of_files)
    
    # Lấy tên tệp không bao gồm đuôi (ví dụ: 'frame_00191')
    base_name = os.path.splitext(os.path.basename(latest_file))[0]
    
    try:
        # Lấy số cuối cùng (ví dụ: 191)
        last_number = int(base_name.split('_')[-1])
        return last_number
    except ValueError:
        # Nếu tên tệp không đúng định dạng, bắt đầu từ 0
        return 0

# --- Bắt đầu chạy ---

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Lấy số thứ tự của ảnh cuối cùng
saved_count = get_last_frame_number(SAVE_DIR)

print(f"Đã tìm thấy {saved_count} ảnh trong thư mục '{SAVE_DIR}'.")
print(f"Bắt đầu trích xuất từ tệp '{VIDEO_PATH}' và lưu từ số {saved_count + 1}...")

# Mở video
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print(f"Lỗi: Không thể mở tệp video tại {VIDEO_PATH}")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    
    if frame_count % FRAME_SKIP == 0:
        # Tăng biến đếm LÊN TRƯỚC khi lưu
        saved_count += 1
        
        save_path = os.path.join(SAVE_DIR, f"frame_{saved_count:05d}.jpg")
        cv2.imwrite(save_path, frame)
        print(f"Đã lưu: {save_path}")

cap.release()
print(f"\nHoàn tất! Tổng số ảnh hiện tại trong thư mục '{SAVE_DIR}' là {saved_count}.")