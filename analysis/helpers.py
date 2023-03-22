import datetime as dt

target_capacity = {
    'Baseline': 25,
    'Moderate': 35,
    'Expanded': 55
}

allocations = {
    'Baseline-Low': {
        "ahts_vessel": ('example_ahts_vessel', 7),
        "towing_vessel": ('example_towing_vessel', 7),
        "mooring_install_vessel": ('example_support_vessel', 7),
        "array_cable_install_vessel": ('example_cable_lay_vessel', 99),
        "export_cable_install_vessel": ("example_cable_lay_vessel",99),
        "port": [('Humboldt', 1)]
            },
    ## Saturate # of vessels to iterate on port constraints and wait for data on actual numbers
    'Baseline-Mid (SC)': {
        "ahts_vessel": ('example_ahts_vessel', 7),
        "towing_vessel": ('example_towing_vessel', 7),
        "mooring_install_vessel": ('example_support_vessel', 7),
        "array_cable_install_vessel": ('example_cable_lay_vessel', 99),
        "export_cable_install_vessel": ("example_cable_lay_vessel",99),
        "port": [('Long Beach', 0), ('Humboldt', 1)]
            },
    'Baseline-Mid (CC)': {
        "ahts_vessel": ('example_ahts_vessel', 7),
        "towing_vessel": ('example_towing_vessel', 7),
        "mooring_install_vessel": ('example_support_vessel', 7),
        "array_cable_install_vessel": ('example_cable_lay_vessel', 99),
        "export_cable_install_vessel": ("example_cable_lay_vessel",99),
        "port": [('Port of San Luis', 0), ('Humboldt', 1)]
            },
    'Moderate-Low': {
        "ahts_vessel": ('example_ahts_vessel', 7),
        "towing_vessel": ('example_towing_vessel', 7),
        "mooring_install_vessel": ('example_support_vessel', 7),
        "array_cable_install_vessel": ('example_cable_lay_vessel', 99),
        "export_cable_install_vessel": ("example_cable_lay_vessel",99),
        "port": [('Humboldt', 1), ('Coos Bay', 0)]
            },
    'Moderate-Mid (SC)': {
        "ahts_vessel": ('example_ahts_vessel', 7),
        "towing_vessel": ('example_towing_vessel', 7),
        "mooring_install_vessel": ('example_support_vessel', 7),
        "array_cable_install_vessel": ('example_cable_lay_vessel', 99),
        "export_cable_install_vessel": ("example_cable_lay_vessel",99),
        "port": [('Long Beach', 0), ('Humboldt', 1), ('Coos Bay', 0)]
            },
    'Expanded-High': {
        "ahts_vessel": ('example_ahts_vessel', 7),
        "towing_vessel": ('example_towing_vessel', 7),
        "mooring_install_vessel": ('example_support_vessel', 7),
        "array_cable_install_vessel": ('example_cable_lay_vessel', 99),
        "export_cable_install_vessel": ("example_cable_lay_vessel",99),
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
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]],
        ["port", "Port of San Luis", [dt.datetime(2037, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Grays Harbor", [dt.datetime(2039, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2038, 1, 1)]]
    ]
}
