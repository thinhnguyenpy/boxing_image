import os
import glob

# --- Cấu hình ---
# Thư mục chứa các tệp .txt của bạn. Dựa trên ảnh của bạn, đó là 'frames'.
# Nếu bạn đã chuyển chúng sang thư mục 'labels', hãy đổi thành 'labels'
LABELS_DIR = 'frames' 
OLD_ID = '0'  # ID cũ bạn muốn thay đổi
NEW_ID = '5'  # ID mới bạn muốn đổi thành
# ----------------

# Lấy danh sách tất cả các tệp .txt trong thư mục
txt_files = glob.glob(os.path.join(LABELS_DIR, '*.txt'))

if not txt_files:
    print(f"Không tìm thấy tệp .txt nào trong thư mục '{LABELS_DIR}'.")
    exit()

print(f"Tìm thấy {len(txt_files)} tệp .txt. Bắt đầu quá trình cập nhật...")

files_changed = 0

# Lặp qua từng tệp
for file_path in txt_files:
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        new_lines = []
        changed_in_file = False
        
        # Lặp qua từng dòng trong tệp
        for line in lines:
            parts = line.strip().split()
            # Kiểm tra nếu dòng không rỗng và class ID khớp với ID cũ
            if parts and parts[0] == OLD_ID:
                # Thay thế ID cũ bằng ID mới
                parts[0] = NEW_ID
                new_line = " ".join(parts) + "\n"
                new_lines.append(new_line)
                changed_in_file = True
            else:
                # Giữ nguyên dòng nếu không khớp
                new_lines.append(line)
        
        # Nếu có sự thay đổi, ghi lại vào tệp
        if changed_in_file:
            with open(file_path, 'w') as f:
                f.writelines(new_lines)
            files_changed += 1
            # print(f"Đã cập nhật tệp: {os.path.basename(file_path)}")

    except Exception as e:
        print(f"Lỗi khi xử lý tệp {file_path}: {e}")

print(f"\nHoàn tất! Đã cập nhật thành công ID trong {files_changed} tệp.")