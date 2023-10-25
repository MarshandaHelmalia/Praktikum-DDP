#soal no 2
#match case luas bangun datar

ket = '''selamat datang di aplikasi menghitung luas bangun datar, silahkan masukkan pilihan:
    pilih 1 untuk menghitung luas persegi
    pilih 2 untuk menghitung luas lingkaran
    pilih 3 untuk menghitung luas segitiga 
    
    pilih angka = '''

luasyangingindihitung = input (ket)

match luasyangingindihitung:
    case "1":
            print ("pilih 1 untuk menghitung luas persegi")
            sisi = int(input ("masukkan angka untuk sisi"))
            luaspersegi = sisi*sisi
            print ("luas persegi dengan sisi", sisi,"adalah", luaspersegi)
    case "2":
            print ("pilih 2 untuk menghitung luas lingkaran")
            r = int(input ("masukkan angka untuk jari-jari"))
            luaslingkaran = 3.14*r**2
            print ("luas lingkaran dengan jari jari",r,"adalah", luaslingkaran)
    case "3":
            print ("pilih 3 untuk menghitung luas segitiga")
            alas = int(input ("masukkan angka untuk alas"))
            tinggi = int(input ("masukkan angka untuk tinggi"))
            luassegitiga = 0.5*alas*tinggi
            print ("luas segitiga dengan alas",alas,"dan tinggi", tinggi,"adalah", luassegitiga)
    case _:
            print ("anda salah memilih")
