import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("simulation_results.csv")

plt.figure(figsize=(12, 6))
width = 0.35
x = range(len(df))

plt.bar([i - width/2 for i in x], df["Consumo_Base_Wh"], width, label='Consumo Base (Sin Agente)', color='#e74c3c')
plt.bar([i + width/2 for i in x], df["Consumo_Opt_Wh"], width, label='Consumo Opt. (Con Agente)', color='#2ecc71')

plt.xlabel('PCs del Laboratorio')
plt.ylabel('Consumo Estimado (Wh)')
plt.title('Comparativa de Consumo Energético: Base vs Optimizado')
plt.xticks(x, df["PC_ID"], rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig('comparativa_consumo.png')
print("¡Gráfico generado exitosamente como 'comparativa_consumo.png'!")