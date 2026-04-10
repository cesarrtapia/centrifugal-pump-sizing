import math

g = 9.81  # gravedad (m/s²)

# -----------------------------
# 🔹 Área de tubería
# -----------------------------
def pipe_area(diameter):
    return math.pi * (diameter ** 2) / 4


# -----------------------------
# 🔹 Velocidad del fluido
# -----------------------------
def velocity(flow_m3s, diameter):
    area = pipe_area(diameter)
    return flow_m3s / area


# -----------------------------
# 🔹 Número de Reynolds
# -----------------------------
def reynolds(rho, velocity, diameter, mu):
    return (rho * velocity * diameter) / mu


# -----------------------------
# 🔹 Factor de fricción (Swamee-Jain)
# -----------------------------
def friction_factor(Re, roughness, diameter):
    if Re < 2000:
        return 64 / Re  # flujo laminar

    return 0.25 / (
        math.log10(
            (roughness / (3.7 * diameter)) +
            (5.74 / (Re ** 0.9))
        ) ** 2
    )


# -----------------------------
# 🔹 Pérdidas por fricción
# -----------------------------
def friction_losses(f, length, diameter, velocity):
    return f * (length / diameter) * (velocity ** 2 / (2 * g))


# -----------------------------
# 🔹 Pérdidas en accesorios
# -----------------------------
def accessory_losses(K_total, velocity):
    return K_total * (velocity ** 2 / (2 * g))


# -----------------------------
# 🔹 TDH
# -----------------------------
def total_dynamic_head(H_static, h_f, h_acc):
    return H_static + h_f + h_acc


# -----------------------------
# 🔹 Potencia hidráulica
# -----------------------------
def hydraulic_power(rho, Q, H):
    return rho * g * Q * H


# -----------------------------
# 🔹 Potencia al eje
# -----------------------------
def shaft_power(P_h, efficiency):
    return P_h / efficiency


# -----------------------------
# 🔹 NPSH disponible
# -----------------------------
def npsh_available(P_atm, P_vap, rho, h_suction):
    return (P_atm / (rho * g)) - (P_vap / (rho * g)) - h_suction


# -----------------------------
# 🔹 Función principal del sistema
# -----------------------------
def calculate_system(data):
    
    # 🔹 Inputs
    rho = data["fluid"]["density"]
    mu = data["fluid"]["viscosity"]
    Q = data["flow_m3s"]

    D = data["pipe"]["diameter"]
    L = data["pipe"]["length"]
    roughness = data["pipe"]["roughness"]

    H_static = data["system"]["static_head"]
    K_total = data["system"]["K_total"]

    efficiency = data["pump"]["efficiency"]

    # 🔹 Cálculos
    V = velocity(Q, D)
    Re = reynolds(rho, V, D, mu)
    f = friction_factor(Re, roughness, D)

    h_f = friction_losses(f, L, D, V)
    h_acc = accessory_losses(K_total, V)

    TDH = total_dynamic_head(H_static, h_f, h_acc)

    P_h = hydraulic_power(rho, Q, TDH)
    P_shaft = shaft_power(P_h, efficiency)

    return {
        "velocity": V,
        "reynolds": Re,
        "friction_factor": f,
        "h_f": h_f,
        "h_acc": h_acc,
        "TDH": TDH,
        "P_h": P_h,
        "P_shaft": P_shaft
    }
