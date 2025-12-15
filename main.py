import os
import time
import csv

Akun = []
KreditScore = 100
Schedule = []
Notif = []

CSV_AKUN = "akun.csv"
def load_csv_akun():
    if not os.path.exists(CSV_AKUN):
        return

    with open(CSV_AKUN, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                Akun.append((row[0], row[1]))


def save_csv_akun(username, password):
    with open(CSV_AKUN, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def cls():
    time.sleep(1)
    os.system('cls')


def Register():
    input("Masukkan Email: ")  
    usrname_signup = input("Masukkan Username: ")
    pass_signup = input("Masukkan Password: ")
    signup = (usrname_signup, pass_signup)

    Akun.append(signup)
    save_csv_akun(usrname_signup, pass_signup)

    print("Registrasi berhasil! Akun telah tersimpan permanen.")
    cls()


def Login():
    usrname_login = input("Masukkan Username: ")
    pass_login = input("Masukkan Password: ")
    login = (usrname_login, pass_login)

    if login in Akun:
        print("Login berhasil.")
        time.sleep(1)
        os.system('cls')
        return usrname_login
    else:
        print("Login gagal. Username atau password salah.")
        return None

load_csv_akun()

while True:
    print("===== SELAMAT DATANG DI COMEET =====")
    chooseStart = input(
        "1. Daftar (Register)\n"
        "2. Masuk (Login)\n"
        "3. Keluar\n"
        "Pilih (1/2/3)>> "
    )

    if chooseStart == "1":
        Register()

    elif chooseStart == "2":
        usrname_login = Login()
        if usrname_login is None:
            cls()
            continue

        cls()

        while True:
            print("===== MENU UTAMA COMEET =====")
            choose2 = input(
                "Pilih menu berikut:\n"
                "1. Cari Username\n"
                "2. Kelola Jadwal Pribadi\n"
                "3. Pertemuan\n"
                "4. Lihat Kredit Score\n"
                "5. Lihat Notifikasi\n"
                "6. Riwayat Pertemuan\n"
                "7. Logout\n"
                "Pilihan (1/2/3/4/5/6/7)>> "
            )
            if choose2 == "1":
                search_usrname = input("Masukkan username yang ingin dicari: ")
                found = False

                for usr, pw in Akun:
                    if search_usrname == usr:
                        found = True
                        break

                if not found:
                    print("Username tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")
                    cls()
                    continue

                print("Username ditemukan.")
                cls()

                while True:
                    choose_sub = input(
                        f"1. Lihat Jadwal {search_usrname}\n"
                        "2. Ajukan Jadwal Pertemuan\n"
                        "3. Kembali\n"
                        "Pilih (1/2/3)>> "
                    )

                    if choose_sub == "1":
                        cls()
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju = item
                            if usr == search_usrname:
                                print(
                                    f"{hari}, {tanggal} {bulan} {tahun}. "
                                    f"Jam: {jam_mulai}-{jam_selesai} (dengan {nama_pengaju})"
                                )

                        input("Tekan Enter untuk kembali...")
                        cls()

                    elif choose_sub == "2":
                        hari = input("Masukkan hari: ")
                        tanggal = input("Masukkan tanggal: ")
                        bulan = input("Masukkan bulan: ")
                        tahun = input("Masukkan tahun: ")
                        jam_mulai = input("Masukkan jam mulai: ")
                        jam_selesai = input("Masukkan jam selesai: ")

                        notif = (search_usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, usrname_login)
                        Notif.append(notif)
                        print("Pengajuan jadwal telah dikirim.")
                        cls()

                    elif choose_sub == "3":
                        cls()
                        break
                    
            elif choose2 == "4":
                print(f"Kredit Score Anda: {KreditScore}")
                input("Tekan Enter untuk kembali...")
                cls()
