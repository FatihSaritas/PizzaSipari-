import streamlit as st 
import sqlite3

conn = sqlite3.connect('pizzadb.sqlite3')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS siparisler(isim TEXT,adres TEXT,pizza TEXT,boy TEXT,icecek TEXT,fiyat REAL)')
conn.commit()

c.execute('SELECT isim FROM pizzalar')
isimler = c.fetchall()


isimlerlist = []
for i in isimler:
    isimlerlist.append(i[0])



st.header('Sipariş Sayfa')

with st.form('sipariş',clear_on_submit=True):
    isim = st.text_input('İsim Soyisim')
    adres = st.text_area('Adress')
    pizza = st.selectbox('Pizza Seç',isimlerlist)
    boy = st.selectbox('Boy',['Small','Medium','Large'])
    icecek = st.selectbox('İçicek',['Ayran','Cola','Cola Zero','Fanta','Sprite','Gazoz','Vişne Suyu','Karışık Meyve Suyu','İce Tea'])
    siparisver = st.form_submit_button('Sipariş Ver')
    
    
    if siparisver:
        if boy == 'Small':    
            c.execute('SELECT smfiyat FROM pizzalar WHERE isim = ?',(pizza,))
            fiyat = c.fetchone()
        elif boy == 'Medium':    
            c.execute('SELECT mdfiyat FROM pizzalar WHERE isim = ?',(pizza,))
            fiyat = c.fetchone()
        elif boy == 'Large':    
            c.execute('SELECT lgfiyat FROM pizzalar WHERE isim = ?',(pizza,))
            fiyat = c.fetchone()
            
    
        icecekler = {                   #Bunları veri tabanına atmadıgımızdan bu şkilde yaptık 
            'Ayran':15,
            'Cola': 20,
            'Cola Zero': 20,
            'Fanta': 17,
            'Sprite': 15,
            'Gazoz': 20,
            'Vişne Suyu': 18,
            'Karışık Meyve Suyu': 20,
            'İce Tea': 18
        }
        
        icecekfiyat = icecekler[icecek]
        
        toplamfiyat = fiyat[0]+icecekfiyat
        
        c.execute('INSERT INTO siparisler VALUES(?,?,?,?,?,?)',(isim,adres,pizza,boy,icecek,toplamfiyat))
        conn.commit()
        
        st.success(f'Sipariş Başarılı Bir Şeklilde Gerçekleştirildi,Toplam Ücret:{toplamfiyat} TL')