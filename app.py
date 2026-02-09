import streamlit as st
import random
from datetime import datetime

# --- SETTING TANGGAL KETEMU (23 Agustus 2024) ---
tanggal_ketemu = datetime(2024, 8, 23, 0, 0) 

st.set_page_config(page_title="Special for Giee", page_icon="🌸")

# --- CSS CUSTOM: ANIMASI & TAMPILAN ---
st.markdown("""
    <style>
    header {visibility: hidden;}
.stAppDeployButton {display:none;}
footer {visibility: hidden;}
    .stApp { background-color: #fff0f5; }
    .stApp, .stMarkdown, p, label { color: #5d1432 !important; font-weight: 500; }
    
    .stButton>button {
        width: 100%; border-radius: 25px; height: 3.5em;
        background-color: #ff69b4; color: white !important;
        font-weight: bold; border: none; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .particle {
        position: fixed; top: -10%; user-select: none; z-index: 9999;
        animation: falling 4s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Efek Visual
def sakura_fall():
    sakura = "".join([f'<div class="particle" style="left:{random.randint(0,95)}%; color:#ffb6c1; font-size:{random.randint(15,25)}px; animation-delay:{random.random()*3}s;">🌸</div>' for _ in range(30)])
    st.markdown(sakura, unsafe_allow_html=True)

def love_rain():
    hearts = "".join([f'<div class="particle" style="left:{random.randint(0,95)}%; color:#ff1493; font-size:{random.randint(15,25)}px; animation-delay:{random.random()*3}s;">❤️</div>' for _ in range(30)])
    st.markdown(hearts, unsafe_allow_html=True)

st.title("Giee's Happiness 🌸")

# --- 1. LOVE COUNTER (SENTIMENTAL) ---
sekarang = datetime.now()
selisih = sekarang - tanggal_ketemu
hari, sisa = selisih.days, selisih.seconds
jam, menit = sisa // 3600, (sisa % 3600) // 60

st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 20px; text-align: center; border: 2px solid #ffb6c1; margin-bottom: 20px;">
        <p style='margin-bottom: 5px;'>Sudah berapa lama kita kenal?</p>
        <p style='font-size: 24px; font-weight: bold; color: #ff69b4;'>{hari} Hari, {jam} Jam, {menit} Menit</p>
        <p style='font-size: 13px; color: #db7093;'>Sejak 23 Agustus 2024 ❤️</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. ROMANTIC WEATHER (PEMBUKA) ---
with st.expander("☁️ Romantic Weather Forecast"):
    if st.button("Cek Cuaca Hari Ini"):
        p = random.choice([
            {"s": "Cerah Berawan", "d": "Hati Giee cerah, rindu sedikit. Hubungi Mas ya! ☀️"},
            {"s": "Hujan Manja", "d": "Potensi hujan kasih sayang 90%. Butuh puk-puk virtual. 🌧️"},
            {"s": "Angin Kangen", "d": "Ada hembusan angin kangen kencang dari arah Mas. 🌬️"},
            {"s": "Cahaya Indah", "d": "Hari ini indah karena Giee selalu ada di pikiran Mas. ✨"}
        ])
        st.write(f"### {p['s']}\n{p['d']}")

# --- 3. GIEE'S VIBE (INTERAKSI UTAMA) ---
with st.expander("✨ Giee's Current Vibe"):
    vibe = st.radio("Giee lagi ngerasa apa sekarang?", ["Lagi Butuh Puk-puk 🥺", "Mode Cantik & Happy 🥰", "Dunia Lagi Gak Asik 😡", "Baterai Low 😴"])
    if st.button("Kirim Vibe ke Mas"):
        if "Puk-puk" in vibe:
            love_rain()
            st.info("Sini Mas puk-puk online... 🤗 Kamu hebat sudah bertahan hari ini. Mas bangga!")
        elif "Cantik" in vibe:
            sakura_fall()
            st.success("Tuh kan! Aura cantiknya emang gak ada lawan! 🌸")
        elif "Gak Asik" in vibe:
            st.warning("Siapa yang bikin kesel? Bilang Mas! Nanti kita jajan enak! 🍦")
        else:
            st.error("Istirahat ya sayang. Mas tungguin di sini. 😴")

# --- 4. DOSIS SAYANG (PENYEJUK HATI) ---
with st.expander("💊 Dosis Sayang Harian"):
     pujian = [
        "Lagi apa? Ingat ya, ada Mas yang selalu bangga sama kamu. ❤️",
        "Kalau capek, senderan ke Mas aja ya. Gak usah dipaksa. 🌸",
        "Giee itu hebat banget tau, Mas beneran kagum sama cara kamu hadapi hari ini.",
        "Meskipun hari ini berat, buat Mas kamu tetep yang paling juara. ✨",
        "Jatah bahagia kamu hari ini sudah diambil belum? Kalau belum, sini Mas kasih. 🍦",
        "Makasih ya sudah mau sabar dan terus bareng Mas sampai sekarang. 🥰",
        "Apapun yang terjadi, Mas selalu di pihak kamu. No debat! 🛡️",
        "Cuma mau bilang: Kamu cantik banget hari ini (dan tiap hari sih). 🌙",
        "Jangan lupa minum air putih dan istirahat ya, kesayangan Mas. 🌻",
        "Gak sabar pengen ketemu terus pamerin ke dunia kalau Mas punya kamu. 🎀"
    ]
    if st.button("Ambil Dosis Cinta"):
        st.write(f"## {random.choice(pujian)}")

# --- 5. SECRET COUPONS (CLOSING) ---
with st.expander("🎟️ Giee's Secret Coupons"):
    kupon_pilihan = st.selectbox("Pilih hadiahmu hari ini:", [
        "Kupon 'Dunia Milik Giee' (Jalan-jalan bebas)",
        "Kupon 'Puk-puk Anti Capek' (Special dari Mas)",
        "Kupon 'Ice Cream Date' (Langsung jajan!)",
        "Kupon 'Mas No Debat' (Mas nurut seharian)",
        "Kupon 'Midnight Talk' (Mas siap dengerin curhat)",
        "Kupon 'Healing Dadakan' (Cari angin malem/jajan)",
        "Kupon 'Bebas Marah Mas' (Otomatis dimaafin)",
        "Kupon 'Giee si Ratu Menu' (Pilih makan sesukamu)"
    ])
    if st.button("Klaim Kupon!"):
        sakura_fall()
        st.write(f"### KLAIM BERHASIL!")
        st.write(f"Kamu memilih: **{kupon_pilihan}**")
        st.write(f"KODE: GIEE-HAPPY-{random.randint(100, 999)}")
        st.toast("Screenshot & kirim ke WhatsApp Mas ya!")

st.markdown("---")

st.caption("Made with ❤️ for Giee")


