def partition(arr, low, high):
    pivot = arr[high]  # Chọn phần tử cuối làm pivot
    i = low - 1  # Vị trí của phần tử nhỏ hơn pivot

    for j in range(low, high):
        if arr[j] <= pivot:  # Nếu phần tử nhỏ hơn hoặc bằng pivot.Nếu muốn dãy giảm dần thì đổi dấu "<=" thành ">="
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Đổi chỗ

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Đưa pivot vào đúng vị trí
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Chia mảng
        quicksort(arr, low, pi - 1)  # Sắp xếp phần bên trái
        quicksort(arr, pi + 1, high)  # Sắp xếp phần bên phải

# Test
arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quicksort(arr, 0, len(arr) - 1)
print("Tăng dần:", arr)
