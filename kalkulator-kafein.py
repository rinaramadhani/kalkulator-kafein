import streamlit as st

# Fungsi untuk menghitung batas kafein harian
def hitung_kafein_ideal(berat_badan_kg, usia, jenis_kelamin, konsumsi_kafein_mg):
    # Batas kafein berdasarkan usia
    if usia < 12:
        batas_kafein_per_kg = 2.5
    elif usia < 18:
        batas_kafein_per_kg = 3.0
    else:
        batas_kafein_per_kg = 5.0 if berat_badan_kg * 5.0 <= 400 else 400 / berat_badan_kg
    
    # Faktor jenis kelamin
    faktor_jenis_kelamin = 0.9 if jenis_kelamin.lower() == "wanita" else 1.0
    
    # Hitung batas harian
    batas_harian = berat_badan_kg * batas_kafein_per_kg * faktor_jenis_kelamin
    
    # Hitung sisa batas aman
    sisa_kafein = batas_harian - konsumsi_kafein_mg
    
    # Status konsumsi
    status = "Aman" if sisa_kafein >= 0 else "Berlebihan"
    
    return {
        "batas_harian_mg": batas_harian,
        "konsumsi_kafein_mg": konsumsi_kafein_mg,
        "sisa_kafein_mg": sisa_kafein,
        "status": status
    }

# Streamlit app
st.title("☕Kalkulator Kafein Harian📊")

# Input data pengguna
berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=1.0, step=0.1)
usia = st.number_input("Masukkan usia (tahun):", min_value=1, step=1)
jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Laki-laki", "Wanita"])

st.write("Masukkan sumber kafein yang dikonsumsi hari ini:")
# Input sumber kafein
kopi = st.number_input("Berapa cangkir kopi (240 ml):", min_value=0, step=1)
teh = st.number_input("Berapa cangkir teh (240 ml):", min_value=0, step=1)
minuman_energi = st.number_input("Berapa kaleng minuman energi (250 ml):", min_value=0, step=1)

# Kandungan kafein per unit (dalam mg)
kafein_kopi = 95 * kopi
kafein_teh = 47 * teh
kafein_energi = 80 * minuman_energi

# Total konsumsi kafein
total_kafein = kafein_kopi + kafein_teh + kafein_energi

# Tombol hitung
if st.button("Hitung"):
    if berat_badan > 0 and usia > 0:
        hasil = hitung_kafein_ideal(berat_badan, usia, jenis_kelamin, total_kafein)
        
        st.subheader("Hasil Kalkulator Kafein")
        st.write(f"**Batas Harian:** {hasil['batas_harian_mg']:.2f} mg")
        st.write(f"**Konsumsi Kafein:** {hasil['konsumsi_kafein_mg']} mg")
        st.write(f"**Sisa Batas Aman:** {hasil['sisa_kafein_mg']:.2f} mg")
        st.write(f"**Status:** {hasil['status']}")
    else:
        st.error("Mohon isi semua data dengan benar!")
