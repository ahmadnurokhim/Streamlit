import streamlit as st
from lorem_text import lorem


# Configuring page
st.set_page_config(
    page_title="Tes Streamlit",
    layout="wide"
)

# Writing in streamlist
st.write("Hello World!")
"Hello world 2"
"# MANTAP 1"
"## MANTAP 1"
"### MANTAP 1"

tombol_tes = st.button("PENCET")
tombol_tes

cekbox = st.checkbox("Cunci")
if cekbox:
    st.write("CUNCIMUX")
else:
    st.write("HMMZZ")

ini_radio = st.radio("PILIH 1", ["AYAM", "RENDANG"])
ini_radio

ini_selectbox = st.selectbox("PILIH 1", ["AYAM", "RENDANG"])
ini_selectbox

ini_multiselect = st.multiselect("PILIH 1", ["AYAM", "RENDANG"])
ini_multiselect

ini_slider = st.slider(
    label="COBA SLIDE",
    min_value=0.0,
    max_value=1.0,
    step=0.01
)
ini_slider

ini_selectslider = st.select_slider(
    "UKURAN BAJOO",
    ["S", "M", "L"]
)
ini_selectslider

ini_kodepos = st.number_input(
    "KODE POS",
    min_value=0,
    max_value=99999,
    step=1
)
ini_kodepos

nama = st.text_input("NAMAMU?")
nama

komen = st.text_area("KOMENNN")
komen

tanggal = st.date_input("TANGGAL LAHIR")
tanggal

jam = st.time_input("MASUKKAN WAKTU")
jam

warna = st.color_picker("WARNA")
warna

col1, col2, col3 = st.columns(3)
with col1:
    "COL1"
with col2:
    "COL2"
with col3:
    "COL3"

kol1, kol2 = st.columns([1, 3])
with kol1:
    "kOL1"
with kol2:
    "kOL2"

with st.sidebar:
    "Titanic"
    kimi_no_nawa = st.text_input("Kimi no nawa?")
    with st.expander("Lorem"):
        st.write(lorem.paragraphs(2))

tab1, tab2, tab3 = st.tabs(['tab 1', 'tab2', 'tab3'])

with tab1:
    st.write(lorem.paragraphs(2))
with tab2:
    st.write(lorem.paragraphs(2))
with tab3:
    st.write(lorem.paragraphs(2))