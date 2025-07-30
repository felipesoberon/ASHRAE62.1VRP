# ASHRAE 62.1-2022 Ventilation Rate Procedure (VRP) Calculator

This project provides a calculation tool for the **Ventilation Rate Procedure (VRP)** for single-zone systems, as specified in **ASHRAE Standard 62.1-2022: Ventilation for Acceptable Indoor Air Quality**.

- **Desktop GUI** using Tkinter (`mainGUI.py`)
- **Command-line calculation** module (`main.py`)
- **Reference data** (occupancy categories, rates, etc.) in `vrp_dictionaries.py`

## Features

- Calculates required **Zone Outdoor Airflow (Voz)** and **Breathing Zone Outdoor Airflow (Vbz)**
- Supports all occupancy categories from ASHRAE 62.1-2022 Table 6-1, including 2019 addendum ab and 2022 addenda a and b
- User inputs: Occupancy type, area (ft²), people (optional), zone air distribution effectiveness (Ez)
- Results shown in a clear, tabular format in the GUI or console
- Rounds up fractional occupants to the next integer (as per ASHRAE convention)

## Getting Started

### Requirements

- Python 3.7 or newer (Tkinter is included with standard Python)

### Files

- `main.py`: Core calculation logic
- `vrp_dictionaries.py`: Reference data and calculation functions
- `mainGUI.py`: Desktop GUI for interactive use

### Run the GUI

```bash
python mainGUI.py
