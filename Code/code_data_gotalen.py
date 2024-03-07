def process_file():
    with open('text.txt', 'r') as file:
        content = file.read()   #Đọc file
    content_without_commas = content.replace(',', '')   #Xóa dấu phẩy
    content_with_line_breaks = content_without_commas.replace(' ', '\n')    #Chuyển đổi tất cả khoảng trắng thành dấu xuống dòng
    with open('file_new.txt', 'w') as file_new:     #Mở tệp tin mới
        file_new.write(content_with_line_breaks)        #Ghi nội dung đã được xử lý vào tệp tin mới

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()     #Đọc toàn bộ nội dung của tệp tin, chia nó thành các dòng và trả về kết quả

def spilit_and_transfer(lst):
    sublist = {}
    for element in lst:
        if element not in sublist:          #Nếu phần tử không tồn tại trong sublist, thêm phần tử vào sublist dưới dạng một danh sách mới. Nếu phần tử đã tồn tại, thêm phần tử vào danh sách hiện tại
            sublist[element] = [element]
        else:
            sublist[element].append(element)
    return list(sublist.values())       #Trả về một danh sách các giá trị trong sublist, mỗi giá trị là một danh sách các phần tử giống nhau

process_file()      #Gọi hàm để xử lý tệp
file = "file_new.txt" 
data = read_file(file)
sublist = spilit_and_transfer(data)     #Chuyển đổi data thành một danh sách các danh sách con và gán nó vào biến sublist
for sublists in sublist:        #Lặp qua từng danh sách con trong sublist và in ra phần tử đầu tiên và số lượng phần tử trong danh sách con đó
    print(sublists[0],len(sublists))