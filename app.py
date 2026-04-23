import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("COVID-19 Data Analysis Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv('/home/jovyan/work/owid-covid-data.csv')
    cols = ['location', 'continent', 'date',
            'total_cases', 'new_cases',
            'total_deaths', 'new_deaths',
            'population']
    df = df[cols].copy()
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna(subset=['total_cases', 'new_cases'])
    return df

df = load_data()

exclude = [
    'World', 'Asia', 'Europe', 'Africa',
    'North America', 'South America', 'Oceania',
    'European Union', 'High income', 'Low income',
    'Upper middle income', 'Lower middle income',
    'High-income countries'
]
df_countries = df[~df['location'].isin(exclude)]

# Summary metrics
col1, col2, col3 = st.columns(3)
world_latest = df[df['location'] == 'World'].iloc[-1]
col1.metric("Total Cases Worldwide", f"{world_latest['total_cases']:,.0f}")
col2.metric("Total Deaths Worldwide", f"{world_latest['total_deaths']:,.0f}")
col3.metric("Number of Countries", f"{df_countries['location'].nunique()}")

st.divider()

# Chart 1 - Top 10 Countries
st.subheader("Top 10 Countries by Total Cases")
top10 = df_countries.groupby('location')['new_cases'].sum().sort_values(ascending=False).head(10).reset_index()
top10.columns = ['Country', 'Total Cases']

fig1 = px.bar(top10, x='Total Cases', y='Country',
              orientation='h', color='Total Cases',
              color_continuous_scale='Reds')
fig1.update_layout(yaxis=dict(autorange='reversed'))
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# Chart 2 - Global daily cases
st.subheader("Daily Cases Worldwide")
world = df[df['location'] == 'World']

fig2 = px.line(world, x='date', y='new_cases',
               labels={'date': 'Date', 'new_cases': 'New Cases'},
               color_discrete_sequence=['steelblue'])
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Chart 3 - Country filter
st.subheader("Country-Level Analysis")
country = st.selectbox("Select a Country:", sorted(df_countries['location'].unique()))
df_country = df_countries[df_countries['location'] == country]

fig3 = px.line(df_country, x='date', y='new_cases',
               title=f'Daily Cases in {country}',
               labels={'date': 'Date', 'new_cases': 'New Cases'},
               color_discrete_sequence=['green'])
st.plotly_chart(fig3, use_container_width=True)