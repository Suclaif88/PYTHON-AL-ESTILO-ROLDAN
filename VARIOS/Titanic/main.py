import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('content/titanic3.csv')

df = df[['fare', 'survived']]
df['fare'] = df['fare'].replace({',': '.'}, regex=True)
df['fare'] = pd.to_numeric(df['fare'], errors='coerce')
df = df.dropna(subset=['fare', 'survived'])

df['survived'] = df['survived'].astype(int)

def calcular_costo_supervivencia(df):
    return df.groupby('survived')['fare'].mean().to_dict()

resultados_fare = calcular_costo_supervivencia(df)

if resultados_fare:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(resultados_fare.keys(), resultados_fare.values(), color=['red', 'green'])
    ax.set_title('Costo promedio del boleto según supervivencia', fontsize=16)
    ax.set_xlabel('Estado', fontsize=12)
    ax.set_ylabel('Costo promedio del boleto (Fare)', fontsize=12)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['No sobrevivieron', 'Sobrevivieron'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print("No hay datos para graficar.")
