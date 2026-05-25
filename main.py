import pandas as pd
import numpy as np

# Bryan Alexis Murillo Arellano
# GENERAR DATOS DE VENTAS HISTÓRICAS
# Angel Misael Barron Sanchez

ventas = pd.DataFrame({
    'Customer_ID': np.random.randint(1000, 2000, 5000),
    'monto': np.random.randint(100, 5000, 5000),
    'fecha': pd.date_range(
        start='2025-01-01',
        periods=5000,
        freq='h'
    ),
    'id_tienda': np.random.randint(1, 20, 5000)
})

ventas.to_csv('data/ventas_historicas.csv', index=False)

print("ventas_historicas.csv generado")

# GENERAR PERFILES DE USUARIO

paises = ['México', 'mex', 'mx', 'USA', 'Canada']

perfiles = pd.DataFrame({
    'Customer_ID': np.arange(1000, 2000),
    'edad': np.random.randint(18, 70, 1000),
    'ingresos': np.random.randint(5000, 50000, 1000),
    'pais': np.random.choice(paises, 1000),
    'puntos_lealtad': np.random.randint(0, 10000, 1000)
})

perfiles.to_json(
    'data/perfiles_usuarios.json',
    orient='records',
    indent=4
)

print("perfiles_usuarios.json generado")

# GENERAR INVENTARIO

inventario = pd.DataFrame({
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'] * 250,
    'stock': np.random.randint(1, 100, 1000),
    'precio': np.random.randint(100, 20000, 1000)
})

# INSERTAR NULOS
inventario.loc[0:100, 'precio'] = np.nan

# INSERTAR DUPLICADOS
inventario = pd.concat([inventario, inventario.iloc[0:50]])

inventario.to_csv('data/inventario.csv', index=False)

print("inventario.csv generado")

print("\nDATOS GENERADOS CORRECTAMENTE")

# ==========================================
# LIMPIEZA DE DATOS
# ==========================================

print("\nINICIANDO LIMPIEZA DE DATOS...")

# LEER ARCHIVOS
ventas = pd.read_csv('data/ventas_historicas.csv')

perfiles = pd.read_json('data/perfiles_usuarios.json')

inventario = pd.read_csv('data/inventario.csv')

# ==========================================
# LIMPIEZA INVENTARIO
# ==========================================

print("\nVALORES NULOS EN INVENTARIO:")
print(inventario.isnull().sum())

# RELLENAR NULOS
inventario['precio'] = inventario['precio'].fillna(
    inventario['precio'].mean()
)

# ELIMINAR DUPLICADOS
inventario = inventario.drop_duplicates()

print("\nINVENTARIO LIMPIO")

# ==========================================
# LIMPIEZA DE PAISES
# ==========================================

perfiles['pais'] = perfiles['pais'].replace({
    'mex': 'México',
    'mx': 'México'
})

print("\nPAISES NORMALIZADOS")

# ==========================================
# NORMALIZAR FECHAS
# ==========================================

ventas['fecha'] = pd.to_datetime(
    ventas['fecha']
)

print("\nFECHAS NORMALIZADAS")

# ==========================================
# GUARDAR LIMPIOS
# ==========================================

ventas.to_csv(
    'output/ventas_limpias.csv',
    index=False
)

perfiles.to_csv(
    'output/perfiles_limpios.csv',
    index=False
)

inventario.to_csv(
    'output/inventario_limpio.csv',
    index=False
)

print("\nDATOS LIMPIOS GUARDADOS")

# ==========================================
# ENRIQUECIMIENTO DE DATOS (JOIN)
# ==========================================

print("\nINICIANDO MERGE DE DATOS...")

data_master = pd.merge(
    ventas,
    perfiles,
    on='Customer_ID',
    how='left'
)

print("\nMERGE COMPLETADO")

print("\nPRIMERAS FILAS:")
print(data_master.head())

# ==========================================
# REGLAS DE NEGOCIO
# ==========================================

print("\nCREANDO SEGMENTOS DE CLIENTES...")

data_master['segmento_cliente'] = np.where(
    (data_master['monto'] > 1000) &
    (data_master['edad'] < 30),
    'Premium Joven',
    'Regular'
)

print("\nSEGMENTOS GENERADOS")

# ==========================================
# GUARDAR DATA MASTER
# ==========================================

data_master.to_csv(
    'output/data_master.csv',
    index=False
)

print("\nDATA MASTER GENERADO")

# ==========================================
# NORMALIZACION Y PCA
# ==========================================

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

print("\nINICIANDO NORMALIZACION...")

# VARIABLES NUMERICAS
variables_numericas = [
    'monto',
    'edad',
    'ingresos',
    'puntos_lealtad'
]

# SCALER
scaler = MinMaxScaler()

datos_escalados = scaler.fit_transform(
    data_master[variables_numericas]
)

print("\nDATOS NORMALIZADOS")

# ==========================================
# PCA
# ==========================================

print("\nAPLICANDO PCA...")

pca = PCA(n_components=3)

componentes = pca.fit_transform(
    datos_escalados
)

# CREAR DATAFRAME PCA
pca_df = pd.DataFrame(
    componentes,
    columns=['PC1', 'PC2', 'PC3']
)

print("\nPCA COMPLETADO")

print("\nVARIANZA EXPLICADA:")
print(pca.explained_variance_ratio_)

# GUARDAR PCA
pca_df.to_csv(
    'output/pca_resultados.csv',
    index=False
)

print("\nARCHIVO PCA GENERADO")

# ==========================================
# VISUALIZACIONES
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

print("\nGENERANDO GRAFICOS...")

# ==========================================
# BOXPLOT
# ==========================================

plt.figure(figsize=(8,5))

sns.boxplot(
    x=data_master['monto']
)

plt.title("Boxplot de Montos de Venta")

plt.savefig(
    'dashboard/boxplot_ventas.png'
)

plt.close()

print("BOXPLOT GENERADO")

# ==========================================
# SCATTER PCA
# ==========================================

plt.figure(figsize=(8,6))

plt.scatter(
    pca_df['PC1'],
    pca_df['PC2']
)

plt.xlabel("PC1")
plt.ylabel("PC2")

plt.title("Scatter Plot PCA")

plt.savefig(
    'dashboard/scatter_pca.png'
)

plt.close()

print("SCATTER PCA GENERADO")

# ==========================================
# GENERAR FLUJO DE USUARIOS
# ==========================================

flujo = pd.DataFrame({
    'source': ['Web', 'Web', 'Carrito'],
    'target': ['Carrito', 'Salida', 'Compra'],
    'value': [4000, 1000, 3000]
})

print("\nFLUJO DE USUARIOS GENERADO")

# ==========================================
# SANKEY DIAGRAM
# ==========================================

import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Web", "Carrito", "Compra", "Salida"]
    ),
    link=dict(
        source=[0, 0, 1],
        target=[1, 3, 2],
        value=[4000, 1000, 3000]
    )
)])

fig.update_layout(
    title_text="Flujo de Usuarios",
    font_size=10
)

fig.write_html(
    "dashboard/sankey_diagram.html"
)

print("SANKEY DIAGRAM GENERADO")

# ==========================================
# ARCHIVO FINAL BI
# ==========================================

data_master.to_csv(
    'output/data_master_clean.csv',
    index=False
)

print("\nARCHIVO FINAL BI GENERADO")