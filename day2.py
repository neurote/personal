sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi2: "))

print("\n1. Toplama(+)\n2. Çıkarma(-)\n3. Çarpma(*)\n4. Bölme(/)\n")
islem = input("Yapmak istediğiniz işlem: ")

if islem == "1" or islem == "+":
    sonuc = sayi1 + sayi2
    print("İki sayının toplamı = ", sonuc)

elif islem == "2" or islem == "-":
    sonuc = sayi1 - sayi2
    print("İki sayının çıkarımı = ", sonuc)

elif islem == "3" or islem == "*":
    sonuc = sayi1 * sayi2
    print("İki sayının çarpımı = ", sonuc)

elif islem == "4" or islem == "/":
    if sayi1 != 0 or sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("İki sayının bölümü = ", sonuc)
    else:
        print("Hatalı işlem, sıfıra bölünülemez.")

else:
    print("Geçersiz işlem.")
