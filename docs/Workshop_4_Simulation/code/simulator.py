import random
import pandas as pd

NUM_PCS = 20
HORAS_LAB = 12
MINUTOS_DIA = HORAS_LAB * 60
TIEMPO_INACTIVIDAD_UMBRAL = 15
CPU_UMBRAL = 20.0 
CONSUMO_PC_ACTIVO = 250 / 60  
CONSUMO_PC_SUSPENDIDO = 10 / 60  

# Probabilidades Conductuales
PROB_OLVIDO = 0.80 
PROB_CARGA_ALTA = 0.15 
PROB_CANCELAR_NUDGE = 0.10 


def simular_dia_laboratorio():
    consumo_base_total = 0
    consumo_optimizado_total = 0
    suspensiones_exitosas = 0
    falsos_positivos_evitados = 0

    log_resultados = []

    for pc in range(NUM_PCS):

        minutos_inactivo = 0
        estado_pc_base = "ACTIVO"
        estado_pc_optimizado = "ACTIVO"

        consumo_base_pc = 0
        consumo_opt_pc = 0


        for minuto in range(MINUTOS_DIA):

            if random.random() < PROB_OLVIDO:
                consumo_base_pc += CONSUMO_PC_ACTIVO
            else:

                if minuto < (MINUTOS_DIA / 2):
                    consumo_base_pc += CONSUMO_PC_ACTIVO
                else:
                    consumo_base_pc += 0 


            if estado_pc_optimizado == "ACTIVO":
                consumo_opt_pc += CONSUMO_PC_ACTIVO


                if random.random() < PROB_OLVIDO:
                    minutos_inactivo += 1
                else:
                    minutos_inactivo = 0 


                if minutos_inactivo >= TIEMPO_INACTIVIDAD_UMBRAL:

                    cpu_actual = random.uniform(5.0, 100.0) if random.random() < PROB_CARGA_ALTA else random.uniform(
                        1.0, 15.0)

                    if cpu_actual < CPU_UMBRAL:
                        if random.random() > PROB_CANCELAR_NUDGE:
                            estado_pc_optimizado = "SUSPENDIDO"
                            suspensiones_exitosas += 1
                        else:
                            minutos_inactivo = 0 
                    else:
                        falsos_positivos_evitados += 1
                        minutos_inactivo = 0

            elif estado_pc_optimizado == "SUSPENDIDO":
                consumo_opt_pc += CONSUMO_PC_SUSPENDIDO

        consumo_base_total += consumo_base_pc
        consumo_optimizado_total += consumo_opt_pc

        log_resultados.append({
            "PC_ID": f"PC_{pc + 1}",
            "Consumo_Base_Wh": round(consumo_base_pc, 2),
            "Consumo_Opt_Wh": round(consumo_opt_pc, 2),
            "Ahorro_Wh": round(consumo_base_pc - consumo_opt_pc, 2)
        })

    print("=== RESULTADOS DE LA SIMULACIÓN (1 DÍA - 20 PCs) ===")
    print(f"Consumo Total SIN Agente: {consumo_base_total / 1000:.2f} kWh")
    print(f"Consumo Total CON Agente: {consumo_optimizado_total / 1000:.2f} kWh")
    print(f"Ahorro Energético: {((consumo_base_total - consumo_optimizado_total) / consumo_base_total) * 100:.2f}%")
    print(f"Suspensiones Exitosas: {suspensiones_exitosas}")
    print(f"Falsos Positivos Evitados (Protección CPU > 20%): {falsos_positivos_evitados}")

    df = pd.DataFrame(log_resultados)
    df.to_csv("simulation_results.csv", index=False)
    print("Datos exportados a 'simulation_results.csv'")


if __name__ == "__main__":
    simular_dia_laboratorio()