import streamlit as st

st.title("Time to fix your posture!")

st.subheader("Things to check for:")
posture_checks = [
    "All at 90 degrees: Back, arms, knees and feet",
    "Arms in line with your body",
    "Shoulder back and chin tucked a bit",
    "Finger tips length to the screen",
    "Top of screen at eye level"
]
st.write("- " + "\n- ".join(posture_checks))