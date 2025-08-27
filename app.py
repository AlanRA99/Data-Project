import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Reading the CSV file
car_data = pd.read_csv('vehicles_us.csv')

# Creating a button in Streamlit (Histogram button)
hist_button = st.button('Construir histograma')

# Histogram button
# what happens when the button is clicked
if hist_button:
    # write a message to the app
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Creating a histogram with plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Add a title to the histogram
    fig.update_layout(title_text='Distribución del Odómetro')

    # Show the plot in the Streamlit app
    st.plotly_chart(fig, use_container_width=True)


# Creating a button in Streamlit (Scatter button)
hist_button_1 = st.button('Construir gráfica de dispersión')

# Scatter plot button
# what happens when the button is clicked
if hist_button_1:
    # write a message to the app
    st.write('Creación de una grafica de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Creating a scatter with plotly.graph_objects
    fig_1 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Add a title to the scatter
    fig_1.update_layout(title_text='Relación entre Odómetro y Precio')

    # Show the plot in the Streamlit app
    st.plotly_chart(fig_1, use_container_width=True)
