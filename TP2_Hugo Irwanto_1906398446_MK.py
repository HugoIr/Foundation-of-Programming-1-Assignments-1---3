import string           # Untuk memudahkan dalam memfilter symbol yang ada
import matplotlib.pyplot as mthplb      # Untuk membuat grafik bar

# Untuk tampilan dan panduan user
print('=======================================================\nMasukkan pesan: (Untuk berhenti masukkan string kosong)\n=======================================================')


list1=[]                        # List untuk penampungan hasil pemisahan kalimat menjadi kata
list3=[]                        # List untuk penampungan setelah di filter stopword
list4=[]                        # List untuk penampungan setelah di filter symbol
list_norep=[]                   # Untuk menampung kata tanpa perulangan dari list 3
list_freq =[]                   # Sebagai list penampung jumlah frekuensi kata


# Untuk mengubah dari kalimat utuh menjadi list yang berisikan kata per elemennya
def lineToWord(line):
    mdf_line= line.lower()
    slot1= mdf_line.split(' ')
    list1.extend(slot1)

# Untuk membuka file
def showFile(txtfile):
    f= open(txtfile, 'r')
    global list2 
    list2= f.read().split('\n')     
       
# Fungsi untuk menyaring stopword dari list kata(list1)
def filterStopword(list_1,list_2):
    for a in list_1:
        if not a in list_2:
            list3.append(a)     # Menampung kata tanpa konjungsi dalam list3

# Fungsi untuk membersihkan whitestring 
def removeWhitestring(test_list):       
    test_list = list(filter(None, test_list)) 
    return test_list

# Fungsi untuk menambahkan kata  yang sudah difilter dari symbol ke dalam list
def filterAppendWord(string,list_destiny):
    temp_word= string.translate(filterer)
    list_destiny.append(temp_word)

# Fungsi untuk kasus
def ifThereIsStrip(string,list_destiny):
    if '-' in string:
        ind1= string.index('-')
        if (string[ind1-1].isalpha() or string[ind1-1].isdigit()) and (string[ind1+1].isalpha() or string[ind1+1].isdigit()):
            if string.index('-') != 0 or string.index('-') != (len(string)-1):
                list_destiny.append(string)
        else:
            filterAppendWord(string,list_destiny)
        
    else:
        list_destiny.append(string)
        
# Fungsi untuk membersihkan simbol dari list
def filterSymbol(list_x,list_destiny):
    global filterer
    filterer= str.maketrans('','',string.punctuation)
    for a in list_x:
        #  Untuk menghilangkan symbol pengapit kata tanpa menghilangkan tanda  
        if ('-' in a) and (a[0] in string.punctuation and a[-1] in string.punctuation):
            mod_a= a.replace(a[0],'')
            mod_a= mod_a.replace(a[-1],'')
            ifThereIsStrip(mod_a,list_destiny)
        # Untuk kasus kata perulangan dengan simbol strip
        elif ('-' in a) and (not(a[0] in string.punctuation or a[-1] in string.punctuation)):
            ifThereIsStrip(a,list_destiny)
        # Untuk memfilter simbol selain kondisi pengecualian diatas
        else:
            filterAppendWord(a,list_destiny)

# Fungsi untuk memfilter kata yang berulang
def filterMultipleWord(list_1,list_destiny):
    index=0
    for i in list_1:
        if not(i in list_1[:index]):
            list_destiny.append(i)      # Menampung hasil filter kata berulang dalam list_destiny(list_norep)
        index += 1

# Fungsi untuk menghitung frekuensi kata
def freqWord(list_count,list_counter):
    for a in list_counter:
        freq= list_count.count(a)
        list_freq.append(freq)      # Menampung hasil perhitungan frekuensi dalam list_counter(list_freq)
        
# Menampilkan tabel 
def tabelFreq():
    dash= '-' * 34
    print('Distribusi frekuensi kata:')
    print(dash)
    print('{:<3} {:<18s} {:<18s}'.format('No','Kata', 'Frekuensi'))
    print(dash)
    for i in range(len(list_norep)):
        print('{:>3} {:<18s} {:<18d} '.format(i+1, list_norep[i], list_freq[i]))

# Menampilkan grafik dengan menggunakan module matplotlib    
def grafikFreq():
    mthplb.figure('Grafik 1')
    list_norep.reverse()
    list_freq.reverse()
    mthplb.barh(list_norep,list_freq)
    mthplb.title('Frekuensi Kemunculan Kata',fontsize=12)
    mthplb.xlabel('Frekuensi',fontsize=11)
    mthplb.tight_layout()
    mthplb.show()
    mthplb.close()

# Fungsi program utama
def main():
    global list1,list4,list3,list_norep,list_freq   
    while True:             # Untuk membuat loop
        pesan=input("Pesan: ")
        if pesan !='':              # Untuk melanjutkan loop input pesan jika pesan yang dimasukkan adalah selain string kosong
            lineToWord(pesan)       # Menambahkan pesan ke dalam list 
            
            
        else:
            showFile('TP2_stopword.txt')            # Memanggil file TP2_Stopword.txt
            list1 = removeWhitestring(list1)        # Membersihkan whitestring dari list1
            filterStopword(list1,list2)             # Menghilangkan konjungsi dari list1 dan menambahkannya ke dalam list baru(list3)
            filterSymbol(list3,list4)               # Menghilangkan simbol yang tidak diperlukan dan menambahkannya ke dalam list baru
            list4= removeWhitestring(list4)         # Membersihkan whitestring dari list4
            filterMultipleWord(list4,list_norep)    # Membuat list baru yang berisikan kata tanpa perulangan
            freqWord(list4,list_norep)              # Membuat list baru yang berisikan frekuensi dari list_norep
            tabelFreq()                             # Menampilkan tabel frekuensi kemunculan kata
            grafikFreq()                            # Menampilkan grafik frekuensi kemunculan kata
            break

# Menjalankan program utama
if __name__ == "__main__":          # Jika module __main__ ,maka akan dijalankan
    main()
