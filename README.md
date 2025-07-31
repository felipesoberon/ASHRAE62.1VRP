ASHRAE 62.1-2022 Ventilation Rate Procedure (VRP) Calculator
===========================================================

This project provides tools for calculating the required outdoor air ventilation rates for single-zone spaces using the Ventilation Rate Procedure (VRP) of ASHRAE Standard 62.1-2022, the leading standard for ventilation and indoor air quality in commercial and institutional buildings.

Overview
--------

The calculator estimates the outdoor air requirements based on the occupancy category, space area, number of people, and zone air distribution effectiveness (Ez), following ASHRAE 62.1 Table 6-1 and Equation 6-2.  
Two interfaces are included: a console application for terminal use and a GUI for easier interaction.

Files and Structure
-------------------

File Name             | Purpose / Function
--------------------- | ------------------------------------------------------------
mainVRPconsole.py     | Console Application: Main script for running the VRP calculation from the command line. Outputs results as a table, including area in ft² and m², number of people (rounded up), Ez, Vbz, Voz, and calculation notes. Reads parameters from inputs.txt.
mainGUI.py            | Graphical User Interface: Standalone script for the GUI application. Lets users enter input parameters and displays results in a table format. Imports and uses computation functions from mainVRP.py.
mainVRP.py            | Computation Module: Contains the computation logic for the VRP calculation, callable from the GUI or other scripts.
vrp_dictionaries.py   | VRP Lookup Table & Calculation Functions: Provides the full ASHRAE 62.1 Table 6-1 as a Python dictionary (VRP_TABLE_6_1), and functions: single_zone_vrp_Vbz (computes breathing zone OA) and single_zone_vrp_Voz (computes zone OA, Eq. 6-2).
inputs.txt            | Input Parameters File: Editable text file to specify occupancy category, area (ft²), number of people (optional), and Ez (zone air distribution effectiveness). If number of people is omitted, the program estimates it using the default occupant density from the VRP table.

How It Works
------------

- Occupancy Category: Select from any ASHRAE Table 6-1 category (e.g., "Classrooms (age 9 plus)", "Office space", etc.).
- Area (ft²): Enter the floor area of the zone in square feet.
- Number of People: Optional; if omitted, will be calculated from the default density.
- Ez: Enter the zone air distribution effectiveness (from ASHRAE Table 6-2 or engineering judgment).

Key Equations (ASHRAE 62.1-2022)
--------------------------------

- Breathing Zone Outdoor Airflow:  
  Vbz = Rp x P + Ra x A  
    where:  
    Rp = Outdoor airflow rate per person (cfm/person)  
    P  = Number of people  
    Ra = Outdoor airflow rate per area (cfm/ft²)  
    A  = Area (ft²)

- Zone Outdoor Airflow:  
  Voz = Vbz / Ez  
    where:  
    Ez = Zone air distribution effectiveness

Example Input (inputs.txt)
--------------------------

occupancy = Classrooms (age 9 plus)   
area_ft2 = 969   
Ez = 1.0   
num_people = (optional, integer)   

Usage
-----

Console
-------

Run the calculator in the console:

    python mainVRPconsole.py

You can edit inputs.txt to change the parameters.

GUI
---

Run the graphical interface:

    python mainGUI.py

Use the form to enter occupancy, area, people, and Ez, then click "Calculate".

References
----------

- ASHRAE Standard 62.1-2022: Ventilation for Acceptable Indoor Air Quality  
  https://www.ashrae.org/technical-resources/standards-and-guidelines/read-only-versions-of-ashrae-standards
- ASHRAE Table 6-1: Minimum Outdoor Air Requirements
- ASHRAE Table 6-2: Zone Air Distribution Effectiveness

Notes
-----

- All calculations follow the procedure and default values of ASHRAE 62.1-2022.
- Results are presented in both imperial (ft², cfm) and metric (m²) units.
- This tool is for engineering estimation and compliance support; final ventilation rates should be confirmed per local codes and engineering review.



