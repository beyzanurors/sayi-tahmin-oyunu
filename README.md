# Python Sayı Tahmin Oyunu (Number Guessing Game)

Bu proje, Python programlama dili ile geliştirilmiş; bilgisayarın 1 ile 100 arasında rastgele seçtiği bir sayıyı kullanıcının ipuçlarıyla bulmaya çalıştığı eğlenceli ve interaktif bir konsol oyunudur.

## Öne Çıkan Özellikler
- **Rastgele Sayı Üretimi (`random` modülü):** Her oyun başlangıcında 1-100 arasında farklı bir sayı atanır.
- **Güçlü Hata Yönetimi (`try-except ValueError`):** Kullanıcı yanlışlıkla harf veya metin girdiğinde program çökmez, nazikçe geçerli bir tam sayı girmesi istenir.
- **Sınır Kontrolü:** 1 ile 100 aralığının dışındaki tahminler kontrol edilerek kullanıcı uyarılır.
- **Dinamik Yönlendirmeler:** Tahmine göre "Daha büyük bir sayı söyleyin" veya "Daha küçük bir sayı söyleyin" şeklinde yönlendirmeler yapar.
- **Skor / Deneme Sayacı:** Doğru sayı bulunduğunda kaçıncı denemede bulduğunu ekrana yazdırır.

## Kullanılan Teknolojiler
- **Python 3**
- **Temel Algoritmalar ve Döngüler (`while`, `if-else`)**
- **Python Standart Kütüphanesi (`random`)**

## Nasıl Çalıştırılır?
1. Bilgisayarınızda Python yüklü olduğundan emin olun.
2. Proje dosyasını (örneğin `sayi_tahmin.py`) bilgisayarınıza indirin.
3. Terminal veya komut satırından dosyanın bulunduğu klasöre giderek şu komutu çalıştırın:
   ```bash
   python sayi_tahmin.py
