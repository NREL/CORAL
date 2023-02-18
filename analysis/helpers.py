import datetime as dt

allocations = {
    'test': {
        "support_vessel": ('example_support_vessel', 2),
        "towing_vessel": ('example_towing_vessel', 2),
        "mooring_install_vessel": ('example_support_vessel', 2),
        "port": [('Port of San Luis', 0), ('Humboldt', 1), ('Coos Bay', 1)]
            },
    'baseline': {
        "support_vessel": ('example_support_vessel', 2),
        "towing_vessel": ('example_towing_vessel', 2),
        "mooring_install_vessel": ('example_support_vessel', 2),
        "port": [('Long Beach', 1), ('Humboldt', 1), ('Coos Bay', 1)]
            },
    'expanded': {
        "support_vessel": ('example_support_vessel', 2),
        "towing_vessel": ('example_towing_vessel', 2),
        "mooring_install_vessel": ('example_support_vessel', 2),
        "port": [('Long Beach', 1), ('Humboldt', 1), ('Coos Bay', 1), ('Grays Harbor', 1), ('Astoria', 1), ('Port of San Luis', 1)]
            },
}

future_allocations = {
    'test': [
        ["port", "Port of San Luis", [dt.datetime(2040, 1, 1)]]
        ]
}
