import random
import csv
import unicodedata
from collections import defaultdict

# --- Dữ liệu nguồn để tạo tên ngẫu nhiên ---
surnames = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Vũ", "Phan",
            "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Đinh",
            "Đoàn", "Võ", "Mai", "Tạ"]
middle_names = ["Văn", "Thị", "Hữu", "Minh", "Ngọc", "Xuân", "Bảo", "Gia",
                "Đức", "Công", "Mạnh", "Quốc", "Đình", "Quang", "Thu", "Thanh"]
first_names = ["An", "Anh", "Bình", "Bảo", "Châu", "Chi", "Dũng", "Duy", "Giang",
               "Hà", "Hải", "Hiếu", "Hoa", "Hùng", "Hương", "Huy", "Khánh",
               "Lan", "Linh", "Long", "Ly", "Mai", "Minh", "Nam", "Nga",
               "Ngân", "Ngọc", "Nhi", "Phong", "Phúc", "Phương", "Quân",
               "Quang", "Sơn", "Tâm", "Thắng", "Thảo", "Trang", "Trung",
               "Tuấn", "Tú", "Việt", "Vy", "Yến"]

# --- Danh sách mã khoa ---
departments = ["VT", "KH", "PT", "KT", "BC", "QT", "FT", "MR", "AT", "CN"]

# --- Hàm loại bỏ dấu và chữ Đ ---
def remove_vietnamese_tones(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.replace('Đ', 'D').replace('đ', 'd')
    return text

# --- Nhập số lượng sinh viên ---
while True:
    try:
        num_students = int(input("Nhập số lượng sinh viên bạn muốn tạo: "))
        if num_students > 0:
            break
        else:
            print("Số lượng phải là số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

# --- Tạo dữ liệu ---
students_data = []
generated_student_codes = set() # Sử dụng set để lưu trữ các mã sinh viên đã tạo
print(f"Đang tạo dữ liệu cho {num_students} sinh viên...")

for i in range(1, num_students + 1):
    ho = random.choice(surnames)
    dem = random.choice(middle_names)
    ten = random.choice(first_names)
    ho_ten = remove_vietnamese_tones(f"{ho} {dem} {ten}")  # Tên không dấu

    # Tạo mã sinh viên duy nhất
    while True:
        department = random.choice(departments)
        if i <= 999:
            potential_ma_sv = f"B22DC{department}{i:03d}"
        else:
            random_number = random.randint(1, 999)
            potential_ma_sv = f"B22DC{random.choice(departments)}{random_number:03d}"

        if potential_ma_sv not in generated_student_codes:
            ma_sv = potential_ma_sv
            generated_student_codes.add(ma_sv)
            break

    chuyen_can = round(random.uniform(6.0, 10.0), 1)
    kiem_tra_gk = round(random.uniform(0.0, 10.0), 1)
    diem_btl = round(random.uniform(0.0, 10.0), 1)
    kiem_tra_ck = round(random.uniform(0.0, 10.0), 1)

    tbm = round((chuyen_can + kiem_tra_gk + diem_btl + kiem_tra_ck) / 4, 1)

    students_data.append([ho_ten, ma_sv, chuyen_can, kiem_tra_gk, diem_btl, kiem_tra_ck, tbm])

# --- Xáo trộn dữ liệu ---
print("Đang xáo trộn dữ liệu...")
random.shuffle(students_data)

# --- Ghi ra file CSV --- (không có cột Khoa)
header = ["STT", "Ho va ten", "Ma sinh vien", "Chuyen can", "Kiem tra giua ky", "Diem BTL", "Kiem tra cuoi ky", "TBM"]

output_filename = f"data_sinhvien_{num_students}.csv"
print(f"Đang ghi dữ liệu ra file '{output_filename}'...")

try:
    with open(output_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for idx, student_info in enumerate(students_data):
            stt = idx + 1
            writer.writerow([stt] + student_info)
    print(f"Đã tạo thành công file '{output_filename}' với {num_students} sinh viên.")
except Exception as e:
    print(f"Có lỗi xảy ra khi ghi file: {e}")

# --- In thử vài dòng đầu ---
print("\n--- Xem trước vài dòng dữ liệu ---")
try:
    with open(output_filename, 'r', encoding='utf-8-sig') as csvfile:
        for i, line in enumerate(csvfile):
            if i < 11:
                print(line.strip())
            else:
                break
except FileNotFoundError:
    print(f"Không tìm thấy file '{output_filename}' để xem trước.")
except Exception as e:
    print(f"Không thể đọc lại file để xem trước: {e}")