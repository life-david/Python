import fitz

# Mở file PDF
pdf_file = fitz.open('filename.pdf')

# Đọc nội dung trong file PDF
for page_num in range(pdf_file.page_count):
    page = pdf_file.load_page(page_num)
    page_text = page.get_text()
    print(page_text)

# Đóng file PDF
pdf_file.close()