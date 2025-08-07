ASHRAE 62.1-2022 Ventilation Rate Procedure (VRP) Calculator
===========================================================

This project provides tools for calculating the required outdoor air ventilation rates for single-zone, 100% outdoor-air, and multiple-zone recirculating systems using the Ventilation Rate Procedure (VRP) of ASHRAE Standard 62.1-2022, the leading standard for ventilation and indoor air quality in commercial and institutional buildings.

Overview
--------

The calculator estimates outdoor air requirements based on occupancy category, space area, number of people (optional), and zone air distribution effectiveness (Ez), following ASHRAE 62.1 Table 6-1 and the calculation procedures for system types 1, 2, and 3.  
The program includes a console application for terminal use, with structured input via command line arguments or shell scripts for multi-zone scenarios.

Files and Structure
-------------------

File Name             | Purpose / Function
--------------------- | ------------------------------------------------------------
mainVRPconsole.py     | Console application for running the VRP calculation. Supports all three system types: 1 (single-zone), 2 (100 percent outdoor-air, multi-zone), and 3 (multiple-zone recirculating). Outputs results in tables for each space and the system, including D, Vou, Ev, Vpz-min, and Vot.
vrp_dictionaries.py   | VRP Lookup Table & Calculation Functions. Provides ASHRAE 62.1 Table 6-1 as a Python dictionary (VRP_TABLE_6_1), and calculation functions for Vbz, Voz, Vot, occupant diversity, Vou, and ventilation efficiency.
multi-zone.sh         | Example Linux shell file demonstrating multi-zone input for system_type 3, assembling command-line arguments for parallel spaces.
runVRP.sh             | Example shell script for batch running VRP calculations over a list of zones/spaces.
README.md             | This file. Explains usage, features, and references.

How It Works
------------

- Occupancy Category: Select from any ASHRAE Table 6-1 category (e.g., "Classrooms (age 9 plus)", "Office space", etc.). Must match the VRP table exactly.
- Area (ft2): Enter the floor area in square feet (or use area_m2 for m2). One value per space.
- Number of People: Optional; if omitted, will be calculated from the default occupant density for the category and area (rounded up).
- Ez: Optional. Zone air distribution effectiveness (from ASHRAE Table 6-2 or engineering judgment). Default is 1.0.
- system_type: 1 = Single-Zone (default), 2 = 100 percent Outdoor-Air (multi-zone), 3 = Multiple-Zone Recirculating System.
- Lists: For multi-zone calculations (types 2 and 3), input lists for -occupancy, -area_ft2 (or -area_m2), -num_people, and -Ez must all be the same length.

Key Equations (ASHRAE 62.1-2022)
--------------------------------

- Breathing Zone Outdoor Airflow:  
  Vbz = Rp x P + Ra x A  
    where:  
    Rp = Outdoor airflow rate per person (cfm/person)  
    P  = Number of people  
    Ra = Outdoor airflow rate per area (cfm/ft2)  
    A  = Area (ft2)

- Zone Outdoor Airflow:  
  Voz = Vbz / Ez  
    Ez = Zone air distribution effectiveness

- Uncorrected Outdoor-Air Intake (for system_type 3):  
  D = sum(num_people) / sum(ceil(default_density * area / 1000))  
  Vou = D x sum(Rp x Pz) + sum(Ra x Az)

- System Ventilation Efficiency (simplified):  
  If D < 0.60: Ev = 0.88 x D + 0.22  
  Else: Ev = 0.75

- Design Outdoor-Air Intake:  
  Vot = Vou / Ev

- Minimum Primary Airflow (each zone):  
  Vpz-min = 1.5 x Voz

Usage
-----

Console (single zone or multi-zone)
-----------------------------------

Example for single zone:

    python mainVRPconsole.py -occupancy "Office space" -area_ft2 950 -num_people 5 -Ez 1.0

Example for multi-zone recirculating system (system_type 3):

    python mainVRPconsole.py \
      -system_type 3 \
      -occupancy "Office space" "Conference/meeting" "Break rooms (General)" \
      -area_ft2 1200 300 200 \
      -num_people 10 12 3 \
      -Ez 1.0 0.8 0.8

All list inputs must be the same length.

Shell Script Example
--------------------

The project supports running with Linux shell files for large or batch inputs.
See multi-zone.sh for an example:

    #!/bin/bash

    OCCUPANCY=( "Office space" "Conference/meeting" "Break rooms (General)" )
    AREA=(1200 300 200)
    PEOPLE=(10 12 3)
    EZ=(1.0 0.8 0.8)
    N=${#OCCUPANCY[@]}
    OCC_ARGS=""
    AREA_ARGS=""
    PEOPLE_ARGS=""
    EZ_ARGS=""
    for ((i=0; i<N; i++)); do
      OCC_ARGS="$OCC_ARGS \"${OCCUPANCY[i]}\""
      AREA_ARGS="$AREA_ARGS ${AREA[i]}"
      PEOPLE_ARGS="$PEOPLE_ARGS ${PEOPLE[i]}"
      EZ_ARGS="$EZ_ARGS ${EZ[i]}"
    done
    eval python3 mainVRPconsole.py -system_type 3 -occupancy $OCC_ARGS -area_ft2 $AREA_ARGS -num_people $PEOPLE_ARGS -Ez $EZ_ARGS

Calculation Results
-------------------

The program outputs the following for each space and system:
- Occupancy category, area (ft2, m2), people, Rp, Ra, Ez, Vbz, Voz
- For multi-zone: occupant diversity (D), uncorrected outdoor air intake (Vou), system ventilation efficiency (Ev), minimum primary airflow for each zone (Vpz-min), and the required system outdoor air intake (Vot) with calculation notes.

References
----------

- ASHRAE Standard 62.1-2022: Ventilation for Acceptable Indoor Air Quality  
  https://www.ashrae.org/technical-resources/standards-and-guidelines/read-only-versions-of-ashrae-standards
- ASHRAE Table 6-1: Minimum Outdoor Air Requirements
- ASHRAE Table 6-2: Zone Air Distribution Effectiveness

Notes
-----

- All calculations follow the procedure and default values of ASHRAE 62.1-2022.
- Results are presented in both imperial (ft2, cfm) and metric (m2) units.
- This tool is for engineering estimation and compliance support; final ventilation rates should be confirmed per local codes and engineering review.
