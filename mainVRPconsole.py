import re
import math
import argparse
from vrp_dictionaries import single_zone_vrp_Vbz, single_zone_vrp_Voz, VRP_TABLE_6_1
from vrp_dictionaries import system_vrp_Vot

FT2_TO_M2 = 0.092903  # 1 ft^2 = 0.092903 m^2


def preprocess_inputs(params, VRP_TABLE_6_1, FT2_TO_M2):
    system_type = int(params.get("system_type", 1))
    
    if system_type > 2:
        print("WARNING: system_type {} not implemented; defaulting to 1 (Single-Zone)" .format(system_type))
        system_type = 1

    occ_raw = params["occupancy"]
    if isinstance(occ_raw, (list, tuple)):
        occupancies = list(occ_raw)
    else:
        occupancies = [occ_raw]    
    
    # Check that all occupancies exist in the table
    for occ in occupancies:
        if occ not in VRP_TABLE_6_1:
            print("ERROR: Occupancy category '{}' not found in VRP table.".format(occ))
            print("Please check the name and try again. (Case and spelling must match exactly.)")
            print("Voz                  |                     0.00 | CFM          | [Zone Outdoor Airflow, Eq. 6-2]")
            print("Vot                  |                     0.00 | CFM          | [Outdoor-Air Intake, Eq. 6-3]")
            print()
            return None, None, None, None, None, None
   
    

    if "area_ft2" in params:
        area_ft2 = params["area_ft2"]
        if isinstance(area_ft2, (list, tuple)):
            areas_ft2 = [float(a) for a in area_ft2]
        else:
            areas_ft2 = [float(area_ft2)]
        areas_m2 = [a * FT2_TO_M2 for a in areas_ft2]
    elif "area_m2" in params:
        area_m2 = params["area_m2"]
        if isinstance(area_m2, (list, tuple)):
            areas_m2 = [float(a) for a in area_m2]
        else:
            areas_m2 = [float(area_m2)]
        areas_ft2 = [a / FT2_TO_M2 for a in areas_m2]
    else:
        raise ValueError("Either area_ft2 or area_m2 must be specified.")


    
    # Optional: num_people
    num_people = params.get("num_people", None)
    if num_people is not None:
        if isinstance(num_people, (list, tuple)):
            num_people_list = [float(n) if n is not None else None for n in num_people]
        else:
            num_people_list = [float(num_people)]
    else:
        num_people_list = [None] * len(occupancies)  # one per occupancy

    # Fill in defaults where num_people is None
    for i in range(len(num_people_list)):
        if num_people_list[i] is None:
            row = VRP_TABLE_6_1[occupancies[i]]
            density = row["Default_Occ_Density_per_1000ft2"]
            if not density or areas_ft2[i] == 0:
                print("WARNING: num_people not given and default density is not available. Setting num_people = 0")
                num_people_list[i] = 0
            else:
                num_people_list[i] = math.ceil((density * areas_ft2[i]) / 1000)




    Ez_param = params.get("Ez", None)
    if Ez_param is not None:
        if isinstance(Ez_param, (list, tuple)):
            Ez_list = [float(e) for e in Ez_param]
        else:
            Ez_list = [float(Ez_param)] * len(occupancies)
    else:
        Ez_list = [1.0] * len(occupancies)



    # For system_type 2: validate lengths
    if system_type == 2:
        n = len(occupancies)
        if n < 2:
            print("ERROR: For 100 pct outdoor-air system, two or more occupancy zones are required.")
            return None, None, None, None, None, None
        if not (len(areas_ft2) == n and len(areas_m2) == n):
            print("ERROR: The number of occupancies and areas must match.")
            return None, None, None, None, None, None
        if num_people_list is not None and len(num_people_list) != n:
            print("ERROR: The number of num_people values must match number of occupancies and areas.")
            return None, None, None, None, None, None
        if Ez_list is not None and len(Ez_list) != n:
            print("ERROR: The number of Ez values must match number of occupancies and areas.")
            return None, None, None, None, None, None

    return system_type, occupancies, areas_ft2, areas_m2, num_people_list, Ez_list


def print_vrp_results(occupancy, area_ft2, area_m2, num_people, info, Voz):
    print("\nASHRAE 62.1-2022 Ventilation Rate Procedure (Single Zone OR Single Space)\n")
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


def print_vrp_system_results(Vot, vot_info):
    print("{:<20} | {:24.2f} | {:<12} | {:<50}".format("Vot", Vot, "CFM", "[Outdoor-Air Intake, Eq. 6-3]"))
    print("{:<20} | {:<93}".format("", vot_info["notes"]))
    print()



def main(**params):
    
    # Read inputs from command line
    system_type, occupancies, areas_ft2, areas_m2, num_people_list, Ez_list = preprocess_inputs(params, VRP_TABLE_6_1, FT2_TO_M2)


    if system_type == 1: # Handle single-zone outdoor-air system (multiple zones)
        
        occupancy = occupancies[0]
        area_ft2 = areas_ft2[0]
        area_m2 = areas_m2[0]
        num_people = num_people_list[0] if num_people_list is not None else None
        Ez = Ez_list[0] if Ez_list is not None else 1.0

        Voz, info = single_zone_vrp_Voz(occupancy, area_ft2, num_people, VRP_TABLE_6_1, Ez)
        Vot, vot_info = system_vrp_Vot(system_type, Voz)

        print_vrp_results(occupancy, area_ft2, area_m2, num_people, info, Voz)
        print_vrp_system_results(Vot, vot_info)

    elif system_type == 2: # Handle 100 pct outdoor-air system (multiple zones)        

        Voz_list = []
        info_list = []
        n_zones = len(occupancies)
        for i in range(n_zones):
            Voz_i, info_i = single_zone_vrp_Voz(occupancies[i],areas_ft2[i],num_people_list[i],VRP_TABLE_6_1,Ez_list[i] if Ez_list is not None else 1.0)
            Voz_list.append(Voz_i)
            info_list.append(info_i)

        Vot, vot_info = system_vrp_Vot(system_type, Voz_list)

        for i in range(n_zones):
            print_vrp_results(occupancies[i],areas_ft2[i],areas_m2[i],num_people_list[i],info_list[i],Voz_list[i])
        print_vrp_system_results(Vot, vot_info)

    elif system_type == 3: # Handle multiple-zone recirculating system
        
        # Implementation goes here
        pass

    else:
        pass  # Unknown system type; do nothing or print an error if you want




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASHRAE 62.1-2022 VRP Console Calculator")

    parser.add_argument("-occupancy", type=str, nargs="+", required=True, help="Occupancy category (one or more, quote if spaces)" )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-area_ft2", type=float, nargs="+", help="Area in square feet (one per occupancy)")
    group.add_argument("-area_m2", type=float, nargs="+", help="Area in square meters (one per occupancy)")
    parser.add_argument("-num_people", type=float, nargs="+", help="Number of people (one per occupancy, optional)")
    parser.add_argument("-Ez", type=float, nargs="+", help="Zone air distribution effectiveness (optional, one per occupancy)")
    parser.add_argument("-system_type", type=int, choices=[1, 2, 3], default=1,
                        help="1 = Single-Zone System (default), "
                             "2 = 100 pct Outdoor-Air System, "
                             "3 = Multiple-Zone Recirculating System")    
    
    args = parser.parse_args()
    p = {k: v for k, v in vars(args).items() if v is not None}
    main(**p)




