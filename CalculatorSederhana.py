#memisalkan variabel a dan b sebagai inputan nilai
#lalu membuat operasi penjumalahan, pengurangan, perkalian, dan pembagian

def tambah(a, b): 
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

# jika b bernilai nol maka akan menghasilkan dari else
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol tidak diizinkan"
#mebuat pilihan operator dan mengkalkulasi keempat operator
while True:
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")

    if pilihan == '5':
        print("Keluar dari program.")
        break

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(angka1, "+", angka2, "=", tambah(angka1, angka2))
        elif pilihan == '2':
            print(angka1, "-", angka2, "=", kurang(angka1, angka2))
        elif pilihan == '3':
            print(angka1, "*", angka2, "=", kali(angka1, angka2))
        elif pilihan == '4':
            hasil_bagi = bagi(angka1, angka2)
            print(angka1, "/", angka2, "=", hasil_bagi)
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pilihan tidak valid. Masukkan nomor operasi yang benar.")
