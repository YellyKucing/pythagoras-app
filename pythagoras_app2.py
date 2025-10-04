import streamlit as st
import random
import matplotlib.pyplot as plt

# Atur halaman
st.set_page_config(page_title="Pythagoras Calculator", page_icon="📐", layout="centered")

# CSS untuk Comic Sans + efek warna-warni
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/comic-sans-ms');
    .welcome {
        font-family: 'Comic Sans MS', sans-serif;
        font-size: 32px;
        color: lime;
        text-align: center;
        background-color: black;
        padding: 15px;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Sambutan
st.markdown("<div class='welcome'>Selamat Datang di Kalkulator Teorema Pythagoras!</div>", unsafe_allow_html=True)

# Input pilihan perhitungan
st.subheader("🔢 Pilih sisi yang ingin dihitung:")
option = st.radio("Hitung sisi:", ["c (miring)", "a (tegak)", "b (tegak)"])

# Variabel awal
a = b = c = None

if option == "c (miring)":
    a = st.number_input("Masukkan sisi a", min_value=0.0, step=1.0)
    b = st.number_input("Masukkan sisi b", min_value=0.0, step=1.0)
    if st.button("Hitung!"):
        c = (a**2 + b**2) ** 0.5
        st.success(f"Hasil: c = √(a² + b²) = {c}")

elif option == "a (tegak)":
    c = st.number_input("Masukkan sisi miring c", min_value=0.0, step=1.0)
    b = st.number_input("Masukkan sisi b", min_value=0.0, step=1.0)
    if st.button("Hitung!"):
        if c > b:
            a = (c**2 - b**2) ** 0.5
            st.success(f"Hasil: a = √(c² - b²) = {a}")
        else:
            st.error("⚠️ c harus lebih besar dari b!")

elif option == "b (tegak)":
    c = st.number_input("Masukkan sisi miring c", min_value=0.0, step=1.0)
    a = st.number_input("Masukkan sisi a", min_value=0.0, step=1.0)
    if st.button("Hitung!"):
        if c > a:
            b = (c**2 - a**2) ** 0.5
            st.success(f"Hasil: b = √(c² - a²) = {b}")
        else:
            st.error("⚠️ c harus lebih besar dari a!")

# Jika semua sisi sudah ada, tampilkan segitiga
if a and b and c:
    fig, ax = plt.subplots()
    # Titik segitiga
    x = [0, a, 0, 0]
    y = [0, 0, b, 0]

    ax.plot(x, y, 'b-', linewidth=2)
    ax.fill(x, y, "skyblue", alpha=0.3)

    # Label sisi
    ax.text(a/2, -0.3, f"a = {a:.2f}", fontsize=12, color="red", ha="center")
    ax.text(-0.3, b/2, f"b = {b:.2f}", fontsize=12, color="green", va="center", rotation=90)
    ax.text(a/2, b/2, f"c = {c:.2f}", fontsize=12, color="purple", ha="center", rotation=30)

    ax.set_aspect("equal")
    ax.axis("off")
    st.pyplot(fig)

# Elemen tambahan: simbol matematika random di layar
symbols = ["+", "-", "×", "÷", "√", "π", "Σ", "∆", "∞", "5", "9", "12", "24", "42"]
for i in range(8):
    st.markdown(
        f"<div style='position:absolute; "
        f"left:{random.randint(20,500)}px; top:{random.randint(150,500)}px; "
        f"font-size:{random.randint(18,45)}px; transform:rotate({random.randint(-40,40)}deg); "
        f"color:rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)}); "
        f"font-weight:bold;'>{random.choice(symbols)}</div>",
        unsafe_allow_html=True
    )

# Footer - link ke Instagram
st.markdown(
    "<hr style='margin-top:50px;margin-bottom:10px;'>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align:center; font-family:Comic Sans MS; font-size:18px;'>"
    "Creator: <a href='https://www.instagram.com/fauzierid1_/?next=%2F' target='_blank' style='color:#FF1493; text-decoration:none;'>@fauzierid1_</a>"
    "</div>",
    unsafe_allow_html=True
)
