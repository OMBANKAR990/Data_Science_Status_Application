import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Data Science Syllabus Viewer", layout="centered")

st.title("📘 Data Science Daily Training Report Generator")

# -----------------------------
# SAMPLE SYLLABUS (Replace with your full syllabus)
# -----------------------------
syllabus = {
    "Day 101": {
        "topic": "Data Modeling & Dashboard Creation with Charts",
        "main_points": [
            "Understanding data models & relationships (One-to-Many, Many-to-Many)",
            "Creating table relationships",
            "Introduction to DAX basics (SUM, COUNT, AVERAGE)",
            "Dashboard Creation with multiple visuals:",
            "Bar Chart",
            "Line Chart",
            "Pie Chart",
            "Column Chart",
            "Card Visual (for KPIs)",
            "Adding slicers and filters for interactivity"
        ]
    }
}

# -----------------------------
# INPUT PANEL
# -----------------------------
day = st.selectbox("Select Training Day", list(syllabus.keys()))

trainer_name = "Om Bankar"
batch_name = "CBZ@ON-X-DSAAI-05~"
batch_mode = "Online"
attendance = "02"

today = datetime.now().strftime("%Y-%m-%d")

# -----------------------------
# FORMAT THE OUTPUT TEXT
# -----------------------------
data = syllabus[day]

output_text = f"""
📚 **Data Science Training Update**

**Date:** {today}  
**Trainer Name:** {trainer_name}  
**Batch Name:** {batch_name}  
**Batch Mode:** {batch_mode}  
**Attendance:** {attendance}  

**Topic:**  
{day}

**{data['topic']}**

**Main Topic:**  
"""

for point in data["main_points"]:
    output_text += f"- {point}\n"

# -----------------------------
# DISPLAY THE OUTPUT
# -----------------------------
st.markdown(output_text)

# -----------------------------
# COPY BUTTON
# -----------------------------
st.code(output_text, language="markdown")
st.download_button("📄 Copy or Download Report", output_text, file_name="training_report.txt")
