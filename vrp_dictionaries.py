import math

VRP_TABLE_6_1 = {
    # Animal Facilities
    "Animal exam room (veterinary office)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Animal imaging (MRI/CT/PET)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Animal operating rooms": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Animal postoperative recovery room": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Animal preparation rooms": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Animal procedure room": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Animal surgery scrub": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Large-animal holding room": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Necropsy": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Small-animal-cage room (static cages)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Small-animal-cage room (ventilated cages)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },

    # Correctional Facilities
    "Booking/waiting": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 50, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": None
    },
    "Cell": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Dayroom": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 30, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": None
    },
    "Guard stations": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 15, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": None
    },

    # Educational Facilities
    "Art classroom": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Classrooms (ages 5-8)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Classrooms (age 9 plus)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 35, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": None
    },
    "Computer lab": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": None
    },
    "Daycare sickroom": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Daycare (through age 4)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Lecture classroom": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 65, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": "YES"
    },
    "Lecture hall (fixed seats)": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 150, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": "YES"
    },
    "Libraries": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": None
    },
    "Media center": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": None
    },
    "Multiuse assembly": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 100, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": "YES"
    },
    "Music/theater/dance": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 35, "DeltaC_ppm": 2100, "Occupied_Standby_Allowed": "YES"
    },
    "Science laboratories": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "University/college laboratories": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Wood/metal shop": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Corridors (ages 5 plus)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },

    # Food and Beverage Service
    "Bars, cocktail lounges": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 100, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": None
    },
    "Cafeteria/fast-food dining": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 100, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Kitchen (cooking)": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Restaurant dining rooms": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 70, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": None
    },

    # General
    "Break rooms (General)": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Coffee stations": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": "YES"
    },
    "Conference/meeting": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 50, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Corridors": {
        "Rp_cfm_per": 0, "Rp_Lps_per": 0, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 0, "DeltaC_ppm": None, "Occupied_Standby_Allowed": "YES"
    },
    "Occupiable storage rooms for liquids or gels": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 2, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },

    # Hotels, Motels, Resorts, Dormitories
    "Barracks sleeping areas": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": "YES"
    },
    "Bedroom/living room": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": "YES"
    },
    "Laundry rooms, central": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Laundry rooms within dwelling units": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Lobbies/prefunction": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 30, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": "YES"
    },
    "Multipurpose assembly": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 120, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },

    # Miscellaneous Spaces
    "Banks or bank lobbies": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 15, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": "YES"
    },
    "Bank vaults/safe deposit": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 5, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": "YES"
    },
    "Computer (not printing)": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 4, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": "YES"
    },
    "Freezer and refrigerated spaces (<50F [10C])": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0, "Ra_Lps_m2": 0, "Default_Occ_Density_per_1000ft2": 0, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Manufacturing where hazardous materials are not used": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 7, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": None
    },
    "Manufacturing where hazardous materials are used (excludes heavy industrial and chemical processes)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 7, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Pharmacy (prep. area)": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Photo studios": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Shipping/receiving": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 2, "DeltaC_ppm": 700, "Occupied_Standby_Allowed": None
    },
    "Sorting, packing, light assembly": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 7, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Telephone closets": {
        "Rp_cfm_per": 0, "Rp_Lps_per": 0, "Ra_cfm_ft2": 0, "Ra_Lps_m2": 0, "Default_Occ_Density_per_1000ft2": 0, "DeltaC_ppm": 700, "Occupied_Standby_Allowed": None
    },
    "Transportation waiting": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 100, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },
    "Warehouses": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 0, "DeltaC_ppm": 700, "Occupied_Standby_Allowed": None
    },

    # Office Buildings
    "Main entry lobbies": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": "YES"
    },
    "Occupiable storage rooms for dry materials": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 2, "DeltaC_ppm": 700, "Occupied_Standby_Allowed": None
    },
    "Office space": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 5, "DeltaC_ppm": 600, "Occupied_Standby_Allowed": "YES"
    },
    "Reception areas": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 30, "DeltaC_ppm": 2100, "Occupied_Standby_Allowed": "YES"
    },
    "Telephone/data entry": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 60, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },

    # Public Assembly Spaces
    "Auditorium seating area": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 150, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },
    "Courtrooms": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 70, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Legislative chambers": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 50, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },
    "Lobbies": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 150, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },
    "Museums (children's)": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 40, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": None
    },
    "Museums/galleries": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 40, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Places of religious worship": {
        "Rp_cfm_per": 5, "Rp_Lps_per": 2.5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 120, "DeltaC_ppm": 1800, "Occupied_Standby_Allowed": "YES"
    },

    # Residential
    "Common corridors": {
        "Rp_cfm_per": 0, "Rp_Lps_per": 0, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 0, "DeltaC_ppm": None, "Occupied_Standby_Allowed": "YES"
    },

    # Retail
    "Sales (except as below)": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 15, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Barbershop": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": "YES"
    },
    "Beauty and nail salons": {
        "Rp_cfm_per": 20, "Rp_Lps_per": 10, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 25, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Coin-operated laundries": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Mall common areas": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 40, "DeltaC_ppm": 2100, "Occupied_Standby_Allowed": "YES"
    },
    "Pet shops (animal areas)": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },
    "Supermarket": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 8, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Bowling alley (seating)": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.12, "Ra_Lps_m2": 0.6, "Default_Occ_Density_per_1000ft2": 40, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },

    # Sports and Entertainment
    "Disco/dance floors": {
        "Rp_cfm_per": 20, "Rp_Lps_per": 10, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 100, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Gambling casinos": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 120, "DeltaC_ppm": 1200, "Occupied_Standby_Allowed": None
    },
    "Game arcades": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 20, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Gym, sports arena (play area)": {
        "Rp_cfm_per": 20, "Rp_Lps_per": 10, "Ra_cfm_ft2": 0.18, "Ra_Lps_m2": 0.9, "Default_Occ_Density_per_1000ft2": 7, "DeltaC_ppm": 900, "Occupied_Standby_Allowed": None
    },
    "Health club/aerobics room": {
        "Rp_cfm_per": 20, "Rp_Lps_per": 10, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 40, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": None
    },
    "Health club/weight rooms": {
        "Rp_cfm_per": 20, "Rp_Lps_per": 10, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 10, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": None
    },
    "Spectator areas": {
        "Rp_cfm_per": 7.5, "Rp_Lps_per": 3.8, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 150, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Stages, studios": {
        "Rp_cfm_per": 10, "Rp_Lps_per": 5, "Ra_cfm_ft2": 0.06, "Ra_Lps_m2": 0.3, "Default_Occ_Density_per_1000ft2": 70, "DeltaC_ppm": 1500, "Occupied_Standby_Allowed": "YES"
    },
    "Swimming (pool & deck)": {
        "Rp_cfm_per": 0, "Rp_Lps_per": 0, "Ra_cfm_ft2": 0.48, "Ra_Lps_m2": 2.4, "Default_Occ_Density_per_1000ft2": 0, "DeltaC_ppm": None, "Occupied_Standby_Allowed": None
    },

    
    # Outpatient Health Care Facilities (ASHRAE 62.1 Table P-1)
    "Birthing room": {
        "Rp_cfm_per": 10.0,
        "Ra_cfm_ft2": 0.18,
        "Default_Occ_Density_per_1000ft2": 15,
        "Notes": "Outpatient health care"
    },
    "Class 1 imaging rooms": {
        "Rp_cfm_per": 7.5,
        "Ra_cfm_ft2": 0.12,
        "Default_Occ_Density_per_1000ft2": 5,
        "Notes": "Outpatient health care"
    },
    "Dental operatory": {
        "Rp_cfm_per": 10.0,
        "Ra_cfm_ft2": 0.18,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "General examination room": {
        "Rp_cfm_per": 7.5,
        "Ra_cfm_ft2": 0.12,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Other dental treatment areas": {
        "Rp_cfm_per": 5.0,
        "Ra_cfm_ft2": 0.06,
        "Default_Occ_Density_per_1000ft2": 5,
        "Notes": "Outpatient health care"
    },
    "Physical therapy exercise area": {
        "Rp_cfm_per": 20.0,
        "Ra_cfm_ft2": 0.18,
        "Default_Occ_Density_per_1000ft2": 7,
        "Notes": "Outpatient health care"
    },
    "Physical therapy individual room": {
        "Rp_cfm_per": 10.0,
        "Ra_cfm_ft2": 0.12,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Physical therapeutic pool area": {
        "Rp_cfm_per": None,   # not given
        "Ra_cfm_ft2": 0.48,
        "Default_Occ_Density_per_1000ft2": None,
        "Notes": "Outpatient health care"
    },
    "Prosthetics and orthotics room": {
        "Rp_cfm_per": 10.0,
        "Ra_cfm_ft2": 0.18,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Psychiatric consultation room": {
        "Rp_cfm_per": 5.0,
        "Ra_cfm_ft2": 0.06,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Psychiatric examination room": {
        "Rp_cfm_per": 5.0,
        "Ra_cfm_ft2": 0.06,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Psychiatric group room": {
        "Rp_cfm_per": 5.0,
        "Ra_cfm_ft2": 0.06,
        "Default_Occ_Density_per_1000ft2": 50,
        "Notes": "Outpatient health care"
    },
    "Psychiatric seclusion room": {
        "Rp_cfm_per": 10.0,
        "Ra_cfm_ft2": 0.12,
        "Default_Occ_Density_per_1000ft2": 5,
        "Notes": "Outpatient health care"
    },
    "Speech therapy room": {
        "Rp_cfm_per": 5.0,
        "Ra_cfm_ft2": 0.06,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Urgent care examination room": {
        "Rp_cfm_per": 7.5,
        "Ra_cfm_ft2": 0.12,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Urgent care observation room": {
        "Rp_cfm_per": 5.0,
        "Ra_cfm_ft2": 0.06,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Urgent care treatment room": {
        "Rp_cfm_per": 7.5,
        "Ra_cfm_ft2": 0.12,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    },
    "Urgent care triage room": {
        "Rp_cfm_per": 10.0,
        "Ra_cfm_ft2": 0.18,
        "Default_Occ_Density_per_1000ft2": 20,
        "Notes": "Outpatient health care"
    }
        
} # -- End of VRP_TABLE_6_1 --





def single_zone_vrp_Vbz(occupancy, area_ft2, num_people, VRP_TABLE_6_1):
    """
    Calculate breathing zone outdoor airflow (Vbz) for a single zone using ASHRAE 62.1 Table 6-1.

    Parameters:
        occupancy (str): Occupancy category (must match key in VRP_TABLE_6_1)
        area_ft2 (float): Zone area in square feet
        num_people (float): Number of people in zone
        VRP_TABLE_6_1 (dict): Dictionary containing VRP values for each occupancy
        Ez (float): Zone air distribution effectiveness (default=1.0)

    Returns:
        Vbz (float): Breathing zone outdoor airflow, CFM
        info (dict): Details of calculation
    """
    occ_row = VRP_TABLE_6_1[occupancy]
    Rp = occ_row["Rp_cfm_per"]  # cfm/person
    Ra = occ_row["Ra_cfm_ft2"]  # cfm/ft^2
    default_density = occ_row["Default_Occ_Density_per_1000ft2"]

    Vbz = Rp * num_people + Ra * area_ft2  # [CFM]
    info = {
        "Rp": Rp,
        "Ra": Ra,
        "num_people": num_people,
        "area_ft2": area_ft2,
        "Vbz": Vbz,
        "default_density": default_density,
        "notes": f"{Rp} cfm/person x {num_people} + {Ra} cfm/ft^2 x {area_ft2} = {Vbz:.2f} CFM (Breathing Zone OA)"
    }
    return Vbz, info





def single_zone_vrp_Voz(occupancy, area_ft2, num_people, VRP_TABLE_6_1, Ez=1.0):
    """
    Calculate zone outdoor airflow (Voz) for a single zone using ASHRAE 62.1 (Eq. 6-2).

    Parameters:
        occupancy (str): Occupancy category (must match key in VRP_TABLE_6_1)
        area_ft2 (float): Zone area in square feet
        num_people (float): Number of people in zone
        VRP_TABLE_6_1 (dict): Dictionary containing VRP values for each occupancy
        Ez (float): Zone air distribution effectiveness (default=1.0)

    Returns:
        Voz (float): Zone outdoor airflow, CFM
        info (dict): Details of calculation
    """
    Vbz, info = single_zone_vrp_Vbz(occupancy, area_ft2, num_people, VRP_TABLE_6_1)
    Voz = Vbz / Ez if Ez > 0 else float('inf')
    info["Ez"] = Ez
    info["Voz"] = Voz
    info["notes"] += f"; Voz = Vbz / Ez = {Vbz:.2f} / {Ez} = {Voz:.2f} CFM (Zone OA per Eq. 6-2)"
    return Voz, info






def system_vrp_Vot(system_type, voz_values, vou=None, ev=None):
    """
    Calculate outdoor-air intake flow (Vot) for a ventilation system
    using ASHRAE 62.1-2022 Section 6.2 logic.

    Parameters
    ----------
    system_type : int
        1 = Single-Zone System
        2 = 100 % Outdoor-Air System
        3 = Multiple-Zone Recirculating System
    voz_values  : float | list[float]
        Zone outdoor-airflow(s) Voz, CFM.
        Accepts a single value (float) or an iterable of values.
    vou        : float, optional
        Uncorrected outdoor-air intake, CFM (required for system_type 3).
    ev         : float, optional
        System ventilation efficiency Ev (required for system_type 3).

    Returns
    -------
    Vot : float
        Outdoor-air intake flow, CFM.
    info : dict
        Calculation notes and echo of inputs.
    """
    # Normalise to list for consistent handling
    if not isinstance(voz_values, (list, tuple)):
        voz_list = [voz_values]
    else:
        voz_list = list(voz_values)

    notes = []

    if system_type == 1:                               # Eq. 6-3
        Vot = voz_list[0]
        notes.append(f"Single-zone: Vot = Voz = {Vot:.2f} CFM")
        
    elif system_type == 2:                             # Eq. 6-4
        Vot = sum(voz_list)
        notes.append(f"100 % OA: Vot = SUM Voz = {Vot:.2f} CFM")
        
    elif system_type == 3:                             # Eq. 6-10
        if vou is None or ev is None:
            raise ValueError("Vou and Ev are required for system_type 3")
        Vot = vou / ev
        notes.append(f"Multi-zone: Vot = {vou:.2f} / {ev:.2f} = {Vot:.2f} CFM")

    else:
        raise ValueError(f"Unknown system_type {system_type}")

    info = {
        "system_type": system_type,
        "voz_values": voz_list,
        "vou": vou,
        "ev": ev,
        "Vot": Vot,
        "notes": "; ".join(notes)
    }
    return Vot, info




def calculate_occupant_diversity(num_people_list, areas_ft2, occupancies, VRP_TABLE_6_1):
    """
    Calculate occupant diversity ratio D for multiple-zone recirculating systems
    as per ASHRAE 62.1 (Equation 6-6).

    Parameters:
        num_people_list (list of float): Actual or estimated number of people per zone.
        areas_ft2 (list of float): Area per zone in ft^2.
        occupancies (list of str): List of occupancy names (must match VRP_TABLE_6_1 keys).
        VRP_TABLE_6_1 (dict): Occupancy table.

    Returns:
        D (float): Occupant diversity ratio.
    """
    numerator = sum(num_people_list)
    denominator = 0.0
    for i in range(len(occupancies)):
        occ_row = VRP_TABLE_6_1[occupancies[i]]
        density = occ_row["Default_Occ_Density_per_1000ft2"]
        area = areas_ft2[i]
        default_people = math.ceil((density * area) / 1000.0) if density else 0.0
        denominator += default_people

    D = numerator / denominator if denominator > 0 else 0.0
    return D





def calculate_uncorrected_outdoor_air_intake(D, num_people_list, areas_ft2, occupancies, VRP_TABLE_6_1):
    """
    Calculate uncorrected outdoor air intake Vou as per ASHRAE 62.1 Eq. 6-5.

    Parameters:
        D (float): Occupant diversity ratio.
        num_people_list (list of float): Number of people per zone.
        areas_ft2 (list of float): Area per zone in ft^2.
        occupancies (list of str): List of occupancy names (must match VRP_TABLE_6_1 keys).
        VRP_TABLE_6_1 (dict): Occupancy table.

    Returns:
        Vou (float): Uncorrected outdoor air intake in CFM.
    """
    sum_Rp_Pz = 0.0
    sum_Ra_Az = 0.0
    for i in range(len(occupancies)):
        occ_row = VRP_TABLE_6_1[occupancies[i]]
        Rp = occ_row["Rp_cfm_per"]
        Ra = occ_row["Ra_cfm_ft2"]
        Pz = num_people_list[i]
        Az = areas_ft2[i]
        sum_Rp_Pz += Rp * Pz
        sum_Ra_Az += Ra * Az

    Vou = D * sum_Rp_Pz + sum_Ra_Az
    return Vou



def calculate_system_ventilation_efficiency_simplified(D):
    """
    Calculate system ventilation efficiency (Ev) using the simplified procedure
    from ASHRAE 62.1 (Eq. 6-7 and 6-8).

    Parameters:
        D (float): Occupant diversity ratio.

    Returns:
        Ev (float): System ventilation efficiency.
    """
    if D < 0.60:
        Ev = 0.88 * D + 0.22
    else:
        Ev = 0.75
    return Ev





def calculate_system_ventilation_efficiency_appendix_A(
        Vou,
        Voz_list,
        Vpz_list=None):
    """
    Calculate system ventilation efficiency (Ev) per Appendix A
    Single-Supply-System method (Eq. A-1 to A-3).

    Parameters
    ----------
    Vou       : float
        Uncorrected outdoor-air intake, CFM  (Eq. 6-5).
    Voz_list  : list[float]
        Zone outdoor-airflow values, CFM.
    Vpz_list  : list[float] | None
        Zone primary airflow values, CFM, at the condition analysed.
        If None, Vpz is set equal to 1.5 × Voz for each zone
        (per Eq. 6-9, a conservative default).

    Returns
    -------
    Ev   : float
        System ventilation efficiency.
    info : dict
        Calculation details: Xs, Zpz list, Evz list, Ev.
    """
    # Default Vpz_list if not supplied
    if Vpz_list is None:
        Vpz_list = [1.5 * v for v in Voz_list]   # Eq. 6-9 default

    if len(Voz_list) != len(Vpz_list):
        raise ValueError("Voz_list and Vpz_list must be the same length")

    # System primary airflow Vps (sum of Vpz values used here)
    Vps = sum(Vpz_list)
    if Vps == 0:
        raise ValueError("Vps is zero; cannot compute Xs")

    # Eq. A-1: average outdoor-air fraction
    Xs = Vou / Vps

    # Eq. A-3 and A-2: zone fractions and zone efficiencies
    Zpz = [voz / vpz if vpz > 0 else 0.0 for voz, vpz in zip(Voz_list, Vpz_list)]
    Evz = [1.0 + Xs - z for z in Zpz]

    # System ventilation efficiency is the minimum Evz
    Ev = min(Evz)

    info = {
        "Xs": Xs,
        "Zpz": Zpz,
        "Evz": Evz,
        "Ev": Ev
    }
    return Ev, info
