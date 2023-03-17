import datetime as dt

allocations = {
    'Baseline-limited-ports': {
        "ahts_vessel": ('example_ahts_vessel', 2),
        "towing_vessel": ('example_towing_vessel', 2),
        "mooring_install_vessel": ('example_support_vessel', 2),
        "port": [('Humboldt', 1), ('Coos Bay', 0)]
            },
    ## Saturate # of vessels to iterate on port constraints and wait for data on actual numbers
    'Baseline-South-CA': {
        "ahts_vessel": ('example_ahts_vessel', 99),
        "towing_vessel": ('example_towing_vessel', 99),
        "mooring_install_vessel": ('example_support_vessel', 99),
        "port": [('Long Beach', 0), ('Humboldt', 1), ('Coos Bay', 0)]
            },
    'Baseline-Central-CA': {
        "ahts_vessel": ('example_ahts_vessel', 99),
        "towing_vessel": ('example_towing_vessel', 99),
        "mooring_install_vessel": ('example_support_vessel', 99),
        "port": [('Port of San Luis', 0), ('Humboldt', 1), ('Coos Bay', 0)]
            },
    'Expanded-all-ports': {
        "ahts_vessel": ('example_ahts_vessel', 99),
        "towing_vessel": ('example_towing_vessel', 99),
        "mooring_install_vessel": ('example_support_vessel', 99),
        "port": [('Long Beach', 0), ('Humboldt', 1), ('Coos Bay', 0), ('Grays Harbor', 0), ('Port of San Luis', 0)]
            },
}

future_allocations = {
    'Baseline-limited-ports': [
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]]
        ],
    'Baseline-South-CA': [
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Long Beach", [dt.datetime(2034, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2038, 1, 1)]]
    ],
    'Baseline-Central-CA': [
        ["port", "Port of San Luis", [dt.datetime(2037, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2038, 1, 1)]]
    ],
    'Expanded-all-ports':[
        ["port", "Long Beach", [dt.datetime(2032, 1, 1)]],
        ["port", "Port of San Luis", [dt.datetime(2037, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2031, 1, 1)]],
        ["port", "Grays Harbor", [dt.datetime(2039, 1, 1)]],
        ["port", "Humboldt", [dt.datetime(2030, 1, 1)]],
        ["port", "Coos Bay", [dt.datetime(2038, 1, 1)]]
    ]
}
