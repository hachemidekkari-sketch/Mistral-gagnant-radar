import streamlit as st
import pandas as pd
import random
import urllib.parse

# --- CONFIGURATION ---
st.set_page_config(page_title="WINNER RADAR PRO - FR", layout="wide")

st.markdown("""
    <style>
    .stMetric { background-color: #1e1e1e; color: white; padding: 20px; border-radius: 15px; border: 1px solid #333; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2E86C1; color: white; font-weight: bold; }
    .winner-box { padding: 20px; border-radius: 15px; border: 2px solid #28B463; background-color: #E9F7EF; color: #186A3B; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DONNÉES EN FRANÇAIS ---
TRENDS_DB = {
    "Brosse de Nettoyage Électrique": {"en": "Electric Spin Scrubber", "us": 92, "fr": 15, "growth": +180, "price": 35.00},
    "Ventilateur de Cou Portable": {"en": "Portable Neck Fan", "us": 85, "fr": 10, "growth": +250, "price": 24.90},
    "Machine à Dumplings Auto": {"en": "Automatic Dumpling Maker", "us": 78, "fr": 5, "growth": +320, "price": 19.90},
    "Adaptateur CarPlay Sans Fil": {"en": "Wireless CarPlay Adapter", "us": 88, "fr": 20, "growth": +90, "price": 49.90},
    "Masque Visage LED Therapy": {"en": "LED Face Mask", "us": 80, "fr": 35, "growth": +110, "price": 45.00},
    "Organisateur de Voiture Luxe": {"en": "Car Seat Gap Organizer", "us": 74, "fr": 12, "growth": +65, "price": 22.50}
}

def get_sourcing_links(product_en):
    q = urllib.parse.quote(product_en)
    return {
        "🚀 AliExpress (Filtre Livraison 10j)": f"https://www.aliexpress.com/wholesale?SearchText={q}&isFreeShip=y&isFavorite=y&shipFromCountry=CN&deliveryDays=12",
        "📦 Alibaba (Gros/Personnalisé)": f"https://www.alibaba.com/trade/search?SearchText={q}",
        "🇨🇳 1688 (Prix Usine)": f"https://search.1688.com/view/index.htm?keywords={q}"
    }

# --- INTERFACE ---
st.title("🚀 Winner Radar : Import USA/Chine ➔ France")
st.subheader("Objectif : Livraison Rapide & Marge Haute")

# Sidebar
with st.sidebar:
    st.header("💎 Pépites Détectées")
    st.write("Produits validés (Gros décalage US/FR) :")
    for fr_name in TRENDS_DB.keys():
        if st.button(fr_name):
            st.session_state.current_prod = fr_name

# Logique de recherche
selected_prod = st.session_state.get('current_prod', "Brosse de Nettoyage Électrique")
data = TRENDS_DB[selected_prod]
product_en = data['en']
sell_price = st.number_input("Ton prix de vente cible (€)", 15.0, 150.0, float(data['price']))

# Affichage des Metrics
st.markdown(f"### Analyse du produit : **{selected_prod}** (*{product_en}*)")
c1, c2, c3 = st.columns(3)
c1.metric("Score USA", f"{data['us']}/100", "🔥 Viral")
c2.metric("Score France", f"{data['fr']}/100", f"Opportunité: {data['us']-data['fr']}%", delta_color="normal")
c3.metric("Croissance Hebdo", f"+{data['growth']}%", "En hausse")

st.divider()

# Business & Sourcing
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='winner-box'>", unsafe_allow_html=True)
    st.markdown("#### 💰 Calcul Rentabilité")
    taxes = sell_price * 0.13
    pub = sell_price * 0.30
    frais = (sell_price * 0.04) + 0.30
    profit_net = sell_price * 0.25 # On garde 25% net
    buy_max = sell_price - taxes - pub - frais - profit_net
    
    st.write(f"✅ **Profit Net visé (25%) :** {round(profit_net, 2)}€")
    st.write(f"📢 **Budget Pub Max :** {round(pub, 2)}€")
    st.markdown(f"### 🎯 PRIX ACHAT MAX : {round(buy_max, 2)}€")
    st.caption("Frais de port inclus ! Cherche ce prix sur AliExpress.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("#### 📦 Sourcing & Logistique")
    links = get_sourcing_links(product_en)
    for name, url in links.items():
        st.markdown(f"**[{name}]({url})**")
    
    st.info("""
    **💡 Conseil Logistique :**
    Sur AliExpress, cherche le logo **'Choice'**. 
    Il garantit souvent une livraison en **10 jours ouvrés** vers la France (souvent via Colis Privé ou Colissimo).
    """)

# Section Stratégie Vidéo
st.divider()
st.subheader("🎥 Ta stratégie de contenu (UGC)")
cv1, cv2, cv3 = st.columns(3)
cv1.write("1. **Le Hook (0-3s) :** Montre le problème immédiatement (ex: une tache impossible à enlever).")
cv2.write("2. **La Solution :** Action du produit avec une musique tendance.")
cv3.write("3. **L'Appel à l'action :** 'Lien en bio -50% seulement aujourd'hui'.")
