# Plaka_Tanima_Sistemi_Projesi

# Araç Plaka Tanıma Sistemi
Bu proje, araç plaka kodlarının görüntülerini okumak,
bu plaka kodlarının numarasını metne dönüştürmek ve plaka bilgilerini
tarih, saat ve plakanın il kodu ile birlikte
veri tabanında anlık olarak kayıtlarını saklamak için kullanılır.

# Uygulama
Araç yönetimi için yaygın olarak kullanılan bir teknoloji olan Plaka Tanıma Sistemi, biletsiz park, geçiş ücretleri, çalıntı araç tespiti ve otomatik faturalandırma
gibi birçok işlemde kullanılır. Plaka Tanıma Sistemi, çeşitli bilgileri bir araya getirerek birden fazla verinin hızlıca toplanmasına ve bu verilerin birbiriyle
ilişkilendirilmesine imkan sağlar.
Otoyollarda sıkça kullanılan bu sistem, araç hız tespiti, ihlal tespiti ve geçiş kayıtları için de etkili bir şekilde kullanılır. 
Otoyol üzerinde belirli noktalara yerleştirilen Radar (Radio Detection And Ranging) hız tespit cihazları, plaka tanıma sistemine entegre edilerek çalışır.
Bu sayede yol üzerinden geçen araçların hızları ve plakaları tespit edilir. Hız ihlali yapan araçlara süratle ceza kesme yeteneğine sahiptir.
Sadece hız ihlali yapan araçlar değil, otoyolu kullanan tüm araçların plakaları tespit edilir ve her araç için resimli bir kayıt oluşturulur.
Ülkemizde, karayolları yönetmeliğine uygun olarak plaka gövdeleri alüminyumdan yapılmış olup boyutları 11x52 cm'dir. Bu plakalar,
araçların hem ön hem de arka kısımlarında bulunmak zorundadır.



# Kütüphaneler
-sqlite3
- OpenCV
- [Tesseract 4](https://github.com/tesseract-ocr/tesseract/wiki)

#Kullanım
- araclar.db tanımlanan plakaların tarih, saat, plaka numarası ve il kodunu gösterir.
- Tesseract OCR işlemi sunan bir kütüphanedir.
- Tesseract 100'den fazla dil seçeneğine sahiptir
 -Eğer değiştirme isterseniz calistir.py dosyası içerisindeki
     config = ('-l tur --oem 1 --psm 3') satırı düzenleyiniz "tur" tercih ettiğiniz dili belirler



#Çalıştırmak İçin;

    python calistir.py

    
