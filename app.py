import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def get_language_popularity_data():
    df = pd.read_csv("./data/popularity.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

dataset = get_language_popularity_data()

st.write('All data about language popularity:')
st.write(dataset)

all_languages = [c for c in dataset.columns if c != 'Date']

top_languages_coun  = 10
top_languages = list(dataset.iloc[-1][1:].sort_values()[-top_languages_coun:].index.values)

languages = st.multiselect(
    "Choose languages",
    list(all_languages),
    top_languages
)
if not languages:
    st.error("Please select at least one language.")
else:
    columns = ['Date']
    columns.extend(languages)
    data = pd.melt(dataset[columns],
                   id_vars = ['Date']).rename(columns={
                       'variable': 'Language',
                       'value': 'Popularity'
                   })

    chart = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y("Popularity", stack=None),
            color="Language:N"
        )
    )
    st.altair_chart(chart, use_container_width=True)
