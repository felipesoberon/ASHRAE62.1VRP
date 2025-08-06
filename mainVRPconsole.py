import re
import math
import argparse
from vrp_dictionaries import single_zone_vrp_Vbz, single_zone_vrp_Voz, VRP_TABLE_6_1

FT2_TO_M2 = 0.092903  # 1 ft^2 = 0.092903 m^2

def main(**params):

    occupancy = params["occupancy"]
    if occupancy not in VRP_TABLE_6_1:
        print("ERROR: Occupancy category '{}' not found in VRP table.".format(occupancy))
        print("Please check the name and try again. (Case and spelling must match exactly.)")
        print("Voz                  |                     0.00 | CFM          | [Zone Outdoor Airflow, Eq. 6-2]") 
        print()
        return    
    
    if "area_ft2" in params:
        area_ft2 = float(params["area_ft2"])
        area_m2 = area_ft2 * FT2_TO_M2
    elif "area_m2" in params:
        area_m2 = float(params["area_m2"])
        area_ft2 = area_m2 / FT2_TO_M2
    else:
        raise ValueError("Either area_ft2 or area_m2 must be specified.")
    num_people = params.get("num_people", None)
    Ez = float(params.get("Ez", 1.0))
    if num_people is not None:
        num_people = float(num_people)
    else:
        # Estimate using default occupant density from VRP table
        row = VRP_TABLE_6_1[occupancy]
        density = row["Default_Occ_Density_per_1000ft2"]
         
        if not density or area_ft2 == 0:
            print("WARNING: num_people not given and default density is not available. Setting num_people = 0")
            num_people = 0
        else:
            num_people = math.ceil((density * area_ft2) / 1000)


    Voz, info = single_zone_vrp_Voz(occupancy, area_ft2, num_people, VRP_TABLE_6_1, Ez)

    print("\nASHRAE 62.1-2022 Ventilation Rate Procedure (Single Zone)\n")
    # Use wider columns: Parameter=20, Value=24, Units=12, Notes=50
    print("{:<20} | {:>24} | {:<12} | {:<50}".format("Parameter", "Value", "Units", "Notes"))
    print("-" * 115)
    print("{:<20} | {:>24} | {:<12} | {:<50}".format("Occupancy", occupancy, "", ""))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Area", area_ft2, "ft^2", ""))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Area", area_m2, "m^2", ""))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("People", num_people, "persons", "(default density: {}/1000 ft^2)".format(info["default_density"])))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Rp", info["Rp"], "cfm/person", ""))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Ra", info["Ra"], "cfm/ft^2", ""))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Ez", info["Ez"], "-", "Zone Air Distribution Effectiveness"))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Vbz", info["Vbz"], "CFM", "[Breathing Zone Outdoor Air]"))
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Voz", Voz, "CFM", "[Zone Outdoor Airflow, Eq. 6-2]"))
    print("-" * 115)
    print("{:<20} | {:<93}".format("Equation used:", info["notes"]))
    print()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASHRAE 62.1-2022 VRP Console Calculator")
    parser.add_argument("-occupancy", type=str, required=True, help="Occupancy category")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-area_ft2", type=float, help="Area in square feet")
    group.add_argument("-area_m2", type=float, help="Area in square meters")
    parser.add_argument("-num_people", type=float, help="Number of people (if not set, uses default density)")
    parser.add_argument("-Ez", type=float, help="Zone air distribution effectiveness (default=1.0)")
    args = parser.parse_args()
    p = {k: v for k, v in vars(args).items() if v is not None}
    main(**p)
