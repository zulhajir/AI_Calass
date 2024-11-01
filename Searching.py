import random

# Membuat daftar angka acak antara 1 sampai 10 dengan panjang 20
random_number = random.choices(range(1, 11), k=20)
print("Daftar angka acak:", random_number)

# Meminta input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Memeriksa apakah angka adalah bilangan genap
if angka % 2 == 0:
    # Mencari indeks dari angka yang dimasukkan
    indexListRandomNumber = [index for index, value in enumerate(random_number) if value == angka]
    
    if indexListRandomNumber:
        print(f"Y1: Angka yang dimasukkan berada pada indeks {indexListRandomNumber}")
    else:
        print("Angka tidak ada dalam list.")
else:
    print("Angka tidak genap")
