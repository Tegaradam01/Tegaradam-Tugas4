def biner_ke_desimal(biner):
    return int(biner, 2)

def desimal_ke_biner(desimal):
    return bin(desimal)[2:]

def oktal_ke_desimal(oktal):
    return int(oktal, 8)

def desimal_ke_oktal(desimal):
    return oct(desimal)[2:]

def heksa_ke_desimal(heksa):
    return int(heksa, 16)

def desimal_ke_heksa(desimal):
    return hex(desimal)[2:]

while True:
    print("Pilih operasi konversi:")
    print("1. Biner ke Desimal")
    print("2. Desimal ke Biner")
    print("3. Oktal ke Desimal")
    print("4. Desimal ke Oktal")
    print("5. Heksadesimal ke Desimal")
    print("6. Desimal ke Heksadesimal")
    print("7. Keluar")
    
    pilihan = int(input("Masukkan pilihan (1-7): "))
    
    if pilihan == 1:
        biner = input("Masukkan bilangan biner: ")
        print("Hasil konversi:", biner_ke_desimal(biner))
    elif pilihan == 2:
        desimal = int(input("Masukkan bilangan desimal: "))
        print("Hasil konversi:", desimal_ke_biner(desimal))
    elif pilihan == 3:
        oktal = input("Masukkan bilangan oktal: ")
        print("Hasil konversi:", oktal_ke_desimal(oktal))
    elif pilihan == 4:
        desimal = int(input("Masukkan bilangan desimal: "))
        print("Hasil konversi:", desimal_ke_oktal(desimal))
    elif pilihan == 5:
        heksa = input("Masukkan bilangan heksadesimal: ")
        print("Hasil konversi:", heksa_ke_desimal(heksa))
    elif pilihan == 6:
        desimal = int(input("Masukkan bilangan desimal: "))
        print("Hasil konversi:", desimal_ke_heksa(desimal))
    elif pilihan == 7:
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-7.")
