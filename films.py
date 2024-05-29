import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Cargando los datos
@st.cache
def load_data():
    data = pd.read_csv('IMDB-Movie-Data.csv')
    return data

data = load_data()

# Sidebar - Añadiendo filtros
st.sidebar.header('Filtros')
selected_years = st.sidebar.multiselect('Año de Lanzamiento', data['Year'].unique(), data['Year'].unique())
selected_rating = st.sidebar.slider('Rating', float(data['Rating'].min()), float(data['Rating'].max()), (float(data['Rating'].min()), float(data['Rating'].max())))
selected_revenue = st.sidebar.slider('Revenue (Millions)', float(data['Revenue (Millions)'].min()), float(data['Revenue (Millions)'].max()), (float(data['Revenue (Millions)'].min()), float(data['Revenue (Millions)'].max())))
selected_duration = st.sidebar.slider('Duración (Minutos)', int(data['Runtime (Minutes)'].min()), int(data['Runtime (Minutes)'].max()), (int(data['Runtime (Minutes)'].min()), int(data['Runtime (Minutes)'].max())))
selected_votes = st.sidebar.slider('Número de Votos', int(data['Votes'].min()), int(data['Votes'].max()), (int(data['Votes'].min()), int(data['Votes'].max())))

# Aplicando filtros
filtered_data = data[(data['Year'].isin(selected_years)) & (data['Rating'] >= selected_rating[0]) & (data['Rating'] <= selected_rating[1]) & 
                     (data['Revenue (Millions)'] >= selected_revenue[0]) & (data['Revenue (Millions)'] <= selected_revenue[1]) &
                     (data['Runtime (Minutes)'] >= selected_duration[0]) & (data['Runtime (Minutes)'] <= selected_duration[1]) &
                     (data['Votes'] >= selected_votes[0]) & (data['Votes'] <= selected_votes[1])]

# Título de la aplicación
st.title('Dashboard de Películas')

# Dashboard de Facturación por Año
st.header('Facturación por Año')
revenue_per_year = filtered_data.groupby('Year')['Revenue (Millions)'].sum()
fig, ax = plt.subplots()
ax.bar(revenue_per_year.index, revenue_per_year.values)
ax.set_xlabel('Año')
ax.set_ylabel('Facturación (Millones)')
ax.set_title('Facturación Total por Año')
st.pyplot(fig)

# Top 20 Películas de Mayor Rating
st.header('Top 20 Películas de Mayor Rating')
top20_rating = filtered_data.sort_values('Rating', ascending=False).head(20)
st.dataframe(top20_rating[['Title', 'Rating']])

# Top 20 Películas con Mayor Revenue
st.header('Top 20 Películas con Mayor Revenue')
top20_revenue = filtered_data.sort_values('Revenue (Millions)', ascending=False).head(20)
st.dataframe(top20_revenue[['Title', 'Revenue (Millions)']])

# Top 20 Películas con Mayores Votos
st.header('Top 20 Películas con Mayores Votos')
top20_votes = filtered_data.sort_values('Votes', ascending=False).head(20)
st.dataframe(top20_votes[['Title', 'Votes']])

# Actores Más Repetidos
st.header('Actores Más Repetidos')
all_actors = ', '.join(filtered_data['Actors']).split(', ')
actors_count = Counter(all_actors)
most_common_actors = pd.DataFrame(actors_count.most_common(20), columns=['Actor', 'Appearances'])
st.dataframe(most_common_actors)
