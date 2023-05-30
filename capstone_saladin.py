# Buku Kuning

buku_kuning = {
    '0213108080' : ['Hotel', 'A One Hotel', 'Albert', 'Jalan Wahid Hasyim No. 80', 'Jakarta'],
    '03129618888' : ['Hotel', 'Neo Tugu Pahlawan', 'Resti', 'Jalan Gunung Sahari Raya No.1', 'Surabaya'],
    '02287348888' : ['Hotel', 'The Trans Luxury Hotel', 'Ami', 'Jalan Gatot Subroto No.289', 'Bandung'],
    '02273107998' : ['Hotel', 'The Papandayan', 'Boy', 'Jalan Gatot Subroto No.83', 'Bandung'],
    '02154372874' : ['Rumah Sakit', 'RSUD Cengkareng', 'Erick', 'Jalan Bumi Cengkareng Indah No.1', 'Jakarta'],
    '02222552766' : ['Rumah Sakit', 'RS Lautan Api', 'Saladin', 'Jalan Satu Maret No. 1', 'Bandung'],
    '03155687901' : ['Rumah Sakit', 'RS Bung Tomo', 'Samuel', 'Jalan Tugu Pahlawan No.15', 'Surabaya'],
    '02125102449' : ['Bank', 'Bank Rakyat Indonesia', 'Hartono', 'Jalan ABC No.55', 'Jakarta'],
    '02212345678' : ['Bank', 'Bank BCA KCP Burangrang', 'Septian', 'Jalan Burangrang No.44', 'Bandung'],
    '08562001905' : ['Bank', 'Bank Hartono Bersaudara', 'Agus', 'Jalan Jakarta No.86', 'Surabaya']
}


def menu_utama():
    while True :
        inp = input('''
Silahkan pilih pilihan menu :
        
    1. Menambahkan Data Nomor Telepon
    2. Melihat Data Nomor Telepon
    3. Mengganti Data Nomor Telepon
    4. Menghapus Data Nomor Telepon
    5. Keluar dari Aplikasi
        
Pilihan menu Anda adalah : ''')
        if inp == '1' :
            create('1','2','3')
        elif inp == '2' :
            read('1','2','3')
        elif inp == '3' :
            update('1','2')
        elif inp == '4' :
            delete('1','2','3')
        elif inp == '5' :
            break
        else :
            print('\nPilihan Anda tidak terdapat di daftar menu\n')

def create(x, y, z):
    while True :
        inp_create = input('''
Silahkan pilih pilihan berikut untuk menambahkan data :
    
    1. Menambahkan 1 Data Nomor Telepon
    2. Menambahkan Banyak Data Nomor Telepon Sekaligus
    3. Kembali ke Menu Utama
    
Pilihan menu Anda adalah : ''')
        
        if inp_create == x :
            create_data = [input('\nMasukan Bidang Industri/Jasa : '), input('Masukan Nama Perusahaan : '), input('Masukkan Nama Pimpinan : '), input('Masukkan Alamat Perusahaan/Jasa : '), input('Masukkan Domisili Perusahaan : ')]
            jumlah_loop = len(create_data)
            while jumlah_loop != 0 :
                for data_kosong in create_data:
                    if data_kosong != '' :
                        jumlah_loop -=1
                    else:
                        print('\nAnda Tidak Memasukkan Data Secara Lengkap, Tolong Masukkan Data dengan Benar\n')
                        create_data = [input('\nMasukan Bidang Industri/Jasa : '), input('Masukan Nama Perusahaan : '), input('Masukkan Nama Pimpinan : '), input('Masukkan Alamat Perusahaan/Jasa : '), input('Masukkan Domisili Perusahaan : ')]
                        jumlah_loop = len(create_data)
                        break
            
            for create_index_kalimat, create_kalimat in enumerate(create_data) :
                create_data[create_index_kalimat] = create_kalimat.title()
            while True:
                create_number = input('Masukkan Nomor Telepon Perusahaan/Jasa : ')
                if create_number != '':
                    create_iterasi = len(create_number)
                    while create_iterasi !=0 :
                        if create_number.isdigit() :
                            while True :
                                if create_number in buku_kuning.keys():
                                    print('\nNomor Tersebut Sudah Ada, Silahkan Masukkan Nomor yang Lain\n')
                                    create_number = input('Masukkan Nomor Telepon Perusahaan/Jasa : ')
                                    break
                                else :
                                    create_iterasi -= 1
                                    break
                        else :
                            print('\nNomor Tersebut Bukanlah Angka, Silahkan Masukkan Nomor yang Benar\n')
                            create_number = input('Masukkan Nomor Telepon Perusahaan/Jasa : ')
                    break
                else :
                    print('\nAnda Tidak Memasukkan Nomor Apapun, Tolong Masukkan Nomor Telepon\n')
            
            create_header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
            while True :
                create_konfirmasi = input(
f'''\nApakah Anda yakin menambahkan data berikut :

{create_header[0]:<30}|{create_header[1]:<30}|{create_header[2]:<30}|{create_header[3]:<40}|{create_header[4]:<15}|{create_header[5]:<20}
{create_data[0]:<30}|{create_data[1]:<30}|{create_data[2]:<30}|{create_data[3]:<40}|{create_data[4]:<15}|{create_number:<20}

Iya/Tidak? ''')
            
                if create_konfirmasi.upper() == 'IYA':
                    buku_kuning.update({create_number : create_data})
                    break
                elif create_konfirmasi.upper() == 'TIDAK':
                    break
                else :
                    print('\nPilihan Anda tidak terdapat di daftar menu\n')
            
        elif inp_create == y :
            create_data_kolektif = [input('Masukan Bidang Industri/Jasa Dipisah Koma Secara Terurut : '), input('Masukan Nama Perusahaan/Jasa Dipisah Koma Secara Terurut : '), input('Masukkan Nama Pimpinan Dipisah Koma Secara Terurut : '), input('Masukkan Alamat Perusahaan/Jasa Dipisah Koma Secara Terurut : '), input('Masukkan Domisili Perusahaan Dipisah Koma Secara Terurut : ')]
            jumlah_loop_kolektif = len(create_data_kolektif)
            while jumlah_loop_kolektif != 0 :
                for data_kosong_kolektif in create_data_kolektif:
                    if data_kosong_kolektif != '' :
                        jumlah_loop_kolektif -=1
                    else:
                        print('\nAnda Tidak Memasukkan Data Secara Lengkap, Tolong Masukkan Data dengan Benar\n')
                        create_data_kolektif = [input('Masukan Bidang Industri/Jasa Dipisah Koma Secara Terurut : '), input('Masukan Nama Perusahaan/Jasa Dipisah Koma Secara Terurut : '), input('Masukkan Nama Pimpinan Dipisah Koma Secara Terurut : '), input('Masukkan Alamat Perusahaan/Jasa Dipisah Koma Secara Terurut : '), input('Masukkan Domisili Perusahaan Dipisah Koma Secara Terurut : ')]
                        jumlah_loop_kolektif = len(create_data_kolektif)
                        break
                    
            create_list_kosong = []
            for create_index, create_nilai in enumerate(create_data_kolektif) :
                create_data_kolektif[create_index] = create_nilai.split(',')
                for huruf in create_data_kolektif[create_index] :
                    if huruf[0] == ' ' :
                        huruf = huruf.replace(' ', '', 1)
                        huruf = huruf.title()
                        create_list_kosong.append(huruf)
                    else :
                        huruf = huruf.title()
                        create_list_kosong.append(huruf)
                create_data_kolektif[create_index] = create_list_kosong.copy()
                create_list_kosong.clear()

            create_values = (list(zip(create_data_kolektif[0],create_data_kolektif[1],create_data_kolektif[2],create_data_kolektif[3],create_data_kolektif[4])))
            
            while True :
                create_key = penghilang_spasi()
                if create_key != '' :
                    create_jumlah_loop = len(create_key)
                    while create_jumlah_loop != 0 :
                        if create_jumlah_loop >= len(create_values) :
                            for create_nomor in create_key :
                                if create_nomor.isdigit() :
                                    if create_nomor in buku_kuning.keys():
                                        print('\nNomor Tersebut Sudah Ada, Silahkan Masukkan Nomor yang Lain\n')
                                        create_key = penghilang_spasi()
                                        create_jumlah_loop = len(create_key)
                                        break
                                    else :
                                        create_jumlah_loop -= 1
                                else :
                                    print('\nNomor Tersebut Bukanlah Sebuah Angka, Silahkan Masukkan Nomor yang Benar\n')
                                    create_key = penghilang_spasi()
                                    create_jumlah_loop = len(create_key)
                                    break
                        else :
                            print('\nJumlah Nomor yang Anda Masukkan Kurang dari Jumlah Data, Silahkan Masukkan Kembali dengan Jumlah Nomor Sesuai dengan Jumlah Data\n')                    
                            create_key = penghilang_spasi()
                            create_jumlah_loop = len(create_key)
                    break
                else :
                    print('\nAnda Tidak Memasukkan Nomor Apapun, Tolong Masukkan Nomor Telepon\n')

            
            create_header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
            while True :
                print(
f'''\nApakah Anda yakin menambahkan data berikut :

{create_header[0]:<30}|{create_header[1]:<30}|{create_header[2]:<30}|{create_header[3]:<40}|{create_header[4]:<15}|{create_header[5]:<20}''')
                for i in range(len(create_values)) :
                    print(f'''
{create_values[i][0]:<30}|{create_values[i][1]:<30}|{create_values[i][2]:<30}|{create_values[i][3]:<40}|{create_values[i][4]:<15}|{create_key[i]:<20}''')
                    
                create_konfirmasi = input('''
Iya/Tidak? ''')
                if create_konfirmasi.upper() == 'IYA':
                    for create_index in range(len(create_values)) :
                        buku_kuning.update({create_key[create_index] : create_values[create_index]})
                    break
                elif create_konfirmasi.upper() == 'TIDAK':
                    break
                else :
                    print('\nPilihan Anda tidak terdapat di daftar menu\n')

        elif inp_create == z :
            break
        else :
            print('\nPilihan Anda tidak terdapat di daftar menu\n')

def read(x,y,z):
    while True :
        
        inp_read = input('''
Silahkan pilih pilihan berikut untuk menampilkan data :
    
    1. Menampilkan Keseluruhan Data Nomor Telepon
    2. Menampilkan Data Nomor Telepon Berdasarkan Kata Kunci
    3. Kembali ke Menu Utama
    
Pilihan menu Anda adalah : ''')
        
        if inp_read == x :
            read_header()
            for read_values in buku_kuning:
                print(f'''
{buku_kuning[read_values][0]:<30}|{buku_kuning[read_values][1]:<30}|{buku_kuning[read_values][2]:<30}|{buku_kuning[read_values][3]:<40}|{buku_kuning[read_values][4]:<15}|{read_values:<20}''')
        
        elif inp_read == y :
            read_inp_kata_kunci = input('\nSilahkan Masukkan Kata Kunci : ')
            read_header()
            for read_values in buku_kuning:
                if read_inp_kata_kunci.title() in buku_kuning[read_values] :
                    print(f'''
{buku_kuning[read_values][0]:<30}|{buku_kuning[read_values][1]:<30}|{buku_kuning[read_values][2]:<30}|{buku_kuning[read_values][3]:<40}|{buku_kuning[read_values][4]:<15}|{read_values:<20}''')

        elif inp_read == z :
            break
        
        else :
            print('\nPilihan Anda tidak terdapat di daftar menu\n')

def update(x,y):
    while True :
        inp_update = input('''
Silahkan pilih pilihan berikut untuk mengganti data :
    
    1. Mengganti Data Nomor Telepon
    2. Kembali ke Menu Utama
    
Pilihan menu Anda adalah : ''')
        
        if inp_update == x :
            update_header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
            print(
f'''\nBerikut Adalah List Nomor Telepon yang Telah Terdaftar :\n
{update_header[0]:<30}|{update_header[1]:<30}|{update_header[2]:<30}|{update_header[3]:<40}|{update_header[4]:<15}|{update_header[5]:<20}''')
            for update_values in buku_kuning :
                print(f'''
{buku_kuning[update_values][0]:<30}|{buku_kuning[update_values][1]:<30}|{buku_kuning[update_values][2]:<30}|{buku_kuning[update_values][3]:<40}|{buku_kuning[update_values][4]:<15}|{update_values:<20}''')
            
            while True :
                update_inp_nomor = input('\nSilahkan Masukkan Nomor Telepon Untuk Mengganti Data : ')
                if update_inp_nomor in buku_kuning.keys() :
                    update_data = [input('\nMasukan Bidang Industri/Jasa : '), input('Masukan Nama Perusahaan : '), input('Masukkan Nama Pimpinan : '), input('Masukkan Alamat Perusahaan/Jasa : '), input('Masukkan Domisili Perusahaan : ')]
                    for update_index_kalimat, update_kalimat in enumerate(update_data) :
                        update_data[update_index_kalimat] = update_kalimat.title()
                    break
                else :
                    print('\nNomor yang Anda Masukkan Tidak Ada Dalam Daftar Yellowpages, Silahkan Masukkan Nomor yang Telah Terdaftar\n')
            while True :
                create_konfirmasi = input(
f'''\nApakah Anda Yakin Ingin Mengupdate Data Berikut :

{update_header[0]:<30}|{update_header[1]:<30}|{update_header[2]:<30}|{update_header[3]:<40}|{update_header[4]:<15}|{update_header[5]:<20}
{update_data[0]:<30}|{update_data[1]:<30}|{update_data[2]:<30}|{update_data[3]:<40}|{update_data[4]:<15}|{update_inp_nomor:<20}

Iya/Tidak? ''')
                if create_konfirmasi.upper() == 'IYA':
                    buku_kuning.update({update_inp_nomor : update_data})
                    break
                elif create_konfirmasi.upper() == 'TIDAK':
                    break
                else :
                    print('\nPilihan Anda tidak terdapat di daftar menu\n')

        elif inp_update == y :
            break

        else :
            print('\nPilihan Anda tidak terdapat di daftar menu\n')

def delete(x, y, z):
    while True :
        inp_delete = input('''
Silahkan pilih pilihan berikut untuk menghapus data :
    
    1. Menghapus 1 Data Nomor Telepon
    2. Menghapus Banyak Nomor Telepon Sekaligus
    3. Kembali ke Menu Utama
    
Pilihan menu Anda adalah : ''')
        if inp_delete == x :
            delete_header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
            print(
f'''\nBerikut Adalah List Nomor Telepon yang Telah Terdaftar :\n
{delete_header[0]:<30}|{delete_header[1]:<30}|{delete_header[2]:<30}|{delete_header[3]:<40}|{delete_header[4]:<15}|{delete_header[5]:<20}''')
            for delete_values in buku_kuning :
                print(f'''
{buku_kuning[delete_values][0]:<30}|{buku_kuning[delete_values][1]:<30}|{buku_kuning[delete_values][2]:<30}|{buku_kuning[delete_values][3]:<40}|{buku_kuning[delete_values][4]:<15}|{delete_values:<20}''')
            
            while True :
                delete_inp_nomor = input('\nSilahkan Masukkan Nomor Telepon Untuk Menghapus Data : ')
                if delete_inp_nomor not in buku_kuning.keys():
                    print('\nNomor yang Anda Masukkan Tidak Ada Dalam Daftar Yellowpages, Silahkan Masukkan Nomor yang Telah Terdaftar\n')
                else :
                    while True :
                        delete_konfirmasi = input(
f'''\nApakah Anda Yakin Ingin Menghapus Data Berikut :

{delete_header[0]:<30}|{delete_header[1]:<30}|{delete_header[2]:<30}|{delete_header[3]:<40}|{delete_header[4]:<15}|{delete_header[5]:<20}
{buku_kuning[delete_inp_nomor][0]:<30}|{buku_kuning[delete_inp_nomor][1]:<30}|{buku_kuning[delete_inp_nomor][2]:<30}|{buku_kuning[delete_inp_nomor][3]:<40}|{buku_kuning[delete_inp_nomor][4]:<15}|{delete_inp_nomor:<20}

Iya/Tidak? ''')
                        if delete_konfirmasi.upper() == 'IYA':
                            buku_kuning.pop(delete_inp_nomor)
                            break
                        elif delete_konfirmasi.upper() == 'TIDAK':
                            break
                        else :
                            print('\nPilihan Anda tidak terdapat di daftar menu\n')
                    break

        elif inp_delete == y :
            delete_header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
            print(
f'''\nBerikut Adalah List Nomor Telepon yang Telah Terdaftar :\n
{delete_header[0]:<30}|{delete_header[1]:<30}|{delete_header[2]:<30}|{delete_header[3]:<40}|{delete_header[4]:<15}|{delete_header[5]:<20}''')
            for delete_values in buku_kuning :
                print(f'''
{buku_kuning[delete_values][0]:<30}|{buku_kuning[delete_values][1]:<30}|{buku_kuning[delete_values][2]:<30}|{buku_kuning[delete_values][3]:<40}|{buku_kuning[delete_values][4]:<15}|{delete_values:<20}''')
            list_delete_number = []
            while True :
                print('Masukkan Daftar Nomor yang Ingin Dihapus')
                delete_key = penghilang_spasi()
                for delete_number in delete_key :
                    if delete_number not in buku_kuning.keys() :
                        continue
                    else :
                        list_delete_number.append(delete_number)

                while True :
                    delete_header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
                    print(
    f'''\nApakah Anda yakin menghapus data berikut :

    {delete_header[0]:<30}|{delete_header[1]:<30}|{delete_header[2]:<30}|{delete_header[3]:<40}|{delete_header[4]:<15}|{delete_header[5]:<20}''')
                    for i_del, n_del in enumerate(list_delete_number) :
                        print(f'''
    {buku_kuning[n_del][0]:<30}|{buku_kuning[n_del][1]:<30}|{buku_kuning[n_del][2]:<30}|{buku_kuning[n_del][3]:<40}|{buku_kuning[n_del][4]:<15}|{list_delete_number[i_del]:<20}''')
                        
                    delete_konfirmasi = input('''
    Iya/Tidak? ''')
                    if delete_konfirmasi.upper() == 'IYA':
                        for del_data in list_delete_number :
                            buku_kuning.pop(del_data)
                        break
                    elif delete_konfirmasi.upper() == 'TIDAK':
                        break
                    else :
                        print('\nPilihan Anda tidak terdapat di daftar menu\n')
                break
        
        elif inp_delete == z :
            break

        else :
            print('\nPilihan Anda tidak terdapat di daftar menu\n')

def penghilang_spasi():
    while True :
        create_number_kolektif = input('Masukan Nomor Telepon Perusahaan/Jasa Dipisah Koma Secara Terurut : ')
        if create_number_kolektif != '' :
            notelp_list_kosong = []
            create_number_kolektif = create_number_kolektif.split(',')
            for index_notelp, notelp in enumerate(create_number_kolektif) :
                if notelp[0] == ' ' :
                    notelp = notelp.replace(' ', '', 1)
                    notelp_list_kosong.append(notelp)
                else :
                    notelp_list_kosong.append(notelp)
                for notelp_final in notelp_list_kosong :
                    create_number_kolektif[index_notelp] = notelp_final
                notelp_list_kosong.clear()
            break
        else :
            print('\nAnda Tidak Memasukkan Nomor Apapun, Tolong Masukkan Nomor Telepon\n')
    return create_number_kolektif

def read_header():
    header = ['Bidang Industri/Jasa', 'Nama Perusahaan', 'Nama Pimpinan', 'Alamat', 'Domisili', 'Nomor Telepon']
    print(
f'''\nBerikut Adalah List Nomor Telepon yang Telah Terdaftar :\n
{header[0]:<30}|{header[1]:<30}|{header[2]:<30}|{header[3]:<40}|{header[4]:<15}|{header[5]:<20}''')

menu_utama()