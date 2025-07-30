# main_streamlit.py

import streamlit as st
from vrp_dictionaries import VRP_TABLE_6_1
from mainVRP import vrp_calculate

st.set_page_config(page_title="ASHRAE 62.1-2022 VRP Calculator", layout="wide")

st.title("ASHRAE 62.1-2022 Ventilation Rate Procedure (VRP) Calculator")

st.write("""
Calculate required outdoor airflow for single-zone ventilation per ASHRAE 62.1-2022 Table 6-1.
""")

# --- Sidebar Inputs ---
st.sidebar.header("Input Parameters")

occupancy_list = list(VRP_TABLE_6_1.keys())
occupancy = st.sidebar.selectbox("Occupancy Category", occupancy_list, index=occupancy_list.index("Classrooms (age 9 plus)"))
area_ft2 = st.sidebar.number_input("Zone Area (ft²)", min_value=1.0, value=969.0, step=1.0)
num_people = st.sidebar.text_input("Number of People (leave blank for default)", value="")
Ez = st.sidebar.number_input("Zone Air Distribution Effectiveness (Ez)", min_value=0.1, max_value=2.0, value=1.0, step=0.05)

# --- Calculate Button ---
if st.sidebar.button("Calculate"):
    try:
        if num_people.strip() == "":
            num_people_val = None
        else:
            num_people_val = int(float(num_people))

        output, Voz, info = vrp_calculate(occupancy, area_ft2, num_people_val, Ez)

        # Build a results table
        st.subheader("Results Table")
        # For nice formatting, use a dataframe
        import pandas as pd
        df = pd.DataFrame(output, columns=["Parameter", "Value", "Units", "Notes"])
        st.table(df)

        st.success(f"Zone Outdoor Airflow (Voz): {Voz:.2f} CFM")
        st.code(info["notes"], language="text")

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("""
---
*2025*
""")
