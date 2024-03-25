import streamlit as st
import sqlite3
import pandas as pd 

st.header('Sipariş Kayıtları')

conn = sqlite3.connect('pizzadb.sqlite3')
c = conn.cursor()

c.execute('SELECT * FROM siparisler')

siparisler = c.fetchall()

df = pd.DataFrame(siparisler)

df.columns = ['isim','adres','pizza','boy','icecek','toplamfiyat']  #siparis sayfasından  siparisler tablosundaki verileri cekicez

st.table(df)