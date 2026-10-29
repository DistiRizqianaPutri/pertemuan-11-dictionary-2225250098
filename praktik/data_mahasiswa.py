
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


def rata_rata_nilai(data):
    if not data:
        return 0
    total = sum(mhs["nilai"] for mhs in data.values())
    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Operasi pencarian
print("=== PENCARIAN MAHASISWA ===")
print(cari_mahasiswa(data_mahasiswa, "A002"))
print(cari_mahasiswa(data_mahasiswa, "A006"))

# 2. Operasi penambahan
data_mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "B",
    "nilai": 90
}
print("\nData mahasiswa berhasil ditambahkan.")

# 3. Operasi pembaruan
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai Budi berhasil diperbarui.")

# 4. Rekap seluruh mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")
for nim, mhs in data_mahasiswa.items():
    print(
        f"NIM: {nim}, "
        f"Nama: {mhs['nama']}, "
        f"Kelas: {mhs['kelas']}, "
        f"Nilai: {mhs['nilai']}"
    )

# 5. Rata-rata nilai
print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai: {rata_rata_nilai(data_mahasiswa):.2f}")
