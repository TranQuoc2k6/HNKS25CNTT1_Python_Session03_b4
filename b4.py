"""
    1.Input: Số lượng nhân sự trong tháng
    2.Output: Hiển thị lỗi nếu người dùng nhập vào là một số âm hoặc bằng 0
    3.Các bước thực hiện:
        + hiển thị dòng chứ Hệ thống báo cáo nhân sự
        + dùng vòng lặp while để cho người nhân viên nhập lại nếu nhập sai 
        + Dừng khi nhập đúng
"""

print("\n\n--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
input_employee_quantity = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
while True:
    if input_employee_quantity <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
        input_employee_quantity = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {input_employee_quantity} nhân sự mới!")
        break
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")