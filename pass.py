import streamlit as st
import re

# Title
st.title("🔐 Password Strength Checker")
st.markdown("""## Well come to the ultimate Password Strenght Checker🔐
""")

# Password Input
password = st.text_input("Enter your password:", type="password")

def check_strength(pw):
    score = 0

    # Criteria checks
    if len(pw) >= 8:
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        score += 1

    return score

def get_strength_label(score):
    if score <= 2:
        return "❌ Weak", "red"
    elif score == 3 or score == 4:
        return "⚠️ Moderate", "orange"
    else:
        return "✅ Strong", "green"

if password:
    strength_score = check_strength(password)
    label, color = get_strength_label(strength_score)
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold'>{label}</span>", unsafe_allow_html=True)
