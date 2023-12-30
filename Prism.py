import math
import os
import time

def image_1(func):
    def wrapper():
        func()
        print("    ##            |")
        print("   #  #@@@@      @|")
        print("  #    #          |")
        print(" #      #         |")
        print("##########        |")
        time.sleep(10)
    return wrapper


def image_2(func):
    def wrapper2():
        func()
        print("    ##             |")
        print("   #  #@@@@       @|")
        print("  #    #  @@@@    @|")
        print(" #      #          |")
        print("##########         |")
        time.sleep(10)
    return wrapper2


@image_1
def goc_chiet_quang():
    n = float(input("Chiết xuất của lăng kính với ánh sáng(n): "))
    D = float(input("Góc lệch của tia sáng(D): "))
    A = round(D/(n-1), 3)
    print(f"Góc chiết quang là: {A}")


@image_1
def chiet_xuat_lang_kinh_vs_anh_sang():
    A = float(input("Góc chiết quang(A): "))
    D = float(input("Góc lệch của tia sáng(D): "))
    n = round((D/A) + 1, 3)
    print(f"Chiết xuất của lăng kính với ánh sáng là: {n}")


@image_1
def goc_lech():
    A = float(input("Góc chiết quang(A): "))
    n = float(input("Chiết xuất của lăng kính với ánh sáng(n): "))
    D = round((n-1)*A, 3)
    print(f"Góc lệch của lăng kính với ảnh sáng là: {D}")


@image_1
def khoang_cach_2_vet_sang():
    A = float(input("Góc chiết quang(A): "))
    n = float(input("Chiết xuất của lăng kính với ánh sáng(n): "))
    D = round((n-1)*A, 3)
    d = float(input("Khoảng cách từ lăng kính tới màn ảnh: "))
    Scale = d*math.tan(D)
    Scale = round(Scale, 3)
    print(f"Khoảng cách giữa hai vệt sáng là: {Scale}")


def mot_tia_sang():
    print("1. Góc chiết quang")
    print("2. Chiết xuất của lăng kính với ánh sáng")
    print("3. Góc lệch của tia sáng")
    print("4. Khoảng cách 2 vệt sáng")
    option = int(input("Đại lượng cần phải tính: "))
    if option == 1: 
        goc_chiet_quang()
    elif option == 2: 
        chiet_xuat_lang_kinh_vs_anh_sang()
    elif option == 3: 
        goc_lech()
    elif option == 4: 
        khoang_cach_2_vet_sang()
    else:
        print("Invalid input")


@image_2
def khoang_cach_d():
    A = float(input("Góc chiết quang(A): "))
    n1 = float(input("Chiết xuất của lăng kính với ánh sáng(n1): "))
    n2 = float(input("Chiết xuất của lăng kính với ánh sáng(n2): "))
    D1 = round((n1-1)*A, 3)
    D2 = round((n2-1)*A, 3)
    quang_pho = float(input("Độ rộng quang quang phổ là: ")) 
    tan_D1 = math.tan(D1 * math.pi / 180)
    tan_D2 = math.tan(D2 * math.pi / 180)
    result = quang_pho/(tan_D2 - tan_D1)
    result = round(result, 3)
    os.system("cls")
    print(f"Khoảng cách từ lăng kính tới màn quan sát là: {result}")


@image_2
def be_rong_quang_pho():
    A = float(input("Góc chiết quang(A): "))
    n1 = float(input("Chiết xuất của lăng kính với ánh sáng(n1): "))
    n2 = float(input("Chiết xuất của lăng kính với ánh sáng(n2): "))
    D1 = round((n1-1)*A, 3)
    D2 = round((n2-1)*A, 3)
    d = float(input("Nhập chiều khoảng cách giữa màn quan sát là lăng kính: "))
    tan_D1 = math.tan(D1 * math.pi / 180)
    tan_D2 = math.tan(D2 * math.pi / 180)
    result = d*(tan_D2 - tan_D1)
    result = round(result, 10)
    os.system("cls")
    print(f"Bề rộng quang phổ là: {result}")


def hai_tia_sang():
    print("1. Khoảng cách d")
    print("2. Bề rộng quang phổ")
    option = int(input("Đại lượng cần phải tính là: "))
    if option == 1: 
        khoang_cach_d()
    elif option == 2:
        be_rong_quang_pho()


while True:
    os.system("cls")
    print("1. Một tia sáng")
    print("2. Hai tia sáng")
    print("Q. Thoát")
    user_input = (input("Gồm bao nhiêu tia sáng ra khỏi lăng kính: "))
    if user_input == "1":
        mot_tia_sang()
    elif user_input == "2": 
        hai_tia_sang()
    elif user_input == "q":
        print("closing program. . .")
        time.sleep(3)
        exit()
    else: 
        print("Invalid Input")
