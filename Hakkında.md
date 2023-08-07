# Ara� Plaka Tan�ma Sistemi
Bu proje, ara� plaka kodlar�n�n g�r�nt�lerini okumak,
bu plaka kodlar�n�n numaras�n� metne d�n��t�rmek ve plaka bilgilerini
tarih, saat ve plakan�n il kodu ile birlikte
veri taban�nda anl�k olarak kay�tlar�n� saklamak i�in kullan�l�r.

## Uygulama
Ara� y�netimi i�in yayg�n olarak kullan�lan bir teknoloji olan Plaka Tan�ma Sistemi, biletsiz park, ge�i� �cretleri, �al�nt� ara� tespiti ve otomatik faturaland�rma
gibi bir�ok i�lemde kullan�l�r. Plaka Tan�ma Sistemi, �e�itli bilgileri bir araya getirerek birden fazla verinin h�zl�ca toplanmas�na ve bu verilerin birbiriyle
ili�kilendirilmesine imkan sa�lar.
Otoyollarda s�k�a kullan�lan bu sistem, ara� h�z tespiti, ihlal tespiti ve ge�i� kay�tlar� i�in de etkili bir �ekilde kullan�l�r. 
Otoyol �zerinde belirli noktalara yerle�tirilen Radar (Radio Detection And Ranging) h�z tespit cihazlar�, plaka tan�ma sistemine entegre edilerek �al���r.
Bu sayede yol �zerinden ge�en ara�lar�n h�zlar� ve plakalar� tespit edilir. H�z ihlali yapan ara�lara s�ratle ceza kesme yetene�ine sahiptir.
Sadece h�z ihlali yapan ara�lar de�il, otoyolu kullanan t�m ara�lar�n plakalar� tespit edilir ve her ara� i�in resimli bir kay�t olu�turulur.
�lkemizde, karayollar� y�netmeli�ine uygun olarak plaka g�vdeleri al�minyumdan yap�lm�� olup boyutlar� 11x52 cm'dir. Bu plakalar,
ara�lar�n hem �n hem de arka k�s�mlar�nda bulunmak zorundad�r.



## K�t�phaneler
-sqlite3
- OpenCV
- [Tesseract 4](https://github.com/tesseract-ocr/tesseract/wiki)

##Kullan�m
- araclar.db tan�mlanan plakalar�n tarih, saat, plaka numaras� ve il kodunu g�sterir.
- Tesseract OCR i�lemi sunan bir k�t�phanedir.
- Tesseract 100'den fazla dil se�ene�ine sahiptir
    -E�er de�i�tirme isterseniz calistir.py dosyas� i�erisindeki
     config = ('-l tur --oem 1 --psm 3') sat�r� d�zenleyiniz "tur" tercih etti�iniz dili belirler



##�al��t�rmak ��in;

    python calistir.py
    
 


