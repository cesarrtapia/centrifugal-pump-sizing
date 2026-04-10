from calculations import calculate_system

data = {
    "fluid": {
        "density": 998,
        "viscosity": 0.001002
    },
    "flow_m3s": 0.0139,
    "pipe": {
        "diameter": 0.0762,
        "length": 100,
        "roughness": 0.000045
    },
    "system": {
        "static_head": 10,
        "K_total": 3.8
    },
    "pump": {
        "efficiency": 0.7
    }
}

results = calculate_system(data)

for k, v in results.items():
    print(f"{k}: {v}")

