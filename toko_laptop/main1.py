import tkinter as tk
from tkinter import ttk
import pandas as pd

class AplikasiTokoLaptopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Toko Laptop")
        
        # Inisialisasi atribut
        self.data_file = "data_toko_laptop.csv"
        self.data_toko_laptop = pd.DataFrame(columns=["Merk", "Tipe", "Harga"])

        # Membuat GUI
        self.buat_gui()

        # Memanggil fungsi load_dari_csv untuk menampilkan data dari CSV saat aplikasi dimulai
        self.load_dari_csv()

    def tambah_laptop(self):
        # Mendapatkan nilai dari Entry
        merk = self.entry_merk.get()
        tipe = self.entry_tipe.get()
        harga = self.entry_harga.get()

        # Memanggil fungsi tambah_laptop_internal dengan nilai yang didapatkan
        self.tambah_laptop_internal(merk, tipe, harga)

        # Mengosongkan input setelah submit
        self.entry_merk.delete(0, tk.END)
        self.entry_tipe.delete(0, tk.END)
        self.entry_harga.delete(0, tk.END)

    def tambah_laptop_internal(self, merk, tipe, harga):
        new_data = pd.DataFrame({"Merk": [merk], "Tipe": [tipe], "Harga": [harga]})
        self.data_toko_laptop = pd.concat([self.data_toko_laptop, new_data], ignore_index=True)
        self.update_tabel()

        # Menyimpan ke CSV secara otomatis
        self.data_toko_laptop.to_csv(self.data_file, index=False)

    def load_dari_csv(self):
        try:
            self.data_toko_laptop = pd.read_csv(self.data_file)
            self.update_tabel()
        except FileNotFoundError:
            pass

    def update_tabel(self):
        self.tree.delete(*self.tree.get_children())
        for index, row in self.data_toko_laptop.iterrows():
            self.tree.insert("", "end", values=(row["Merk"], row["Tipe"], row["Harga"]))

    def buat_gui(self):
        # Label dan Entry untuk input data laptop
        ttk.Label(self.root, text="Merk Laptop:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_merk = ttk.Entry(self.root)
        self.entry_merk.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Tipe Laptop:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_tipe = ttk.Entry(self.root)
        self.entry_tipe.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Harga Laptop:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_harga = ttk.Entry(self.root)
        self.entry_harga.grid(row=2, column=1, padx=5, pady=5)

        # Tombol Tambah Laptop
        tombol_tambah = ttk.Button(self.root, text="Tambah Laptop", command=self.tambah_laptop)
        tombol_tambah.grid(row=3, column=0, columnspan=2, pady=10)

        # Tabel untuk menampilkan data laptop
        self.tree = ttk.Treeview(self.root, columns=("Merk", "Tipe", "Harga"), show="headings")
        self.tree.heading("Merk", text="Merk")
        self.tree.heading("Tipe", text="Tipe")
        self.tree.heading("Harga", text="Harga")
        self.tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiTokoLaptopGUI(root)
    root.mainloop()
