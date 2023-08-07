# -*- coding: utf-8 -*-
from datetime import date, datetime
import numpy as np
import cv2
import  imutils
import sys
import pytesseract
import time
import sqlite3


print("""        
              *-----------------------------------HALİL COŞGUN--------------------------------------*
              *                                                                                     *
              *                                                                                     *
              *-------------------------------PLAKA TANIMA SISTEMİ----------------------------------*
              *                                                                                     *
              *                                                                                     *
              *-------------------------------SAKARYA ÜNİVERSİTESİ----------------------------------*""")






resimadi=input("""



 LÜtfen Resmin Adını Uzantısı ile birlikte giriniz(png,jpg vs):""")
image = cv2.imread("data/" + resimadi)
image = imutils.resize(image, width=500)
cv2.imshow("Orjinal Resim", image)
cv2.waitKey(0)

#Resme Gri Tonlama İşlemi
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Tonlamali Resim", gray)
cv2.waitKey(0)


#Bileteral Filtreleme
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("Bilateral Filtreleme", gray)
cv2.waitKey(0)

#Kenar Tespiti
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("Kenar Tespiti", edged)
cv2.waitKey(0)

#Öncelikle gri tonlama verdiğimiz ve sonrasında canny uygulanan
#‘edged’ görüntüsünde ki kenarları bulmak için ‘findContours()’ 
#fonskiyonunu kullandık.
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
NumberPlateCnt = None 

count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True) 
        if len(approx) == 4:  
            NumberPlateCnt = approx 
            break

#Plaka Dışında Kalan Alanları Maskele
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)               

kernel = np.ones((5, 5), np.uint8)
dilated_mask = cv2.dilate(new_image, kernel, iterations=1)

new_image = cv2.bitwise_and(image, image, mask=dilated_mask)

cv2.imshow("Tespit Edilmis Plaka Goruntusu", new_image)
cv2.waitKey(0)




#Tesseract ,Türkçe dili, Seviye 1 motoru ve sayfa tespit ayarları
config = ('-l tur --oem 1 --psm 3')

#Tespit edilen plakaya Tesseract OCR uygulama işlemi
text = pytesseract.image_to_string(new_image, config=config)



#Tanımlanan metni ekrana yazdırma ve diğer pencereleri kapatma
print(" Tespit Edilen Plaka:",text)
cv2.waitKey(0)
cv2.destroyAllWindows()

#data klasöründe bulunan görsellerde ki plaka kodları kotrolü
print("Veritabanına kaydediliyor...")
time.sleep(3)
sehir =""
ilk_iki_karakter = text[:2]
if ilk_iki_karakter== "35":
         sehir="Izmir"
elif ilk_iki_karakter=="34":
        sehir="Istanbul"
elif ilk_iki_karakter=="60":
        sehir="Tokat"
elif ilk_iki_karakter=="61":
        sehir="Trabzon"
elif ilk_iki_karakter=="06":
        sehir="Ankara"
elif ilk_iki_karakter=="48":
        sehir="Muğla"
elif ilk_iki_karakter=="16":
        sehir="Bursa"
else:  
        sehir="yabanci plaka"

#SQLite veritabanı dosyasına bağlantı oluşturur. 
database_connect = sqlite3.connect("araclar.db")
#Bağlantı üzerinde bir imleç (cursor) oluşturur. İmleç, veritabanı üzerinde SQL sorgularını
#çalıştırmak ve sonuçları işlemek için kullanılır. 
imlec = database_connect.cursor()

#Tablo sorugu, eğer oluşturulmuşsa tekrar oluşturulmasına gerek yoktur
imlec.execute("""CREATE TABLE IF NOT EXISTS girisler(plaka_no TEXT, tarih TIMESTAMP,kayitli_oldugu_sehir TEXT)""")

#Plaka ve tarih değerlerini sorguya ekleme
sorgu = "INSERT INTO girisler(plaka_no, tarih,kayitli_oldugu_sehir) VALUES (?, ?, ?)"
degerler = (text,datetime.now(),sehir)
#Veri tabanına başarılı kayıt sorgulama 
try:
  imlec.execute(sorgu, degerler)
  database_connect.commit()
  print("Veritabanına başarıyla kaydedildi.")

except sqlite3.Error as e:
    print("Kayıt eklenirken bir hata oluştu:", e)

#Veritabanı Bağlantısını Kapat
database_connect.close()
#5 saniye sonra bilgi ver ve bir tuşa basmanın ardından tüm pencereleri kapat
time.sleep(5)
cv2.waitKey(0)





