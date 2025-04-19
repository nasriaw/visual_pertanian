import streamlit as st
import pandas as pd
import plotly.express as px
with pd.ExcelFile('koordinat_desa_malangkab_luas_sawah.xls') as xls:
         data = pd.read_excel(xls,'koordinat_desa')  

df = pd.DataFrame(data)
fig = px.scatter_mapbox(df, hover_name='kec', hover_data=[(df.desa_kel), (df.luas_sawah_ha), (df.produksi_beras_ton)], lat='centroid_lat', lon='centroid_lon', size_max=20, zoom=10, mapbox_style='carto-positron')
fig.show()
