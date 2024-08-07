# main.py
def add_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    result = add_two_numbers(a, b)
    print(f"Tổng của {a} và {b} là {result}")
