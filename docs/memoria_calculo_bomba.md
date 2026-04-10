# MEMORIA DE CÁLCULO PARAMÉTRICA

## Sistema de Selección de Bombas Centrífugas

---

##  1. Objetivo

Desarrollar un modelo de cálculo generalizado para la selección de bombas centrífugas en sistemas hidráulicos, permitiendo al usuario definir condiciones de operación, propiedades del fluido y características del sistema.

Este modelo está diseñado para ser implementado posteriormente como herramienta computacional.

---

##  2. Alcance del modelo

El sistema permitirá:

* Definir múltiples fluidos (no solo agua)
* Configurar condiciones hidráulicas variables
* Calcular TDH automáticamente
* Evaluar potencia requerida
* Verificar condiciones de cavitación (NPSH)
* Generar curvas del sistema
* Determinar punto de operación bomba-sistema

---

##  3. Definición de datos de entrada

###  3.1 Propiedades del fluido

| Parámetro        | Descripción            | Unidad  |
| ---------------- | ---------------------- | ------- |
| Tipo de fluido   | Agua / personalizado   | -       |
| Densidad (ρ)     | Masa volumétrica       | kg/m³   |
| Viscosidad (μ)   | Viscosidad dinámica    | Pa·s    |
| Presión de vapor | Para cálculo de NPSH   | Pa      |
| Temperatura      | Condición de operación | °C / °F |

---

### 3.2 Condiciones del sistema

| Parámetro           | Unidad               |
| ------------------- | -------------------- |
| Caudal (Q)          | m³/h, L/s, GPM       |
| Elevación estática  | m / ft               |
| Presión de descarga | bar / psi (opcional) |

---

###  3.3 Tubería principal

| Parámetro        | Unidad     |
| ---------------- | ---------- |
| Diámetro interno | m / in     |
| Longitud         | m / ft     |
| Rugosidad        | m          |
| Material         | (opcional) |

---

###  3.4 Línea de succión

| Parámetro          | Unidad |
| ------------------ | ------ |
| Longitud           | m      |
| Diámetro           | m      |
| Altura de succión  | m      |
| Pérdidas estimadas | m      |

---

###  3.5 Accesorios

Los accesorios se definirán como una lista:

Ejemplo:

* Codos 90°
* Válvulas
* Tees
* Reducciones

Cada uno con coeficiente K asociado.

---

###  3.6 Sistema de unidades

El sistema permitirá selección de unidades:

* Caudal: m³/h, L/s, GPM
* Presión: Pa, bar, psi
* Temperatura: °C, °F

Todos los cálculos internos se realizarán en **Sistema Internacional (SI)**.

---

##  4. Modelo matemático

---

### 4.1 Velocidad del fluido

V = \frac{Q}{A}

---

### 4.2 Número de Reynolds

Re = \frac{\rho V D}{\mu}

---

### 4.3 Factor de fricción (Darcy-Weisbach)

Se utilizará correlación de **Swamee-Jain** para flujo turbulento.

---

### 4.4 Pérdidas por fricción

h_f = f \cdot \frac{L}{D} \cdot \frac{V^2}{2g}

---

### 4.5 Pérdidas en accesorios

h_{acc} = K \cdot \frac{V^2}{2g}

---

### 4.6 Carga dinámica total (TDH)

TDH = H_{est\acute{a}tica} + h_f + h_{acc}

---

### 4.7 Potencia hidráulica

P_h = \rho g Q H

---

### 4.8 Potencia al eje

$$
P_{eje} = \frac{P_h}{\eta}
$$

---

### 4.9 NPSH disponible

$$
NPSHa = \frac{P_{atm}}{\rho g} - \frac{P_{vap}}{\rho g} - h_{suc}
$$

---

##  5. Modelo para generación de curvas

---

### 5.1 Curva del sistema

H = H_{est\acute{a}tica} + K Q^2

Permite evaluar la carga del sistema para distintos caudales.

---

### 5.2 Curva de la bomba (modelo simplificado)

H = a - b Q^2

---

### 5.3 Punto de operación

Se determina como la intersección entre:

* Curva del sistema
* Curva de la bomba

---

##  6. Resultados esperados

El sistema deberá entregar:

* TDH
* Pérdidas por fricción
* Pérdidas en accesorios
* Potencia hidráulica
* Potencia requerida
* NPSHa
* Punto de operación
* Gráficas:

  * Curva del sistema
  * Curva de la bomba
  * Punto de operación

---

##  7. Implementación futura

Este modelo será implementado como:

* Motor de cálculo en Python
* Interfaz interactiva (web app)
* Herramienta de ingeniería para selección de bombas

---

##  8. Conclusión

Este documento define la base matemática y estructural para el desarrollo de una herramienta profesional de selección de bombas centrífugas, adaptable a múltiples condiciones de operación y tipos de fluidos.

