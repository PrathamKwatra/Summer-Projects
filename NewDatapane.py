import pandas as pd
import altair as alt
import datapane as dp

dataset = pd.read_csv('https://data.humdata.org/dataset/c87c4508-9caf-4959-bf06-6ab4855d84c6/resource/8c7d6af8-c703-4904-b5d0-0ab693e54ee4/download/covid-19-tests-country.csv')
df = dataset.groupby(['Entity', 'Year'])['Total COVID-19 tests'].sum().reset_index()

plot = alt.Chart(df).mark_area(opacity=0.4, stroke='black').encode(
    x='Year:T',
    y=alt.Y('Total COVID-19 tests:Q', stack=None),
    color=alt.Color('Entity:N', scale=alt.Scale(scheme='set1')),
    tooltip='Entity:N'
).interactive().properties(width='container')

dp.Report(
    dp.Plot(plot), 
    dp.DataTable(df)
).save(path='report.html', open=True)
