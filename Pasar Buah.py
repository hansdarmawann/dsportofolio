# Soal 2
# Lalu untuk soal berikutnya, dari app market yang sudah kita kerjakan di session sebelumnya, pada kali ini teman teman perlu menambahkan fitur sebagai berikut :
# Yang pertama, sekarang user tidak hanya bisa belanja namun ada 3 pilihan tambahan  yaitu (Menampilkan daftar buah, Menambah buah, dan Menghapus buah)
# Jadi programnya akan memiliki 5 menu utama :
#     1 . Menampilkan daftar buah
#     2 . Menambah buah
#     3 . Menghapus buah
#     4 . Membeli buah
#     5 . Exit Program
#   Kemudian Yang kedua, saat Pertama kali program dimulai, daftar buah sudah berisikan 3 buah beserta stock dan harganya. (Done)
# Yang ketiga, Untuk setiap selesai menambah dan menghapus buah, program akan menampilkan daftar buah terbaru. (Done)
# Yang keempat, Saat proses membeli, gunakanlah system seperti keranjang belanja atau cart. (Done)
# Yang kelima, Seperti program market sebelumnya, kalau duitnya lebih kecil dari total harga belanjanya akan diminta input ulang sampai duitnya cukup.
# Kemudin Yang keenam, Saat selesai membeli buah jangan lupa untuk mengurangi stock dari buah2 yang dibeli, dan kemudian kosongkan cartnya
# Lalu Yang ketujuh, Setiap selesai menggunakan suatu menu, program akan Kembali ke main menu, dan program hanya akan berhenti bila user menjalankan menu Exit Program. (Done)
# Ok Hint untuk mengerjakan soal ini, gunakanlah Python List untuk menyimpan data dari buah-buah, supaya nanti dapat menambahkan buah baru dan menghapus buah yang ada. Dan otomatis di program ini (Done)
# Juga membutuhkan Python Conditional Statement dan Looping Statement. (Done)

# Untuk jelasnya fitur dan tampilan dari program marketnya, bisa dilihat di gambar

# Yang ini adalah contoh kalau Menu 1 dan menu 5 dijalankan

# ---
listBuah = [
    {
        "nama":"Apel",
        "stock":20,
        "harga":10000
    },
    {
        "nama":"Jeruk",
        "stock":15,
        "harga":15000
    },
    {
        "nama":"Anggur",
        "stock":25,
        "harga":20000
    }
]

keranjang =[]

def tampilkanBuah():
    print(f"{"Index":<10}|{"Nama":<10}|{"Stok":<10}|{"Harga":<10}")
    [print(f"{i[0]:<10}|{i[1]["nama"]:<10}|{i[1]["stock"]:<10}|{i[1]["harga"]:<10}") for i in enumerate(listBuah)]

def tambahBuah(): #asumsi informasi buah bisa di-update. Jika nama buah yang di-input persis, maka tinggal update stok dan harganya.
    while True:
        inputNama = input("Masukkan Nama Buah: ")
        if not(inputNama.isalpha()):
            print("Input nama buah tidak valid")
        else:
            break
    while True:
        inputStock = input("Masukkan Stock Buah: ")
        if not(inputStock.isdigit()):
            print("Input stock buah tidak valid.")
        else:
            inputStock = int(inputStock)
            break
    
    while True:
        inputHarga = input("Masukkan Harga Buah: ")
        if not(inputHarga.isdigit()):
            print("Input harga buah tidak valid.")
        else:
            inputHarga = int(inputHarga)
            break

    found = False

    inputNama = inputNama.title()

    for i in listBuah:
        if i["nama"] == inputNama:
            found = True
            i["stock"] = inputStock
            i["harga"] = inputHarga
            break
    if not found:
        buahBaru = {
            "nama":inputNama,
            "stock":inputStock,
            "harga":inputHarga
        }
        listBuah.append(buahBaru)


    tampilkanBuah()
    
def hapusBuah():
    while True:
        tampilkanBuah()
        inputIndex = input("Masukkan index buah yang ingin dihapus: ")
        if not inputIndex.isdigit():
            print("Input tidak valid.")
        else:
            inputIndex = int(inputIndex)
            if inputIndex < len(listBuah):
                listBuah.pop(inputIndex)
                tampilkanBuah()
                break
            else:
                print("Input tidak valid.")


def tambahKeranjang():
    while True:
        inputIndex = input("Masukkan index buah yang ingin dibeli: ")
        if inputIndex.isdigit():
            inputIndex = int(inputIndex)
            break
        else:
            print("Input tidak valid.")
    while True:            
        inputJumlah = input("Masukkan jumlah buah yang ingin dibeli: ")
        if inputJumlah.isdigit():
            inputJumlah = int(inputJumlah)
            break
        else:
            print("Input tidak valid.")
    if inputJumlah > listBuah[inputIndex]["stock"]:
        print(f"Stock tidak cukup, stock {listBuah[inputIndex]["nama"]} tinggal {listBuah[inputIndex]["stock"]}")
    else:
        found = False
        for i in keranjang:
            if i["nama"] == listBuah[inputIndex]["nama"]:
                i["qty"] += inputJumlah  # Tambahkan jumlah yang dibeli
                i["harga"] = listBuah[inputIndex]["harga"]
                i["totalHarga"] = i["qty"] * listBuah[inputIndex]["harga"]  # Update total harga
                found = True
                break

        # Jika buah belum ada di keranjang, tambahkan ke keranjang baru
        if not found:
            beliBuah = {
                "nama": listBuah[inputIndex]["nama"],
                "qty": inputJumlah,
                "harga":listBuah[inputIndex]["harga"],
                "totalHarga": inputJumlah * listBuah[inputIndex]["harga"]
            }
            keranjang.append(beliBuah)
        tampilkanKeranjang()

def tampilkanKeranjang():
    print(f"{"Nama":<10}|{"Qty":<10}|{"Harga":<10}")
    [print(f"{i["nama"]:<10}|{i["qty"]:<10}|{i["harga"]:<10}") for i in keranjang]
        
def tampilkanKeranjangFinal():
    print(f"{"Nama":<10}|{"Qty":<10}|{"Harga":<10}|{"Total Harga":<10}")
    [print(f"{i["nama"]:<10}|{i["qty"]:<10}|{i["harga"]:<10}|{i["totalHarga"]:<10}") for i in keranjang]

def bayarBelanjaan():
    tampilkanKeranjangFinal()
    totalBelanja = sum([i["totalHarga"] for i in keranjang])
    print(f"Total yang harus dibayar: {totalBelanja}")
    uang = 0
    while True:
        while True:
            uang = input("Masukkan jumlah uang: ")
            if uang.isdigit():
               uang = int(uang)
               break
            else:
                print("Input tidak valid")

        if uang < totalBelanja:
            print(f"Uang anda tidak cukup. Uang anda kurang {totalBelanja - uang}")
        elif uang >= totalBelanja:
            print("Terima kasih.")
            if uang > totalBelanja:
                print(f"Uang kembalian anda: {uang - totalBelanja}")
            for i in keranjang:
                for j in listBuah:
                    if j["nama"] == i["nama"]:
                        j["stock"] -= i["qty"]
            keranjang.clear()
            break
        else:
            print("Input tidak valid.")


def exitProgram():
    print("Terima kasih. Program keluar.")

def main():
    menu = 1
    # inputLagi4 = " "
    while menu != 5:
        print("""
        Selamat Datang di Pasar Buah
            
        List Menu   :
            1 . Menampilkan daftar buah
            2 . Menambah buah
            3 . Menghapus buah
            4 . Membeli buah
            5 . Exit Program
        """)
        menu = input("Masukkan angka Menu yang ingin dimasukkan: ")
        if menu == 1:
            tampilkanBuah()
        elif menu == 2:
            tambahBuah()
        elif menu == 3:
            hapusBuah()
        elif menu == 4:
            tampilkanBuah()
            inputLagi4=" "
            while inputLagi4!="tidak":
                if inputLagi4=="tidak":
                    break
                elif inputLagi4=="ya" or inputLagi4==" ":
                    tambahKeranjang()
                else:
                    print("Input tidak valid.")
                inputLagi4 = input("Mau beli yang lain ? (ya/tidak): ")
            bayarBelanjaan()

        elif menu == 5:
            exitProgram()
            break
        else:
            print("Pilihan input tidak valid!")

if __name__=="__main__":
    main()