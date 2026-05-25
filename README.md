# Proyecto ETL - Análisis Global de Retail y Comportamiento del Cliente

## Descripción
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) utilizando Python para integrar, limpiar, transformar y analizar datos provenientes de múltiples fuentes heterogéneas.

El objetivo es centralizar la información de retail y generar un repositorio maestro optimizado para Business Intelligence y análisis avanzado.

---

# Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn
- PCA
- ETL Pipeline

---

# Fuentes de Datos

- CSV
- JSON
- Datos simulados SQL
- Visualizaciones
- Sankey Diagram
- PCA

---

# Pipeline ETL

## Extract
Se generaron y cargaron datos desde:
- ventas_historicas.csv
- perfiles_usuarios.json
- inventario.csv

## Transform
Se aplicaron:
- Limpieza de nulos
- Eliminación de duplicados
- Normalización de fechas
- Limpieza de categorías
- Reglas de negocio
- Escalado Min-Max

## Load
Se generó:
- data_master_clean.csv

---

# Analítica Avanzada

Se aplicó PCA para reducir dimensiones y analizar el comportamiento de los clientes.

---

# Visualizaciones

- Boxplot de ventas
- Scatter Plot PCA
- Sankey Diagram

---

# Ejecución

```bash
python main.py
```

---

# Autor
Proyecto desarrollado para la materia:
Programación para el Procesamiento de Datos.
Bryan Alexis Murillo Arellano
Angel Misael Barron Sanchez