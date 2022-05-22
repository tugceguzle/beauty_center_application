import sqlite3
vt=sqlite3.connect('musteribilgileri.sqlite')
im=vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS bilgiler (RANDEVU_NUMARASI, TARİH, AD, SOYAD,  YAPILAN_İŞLEM, ÖDENEN_TUTAR)")
kategori=["MANİKÜR&PEDİKÜR","NAİLART","CİLT BAKIMI","KAŞ&KİRPİK İŞLEMLERİ","SAÇ İŞLEMLERİ","DOLGU&BOTOX İŞLEMLERİ"]
islem={
        "MANİKÜR&PEDİKÜR":["MANİKÜR","PEDİKÜR"],
        "NAİLART":["KALICI OJE","PROTEZ TIRNAK"],
        "CİLT BAKIMI":["GREENPEEL","DERMAPEN(4+2)","KİMYASAL PEELİNG"],
        "KAŞ&KİRPİK İŞLEMLERİ":["KİRPİK LİFTİNG","MİCROBLADİNG","İPEK KİRPİK"],
        "SAÇ İŞLEMLERİ":["KERATİN BAKIMI","BREZİLYA FÖNÜ","SAÇ KESİMİ"],
        "DOLGU&BOTOX İŞLEMLERİ":["NAZOLABİAL ÇİZGİ DOLGUSU","GÖZALTI DOLGUSU","ÇENE HATTI DOLGUSU","DUDAK BOTOXU","KAŞ KALDIRMA BOTOXU"],
        }
tutar={
        "MANİKÜR":90,
        "PEDİKÜR":110,
        "KALICI OJE":60,
        "PROTEZ TIRNAK":250,
        "GREENPEEL":650,
        "DERMAPEN(4+2)":390,
        "KİMYASAL PEELİNG":110,
        "KİRPİK LİFTİNG":130,
        "MİCROBLADİNG":335,
        "İPEK KİRPİK":215,
        "KERATİN BAKIMI":780,
        "BREZİLYA FÖNÜ":675,
        "SAÇ KESİMİ":290,
        "NAZOLABİAL ÇİZGİ DOLGUSU":675,
        "GÖZALTI DOLGUSU":650,
        "ÇENE HATTI DOLGUSU":730,
        "DUDAK BOTOXU":580,
        "KAŞ KALDIRMA BOTOXU":875,
        }
calisanlar=[["Burcu","Özalan","MANİKÜR&PEDİKÜR"],["Seçil","Demir","NAİLART"],["Yağmur","Kaya","CİLT BAKIMI"],["Tarık","Akar","KAŞ&KİRPİK İŞLEMLERİ"],["Hakan","Şensoy","SAÇ İŞLEMLERİ"],["Deniz","Göksoy","DOLGU&BOTOX İŞLEMLERİ"]]
class calisanbilgileri():
    ad=""
    soyad=""
    departman=""
calisan1=calisanbilgileri()
calisan1.ad=calisanlar[0][0]
calisan1.soyad=calisanlar[0][1]
calisan1.departman=calisanlar[0][2]
calisan2=calisanbilgileri()
calisan2.ad=calisanlar[1][0]
calisan2.soyad=calisanlar[1][1]
calisan2.departman=calisanlar[1][2]
calisan3=calisanbilgileri()
calisan3.ad=calisanlar[2][0]
calisan3.soyad=calisanlar[2][1]
calisan3.departman=calisanlar[2][2]
calisan4=calisanbilgileri()
calisan4.ad=calisanlar[3][0]
calisan4.soyad=calisanlar[3][1]
calisan4.departman=calisanlar[3][2]
calisan5=calisanbilgileri()
calisan5.ad=calisanlar[4][0]
calisan5.soyad=calisanlar[4][1]
calisan5.departman=calisanlar[4][2]
calisan6=calisanbilgileri()
calisan6.ad=calisanlar[5][0]
calisan6.soyad=calisanlar[5][1]
calisan6.departman=calisanlar[5][2]
gunlukkazanc=[]
toplam=0
toplamtutar=0
odenecektoplamtutar=[]
while True:
    print("SİSTEME HOŞGELDİNİZ!")
    karar=input("Sistemden çıkmak istiyor musunuz?(e/h):")
    if karar=="h":
        sayac=0
        def randevuno(x,y):
            return(x+y)
        def odenecektutar():
            toplamtutar=sum(odenecektoplamtutar)
            odenecektoplamtutar.clear()
            return(toplamtutar)
        while True:
            gunsonu=input("Gün sonu geldi mi?(e/h):")
            if gunsonu=="e":
                gunluk=open("gunlukrapor.txt","a")
                for i in gunlukkazanc:
                    toplam+=i
                gunluk.write("GÜNLÜK TOPLAM KAZANÇ={} TL'DİR.\n".format(toplam))
                gunluk.close()
                break
            else:
                cevap=input("Yeni bir müşteri mi geldi?(e/h):")
                if cevap=="h":
                    print("Müşterinin gelmesini bekleyiniz.")
                elif cevap=="e":
                    while True:
                        veri=open("musteribilgileri.txt","a")
                        gunluk=open("gunlukrapor.txt","a")
                        sayac=sayac+1
                        ad=input("AD:")
                        soyad=input("SOYAD:")
                        print("\nKATEGORİLER:")
                        print(kategori)
                        try:
                            yapilacak=input("İŞLEM YAPILACAK OLAN KATEGORİ:")
                        except KeyError:
                            print("LÜTFEN GEÇERLİ BİR KATEGORİ GİRİNİZ.")
                        finally:
                            print("LÜTFEN GEÇERLİ BİR KATEGORİ GİRİNİZ.")
                            yapilacak=input("İŞLEM YAPILACAK OLAN KATEGORİ:")                            
                        print("\nİŞLEMLER:")
                        print(islem[(yapilacak)])
                        try:
                            sonislem=input("YAPILACAK İŞLEM:")
                        except KeyError:
                            print("LÜTFEN GEÇERLİ BİR İŞLEM GİRİNİZ.")
                        finally:
                            print("LÜTFEN GEÇERLİ BİR İŞLEM GİRİNİZ.")
                            sonislem=input("YAPILACAK İŞLEM:")
                        try:
                            celnumber=int(input("TELEFON NO:"))
                        except ValueError:
                            print("LÜTFEN SADECE SAYI GİRİNİZ.")
                            celnumber=int(input("TELEFON NO:"))
                        try:
                            tarih=input("TARİH:")
                        except ValueError:
                            print("LÜTFEN TARİHİ GG/AA/YY OLARAK GİRİNİZ.")
                        finally:
                            print("LÜTFEN TARİHİ GG/AA/YY OLARAK GİRİNİZ.")
                            tarih=input("TARİH:")
                        islemtutari=tutar[(sonislem)]
                        odenecektoplamtutar.append(islemtutari)
                        gunlukkazanc.append(islemtutari)
                        gunluk.write("{} işleminden {} TL kazanıldı.\n".format(sonislem,islemtutari))
                        gunluk.close()
                        a,b,c=tarih.split("/")
                        d=a+b+c
                        x=str(d)
                        y=str(sayac)
                        veri.write("{}. müşterimiz Sy. {} {} için {} tarihinde {} nolu randevu oluşturulmuştur.Yapılacak işlem {} işlem tutarı {} TL'dir.\n".format(sayac,ad,soyad,tarih,randevuno(x,y),sonislem,islemtutari))
                        veri.close()
                        im.execute("INSERT INTO bilgiler VALUES (?,?,?,?,?,?)", (randevuno(x,y),tarih,ad,soyad,sonislem,islemtutari))
                        vt.commit()
                        devam=input("Bu müşteri için başka randevu girilecek mi?(e/h)")
                        while True:
                            if devam=="e":
                                veri=open("musteribilgileri.txt","a")
                                gunluk=open("gunlukrapor.txt","a")
                                print("\nKATEGORİLER:")
                                print(kategori)
                                yapilacak=input("İŞLEM YAPILACAK OLAN KATEGORİ:")
                                print("\nİŞLEMLER:")
                                print(islem[(yapilacak)])
                                sonislem=input("YAPILACAK İŞLEM:")
                                islemtutari=tutar[(sonislem)]
                                gunlukkazanc.append(islemtutari)
                                odenecektoplamtutar.append(islemtutari)
                                gunluk.write("{} işleminden {} TL kazanıldı.\n".format(sonislem,islemtutari))
                                gunluk.close()
                                a,b,c=tarih.split("/")
                                d=a+b+c
                                x=str(d)
                                y=str(sayac+1)
                                veri.write("{}. müşterimiz Sy. {} {} için {} tarihinde {} nolu randevu oluşturulmuştur.Yapılacak işlem {} işlem tutarı {} TL'dir.\n".format(sayac,ad,soyad,tarih,randevuno(x,y),sonislem,islemtutari))
                                veri.close()
                                im.execute("INSERT INTO bilgiler VALUES (?,?,?,?,?,?)", (randevuno(x,y),tarih,ad,soyad,sonislem,islemtutari))
                                vt.commit()
                                devam=input("Bu müşteri için başka randevu girilecek mi?(e/h):")
                                if devam=="e":
                                    continue
                                else:
                                    print("Ödenecek Tutar:{}".format(odenecektutar()))
                                    break
                            else:
                                print("Ödenecek Tutar:{}".format(odenecektutar()))
                                break
                        break
                else:
                    print("Geçerli değer giriniz.")
    else:
        vt.close()
        break