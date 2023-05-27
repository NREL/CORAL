import datetime as dt

target_capacity = {
    'Baseline': 25,
    'Moderate': 35,
    'Expanded': 55
}

allocations = {
    'Baseline-Low': {
        "ahts_vessel": ('example_ahts_vessel', 2), # =6 AHTS (2 projects at a time, 3 groups per project, 1 AHTS per group)
        "towing_vessel": ('example_towing_vessel', 2), # =12 tugs (2 projects at a time, 3 groups per project, 2 tugs per group)
        "mooring_install_vessel": ('example_support_vessel', 2), # =2 AHTS (2 projects at a time, 1 per project)
        "array_cable_install_vessel": ('example_array_cable_lay_vessel', 2), # =2 CLVs (2 projects at a time, 1 CLV per project)
        "export_cable_install_vessel": ("example_export_cable_lay_vessel", 2), # =2 CLVs (2 projects at a time, 1 CLV per project)
        "port": [('Humboldt', 1)]
            },
    ## Saturate # of vessels to iterate on port constraints and wait for data on actual numbers
    'Baseline-Mid (SC)': {
        "ahts_vessel": ('example_ahts_vessel', 4), # =12 AHTS
        "towing_vessel": ('example_towing_vessel', 4), # =24 tugs
        "mooring_install_vessel": ('example_support_vessel', 4), # =4 AHTS
        "array_cable_install_vessel": ('example_array_cable_lay_vessel', 4), # =4 CLV (array)
        "export_cable_install_vessel": ("example_export_cable_lay_vessel", 4), # =4 CLV (export)
        "port": [('Long Beach', 0), ('Humboldt', 1)]
            },
    'Baseline-Mid (CC)': {
        "ahts_vessel": ('example_ahts_vessel', 3), # =9 AHTS
        "towing_vessel": ('example_towing_vessel', 3), # =18 tugs
        "mooring_install_vessel": ('example_support_vessel', 3), # =3 AHTS
        "array_cable_install_vessel": ('example_array_cable_lay_vessel', 3), # =3 CLV (array)
        "export_cable_install_vessel": ("example_export_cable_lay_vessel",3), # =3 CLV (export)
        "port": [('Port of San Luis', 0), ('Humboldt', 1)]
            },
    'Moderate-Low': {
        "ahts_vessel": ('example_ahts_vessel', 4), # =12 AHTS
        "towing_vessel": ('example_towing_vessel', 4), # =24 tugs
        "mooring_install_vessel": ('example_support_vessel', 4), # =4 AHTS
        "array_cable_install_vessel": ('example_array_cable_lay_vessel', 4), # =4 CLV (array)
        "export_cable_install_vessel": ("example_export_cable_lay_vessel",4), # =4 CLV (export)
        "port": [('Humboldt', 1), ('Coos Bay', 0)]
            },
    'Moderate-Mid (SC)': {
        "ahts_vessel": ('example_ahts_vessel', 5), # =15 AHTS
        "towing_vessel": ('example_towing_vessel', 5), # =30 tugs
        "mooring_install_vessel": ('example_support_vessel', 5), # =5 AHTS
        "array_cable_install_vessel": ('example_array_cable_lay_vessel', 5), # =5 CLV (array)
        "export_cable_install_vessel": ("example_export_cable_lay_vessel",5), # =5 CLV (export)
        "port": [('Long Beach', 0), ('Humboldt', 1), ('Coos Bay', 0)]
            },
    'Expanded-High': {
        "ahts_vessel": ('example_ahts_vessel', 9), # =27 AHTS
        "towing_vessel": ('example_towing_vessel', 9), # =54 tugs
        "mooring_install_vessel": ('example_support_vessel', 9), # =9 AHTS
        "array_cable_install_vessel": ('example_array_cable_lay_vessel', 9), # =9 CLV (array)
        "export_cable_install_vessel": ("example_export_cable_lay_vessel",9), # =9 CLV (export)
        "port": [('Long Beach', 0), ('Humboldt', 1), ('Coos Bay', 0), ('Grays Harbor', 0), ('Port of San Luis', 0)]
            }
}

future_allocations = {
    'Baseline-Low': [
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]]
    ],
    'Baseline-Mid (SC)': [
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Long Beach", [dt.datetime(2034, 1, 1)]]
    ],
    'Baseline-Mid (CC)': [
        ["port", "Port of San Luis", [dt.datetime(2037, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]]
    ],
    'Moderate-Low':[
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2038, 1, 1)]]
    ],
    'Moderate-Mid (SC)':[
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2038, 1, 1)]]
    ],
    'Expanded-High':[
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]],
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]], # Add 2nd line
        # ["port", "Long Beach", [dt.datetime(2035, 1, 1)]], # Add 3rd line
        ["port", "Port of San Luis", [dt.datetime(2037, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2032, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2035, 1, 1)]], # Accelerate from 2038
        ["port", "Grays Harbor", [dt.datetime(2035, 1, 1)]], # Accelerate from 2039
        ["port", "Grays Harbor", [dt.datetime(2035, 1, 1)]], # Add 2nd line
        #["port", "Grays Harbor", [dt.datetime(2035, 1, 1)]], # Add 3rd line/2nd port
    ]
}
