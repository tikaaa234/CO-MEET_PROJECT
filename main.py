#CO-Meet

import os
import time
import csv

KreditScore = []
Schedule = []
Akun = []
Notif = []
Riwayat = []

CSV_AKUN = "akun.csv"
CSV_SCHEDULE = "schedule.csv"
CSV_RIWAYAT = "riwayat.csv"
CSV_KREDITSCORE = "kreditscore.csv"
CSV_NOTIF = "notif.csv"


# ===================== CSV =========================
def load_csv_akun():
    if not os.path.exists(CSV_AKUN):
        return

    with open(CSV_AKUN, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                Akun.append((row[0], row[1], row[2]))


def save_csv_akun(username, password, em):
    with open(CSV_AKUN, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, em])


def load_csv_schedule():
    if not os.path.exists(CSV_SCHEDULE):
        return

    with open(CSV_SCHEDULE, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 8:
                Schedule.append(tuple(row))


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

def load_csv_kreditscore():
    if not os.path.exists(CSV_KREDITSCORE):
        return
    
    with open (CSV_KREDITSCORE, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                KreditScore.append((row[0], row[1]))

def save_csv_kreditscore(kreditscore, usrname):
    with open(CSV_KREDITSCORE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([kreditscore, usrname])

def rewrite_csv_kreditscore():
    with open(CSV_KREDITSCORE, "w", newline="") as file:
        writer = csv.writer(file)
        for item in KreditScore:
            writer.writerow(item)

def load_csv_notif():
    if not os.path.exists(CSV_NOTIF):
        return
    
    with open (CSV_NOTIF, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 8:
                Notif.append(tuple(row))

def input_jadwal():
    while True:
        os.system('cls')

        data = input("Hari & Tanggal (Senin 12/9/2025) (0 untuk kembali): ").strip()
        if data == "0":
            return None

        jam = input("Jam (08-10) (0 untuk kembali): ").strip()
        if jam == "0":
            return None

        # ===== VALIDASI DASAR =====
        pisah = data.split()
        if len(pisah) != 2:
            print("Format hari & tanggal salah.")
            cls()
            continue

        hari, tanggal = pisah
        pisah_tgl = tanggal.split("/")
        if len(pisah_tgl) != 3:
            print("Format tanggal salah.")
            cls()
            continue

        tgl, bulan, tahun = pisah_tgl

        pisah_jam = jam.split("-")
        if len(pisah_jam) != 2:
            print("Format jam salah.")
            cls()
            continue

        jam_mulai, jam_selesai = pisah_jam

        if (
            not hari.isalpha()
            or not (tgl.isdigit() and bulan.isdigit() and tahun.isdigit())
            or not (jam_mulai.isdigit() and jam_selesai.isdigit())
            or not (1 <= int(tgl) <= 31 and 1 <= int(bulan) <= 12)
            or not (0 <= int(jam_mulai) < int(jam_selesai) <= 24)
        ):
            print("Data tidak valid.")
            cls()
            continue

        # ===== JIKA SEMUA BENAR =====
        return hari, tgl, bulan, tahun, jam_mulai, jam_selesai

# =====================================================


def cls():
    time.sleep(1)
    os.system('cls')


def Register():
    while True: 
        email = input("Masukkan Email: ").strip()
        usrname_signup = input("Masukkan Username: ").strip()
        pass_signup = input("Masukkan Password: ").strip()
        if email == "" or usrname_signup == "" or pass_signup == "":
            print("Harap isi data dengan benar! Silahkan isi kembali")
            cls()
            break
        elif "@" not in email:
            print("Format email belum benar! Silahkan isi kembali")
            cls()
            break
        elif len(pass_signup) < 5:
            print("Password minimal 5 karakter!")
            cls()
            break
        elif usrname_signup == pass_signup:
            print("Username tidak boleh sama dengan password! Silahkan isi kembali")
            cls()
            break
        
        email_terpakai = False
        username_signup_terpakai = False

        for usr, pw, gmail in Akun:
            if gmail == email:
                email_terpakai = True
                break
            elif usr == usrname_signup:
                username_signup_terpakai = True
                break
        
        if email_terpakai:
            print("Email sudah terpakai! Silahkan isi kembali")
            cls()
            break

        elif username_signup_terpakai:
            print("Username sudah terpakai! Silahkan isi kembali")
            cls()
            break

        signup = (usrname_signup, pass_signup, email)

        Akun.append(signup)
        save_csv_akun(usrname_signup, pass_signup, email)

        first_kreditscore = 100
        kreditscore_sv = (first_kreditscore, usrname_signup)
        KreditScore.append(kreditscore_sv)
        save_csv_kreditscore(first_kreditscore, usrname_signup)

        print("Registrasi berhasil! Akun telah tersimpan permanen.")
        cls()
        break


def Login():
    usrname_login = input("Masukkan Username: ")
    pass_login = input("Masukkan Password: ")
    for usr, pw, gmail in Akun:
        if usr == usrname_login and pw == pass_login:
            print("Login berhasil.")
            cls()
            return usrname_login
    
    print("Login gagal. Username atau password salah.")
    return None

def tampilkan_notif_user(Notif, usrname_login):
    daftar = []

    for item in Notif:
        usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
        if usr == usrname_login:
            daftar.append(item)

    if not daftar:
        print("Tidak ada notifikasi.")
        input("Tekan Enter untuk kembali...")
        return None

    print("\nDaftar notifikasi:")
    for i, item in enumerate(daftar, start=1):
        _, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
        print(
            f"{i}. {hari}, {tanggal}-{bulan}-{tahun} | "
            f"Jam {jam_mulai}-{jam_selesai} | dari {pengaju}"
        )

    return daftar


def tampilkan_notifikasi(Notif, usrname_login):
    daftar = []
    no = 1

    for item in Notif:
        usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
        if usr == usrname_login:
            print(
                f"{no}. {hari}, {tanggal}-{bulan}-{tahun}| "
                f"Jam {jam_mulai}-{jam_selesai} | dari {pengaju}"
            )
            daftar.append(item)
            no += 1

    return daftar

def proses_notifikasi(index, daftar, Notif, Schedule):
    item = daftar[index]

    usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item

    print("\n1. Terima\n2. Tolak\n3. Kembali")
    pilih = input("Pilih (1/2/3)>> ")

    if pilih == "1":
        # jadwal untuk penerima
        data_penerima = (
            usr,
            hari,
            tanggal,
            bulan,
            tahun,
            jam_mulai,
            jam_selesai,
            pengaju
        )
        Schedule.append(data_penerima)
        save_csv_schedule(data_penerima)

        # jadwal untuk pengaju (dibalik)
        data_pengaju = (
            pengaju,
            hari,
            tanggal,
            bulan,
            tahun,
            jam_mulai,
            jam_selesai,
            usr
        )
        Schedule.append(data_pengaju)
        save_csv_schedule(data_pengaju)

        Notif.remove(item)
        simpan_notif_csv(Notif)

        print("Pengajuan diterima.")

    elif pilih == "2":
        Notif.remove(item)
        simpan_notif_csv(Notif)
        print("Pengajuan ditolak.")

    else:
        return


def simpan_notif_csv(Notif):
    with open("notif.csv", "w", newline="") as f:
        w = csv.writer(f)
        for row in Notif:
            w.writerow(row)

def tampilkan_list_jadwal(Jadwal, usrname_login):
    daftar = []
    no = 1

    for item in Jadwal:
        usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
        if usr == usrname_login:
            print(
                f"{no}. {hari}, {tanggal}-{bulan}-{tahun}| "
                f"Jam {jam_mulai}-{jam_selesai} | oleh {pengaju}"
            )
            daftar.append(item)
            no += 1

    return daftar

def proses_hapus_jadwal(index, daftar, Schedule):
    item = daftar[index]

    print("\n1. Hapus\n2. Kembali")
    pilih = input("Pilih (1/2)>> ")

    if pilih == "1":
        Schedule.remove(item)
        simpan_jadwal_csv(Schedule)
        print("Jadwal berhasil dihapus.")
    else:
        return

    
def simpan_jadwal_csv(schedule):
    with open("schedule.csv", "w", newline="") as f:
        w = csv.writer(f)
        for row in schedule:
            w.writerow(row)



# ==================== LOAD CSV DI AWAL ====================
load_csv_akun()
load_csv_schedule()
load_csv_riwayat()
load_csv_kreditscore()
load_csv_notif()
# ==========================================================


# ==================== MENU REGISTER / LOGIN ====================
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

        # ================= MASUK KE MENU UTAMA SETELAH LOGIN =================
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

            # =================== 1. SEARCH USERNAME ===================
            if choose2 == "1":
                cls()
                search_usrname = input("Masukkan username yang ingin dicari: ")
                found = False

                for usr, pw, email in Akun:
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
                        ada_jadwal = False

                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if usr == search_usrname:
                                print(
                                    f"{hari}, {tanggal}-{bulan}-{tahun}. "
                                    f"Jam: {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                                )
                                ada_jadwal = True

                        if not ada_jadwal:
                            print("Tidak ada jadwal.")

                        input("Tekan Enter untuk kembali...")
                        cls()


                    elif choose_sub == "2":
                        cls()
                        hasil = input_jadwal()
                        if hasil is None:
                            cls()
                            continue  # balik ke menu:
                                    # 1. Lihat Jadwal
                                    # 2. Ajukan Jadwal
                                    # 3. Kembali

                        hari, tanggal, bulan, tahun, jam_mulai, jam_selesai = hasil

                        notif = (
                            search_usrname,
                            hari,
                            tanggal,
                            bulan,
                            tahun,
                            jam_mulai,
                            jam_selesai,
                            usrname_login
                        )

                        Notif.append(notif)
                        simpan_notif_csv(Notif)

                        print("Pengajuan jadwal telah dikirim.")
                        cls()


                    elif choose_sub == "3":
                        cls()
                        break

                    else:
                        cls()
                        continue

            # =================== 2. EDIT JADWAL PRIBADI ===================
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
                        cls()
                        hasil = input_jadwal()
                        if hasil is None:
                            cls()
                            continue

                        hari, tanggal, bulan, tahun, jam_mulai, jam_selesai = hasil

                        data = (usrname_login, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, "Pribadi")
                        Schedule.append(data)
                        save_csv_schedule(data)
                        print("Jadwal berhasil ditambahkan.")
                        cls()

                    elif choose3 == "2":
                        while True:
                            cls()

                            daftar = []
                            no = 1

                            for item in Schedule:
                                usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                                if usr == usrname_login and pengaju == "Pribadi":
                                    print(
                                        f"{no}. {hari}, {tanggal}-{bulan}-{tahun}| "
                                        f"Jam {jam_mulai}-{jam_selesai} | oleh {pengaju}"
                                    )
                                    daftar.append(item)
                                    no += 1

                            if not daftar:
                                print("Jadwal Anda Kosong.")
                                input("Tekan Enter untuk kembali...")
                                cls()
                                break

                            pilih = input("Masukkan nomor jadwal yang ingin dihapus (0 untuk kembali): ")
                            if pilih == "0":
                                cls()
                                break

                            if not pilih.isdigit():
                                continue

                            pilih = int(pilih)

                            if 1 <= pilih <= len(daftar):
                                proses_hapus_jadwal(pilih - 1, daftar, Schedule)
                                input("Tekan Enter untuk lanjut...")
                                cls()
                            else:
                                continue

                    elif choose3 == "3":
                        cls()
                        print("Jadwal Anda:")
                        for item in Schedule:
                            usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                            if usr == usrname_login and pengaju == "Pribadi":
                                print(
                                    f"{hari}, {tanggal}-{bulan}-{tahun}. "
                                    f"Jam: {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                                )
                        input("Tekan Enter untuk kembali...")
                        cls()

                    elif choose3 == "4":
                        cls()
                        break
                    
                    else:
                        cls()
                        continue

            # =================== 3. PERTEMUAN ===================
            elif choose2 == "3":
                cls()
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
                                    f"{hari}, {tanggal}-{bulan}-{tahun} "
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
                                    f"{idx}. {hari}, {tanggal}-{bulan}-{tahun} "
                                    f"Jam {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                                )
                                idx += 1

                        if not user_jadwal:
                            print("Tidak ada pertemuan untuk ditampilkan.")
                            input("Tekan Enter untuk kembali...")
                            cls()
                            continue

                        pilih_detail = input("Masukkan nomor pertemuan yang ingin dilihat (atau 0 untuk kembali): ")
                        if pilih_detail == "0":
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
                        print(f"Partner : {pengaju}")
                        print(f"Hari    : {hari}")
                        print(f"Tanggal : {tanggal}")
                        print(f"Bulan   : {bulan}")
                        print(f"Tahun   : {tahun}")
                        print(f"Jam     : {jam_mulai} - {jam_selesai}")
                   

                        while True:
                            choose_detail = input(
                                "1. Pertemuan Terealisasikan\n"
                                "2. Pertemuan Tidak Terealisasikan\n"
                                "3. Kembali\n"
                                "Pilih (1/2/3)>> "
                            )
                            if choose_detail == "1":
                                # pindahkan detail_item ke Riwayat (untuk user ini)
                                if pengaju != "Pribadi":
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

                                    kreditscore_pengaju = None
                                    kreditscrore_remove = None
                                    for i in KreditScore:
                                        i_kreditscore, i_akun = i
                                        if i_akun == pengaju:
                                            kreditscore_pengaju = i
                                            kreditscrore_remove = i
                                            break
                                    
                                    KreditScore.remove(kreditscrore_remove)
                                    kreditscore_pengaju = (int(kreditscore_pengaju[0]), kreditscore_pengaju[1])
                                    kreditscore_pengaju_baru = kreditscore_pengaju[0]
                                    if kreditscore_pengaju[0] <= 100:
                                        tambah_kreditscore_pengaju = kreditscore_pengaju_baru + 5
                                        if tambah_kreditscore_pengaju >= 100:
                                            kreditscore_baru = kreditscore_pengaju_baru, pengaju
                                            KreditScore.append(kreditscore_baru)
                                            save_csv_kreditscore(tambah_kreditscore_pengaju, pengaju)
                                        else:
                                            kreditscore_baru = (tambah_kreditscore_pengaju, pengaju)
                                            KreditScore.append(kreditscore_baru)
                                            save_csv_kreditscore(tambah_kreditscore_pengaju, pengaju)
                                    


                                    # update file schedule
                                    rewrite_csv_schedule()
                                    rewrite_csv_kreditscore()

                                    print("Pertemuan berhasil dipindahkan ke riwayat.")
                                    input("Tekan Enter untuk kembali...")
                                    cls()
                                    break
                                
                                else:
                                    Riwayat.append(detail_item)
                                    save_csv_riwayat(detail_item)
                                    Schedule.remove(detail_item)

                                    rewrite_csv_schedule()

                                    print("Pertemuan berhasil dipindahkan ke riwayat.")
                                    input("Tekan Enter untuk kembali...")
                                    cls()
                                    break


                            elif choose_detail == "2":
                                if pengaju != "Pribadi":
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
                                        # hapus pasangan dari Schedule
                                        Schedule.remove(pasangan)

                                    # hapus detail_item dari Schedule (pemilik yang saat ini mengakhiri)
                                    removed = False
                                    for s in list(Schedule):
                                        if s == detail_item:
                                            Schedule.remove(s)
                                            removed = True
                                            break

                                    kreditscore_pengaju = None
                                    kreditscrore_remove = None
                                    for i in KreditScore:
                                        i_kreditscore, i_akun = i
                                        if i_akun == pengaju:
                                            kreditscore_pengaju = i
                                            kreditscore_remove = i
                                            break
                                    
                                    KreditScore.remove(kreditscore_remove)
                                    kreditscore_pengaju = (int(kreditscore_pengaju[0]), kreditscore_pengaju[1])
                                    kreditscore_pengaju_baru = kreditscore_pengaju[0]
                                    if kreditscore_pengaju[0] <= 100:
                                        kurang_kreditscore_pengaju = kreditscore_pengaju_baru - 10
                                        if kurang_kreditscore_pengaju <= 0:
                                            kreditscore_nol = 0
                                            kreditscore_baru = kreditscore_nol, pengaju
                                            KreditScore.append(kreditscore_baru)
                                            save_csv_kreditscore(kurang_kreditscore_pengaju, pengaju)
                                        else:
                                            kreditscore_baru = (kurang_kreditscore_pengaju, pengaju)
                                            KreditScore.append(kreditscore_baru)
                                            save_csv_kreditscore(kurang_kreditscore_pengaju, pengaju)
                                    


                                    # update file schedule
                                    rewrite_csv_schedule()
                                    rewrite_csv_kreditscore()

                                    print("Pertemuan diakhiri.")
                                    input("Tekan Enter untuk kembali...")
                                    cls()
                                    break

                                else:
                                    Schedule.remove(detail_item)

                                    rewrite_csv_schedule()

                                    print("Pertemuan diakhiri.")
                                    input("Tekan Enter untuk kembali...")
                                    cls()
                                    break


                            elif choose_detail == "3":
                                cls()
                                break

                    elif choose_meet == "3":
                        cls()
                        break

            # =================== 4. CREDIT SCORE ===================
            elif choose2 == "4":
                cls()
                for item in KreditScore:
                    kreditscore, usr = item
                    if usr == usrname_login:
                        print(f"Kredit Score Anda: {kreditscore}")
                        input("Tekan Enter untuk kembali...")
                        cls()

            # =================== 5. NOTIFIKASI ===================
            elif choose2 == "5":
                while True:
                    cls()

                    daftar = tampilkan_notifikasi(Notif, usrname_login)

                    if not daftar:
                        print("Tidak ada notifikasi.")
                        input("Tekan Enter untuk kembali...")
                        cls()
                        break

                    pilih = input("\nPilih nomor notifikasi (0 untuk kembali)>> ")

                    if pilih == "0":
                        cls()
                        break

                    if not pilih.isdigit():
                        continue

                    pilih = int(pilih)

                    if 1 <= pilih <= len(daftar):
                        proses_notifikasi(pilih - 1, daftar, Notif, Schedule)
                        input("\nTekan Enter untuk lanjut...")
                    else:
                        continue


            # =================== 6. RIWAYAT PERTEMUAN ===================
            elif choose2 == "6":
                cls()
                print("=== Riwayat Pertemuan Anda ===")
                ada = False

                for item in Riwayat:
                    usr, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, pengaju = item
                    if usr == usrname_login:
                        print(
                            f"{hari}, {tanggal}-{bulan}-{tahun} "
                            f"Jam {jam_mulai}-{jam_selesai} (dengan {pengaju})"
                        )
                        ada = True

                if not ada:
                    print("Belum ada riwayat pertemuan.")

                input("Tekan Enter untuk kembali...")
                cls()

            # =================== 7. LOGOUT ===================
            elif choose2 == "7":
                print("Logout berhasil.")
                cls()
                break

            else:
                print("Pilihan tidak tersedia.")
                cls()

    elif chooseStart == "3":
        print("Terima kasih telah menggunakan Comeet!")
        break

    else:
        print("Pilihan tidak tersedia.")
        cls()