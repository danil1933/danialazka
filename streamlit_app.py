import streamlit as st

st.title("🎈 Danialazka Web")
st.write(
    "dunia boleh saja melawanku ku punya doa ibu #perunggu"
)
st.image("IMG_3530.jpeg",width=200)

st.title("33x , tapi , ini abadi")
st.header("aplikasi mengecek nilai ganjil/genap")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")
