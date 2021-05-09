# Source code terinspirasi dari https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/

NO_OF_CHARS = 256

def lastOccurrence(string, size):
	# Input: pola, panjang
    # Output: list of fungsi last occurrence

	# Inisialisasi dengan -1
	last_occ = [-1]*NO_OF_CHARS

	# Mengganti dengan kemunculan terakhir
	for i in range(size):
		last_occ[ord(string[i])] = i

	return last_occ

def searchBM(txt, pat):
    # Input: teks, pola
    # Output: list of indeks terakhir pola ditemukan

    # List untuk output
    list_idx = []

    # Panjang pola dan teks
    m = len(pat)
    n = len(txt)    

    # Fungsi last occurrence
    last_occ = lastOccurrence(pat, m)  

    # Jumlah pergeseran
    s = 0
    while(s <= n-m):

    	j = m-1 

    	# Pemeriksaan pola dari belakang
    	while (j >= 0) and (pat[j] == txt[s+j]):
    		j -= 1  

    	# J mencapai -1 dan bukan berada di akhir teks
    	if (j < 0) and ((s+m) < n):
            list_idx.append(s+m)
            s += (m-last_occ[ord(txt[s+m])] if s+m<n else 1)

    	else:
    		s += max(1, j-last_occ[ord(txt[s+j])])
    
    return list_idx


#import re
#pat = "aku"
#string = "hari ini aku berjalan sama temen aku yang"
#list = searchBM(string, pat)
#found = []
#print(list)
#for i in list:
#    word = re.search("( \w+)", string[i:])
#    if word != None:
#        found.append((word.group(0))[1:])
#print(found)
