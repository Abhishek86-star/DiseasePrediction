import pickle
import streamlit as st
import warnings

warnings.filterwarnings("ignore")

# ---------------- Page Configuration -----------------
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="centered"
)
# ---------------- Custom CSS -----------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 55%, #ecfeff 100%);
    color: #1e293b;
}

/* Main title */
.title {
    text-align: center;
    color: #123b70;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -0.8px;
}

/* Subtitle */
.sub {
    text-align: center;
    color: #64748b;
    font-size: 16px;
}

/* Content card */
.box {
    background: rgba(255, 255, 255, 0.96);
    padding: 26px;
    border: 1px solid #dbeafe;
    border-radius: 18px;
    box-shadow: 0 8px 28px rgba(30, 64, 175, 0.09);
}

/* Input labels */
.stNumberInput label,
.stSelectbox label {
    color: #334155 !important;
    font-weight: 600 !important;
}

/* Input fields */
.stNumberInput input {
    background: #ffffff !important;
    border-radius: 10px !important;
}

/* Predict button */
.stButton > button {
    width: 100%;
    min-height: 44px;
    background: linear-gradient(90deg, #1d4ed8, #0f766e);
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1e40af, #115e59);
    box-shadow: 0 5px 14px rgba(29, 78, 216, 0.2);
}

/* Prediction result */
.result {
    background: #ffffff;
    padding: 26px 20px;
    border: 1px solid #bfdbfe;
    border-left: 6px solid #0f766e;
    border-radius: 15px;
    text-align: center;
    font-size: 25px;
    color: #0f766e;
    font-weight: 750;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.06);
}

/* Warning boxes */
.stAlert {
    border-radius: 11px;
}

/* Footer */
footer {
    visibility: hidden;
}

/* Mobile-friendly title */
@media (max-width: 600px) {
    .title {
        font-size: 30px;
    }

    .box {
        padding: 16px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- Title -----------------
st.markdown("<div class='title'>🩺 Disease Prediction System</div>", unsafe_allow_html=True)

st.markdown(
"<div class='sub'>Predict the expected disease using patient's health parameters.</div>",
unsafe_allow_html=True)

st.write("")

# ---------------- Sidebar -----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966486.png", width=120)

st.sidebar.title("Health Tips")

st.sidebar.success("""
✔ Drink plenty of water

✔ Exercise daily

✔ Eat healthy food

✔ Sleep 7-8 hours

✔ Regular health checkups
""")

# ---------------- Input Card -----------------

st.subheader("📝 Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("👤 Age", 1, 120)

    hrb = st.number_input(
        "❤️ Heart Rate (bpm)",
        30,
        220
    )


with col2:
    bt_f = st.number_input(
        "Body Temperature (°F)",
        min_value=90.0,
        max_value=110.0,
        value=98.6,
        step=0.1,
        format="%.1f"
    )

    bt = (bt_f - 32) * 5 / 9

    
    os = st.number_input(
        "🫁 Oxygen Saturation (%)",
        50,
        100
    )

st.write("")

btn = st.button("🔍 Predict Disease", use_container_width=True)


# ---------------- Prediction -----------------
if btn:
    dp = pickle.load(open("dp_new.pkl", "rb"))

    warnings = []

    # Temperature is converted from Fahrenheit to Celsius 
    if bt_f >= 104:
        warnings.append("Very high body temperature entered.")
    elif bt_f < 95:
        warnings.append("Very low body temperature entered.")

    if hrb > 120:
        warnings.append("High heart rate entered.")
    elif hrb < 50:
        warnings.append("Low heart rate entered.")

    if os < 90:
        warnings.append("Very low oxygen saturation entered.")
    elif os < 95:
        warnings.append("Oxygen saturation is below the usual range.")


    for warning in warnings:
        st.warning(warning + " Model prediction may be unreliable.")

    res = dp.predict([[age, hrb, bt, os]])[0]

    st.write("")



    st.markdown(f"""
    <div class="result">
        🩺 Expected Disease<br><br>
        <span style='font-size:35px;color:#dc2626;'>{res}</span>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

# ---------------- Footer -----------------
st.write("")
st.markdown("---")
st.markdown(
"""
<center>
Made with ❤️ using <b>Python & Streamlit</b><br>
© 2026 Disease Prediction System
</center>
""",
unsafe_allow_html=True
)