import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

# Title
st.title("Bosozoku Car Builder")

# User input
name = st.text_input("Enter your driver name:", "street Racer")

st.subheader(f"{name}'s Custom Build")

#customization sliders

exhaust = st.slider("Exhaust Height", 0, 10, 5)
exhaust2 = st.slider("Exhaust Shape", heart, star, straight)
spoiler = st.slider("Spoiler Size", 0, 10, 5)
ride_height = st.slider("Lowered Suspension", 0, 10, 5)
paint = st.slider("Paint Flsshiness", 0, 10, 5) 

# NEW: Exhaust shape dropdown
exhaust_shape = st.selectbox("Choose Exhaust Shape:", ["Straight pipes", "Heart pipes", "Star pipes", "Curved pipes"])

# NEW: Paint color picker
paint_color = st.color_picker("Pick Your Paint Color:", "#ff0000")

# Data for chart
features = ["Exhaust Height", "Spoiler", "Suspension", "Paint Flash"]
values = [Exhaust_Height, Spoiler, Ride_Height, Paint_Flash]

df = pd.DataFrame({"Feature": features, "Level": values})

# Chart type selector
chart_type = st.selectbox("Choose visualization:", ["Bar Chart", "Line Chart"])

# Build button
if st.button("Build My Car"):

    st.subheader(" Build Intensity")

    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        ax.bar(df["Feature"], df["Level"])
    else:
        ax.plot(df["Feature"], df["Level"], marker='o')

    ax.set_ylabel("Intensity Level")
    ax.set_title(f"{name}'s Bosozoku Style")

    st.pyplot(fig)

    # Show selected customization
    st.subheader(" Custom Design Preview")
    st.write(f"**Exhaust Style:** {exhaust_shape}")
    st.write(f"**Paint Color:** {paint_color}")

    # Display color visually
    st.markdown (f"<div style='width:100px;height:50px;background-color:{paint_color};border:1px solid #000'></div>", unsafe_allow_html=True)

# Style rating system
if st.checkbox("Show Style Rating"):
    total = sum(values)

    # Bonus points based on exhaust type
    if exhaust_shape == "Heart shape":
        total += 5

    if total > 35:
        st.success("EXTREME BOSOZOKU BUILD!")
    elif total > 20:
        st.warning("⚡ Moderate Style Build")
    else:
        st.info("🚗 Mild Custom Build")