import streamlit as st 
import sqlite3

conn = sqlite3.connect('pizzadb.sqlite3')                                                                                                    #BU bize bir database oluşturmamızı sağlıyor varsa direkt bağlanır.
c = conn.cursor()                                                                                                                           # c sayesinde sql işlemlerimizi yapıcaz tablo oluşturma ekle ve benzeri işlemleri 
c.execute('CREATE TABLE IF NOT EXISTS pizzalar(isim TEXT , smfiyat REAL, mdfiyat REAL , lgfiyat REAL , icindekiler TEXT, resim TEXT)')       #Real sqlde floata denktir resim text dememiz sebebi resmi sql koyamayız yolunu ekleyebiliriz.

conn.commit()                                                                                                                              #BU işlemi bitirip kayıt ediyoruz commit ederek

st.header('Pizza Ekle')

with st.form('PizzaEkle',clear_on_submit=True):                                                                                              #Clear on submıt bilgileri girdikten sonra ekle bastıgımızda tüm pencereyi temizlememizi sağlar.
    isim = st.text_input('Pizza İsmi')
    smfiyat = st.number_input('Small Fiyat')
    mdfiyat = st.number_input('Medium Fiyat')
    lgfiyat = st.number_input('Large Fiyat')
    icindekiler = st.multiselect('icindekiler',['Mantar','Zeytin','Mısır','Ketçap','Mayonez','Sucuk','Kaşar','Pastırma','Jambon','Mozarella','Salam',
                                                'Hindi Füme','Domates','BBQ Sos','Burger Sos','Roka','Parmesan','Ton Balığı','Ananas','Tavuk','Fesleğen','Kavurma'])
    
    resim = st.file_uploader('Pizza Resmi Ekleyiniz')
    ekle = st.form_submit_button('Pizza Ekle')
    
    if ekle:
        icindekiler = str(icindekiler)                                   #icindekiler verilerini bir metne dönüştürüyoruz.
        icindekiler = icindekiler.replace('[','')                       #Bütün listeyi ele almak için başlangıç parantezi ve kapanışını aldık 
        icindekiler = icindekiler.replace(']','')
        icindekiler = icindekiler.replace("'",'')                           #Gelen seçtiğimiz icidekiler kısmının tırnaklarını kaldırdık
    
        resimurl = 'img/'+ resim.name
        
        open(resimurl,'wb').write(resim.read())
        
        c.execute('INSERT INTO pizzalar VALUES(?,?,?,?,?,?)',(isim,smfiyat,mdfiyat,lgfiyat,icindekiler,resimurl))                   #6 DEĞER TABLODAKİLER ama tek fark resim değil resim url var en sonda dikkat et.
        
        conn.commit()
        
        st.success('Pizza Başarıyla Eklendi.')