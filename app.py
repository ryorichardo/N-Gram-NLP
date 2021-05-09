import re
from BM import searchBM
import time

# Path dataset, ubah sesuai lokasi dataset yang dituju
path = "data\\ind_mixed_2012_300K-sentences.txt"

# Input
n = int(input("Masukkan jenis N gram (range 2 sampai 4): "))
while (n < 2 or n > 4):
    n = int(input("N di luar range! Masukkan jenis N gram (range 2 sampai 4): "))
string = str(input("Masukkan teks: "))

# Regex untuk mengambil karakter alfabet saja
regex = re.compile("[^a-zA-Z \.]")

# Pemrosesan string input
string_alpha_only = regex.sub("", string)                       # Membuang karakter selain alphabet dan titik
string_no_multi_spaces = re.sub(" +", " ", string_alpha_only)   # Membuang ekstra spasi
string_lowered = string_no_multi_spaces.lower()                 # Lowercase
m = len(string_lowered.split())                                 # Menyimpan jumlah kata
string_last_n = string_lowered.split()[(m-n+1):]                # Mengambil last (n-1) words
string_final = " ".join(string_last_n)                          # Join dalam satu string

# Regex untuk mengambil kata berikutnya dari dataset
search_regex = string_final + " (\w+)"

# Inisialisasi list prediksi kata
found_words = []

start = time.time()

# Pencarian prediksi kata
with open(path, encoding="utf-8") as dataset:
    for line in dataset:
        alpha_only = regex.sub("", line)                    # Membuang karakter selain alphabet dan titik
        no_multi_spaces = re.sub(" +", " ", alpha_only)     # Membuang ekstra spasi
        lowered = no_multi_spaces.lower()                   # Lowercase
        list = searchBM(lowered, string_final)
        for i in list:
                word = re.search("( \w+)", lowered[i:])
                if word != None:
                    found_words.append((word.group(0))[1:])
        
        #found_words += re.findall(search_regex, lowered)    # Mencari kata yang ketemu dan melakukan concat dengan list

# Pengurutan prediksi kata berdasarkan akurasi
count_all = len(found_words)    # Jumlah semua prediksi kata
sorted_found_words = sorted(found_words, key = found_words.count, reverse = True)   # Mengurutkan found_words dari jumlah kemunculannya
words = []                      # Inisialisasi list untuk menampung setiap kata unik
count_words = []                # Inisialisasi list untuk menampung jumlah kemunculan setiap kata unik

# Menampung setiap kata unik serta jumlah kemunculannya
for word in sorted_found_words:
    if word in words:
        count_words[words.index(word)] += 1 # Menambah jumlah kemunculan jika sudah ada di list
    else:
        words.append(word)                  # Menambah kata jika belum ada di list
        count_words.append(1)

# Output
print("Waktu: ", time.time()-start)
print("Prediksi kata:")

# Pola ditemukan berjumlah >= 3
if (count_all >= 3):
    for i in range (3): 
        print(str(i+1) + ". " + words[i] + " , akurasi " + str(round((count_words[i] / count_all * 100), 2)) + "%")

# Pola tidak ditemukan
elif (count_all == 0):
    print("Tidak ada rekomendasi kata, tidak ditemukan pola pada dataset.")

# Pola ditemukan berjumlah 1 atau 2
else:
    for i in range (count_all):
        print(str(i+1) + ". " + words[i] + " , akurasi " + str(round((count_words[i] / count_all * 100), 2)) + "%")