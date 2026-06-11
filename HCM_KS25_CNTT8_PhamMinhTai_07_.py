transactions = []
next_id = 1


def validate_type(transaction_type):
    return transaction_type.lower() in ["thu", "chi"]


def add_transaction():
    global next_id

    print("\n=== THÊM GIAO DỊCH ===")

    reason = input("Lý do thu chi: ")

    transaction_type = input("Loại giao dịch (Thu/Chi): ")

    if not validate_type(transaction_type):
        print("Loại giao dịch không hợp lệ!")
        return

    try:
        amount = float(input("Số tiền phát sinh: "))
        tax = float(input("Thuế (%): "))

        if amount <= 0:
            print("Số tiền phải lớn hơn 0")
            return

        if tax < 0:
            print("Thuế không hợp lệ")
            return

    except ValueError:
        print("Dữ liệu nhập không hợp lệ!")
        return

    real_amount = amount * (1 + tax / 100)

    transaction = {
        "id": next_id,
        "reason": reason,
        "type": transaction_type.capitalize(),
        "amount": amount,
        "tax": tax,
        "real_amount": real_amount
    }

    transactions.append(transaction)
    next_id += 1

    print("Thêm giao dịch thành công!")


def display_transactions():
    print("\n=== NHẬT KÝ GIAO DỊCH ===")

    if not transactions:
        print("Chưa có giao dịch nào!")
        return

    for t in transactions:
        print(
            f"ID:{t['id']} | "
            f"{t['reason']} | "
            f"{t['type']} | "
            f"{t['amount']:,.0f} VNĐ | "
            f"Thuế {t['tax']}% | "
            f"Thực tế {t['real_amount']:,.0f} VNĐ"
        )


def update_transaction():
    try:
        transaction_id = int(input("Nhập ID cần cập nhật: "))
    except ValueError:
        print("ID không hợp lệ!")
        return

    for t in transactions:
        if t["id"] == transaction_id:

            t["reason"] = input("Lý do mới: ")

            new_type = input("Loại mới (Thu/Chi): ")

            if not validate_type(new_type):
                print("Loại giao dịch không hợp lệ!")
                return

            try:
                amount = float(input("Số tiền mới: "))
                tax = float(input("Thuế mới (%): "))
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                return

            t["type"] = new_type.capitalize()
            t["amount"] = amount
            t["tax"] = tax
            t["real_amount"] = amount * (1 + tax / 100)

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy giao dịch!")


def delete_transaction():
    try:
        transaction_id = int(input("Nhập ID cần xóa: "))
    except ValueError:
        print("ID không hợp lệ!")
        return

    for t in transactions:
        if t["id"] == transaction_id:
            transactions.remove(t)
            print("Đã xóa giao dịch!")
            return

    print("Không tìm thấy giao dịch!")


def search_transaction():
    keyword = input("Nhập từ khóa tìm kiếm: ").lower()

    found = False

    for t in transactions:
        if keyword in t["reason"].lower():
            print(t)
            found = True

    if not found:
        print("Không tìm thấy giao dịch!")


def statistics():
    total_income = 0
    total_expense = 0

    for t in transactions:
        if t["type"] == "Thu":
            total_income += t["real_amount"]
        else:
            total_expense += t["real_amount"]

    profit = total_income - total_expense

    print("\n=== THỐNG KÊ ===")
    print(f"Tổng thu : {total_income:,.0f} VNĐ")
    print(f"Tổng chi : {total_expense:,.0f} VNĐ")
    print(f>Dòng tiền ròng : {profit:,.0f} VNĐ")


while True:

    print("\n" + "=" * 50)
    print("CHƯƠNG TRÌNH QUẢN LÝ DÒNG TIỀN")
    print("=" * 50)
    print("1. Hiển thị nhật ký giao dịch")
    print("2. Ghi nhận giao dịch mới")
    print("3. Cập nhật giao dịch")
    print("4. Xóa giao dịch")
    print("5. Tìm kiếm giao dịch")
    print("6. Thống kê dòng tiền")
    print("7. Thoát")
    print("=" * 50)

    choice = input("Chọn chức năng (1-7): ")

    match choice:

        case "1":
            display_transactions()

        case "2":
            add_transaction()

        case "3":
            update_transaction()

        case "4":
            delete_transaction()

        case "5":
            search_transaction()

        case "6":
            statistics()

        case "7":
            print("Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")