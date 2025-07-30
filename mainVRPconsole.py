import re
import math
from vrp_dictionaries import single_zone_vrp_Vbz, single_zone_vrp_Voz, VRP_TABLE_6_1

FT2_TO_M2 = 0.092903  # 1 ft² = 0.092903 m²



def read_inputs(path):
    pat = re.compile(r'^\s*([^#=]+?)\s*=\s*([^\n#]+)')
    values = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = pat.match(line)
            if m:
                key, val = m.groups()
                values[key.strip()] = val.strip()
    return values




def main(cfg_file="inputs.txt"):
    params = read_inputs(cfg_file)
    occupancy = params["occupancy"]
    area_ft2 = float(params["area_ft2"])
    area_m2 = area_ft2 * FT2_TO_M2
    num_people = params.get("num_people", None)
    Ez = float(params.get("Ez", 1.0))  
    if num_people is not None:
        num_people = float(num_people)
    else:
        # Estimate using default occupant density from VRP table
        row = VRP_TABLE_6_1[occupancy]
        density = row["Default_Occ_Density_per_1000ft2"]
        if not density or area_ft2 == 0:
            raise ValueError("num_people not given and default density is not available.")
        num_people = math.ceil((density * area_ft2) / 1000)

    Voz, info = single_zone_vrp_Voz(occupancy, area_ft2, num_people, VRP_TABLE_6_1, Ez)


    print("\nASHRAE 62.1-2022 Ventilation Rate Procedure (Single Zone)\n")
    print(f"{'Parameter':<20} | {'Value':>12} | {'Units':<10} | {'Notes'}")
    print("-" * 65)
    print(f"{'Occupancy':<20} | {occupancy:>12} | {'':<10} |")
    print(f"{'Area':<20} | {area_ft2:12.2f} | {'ft²':<10} |")
    print(f"{'Area':<20} | {area_m2:12.2f} | {'m²':<10} |")
    print(f"{'People':<20} | {num_people:12.2f} | {'persons':<10} | (default density: {info['default_density']}/1000 ft²)")
    print(f"{'Rp':<20} | {info['Rp']:12.2f} | {'cfm/person':<10} |")
    print(f"{'Ra':<20} | {info['Ra']:12.2f} | {'cfm/ft²':<10} |")
    print(f"{'Ez':<20} | {info['Ez']:12.2f} | {'-':<10} | Zone Air Distribution Effectiveness")
    print(f"{'Vbz':<20} | {info['Vbz']:12.2f} | {'CFM':<10} | [Breathing Zone Outdoor Air]")
    print(f"{'Voz':<20} | {Voz:12.2f} | {'CFM':<10} | [Zone Outdoor Airflow, Eq. 6-2]")
    print("-" * 65)
    print(f"{'Equation used:':<20} | {info['notes']}")
    print()





if __name__ == "__main__":
    main()
