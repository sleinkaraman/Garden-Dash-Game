# Garden Dash

Garden Dash, Python ve Pygame Zero kütüphanesi kullanılarak geliştirilmiş eğlenceli bir 2D oyundur. Oyuncu, bir bahçede meyveleri toplarken köpeklerden kaçmaya çalışır. Toplanan her meyve ile puan kazanırken, köpeklere yakalanırsanız oyun sona erer. 
---

## Kurulum

1. Bu depoyu klonlayın:

    ```bash
    git clone https://github.com/sizin-kullanici-adiniz/GardenDash.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd GardenDash
    ```

3. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install pgzero
    ```

4. Oyunu başlatın:

    ```bash
    python main.py
    ```

---

## Nasıl Oynanır?

### Oyuna Başlama
Ana menüde "Oyuna Başla" butonuna tıklayarak oyunu başlatın.

### Kontroller

- **Yukarı Hareket**: Yukarı Ok Tuşu
- **Aşağı Hareket**: Aşağı Ok Tuşu
- **Sağa Hareket**: Sağ Ok Tuşu
- **Sola Hareket**: Sol Ok Tuşu

### Amaç
Bahçede rastgele beliren meyveleri toplayarak puan kazanın. Köpeklerden kaçarak oyuna devam edin.

### Oyun Sonu
Köpeklere yakalanırsanız oyun biter. "Yeniden Başla" butonuyla oyunu tekrar başlatabilir veya "Çıkış" butonuyla oyundan çıkabilirsiniz.

---

## Oyun Özellikleri

- **Müzik Aç/Kapa**: Ana menüde veya oyun sonu ekranında "Müziği Aç/Kapa" butonuyla arka plan müziğini kontrol edebilirsiniz.
- **Skor Sistemi**: Toplanan her meyve 10 puan kazandırır. Skorunuzu yüksek tutmaya çalışın!
- **Zorluk**: Köpekler rastgele hareket eder ve oyuncuyu yakalamaya çalışır. Stratejinizi iyi kurun!

---

## Kod Yapısı

- `main.py`: Oyunun ana dosyasıdır. Tüm oyun mantığı ve kontroller bu dosyada bulunur.
- **Hero Sınıfı**: Oyuncunun karakterini temsil eder. Hareket ve animasyon işlemleri bu sınıfta yönetilir.
- **Dog Sınıfı**: Köpekleri temsil eder. Rastgele hareket ederler ve oyuncuya yaklaşmaya çalışırlar.
- **Fruit Sınıfı**: Toplanabilir meyveleri temsil eder. Rastgele konumlarda belirirler.

---

## Temel Fonksiyonlar

- `start_game()`: Oyunu başlatır ve tüm değişkenleri başlangıç durumuna getirir.
- `update()`: Oyunun ana güncelleme döngüsüdür. Karakter hareketleri, çarpışma kontrolü ve puanlama burada yapılır.
- `draw()`: Oyunun grafiklerini ekrana çizer. Menü, oyun alanı ve oyun sonu ekranı bu fonksiyonla yönetilir.
- `on_mouse_down()`: Fare tıklamalarını işler. Butonlara tıklanma durumlarını kontrol eder.

---

