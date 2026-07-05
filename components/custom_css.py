import streamlit as st

def load_css():

    st.markdown("""
<style>

.stApp{

background:#0F172A;
color:white;

}

/* Hide Streamlit Header */

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}

/* Sidebar */

section[data-testid="stSidebar"]{

background:#111827;

}

/* Titles */

.main-title{

font-size:42px;

font-weight:700;

text-align:center;

color:#22C55E;

}

.sub-title{

text-align:center;

color:#CBD5E1;

margin-bottom:30px;

}

/* Glass Card */

.glass{

background:rgba(255,255,255,0.08);

border-radius:20px;

padding:25px;

backdrop-filter:blur(12px);

border:1px solid rgba(255,255,255,.15);

box-shadow:0px 10px 30px rgba(0,0,0,.35);

margin-bottom:20px;

}

/* Buttons */

.stButton>button{

background:#16A34A;

color:white;

border-radius:15px;

height:55px;

font-size:18px;

font-weight:bold;

border:none;

}

.stButton>button:hover{

background:#22C55E;

}

/* Number Inputs */

div[data-baseweb="input"]{

background:#1E293B;

border-radius:12px;

}

/* Metric */

[data-testid="metric-container"]{

background:#1E293B;

border-radius:15px;

padding:15px;

}

</style>
""", unsafe_allow_html=True)