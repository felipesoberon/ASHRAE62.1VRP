# main.py

from vrp_dictionaries import single_zone_vrp_Voz, VRP_TABLE_6_1

FT2_TO_M2 = 0.092903

def vrp_calculate(occupancy, area_ft2, num_people=None, Ez=1.0):
    """
    Returns (results_list, Voz, info_dict)
    results_list: list of table rows to display (Parameter, Value, Units, Notes)
    Voz: float
    info_dict: calculation details
    """
    if num_people is None:
        row = VRP_TABLE_6_1[occupancy]
        density = row["Default_Occ_Density_per_1000ft2"]
        if not density or area_ft2 == 0:
            print("WARNING: num_people not given and default density is not available. Setting num_people = 0")
            num_people = 0
        else:
            import math
            num_people = math.ceil((density * area_ft2) / 1000)

    Voz, info = single_zone_vrp_Voz(occupancy, area_ft2, num_people, VRP_TABLE_6_1, Ez)
    area_m2 = area_ft2 * FT2_TO_M2

    output = []
    output.append(("Occupancy", occupancy, "", ""))
    output.append(("Area", f"{area_ft2:.2f}", "ft²", ""))
    output.append(("Area", f"{area_m2:.2f}", "m²", ""))
    output.append(("People", f"{num_people}", "persons", f"(default density: {info['default_density']}/1000 ft²)"))
    output.append(("Rp", f"{info['Rp']:.2f}", "cfm/person", ""))
    output.append(("Ra", f"{info['Ra']:.2f}", "cfm/ft²", ""))
    output.append(("Ez", f"{info['Ez']:.2f}", "-", "Zone Air Distribution Effectiveness"))
    output.append(("Vbz", f"{info['Vbz']:.2f}", "CFM", "[Breathing Zone Outdoor Air]"))
    output.append(("Voz", f"{Voz:.2f}", "CFM", "[Zone Outdoor Airflow, Eq. 6-2]"))

    return output, Voz, info

# The rest of your code can remain as a command-line program or be omitted.
