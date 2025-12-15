import os
import time
import csv

Akun = []
KreditScore = 100
Schedule = []
Notif = []
Riwayat = []


CSV_AKUN = "akun.csv"
CSV_SCHEDULE = "schedule.csv"
CSV_RIWAYAT = "riwayat.csv"

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

def save_csv_schedule(item):
    with open(CSV_SCHEDULE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(item)


def rewrite_csv_schedule():
    with open(CSV_SCHEDULE, "w", newline="") as file:
        writer = csv.writer(file)
        for item in Schedule:
            writer.writerow(item)

def load_csv_riwayat():
    if not os.path.exists(CSV_RIWAYAT):
        return

    with open(CSV_RIWAYAT, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 8:
                Riwayat.append(tuple(row))


def save_csv_riwayat(item):
    with open(CSV_RIWAYAT, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(item)

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

            elif choose2 == "3":
                while True:
                    print("=== MENU PERTEMUAN ===")
                    choose_meet = input(
                        "1. Lihat Pertemuan Aktif\n"
                        "2. Detail Pertemuan\n"
                        "3. Kembali\n"
                        "Pilih (1/2/3)>> "
                    )

                    if choose_meet == "1":
                        cls()
                        ada = False
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if usr == usrname_login:
                                print(
                                    f"{hari}, {tanggal} {bulan} {tahun} "
                                    f"Jam {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                                )
                                ada = True
                        if not ada:
                            print("Tidak ada pertemuan aktif.")

                        input("Tekan Enter untuk kembali...")
                        cls()

                    elif choose_meet == "2":
                        cls()
                        user_jadwal = []
                        idx = 1
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if usr == usrname_login:
                                user_jadwal.append(item)
                                print(
                                    f"{idx}. {hari}, {tanggal} {bulan} {tahun} "
                                    f"Jam {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                                )
                                idx += 1

                        if not user_jadwal:
                            print("Tidak ada pertemuan untuk ditampilkan.")
                            input("Tekan Enter untuk kembali...")
                            cls()
                            continue

                        pilih_detail = input("Masukkan nomor pertemuan yang ingin dilihat (atau 'k' untuk kembali): ")
                        if pilih_detail.lower() == 'k':
                            cls()
                            continue

                        if not pilih_detail.isdigit():
                            print("Input tidak valid.")
                            input("Tekan Enter untuk kembali...")
                            cls()
                            continue

                        nomor = int(pilih_detail)
                        if nomor < 1 or nomor > len(user_jadwal):
                            print("Nomor tidak valid.")
                            input("Tekan Enter untuk kembali...")
                            cls()
                            continue

                        detail_item = user_jadwal[nomor - 1]
                        usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = detail_item

                        print("=== DETAIL PERTEMUAN ===")
                        print(f"Partner: {usr}")
                        print(f"Hari: {hari}")
                        print(f"Tanggal: {tanggal} {bulan} {tahun}")
                        print(f"Jam: {jam_mulai} - {jam_selesai}")
                        print(f"Pengaju: {pengaju}")

                        while True:
                            choose_detail = input(
                                "1. Akhiri Pertemuan\n"
                                "2. Kembali\n"
                                "Pilih (1/2)>> "
                            )
                            if choose_detail == "1":
                                # pindahkan detail_item ke Riwayat (untuk user ini)
                                Riwayat.append(detail_item)
                                save_csv_riwayat(detail_item)

                                # cari dan hapus schedule pasangan (jika ada), lalu masukkan juga ke riwayat
                                pasangan = None
                                for s in list(Schedule):  # copy list untuk aman
                                    s_usr, s_hari, s_tanggal, s_bulan, s_tahun, s_jam_mulai, s_jam_selesai, s_pengaju = s
                                    # pasangan adalah entri di mana pemilik adalah pengaju dan partner adalah usr
                                    if (
                                        s_usr == pengaju
                                        and s_hari == hari
                                        and s_tanggal == tanggal
                                        and s_bulan == bulan
                                        and s_tahun == tahun
                                        and s_jam_mulai == jam_mulai
                                        and s_jam_selesai == jam_selesai
                                        and s_pengaju == usr
                                    ):
                                        pasangan = s
                                        break

                                if pasangan:
                                    Riwayat.append(pasangan)
                                    save_csv_riwayat(pasangan)
                                    # hapus pasangan dari Schedule
                                    Schedule.remove(pasangan)

                                # hapus detail_item dari Schedule (pemilik yang saat ini mengakhiri)
                                removed = False
                                for s in list(Schedule):
                                    if s == detail_item:
                                        Schedule.remove(s)
                                        removed = True
                                        break

                                # update file schedule
                                rewrite_csv_schedule()

                                print("Pertemuan berhasil dipindahkan ke riwayat.")
                                input("Tekan Enter untuk kembali...")
                                cls()
                                break

                            elif choose_detail == "2":
                                cls()
                                break

                    elif choose_meet == "3":
                        cls()
                        break
                    
            elif choose2 == "2":
                cls()
                while True:
                    choose3 = input(
                        "Kelola Jadwal Pribadi:\n"
                        "1. Tambah Jadwal\n"
                        "2. Hapus Jadwal\n"
                        "3. Lihat Jadwal Saya\n"
                        "4. Kembali\n"
                        "Pilih (1/2/3/4)>> "
                    )

                    if choose3 == "1":
                        hari = input("Masukkan hari: ")
                        tanggal = input("Masukkan tanggal: ")
                        bulan = input("Masukkan bulan: ")
                        tahun = input("Masukkan tahun: ")
                        jam_mulai = input("Masukkan jam mulai: ")
                        jam_selesai = input("Masukkan jam selesai: ")

                        data = (usrname_login, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, "Pribadi")
                        Schedule.append(data)
                        save_csv_schedule(data)
                        print("Jadwal berhasil ditambahkan.")
                        cls()

                    elif choose3 == "2":
                        print("Daftar Jadwal Anda:")
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if usr == usrname_login:
                                print(
                                    f"{hari}, {tanggal} {bulan} {tahun} "
                                    f"Jam {jam_mulai}-{jam_selesai}"
                                )

                        hapus = input("Masukkan hari,tanggal,bulan yang ingin dihapus (pisahkan dengan koma): ").split(",")
                        hapus = [x.strip() for x in hapus]

                        found = False
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if (
                                usr == usrname_login
                                and hari == hapus[0]
                                and tanggal == hapus[1]
                                and bulan == hapus[2]
                            ):
                                Schedule.remove(item)
                                rewrite_csv_schedule()
                                print("Jadwal berhasil dihapus.")
                                found = True
                                break

                        if not found:
                            print("Jadwal tidak ditemukan.")

                        cls()

                    elif choose3 == "3":
                        print("Jadwal Anda:")
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if usr == usrname_login:
                                print(
                                    f"{hari}, {tanggal} {bulan} {tahun}. "
                                    f"Jam: {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                                )
                        input("Tekan Enter untuk kembali...")
                        cls()

                    elif choose3 == "4":
                        cls()
                        break