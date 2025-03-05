import pandas as pd
import random
import os

DEFAULT_EXCEL_PATH = "D:/Code/Python/BTL_CTGLGT/danh sach.xlsx"  # Đường dẫn mặc định

def convert_to_4_scale(grade):
    """Chuyển điểm từ thang 10 sang thang 4 theo Chia để Trị."""
    if grade >= 9.0:
        return 4.0
    elif grade >= 8.5:
        return 3.7
    elif grade >= 8.0:
        return 3.5
    elif grade >= 7.0:
        return 3.0
    elif grade >= 6.5:
        return 2.5
    elif grade >= 5.5:
        return 2.0
    elif grade >= 5.0:
        return 1.5
    elif grade >= 4.0:
        return 1.0
    else:
        return 0.0

def calculate_average(grades, left, right):
    """Tính điểm trung bình bằng Chia để Trị."""
    if left == right:
        return grades[left], convert_to_4_scale(grades[left])
    
    mid = (left + right) // 2
    avg1_10, avg1_4 = calculate_average(grades, left, mid)
    avg2_10, avg2_4 = calculate_average(grades, mid + 1, right)
    
    return (avg1_10 + avg2_10) / 2, (avg1_4 + avg2_4) / 2

def find_max_min(arr, left, right):
    """Tìm điểm cao nhất và thấp nhất bằng Chia để Trị."""
    if left == right:
        return arr[left], arr[left]
    
    mid = (left + right) // 2
    max1, min1 = find_max_min(arr, left, mid)
    max2, min2 = find_max_min(arr, mid + 1, right)
    
    return max(max1, max2), min(min1, min2)

def quick_sort(arr):
    """Sắp xếp sinh viên theo điểm trung bình bằng Quick Sort (Chia để Trị)."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[1] > pivot[1]]
    middle = [x for x in arr if x[1] == pivot[1]]
    right = [x for x in arr if x[1] < pivot[1]]
    
    return quick_sort(left) + middle + quick_sort(right)

def read_data_from_excel(file_path):
    """Đọc dữ liệu từ file Excel."""
    df = pd.read_excel(file_path)
    students = {}
    for _, row in df.iterrows():
        name = row['Tên Sinh Viên']
        grades = list(row[1:])  # Lấy tất cả điểm các môn
        students[name] = grades
    return students

def input_student_data():
    """Nhập dữ liệu sinh viên thủ công."""
    students = {}
    num_students = int(input("Nhập số lượng sinh viên: "))
    num_subjects = int(input("Nhập số môn học: "))
    
    for _ in range(num_students):
        name = input("Nhập tên sinh viên: ")
        grades = [float(input(f"Nhập điểm môn {i+1} (thang 10): ")) for i in range(num_subjects)]
        students[name] = grades
    return students

def export_to_excel(students, output_file):
    """Xuất danh sách sinh viên ra file Excel."""
    data = []
    for name, grades in students.items():
        avg_10, avg_4 = calculate_average(grades, 0, len(grades) - 1)
        data.append([name, avg_10, avg_4] + grades)
    
    columns = ['Tên Sinh Viên', 'TB Thang 10', 'TB Thang 4'] + [f'Môn {i+1}' for i in range(len(grades))]
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(output_file, index=False)
    print(f"✅ Dữ liệu đã được xuất ra {output_file}")

def main():
    """Chương trình chính."""
    choice = input("Bạn muốn nhập dữ liệu từ file Excel (1) hay nhập thủ công (2)? ")
    if choice == "1":
        file_path = input(f"Nhập đường dẫn file Excel (hoặc nhấn Enter để dùng mặc định: {DEFAULT_EXCEL_PATH}): ") or DEFAULT_EXCEL_PATH
        students = read_data_from_excel(file_path)
    else:
        students = input_student_data()
    
    # Tính điểm trung bình theo Chia để Trị
    avg_scores = {name: calculate_average(grades, 0, len(grades) - 1)[0] for name, grades in students.items()}
    avg_list = list(avg_scores.values())
    
    # Tìm điểm cao nhất/thấp nhất bằng Chia để Trị
    max_score, min_score = find_max_min(avg_list, 0, len(avg_list) - 1)
    
    # Sắp xếp danh sách sinh viên theo điểm trung bình bằng Quick Sort
    sorted_students = quick_sort(list(avg_scores.items()))
    
    print("\nDanh sách sinh viên sắp xếp theo điểm trung bình:")
    for i, (name, avg) in enumerate(sorted_students, start=1):
        print(f"{i}. {name} - TB: {avg:.2f}")
    
    print(f"\nĐiểm trung bình cao nhất: {max_score:.2f}")
    print(f"Điểm trung bình thấp nhất: {min_score:.2f}")
    
    # Xuất file Excel ra đường dẫn mặc định
    output_path = "D:/Code/Python/BTL_CTGLGT/ket qua danh sach.xlsx"
    export_to_excel(students, output_path)

if __name__ == "__main__":
    main()
