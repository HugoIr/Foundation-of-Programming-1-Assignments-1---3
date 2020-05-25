# NOTES : Lokasi ekspor file harus disesuaikan dengan lokasi penyimpanan user (Ubah pada fungsi ekspor)

import csv
from pandas import DataFrame
import matplotlib.pyplot as mpl
impdic={}

# Untuk mengimpor csvfile
def impor(csvfile):
    try:
        with open(csvfile, 'r') as rfile:       # CSV-File dinamakan sebagai rfile
            read= csv.reader(rfile)             # Membaca rfile
            try:
                impdicc={}              # Membuat dictinary sebagai tempat penampungan sementara
                for baris in read:
                    impdicc[baris[0]] = {'tipe':baris[1],'provinsi':baris[2],'url':baris[3]}     # Memasukkan per baris per item yang dipisahkan dengan koma ke dalam dictionary
                impdic.update(impdicc)  # Mengupdate dictionary dengan impdicc
                print('Terimpor {} baris'.format(len(impdicc)))
            except:
                print('Format tiap baris file csv adalah <namawarisanbudaya>,<tipe>,<provinsi>,<referenceurl>')
    except FileNotFoundError:
        print('File tidak dapat ditemukan(file harus satu lokasi dengan file python TP3)')
        
def carinama(nama,dic):
    if len(dic) !=0:
        global outs
        outs= []                    # Sebagai list output
        if nama=='*':
            for i in dic:
                outs.clear()        # Membersihkan list output karena hendak digunakan berulang kali
                outs.append(i)
                outs.extend(list(dic[i].values()))
                print(','.join(outs))       # Mengeprint item dengan dipisahkan oleh koma
                
        elif not(nama in dic):              # Jika nama tidak terdapat di dalam dictionary
            print(nama,'tidak ditemukan')
        else:
            for i in dic:
                if i == nama:
                    outs.append(nama)
                    outs.extend(list(dic[i].values()))
                    print(','.join(outs))   # Mengeprint item dengan dipisahkan oleh koma
    else:
        print('File belum diimpor')

def cari(item,dic,val):
    if len(dic) !=0:
        counter= 0              # Sebagai base counter
        for i in dic:
            if item == dic[i][val]:
                counter += 1    # Untuk menghitung jumlah item
                print('{},{}'.format(i,','.join(dic[i].values())))      
        if val=='tipe':
            print('*Ditemukan {} {}*'.format(counter,item))
        elif val=='provinsi':
            print('*Ditemukan {} warisan budaya*'.format(counter))
    else:
        print('File belum diimpor')
def stat(dic,lsin):
    if len(dic) !=0:
        if len(lsin) ==1:
            print('Terdapat',len(dic),'warisan budaya')     # Menghitung banyaknya keys dalam dictionary
        else:
            print('Perintah tidak menerima argumen')
    else:
        print('File belum diimpor')
        
def itemnorep(dic,item):
    items= set()            # Sehingga tidak ada perulangan
    for i in dic:
        items.add(dic[i][item])     # Menambahkan item dari dictionary ke set items
    global itemls           # Digunakan juga pada fungsi itemstat
    itemls= list(items)             # Membuat copy-an set items dalam bentuk list

def itemhitung(dic,lst,item):
    global freq     # Digunakan juga pada fungsi itemstat
    freq=[]
    for i in range(len(lst)):
        cnt=0
        for j in dic:
            if dic[j][item] == lst[i]:      # Jika tipe dalam dic sama dengan tipe dalam list
                cnt+=1
        freq.append(cnt)                    # Menambahkan jumlah ke dalam list
        
# Fungsi reverse tuple on list
def rvstol(lst):
    return [t[::-1] for t in lst]   # Mengembalikan urutan elemen tuple yang di-reverse

# Fungsi untuk menghitung statistik
def itemstat(dic,itemstr,lsin):
    if len(dic) != 0:
        if len(lsin) == 1:
            itemnorep(dic,itemstr)
            itemhitung(dic,itemls,itemstr)
            statls=[]       
            for i in range(len(itemls)):
                statls.append((itemls[i],freq[i]))      # Menambahkan tuple yang berisikan item beserta frekuensinya
            out= rvstol(list(reversed(sorted(rvstol(statls)))))       # Membalikan isi tuple dalam list, kemudian di-sort, kemudian di-
                                                                      # kemudian dibalikkan lagi isi tuple (Sort dari terbesar-terkecil)
            print(out)
            mpl.title(' Statistik {} warisan budaya Indonesia'.format(itemstr), fontsize = 15)
            mpl.bar(range(len(out)),[i[1] for i in out])        # Membuat bar sumbu y dari nilai list frekuensi
            mpl.xticks(range(len(out)),[i[0] for i in out])     # Membuat bar sumbu x dari nilai list nama item
            mpl.show()                                          # Menampilkan matplotlib
        else:
            print('Perintah tidak menerima argumen')
    else:
        print('File belum diimpor')

def tambah(item,dic):
    try:
        c=0     # Sebagai counter
        # Untuk mengetahui apakah terdapat penggunaan tanda ;;; secara berturut-turut dengan jumlah lebih dari 3 
        for i in range(len(item)-1):
            if item[i]==';' and item[i+1]==';':
                c+=1
                if c>2:
                    print('Ketik nama;;;tipe;;;provisi;;;referenceurl')
                    break
            elif item[i] ==';' and item[i+1] != ';':
                c=0
        if c<=2:
            item= item.split(';;;')
            dic[item[0]] = {'tipe':item[1],'provinsi':item[2],'url':item[3]}        # Menambahkan item pada dictionary
            print(item[0],'ditambahkan')
    except IndexError:
            print('Ketik nama;;;tipe;;;provisi;;;referenceurl')

def update(item,dic):
    try:
        c=0     # Sebagai counter
        # Untuk mengetahui apakah terdapat penggunaan tanda ;;; secara berturut-turut dengan jumlah lebih dari 3 
        for i in range(len(item)-1):
            if item[i]==';' and item[i+1]==';':
                c+=1
                if c>2:
                    print('Ketik nama;;;tipe;;;provisi;;;referenceurl')
                    break
            elif item[i] ==';' and item[i+1] != ';':
                c=0
        if c<=2:    
            item= item.split(';;;')
            if item[0] in dic:
                dic.update({item[0]:{'tipe':item[1],'provinsi':item[2],'url':item[3]}})     # Update item pada dictionary
                print(item[0],'diupdate')
            else:           # Jika item tidak ditemukan dalam dictionary
                print('{} tidak ditemukan atau format penulisan tidak tepat'.format(item[0]))
    except IndexError:
        print('Ketik nama;;;tipe;;;provinsi;;;referenceurl')
        
def hapus(item, dic):
    try:
        dic.pop(item)   # Menghapus key item pada dictionary
        print(item,'dihapus')
    except KeyError:
        print('{} tidak ditemukan'.format(item))
        
# Membuat dictionary yang berisikan list sehingga urutan data tetap sama
def dictipe2(dic):
    global de
    de={}               # Sebagai dictionary tipe 2
    for i in impdic:
        d,t,p,u=[],[],[],[]     # Membuat list per tipe
        for j in impdic:        # Menambahkan tipe dari tiap keys ke dalam list
            d.append(j)
            t.append(impdic[j]['tipe'])
            p.append(impdic[j]['provinsi'])
            u.append(impdic[j]['url'])
        de['Nama'],de['Tipe'],de['Provinsi'],de['URL']= d,t,p,u     # Menambahkan list ke dalam dictionary

def ekspor(namafile,dic1,dic2):
    df= DataFrame(dic2, columns=['Nama','Tipe','Provinsi','URL'])       # Merepresentasikan data dalam bentuk baris dan kolom
    export= df.to_csv(r'C:\Python\{}'.format(namafile),index=False, header=False)       # Mengekspor dataframe ke dalam file csv (Lokasi ekspor C:\Python\)
    print('Terekspor {} baris'.format(len(dic1)))
def bantuan(lsin):
    if len(lsin) ==1:
        perintah=['IMPOR','EKSPOR','CARINAMA','CARITIPE','CARIPROV','STAT','STATTIPE','STATPROV','TAMBAH','UPDATE','HAPUS','KELUAR']
        keterangan=['Mengimpor file csv dengan format tiap barisnya \'nama,tipe,provinsi,reference url\'','Mengekspor hasil ke dalam file baru',
                    'Mencari berdasarkan nama budaya','Mencari berdasarkan tipe budaya','Mencari berdasarkan provinsi budaya','Menampilkan jumlah warisan budaya',
                    'Menampilkan nama tipe budaya dari yang terbanyak + bar statistiknya',
                    'Menampilkan nama provinsi budaya dari yang terbanyak + bar statistiknya',
                    'Menambahkan warisan budaya dengan format nama;;;tipe;;;provinsi;;;reference url','Mengupdate warisan budaya dengan format nama;;;tipe;;;provinsi;;;reference url',
                    'Menghapus data budaya','Untuk menghentikan program']
        print('-'*95)
        print('{:>10}  |  {:<100}'.format('Perintah','Keterangan'))
        print('-'*95)
        for i in range(len(perintah)):
            print('{:>10}  |  {:<100}'.format(perintah[i],keterangan[i]))       # Menampilkan perintah beserta keterangan dalam bentuk menyerupai tabel
        print('-'*95)
    else:
        print('Perintah tidak menerima argumen')
def main():
    print('#####\nBudayaKB Lite v1.0\n~Kalau bukan kita yang melestarikan budaya, siapa lagi?~\nKetik BANTUAN untuk menampilkan bantuan')
    while True:
        try:
            inp= input('#####\nMasukkan perintah: ')
            lsin= inp.split()
            if len(lsin) > 2:
                lsin =[lsin[0],' '.join([lsin[i] for i in range(1,len(lsin))])]        # Menggabungkan list[1] sampai list[n] menjadi sebuah string

            if lsin[0] == 'KELUAR':
                if len(lsin) ==1:
                    print('~Sampai jumpa, jangan lupa mencintai warisan budaya Indonesia!~')
                    break
                else:
                    print('Perintah tidak menerima argumen')
            elif lsin[0] == 'BANTUAN':
                bantuan(lsin)
            elif lsin[0] == 'STAT':
                stat(impdic,lsin)
            elif lsin[0] == 'STATTIPE':
                itemstat(impdic,'tipe',lsin)
            elif lsin[0] == 'STATPROV':
                itemstat(impdic,'provinsi',lsin)
            elif lsin[0] == 'IMPOR':
                impor(lsin[1])
            elif lsin[0] == 'CARINAMA':
                carinama(lsin[1],impdic)
            elif lsin[0] == 'CARITIPE':
                cari(lsin[1],impdic,'tipe')
            elif lsin[0] == 'CARIPROV':
                cari(lsin[1],impdic,'provinsi')
            elif lsin[0] == 'EKSPOR':
                dictipe2(impdic)
                ekspor(lsin[1],impdic,de)
            elif lsin[0] == 'TAMBAH':
                tambah(lsin[1],impdic)
            elif lsin[0] == 'HAPUS':
                hapus(lsin[1],impdic)
            elif lsin[0] == 'UPDATE':
                update(lsin[1],impdic)
           
            else:
                print('Perintah tidak ditemukan')
        except IndexError:
            print('Ketik BANTUAN untuk menampilkan bantuan')

if __name__ == '__main__':
    main()
