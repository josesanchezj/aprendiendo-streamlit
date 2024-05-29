import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Cargando los datos
@st.cache
def load_data():
    data = pd.read_csv('/path/to/your/file.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Dashboard de Películas')

# Dashboard de Facturación por Año
st.header('Facturación por Año')
revenue_per_year = data.groupby('Year')['Revenue (Millions)'].sum()
fig, ax = plt.subplots()
ax.bar(revenue_per_year.index, revenue_per_year.values)
ax.set_xlabel('Año')
ax.set_ylabel('Facturación (Millones)')
ax.set_title('Facturación Total por Año')
st.pyplot(fig)

# Top 20 Películas de Mayor Rating
st.header('Top 20 Películas de Mayor Rating')
top20_rating = data.sort_values('Rating', ascending=False).head(20)
st.dataframe(top20_rating[['Title', 'Rating']])

# Top 20 Películas con Mayor Revenue
st.header('Top 20 Películas con Mayor Revenue')
top20_revenue = data.sort_values('Revenue (Millions)', ascending=False).head(20)
st.dataframe(top20_revenue[['Title', 'Revenue (Millions)']])

# Top 20 Películas con Mayores Votos
st.header('Top 20 Películas con Mayores Votos')
top20_votes = data.sort_values('Votes', ascending=False).head(20)
st.dataframe(top20_votes[['Title', 'Votes']])

# Actores Más Repetidos
st.header('Actores Más Repetidos')
all_actors = ', '.join(data['Actors']).split(', ')
actors_count = Counter(all_actors)
most_common_actors = pd.DataFrame(actors_count.most_common(20), columns=['Actor', 'Appearances'])
st.dataframe(most_common_actors)
