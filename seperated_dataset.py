import csv
import os

# Đường dẫn đến tệp CSV lớn
large_csv_file = 'dataset/data/NF-UQ-NIDS-v2.csv'

# Tạo thư mục mới để lưu các tệp nhỏ
output_folder = 'dataset-v2'
os.makedirs(output_folder, exist_ok=True)

# Giới hạn dung lượng mỗi file nhỏ (150,000 KB)
max_file_size = 150000 * 1024  # 150,000 KB in bytes
chunk_count = 1

with open(large_csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Lấy dòng tiêu đề

    # Khởi tạo file nhỏ đầu tiên
    output_file = os.path.join(output_folder, f'part_{chunk_count}.csv')
    out_file = open(output_file, mode='w', newline='', encoding='utf-8')
    writer = csv.writer(out_file)
    writer.writerow(header)  # Ghi dòng tiêu đề

    for row in reader:
        writer.writerow(row)

        # Kiểm tra kích thước file
        if out_file.tell() >= max_file_size:
            out_file.close()
            print(f'{output_file} đã được tạo (khoảng {max_file_size / (1024 * 1024)} MB)')

            # Tạo file nhỏ tiếp theo
            chunk_count += 1
            output_file = os.path.join(output_folder, f'part_{chunk_count}.csv')
            out_file = open(output_file, mode='w', newline='', encoding='utf-8')
            writer = csv.writer(out_file)
            writer.writerow(header)  # Ghi dòng tiêu đề vào file mới

    # Đóng file cuối cùng
    out_file.close()
    print(f'{output_file} đã được tạo')
