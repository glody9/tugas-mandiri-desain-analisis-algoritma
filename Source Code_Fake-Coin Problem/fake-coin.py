import random
koin_asli = 1
koin_palsu = 0
# mengacak koin supaya mendapatkan array yang random
def mengacak_koin(n):  
    global koin 
    koin= [koin_asli] * (n - 1) + [koin_palsu] * (1) #membuat array koin yang acak
    random.shuffle(koin)
    print(koin)
    return koin
def test_koin_palsu(n):
    for i in range(1,n):
        if koin[0]==koin[i]:
            pass
        elif koin[0]<koin[i]:
            return print(1,"ini koin yang palsu")
        else:
            return print(i+1,"ini koin yang palsu")
n=int(input("masukkan jumlah koin:"))
mengacak_koin(n)
test_koin_palsu(n)
