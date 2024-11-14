# Program Stock Opname Sederhana

# Dictionary untuk menyimpan data stok barang
stok_barang = {}

# Fungsi untuk menambahkan barang baru
def tambah_barang():
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    stok_barang[kode_barang] = {
        'nama_barang': nama_barang,
        'jumlah': jumlah
    }
    print(f"Barang '{nama_barang}' berhasil ditambahkan.\n")

# Fungsi untuk memperbarui jumlah stok barang
def update_stok():
    kode_barang = input("Masukkan kode barang yang ingin diperbarui: ")
    if kode_barang in stok_barang:
        jumlah_baru = int(input("Masukkan jumlah stok terbaru: "))
        stok_barang[kode_barang]['jumlah'] = jumlah_baru
        print(f"Stok barang '{stok_barang[kode_barang]['nama_barang']}' berhasil diperbarui.\n")
    else:
        print("Kode barang tidak ditemukan.\n")

# Fungsi untuk menampilkan daftar stok barang
def lihat_stok():
    if stok_barang:
        print("Daftar Stok Barang:")
        for kode, data in stok_barang.items():
            print(f"Kode Barang: {kode}, Nama: {data['nama_barang']}, Jumlah: {data['jumlah']}")
        print("\n")
    else:
        print("Stok kosong.\n")

# Fungsi untuk menghapus barang dari stok
def hapus_barang():
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    if kode_barang in stok_barang:
        del stok_barang[kode_barang]
        print("Barang berhasil dihapus.\n")
    else:
        print("Kode barang tidak ditemukan.\n")

# Menu utama
def menu():
    while True:
        print("=== Program Stock Opname ===")
        print("1. Tambah Barang")
        print("2. Update Stok")
        print("3. Lihat Stok")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            update_stok()
        elif pilihan == '3':
            lihat_stok()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.\n")

# Menjalankan program
menu()
