# Araç Plaka Tanýma Sistemi
Bu proje, araç plaka kodlarýnýn görüntülerini okumak,
bu plaka kodlarýnýn numarasýný metne dönüþtürmek ve plaka bilgilerini
tarih, saat ve plakanýn il kodu ile birlikte
veri tabanýnda anlýk olarak kayýtlarýný saklamak için kullanýlýr.

## Uygulama
Araç yönetimi için yaygýn olarak kullanýlan bir teknoloji olan Plaka Tanýma Sistemi, biletsiz park, geçiþ ücretleri, çalýntý araç tespiti ve otomatik faturalandýrma
gibi birçok iþlemde kullanýlýr. Plaka Tanýma Sistemi, çeþitli bilgileri bir araya getirerek birden fazla verinin hýzlýca toplanmasýna ve bu verilerin birbiriyle
iliþkilendirilmesine imkan saðlar.
Otoyollarda sýkça kullanýlan bu sistem, araç hýz tespiti, ihlal tespiti ve geçiþ kayýtlarý için de etkili bir þekilde kullanýlýr. 
Otoyol üzerinde belirli noktalara yerleþtirilen Radar (Radio Detection And Ranging) hýz tespit cihazlarý, plaka tanýma sistemine entegre edilerek çalýþýr.
Bu sayede yol üzerinden geçen araçlarýn hýzlarý ve plakalarý tespit edilir. Hýz ihlali yapan araçlara süratle ceza kesme yeteneðine sahiptir.
Sadece hýz ihlali yapan araçlar deðil, otoyolu kullanan tüm araçlarýn plakalarý tespit edilir ve her araç için resimli bir kayýt oluþturulur.
Ülkemizde, karayollarý yönetmeliðine uygun olarak plaka gövdeleri alüminyumdan yapýlmýþ olup boyutlarý 11x52 cm'dir. Bu plakalar,
araçlarýn hem ön hem de arka kýsýmlarýnda bulunmak zorundadýr.



## Kütüphaneler
-sqlite3
- OpenCV
- [Tesseract 4](https://github.com/tesseract-ocr/tesseract/wiki)

##Kullaným
- araclar.db tanýmlanan plakalarýn tarih, saat, plaka numarasý ve il kodunu gösterir.
- Tesseract OCR iþlemi sunan bir kütüphanedir.
- Tesseract 100'den fazla dil seçeneðine sahiptir
    -Eðer deðiþtirme isterseniz calistir.py dosyasý içerisindeki
     config = ('-l tur --oem 1 --psm 3') satýrý düzenleyiniz "tur" tercih ettiðiniz dili belirler



##Çalýþtýrmak Ýçin;

    python calistir.py
    
 


