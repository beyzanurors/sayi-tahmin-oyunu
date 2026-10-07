import random


def sayi_tahmin_oyunu():
  print("Sayı Tahmin Oyununa Hoş Geldiniz!")
  print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?\n")

  # 1 ile 100 arasında rastgele bir sayı seçiyoruz
  tutulan_sayi = random.randint(1, 100)
  deneme_sayisi = 0

  while True:
    try:
      # Kullanıcıdan tahmin alıyoruz
      tahmin = int(input("Tahmininiz nedir? "))
      deneme_sayisi += 1

      # Sınır kontrolü
      if tahmin < 1 or tahmin > 100:
        print("Lütfen 1 ile 100 arasında bir sayı girin!")
        continue

      # Tahmin karşılaştırmaları
      if tahmin < tutulan_sayi:
        print(" Daha büyük bir sayı söyleyin!")
      elif tahmin > tutulan_sayi:
        print(" Daha küçük bir sayı söyleyin!")
      else:
        print(f"\n Tebrikler! Sayıyı {deneme_sayisi}. denemede buldunuz.")
        break

    except ValueError:
      print(" Lütfen geçerli bir tam sayı girin!")


if __name__ == "__main__":
  sayi_tahmin_oyunu()