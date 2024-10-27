import os
import requests

def tai_va_luu_anh(url, ten_file, thu_muc):
    try:       
        response = requests.get(url)
        
        if response.status_code == 200:
            duong_dan_toan_bo = os.path.join(thu_muc, ten_file)
            with open(duong_dan_toan_bo, 'wb') as f:
                f.write(response.content)
            print("Ảnh đã được tải về thành công.")
        else:
            print(f"Lỗi: Không thể tải ảnh từ URL ({response.status_code}).")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

if __name__ == "__main__":
    for i in range(69,189):
        url_anh = f"http://dlib.ptit.edu.vn/flowpaper/services/view.php?doc=20907893438507474322038146840303507280&format=jpg&page={i}&subfolder=20/90/78/" 

        ten_file = f"page-{i}.png"

        thu_muc = "D:\CODE\TEST" # đường dẫn thư mục

        tai_va_luu_anh(url_anh, ten_file, thu_muc)
