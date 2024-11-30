class LaporanKeuangan:
    def __init__(data):  
        data.transaksi = {
            "Pemasukan": [],
            "Pengeluaran": []
        }
    def tambah_data(data, tipe, jumlah): 
        if tipe == "Pemasukan" or tipe == "Pengeluaran":
            data.transaksi[tipe].append(jumlah)
            print(f"{tipe} sebesar Rp {jumlah:,} berhasil ditambahkan.")
        else:
            print("Tipe transaksi tidak valid. Pilih 'Pemasukan' atau 'Pengeluaran'.")
    
    def tampilkan_laporan(data):
        total_pemasukan = sum(data.transaksi["Pemasukan"])
        total_pengeluaran = sum(data.transaksi["Pengeluaran"])
        saldo_akhir = total_pemasukan - total_pengeluaran
        
        print("\n=== LAPORAN KEUANGAN ===")
        print(f"Total Pemasukan   : Rp {total_pemasukan:,}")
        print(f"Total Pengeluaran : Rp {total_pengeluaran:,}")
        print(f"Saldo Akhir       : Rp {saldo_akhir:,}")


