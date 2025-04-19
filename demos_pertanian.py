# Copyright 2018-2020 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import urllib.error

def intro():
    import streamlit as st
#    st.sidebar.success("Pilih Komoditas Diatas.")
    st.markdown(
        """
        Visual Data Pertanian Kabupaten Malang, data musim tanam Okt-Mar 2018 dan Jan-Sept 2019 
        serta data  Panen Jan-Des2019, untuk komoditas Utama Padi, Jagung, Cabe Rawit, Cabe Besar,
        Bawang Merah dan Bawang Putih

        **👈 Pilih Komoditas di menu di samping ini.
    """
    )
# ==1. PADI/BERAS ===========================================================================
def padi_visual():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

    with pd.ExcelFile('data_ltt_produksi_pertanian_2019.xls') as xls:
         data1 = pd.read_excel(xls, 'data_ltt_produksi_beras')
    with pd.ExcelFile('data_pertanian_2019.xls') as xls:
         data7 = pd.read_excel(xls, 'data_padi_2019')
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019_tanpa_total.xls') as xls:
         data13 = pd.read_excel(xls, 'data_ltt_produksi_beras')     
    with pd.ExcelFile('koordinat_desa_malangkab_luas_sawah.xls') as xls:
         data19 = pd.read_excel(xls,'koordinat_desa')     
    
    data13 = data13.astype(str)
    
    st.write('Wilayah Kabupaten Malang, Tahun 2019')
#    st.sidebar.title('1.a. Produksi Padi/Beras,')
    select = st.sidebar.selectbox('Pilih Bulan, Jan-Des, atau total', data1['Bulan'])
    bulan_data_padi=data1[data1['Bulan'] == select]
    
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'status':['Luas Tanam (ha)','Produksi Beras (ton)','Kebutuhan (ton)', 'Surplus_Beras_ton'],
         'kuantitas':(
          dataset.iloc[0]['Luas_Tanam_ha'], 
          dataset.iloc[0]['Produksi_ton'],
          dataset.iloc[0]['Kebutuhan_ton'], 
          dataset.iloc[0]['Surplus_Beras_ton'], 
#           dataset.iloc[0]['Surplus_komulatif_ton'], 
          )})
         return total_dataframe
    bulan_total_padi = get_total_dataframe(bulan_data_padi)
    if st.sidebar.checkbox("Show Analysis by Komoditas Padi", True, key=2):
#         st.title("1. Data Padi dan Beras")
       
    #     st.markdown("### Bulan: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=3):
         if st.checkbox('1. Data Tanam dan Produksi Bulanan Padi'):
           st.markdown("### Bulan: %s" % (select))
           bulan_total_padi_graph = px.bar(
           bulan_total_padi, 
             x='status',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='kuantitas')
           st.plotly_chart(bulan_total_padi_graph)
    # =============================================================================
#    st.sidebar.title('1.b.Data Tahunan Padi/Beras,')
    #st.sidebar.checkbox("Data terpilah sesuai Komoditas", True, key=3)
    select = st.sidebar.selectbox('Pilih Attribut Komoditas',data7['Attribut'])
    bulan_data_attribut_padi = data7[data7['Attribut'] == select]
    #select_status = st.sidebar.radio("Data terpilah sesuai Attribut", ('Sawah', 'Tegal', 'Beras', 'konsumsi', 'Surplus'))
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'bulan':['Januari', 'Februari', 'Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],
         'kuantitas':(dataset.iloc[0]['Januari'],
          dataset.iloc[0]['Februari'],
          dataset.iloc[0]['Maret'], 
          dataset.iloc[0]['April'],
          dataset.iloc[0]['Mei'],
          dataset.iloc[0]['Juni'],
          dataset.iloc[0]['Juli'],
          dataset.iloc[0]['Agustus'],
          dataset.iloc[0]['September'],
          dataset.iloc[0]['Oktober'],
          dataset.iloc[0]['November'],
          dataset.iloc[0]['Desember'],
          )})
         return total_dataframe
    bulan_total_padi = get_total_dataframe(bulan_data_attribut_padi)
    if st.sidebar.checkbox("Show Analysis by Attribut", True, key=11):
    #     st.markdown("### Attribut Komoditas: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=12):
         if st.checkbox('2. Grafik Data Bulanan Padi'):    
            st.markdown("### Attribut Komoditas: %s" % (select))    
            bulan_total_padi_graph = px.bar(
             bulan_total_padi, 
             x='bulan',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='bulan')
            st.plotly_chart(bulan_total_padi_graph)
    # =============================================================================
    def get_table():
         datatable = data1[['Bulan', 'Luas_Tanam_ha', 'Produksi_ton','Kebutuhan_ton','Surplus_Beras_ton','Komulatif_Surplus_Beras_ton',]]
         datatable = datatable[datatable['Bulan'] != 'State Unassigned']
         return datatable
    datatable1 = get_table()
    
    if st.checkbox('3. Show raw data Padi'):
        st.subheader('Raw data Padi')
        st.dataframe(datatable1) # will display the dataframe
    #    st.table(datatable1)# will display the table
    
    if st.checkbox('4. Show line chart data Padi'):
        st.subheader('Line Chart data Padi')
        st.line_chart(data13)
    #    st.dataframe(data13) # will display the dataframe
    #    st.plotly_chart(data13)
    
    df = pd.DataFrame(data19)
    if st.checkbox('5. Peta Titik Luas sawah per Desa'):
        st.subheader('Lokasi Sawah')
        fig = px.scatter_mapbox(df, hover_name='kec', hover_data=[(df.desa_kel), (df.luas_sawah_ha), (df.produksi_beras_ton)], lat='centroid_lat', lon='centroid_lon', size_max=20, zoom=10, mapbox_style='carto-positron')
        fig.show()
        
# ==2. jagung ===========================================================================         
def jagung_visual():
    import streamlit as st
    import pandas as pd
    import plotly.express as px 
    
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019.xls') as xls:
         data2 = pd.read_excel(xls, 'data_ltt_produksi_jagung')
    with pd.ExcelFile('data_pertanian_2019.xls') as xls:
         data8 = pd.read_excel(xls, 'data_jagung_2019')
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019_tanpa_total.xls') as xls:
         data14 = pd.read_excel(xls, 'data_ltt_produksi_jagung')
   
    data2 = data2.astype(str)
    data14 = data14.astype(str)
   
    st.write('Wilayah Kabupaten Malang, Tahun 2019')
#    st.sidebar.title('2.a. Produksi Jagung,')
    select = st.sidebar.selectbox('Pilih Bulan, Jan-Des, atau total setahun', data2['Bulan'])
    bulan_data_jagung=data2[data2['Bulan'] == select]
    
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'status':['Luas Tanam (ha)','Produksi Jagung (ton)','Kebutuhan (ton)', 'Surplus_Jagung_ton'],
         'kuantitas':(
          dataset.iloc[0]['Luas_Tanam_ha'], 
          dataset.iloc[0]['Produksi_ton'],
          dataset.iloc[0]['Kebutuhan_ton'], 
          dataset.iloc[0]['Surplus_Jagung_ton'], 
          )})
         return total_dataframe
    bulan_total_jagung = get_total_dataframe(bulan_data_jagung)
    if st.sidebar.checkbox("Show Analysis by Komoditas Jagung", True, key=4):
    #     st.title("2. Data Jagung.")
    #     st.markdown("### Bulan: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=5):
         if st.checkbox('1. Data Tanam dan Produksi Bulanan Jagung'):
           st.markdown("### Bulan: %s" % (select))
           bulan_total_jagung_graph = px.bar(
             bulan_total_jagung, 
             x='status',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='kuantitas')
           st.plotly_chart(bulan_total_jagung_graph)
    # =============================================================================
#    st.sidebar.title('2.b.Data Tahunan Jagung,')
    #st.sidebar.checkbox("Data terpilah sesuai Komoditas", True, key=11)
    select = st.sidebar.selectbox('Pilih Attribut Komoditas',data8['Attribut'])
    bulan_data_attribut_jagung = data8[data8['Attribut'] == select]
    #select_status = st.sidebar.radio("Data terpilah sesuai Attribut", ('Sawah', 'Tegal', 'Beras', 'konsumsi', 'Surplus'))
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'bulan':['Januari', 'Februari', 'Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],
         'kuantitas':(dataset.iloc[0]['Januari'],
          dataset.iloc[0]['Februari'],
          dataset.iloc[0]['Maret'], 
          dataset.iloc[0]['April'],
          dataset.iloc[0]['Mei'],
          dataset.iloc[0]['Juni'],
          dataset.iloc[0]['Juli'],
          dataset.iloc[0]['Agustus'],
          dataset.iloc[0]['September'],
          dataset.iloc[0]['Oktober'],
          dataset.iloc[0]['November'],
          dataset.iloc[0]['Desember'],
          )})
         return total_dataframe
    bulan_total_jagung = get_total_dataframe(bulan_data_attribut_jagung)
    if st.sidebar.checkbox("Show Analysis by Attribut", True, key=12):
    #     st.markdown("### Attribut Komoditas: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=13):
          if st.checkbox('2. Grafik Data Bulanan Jagung'):
           st.markdown("### Attribut Komoditas: %s" % (select))
           bulan_total_jagung_graph = px.bar(
             bulan_total_jagung, 
             x='bulan',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='bulan')
           st.plotly_chart(bulan_total_jagung_graph)
    # =============================================================================
            
    def get_table():
         datatable = data2[['Bulan', 'Luas_Tanam_ha', 'Produksi_ton','Kebutuhan_ton','Surplus_Jagung_ton']]
         datatable = datatable[datatable['Bulan'] != 'State Unassigned']
         return datatable
    datatable2 = get_table()
    
    if st.checkbox('3. Show raw data Jagung'):
        st.subheader('Raw data Jagung')
        st.dataframe(datatable2) # will display the dataframe
    #   st.table(datatable2)# will display the table
    
    if st.checkbox('4. Show line chart data Jagung'):
        st.subheader('Line Chart data Jagung')
        st.line_chart(data14)
        
# ==3. Cabe Rawit ===========================================================================
def caberawit_visual():
    import streamlit as st
    import pandas as pd
    import plotly.express as px 
    
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019.xls') as xls:
         data3 = pd.read_excel(xls, 'data_ltt_produksi_cabe_rawit')
    with pd.ExcelFile('data_pertanian_2019.xls') as xls:
         data9 = pd.read_excel(xls, 'data_cabe_rawit_2019')
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019_tanpa_total.xls') as xls:
          data15 = pd.read_excel(xls, 'data_ltt_produksi_cabe_rawit')
          
    data3 = data3.astype(str)
    data15 = data15.astype(str)
    
    st.write('Wilayah Kabupaten Malang, Tahun 2019')      
#    st.sidebar.title('3.a. Produksi Cabe Rawit,')
    select = st.sidebar.selectbox('Pilih Bulan, Jan-Des, atau total tahunan', data3['Bulan'])
    bulan_data_cabe_rawit=data3[data3['Bulan'] == select]
    
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'status':['Luas Tanam (ha)','Produksi (ton)','Kebutuhan (ton)', 'Surplus_Cabe_Rawit_ton'],
         'kuantitas':(
          dataset.iloc[0]['Luas_Tanam_ha'], 
          dataset.iloc[0]['Produksi_ton'],
          dataset.iloc[0]['Kebutuhan_ton'], 
          dataset.iloc[0]['Surplus_Cabe_Rawit_ton'], 
          )})
         return total_dataframe
    bulan_total_cabe_rawit = get_total_dataframe(bulan_data_cabe_rawit)
    if st.sidebar.checkbox("Show Analysis by Komoditas Cabe Rawit", True, key=6):
#         st.title("3. Data Cabe Rawit.")
    #     st.markdown("### Bulan: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=7):
         if st.checkbox('1. Data Tanam dan Produksi Bulanan Cabe Rawit'):
            st.markdown("### Bulan: %s" % (select))
            bulan_total_cabe_rawit_graph = px.bar(
              bulan_total_cabe_rawit, 
              x='status',
              y='kuantitas',
              labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
              color='kuantitas')
            st.plotly_chart(bulan_total_cabe_rawit_graph)
    # =============================================================================
#    st.sidebar.title('3.b.Data Tahunan Cabe Rawit,')
    #st.sidebar.checkbox("Data terpilah sesuai Komoditas", True, key=11)
    select = st.sidebar.selectbox('Pilih Attribut Komoditas',data9['Attribut'])
    bulan_data_attribut_cabe_rawit = data9[data9['Attribut'] == select]
    #select_status = st.sidebar.radio("Data terpilah sesuai Attribut", ('Sawah', 'Tegal', 'Beras', 'konsumsi', 'Surplus'))
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'bulan':['Januari', 'Februari', 'Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],
         'kuantitas':(dataset.iloc[0]['Januari'],
          dataset.iloc[0]['Februari'],
          dataset.iloc[0]['Maret'], 
          dataset.iloc[0]['April'],
          dataset.iloc[0]['Mei'],
          dataset.iloc[0]['Juni'],
          dataset.iloc[0]['Juli'],
          dataset.iloc[0]['Agustus'],
          dataset.iloc[0]['September'],
          dataset.iloc[0]['Oktober'],
          dataset.iloc[0]['November'],
          dataset.iloc[0]['Desember'],
          )})
         return total_dataframe
    bulan_total_cabe_rawit = get_total_dataframe(bulan_data_attribut_cabe_rawit)
    if st.sidebar.checkbox("Show Analysis by Attribut", True, key=13):
    #     st.markdown("### Attribut Komoditas: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=14):
          if st.checkbox('2. Grafik Data Bulanan Cabe Rawit'):
           st.markdown("### Attribut Komoditas: %s" % (select))
           bulan_total_cabe_rawit_graph = px.bar(
              bulan_total_cabe_rawit, 
              x='bulan',
              y='kuantitas',
              labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
              color='bulan')
           st.plotly_chart(bulan_total_cabe_rawit_graph)
    # =============================================================================
    
    def get_table():
         datatable = data3[['Bulan', 'Luas_Tanam_ha', 'Produksi_ton','Kebutuhan_ton','Surplus_Cabe_Rawit_ton']]
         datatable = datatable[datatable['Bulan'] != 'State Unassigned']
         return datatable
    datatable3 = get_table()
    
    if st.checkbox('3. Show raw data Cabe Rawit'):
        st.subheader('Raw data Cabe Rawit')
        st.dataframe(datatable3) # will display the dataframe
    #    st.table(datatable3)# will display the table
    
    if st.checkbox('4. Show line chart data Cabe Rawit'):
        st.subheader('Line Chart data Cabe Rawit')
        st.line_chart(data15)  

# ==4. Cabe Besar ===========================================================================
def cabebesar_visual():
    import streamlit as st
    import pandas as pd
    import plotly.express as px 
    
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019.xls') as xls:
         data4 = pd.read_excel(xls, 'data_ltt_produksi_cabe_besar')
    with pd.ExcelFile('data_pertanian_2019.xls') as xls:
         data10 = pd.read_excel(xls, 'data_cabe_besar_2019')
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019_tanpa_total.xls') as xls:
         data16 = pd.read_excel(xls, 'data_ltt_produksi_cabe_besar')       
    
    data4 = data4.astype(str)
    data16 = data16.astype(str)
    
    st.write('Wilayah Kabupaten Malang, Tahun 2019')
#    st.sidebar.title('4.a. Produksi Cabe Besar,')
    select = st.sidebar.selectbox('Pilih Bulan, Jan-Des, atau total 1 tahun', data4['Bulan'])
    bulan_data_cabe_besar=data4[data4['Bulan'] == select]
    
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'status':['Luas Tanam (ha)','Produksi (ton)','Kebutuhan (ton)', 'Surplus_Cabe_Besar_ton'],
         'kuantitas':(
          dataset.iloc[0]['Luas_Tanam_ha'], 
          dataset.iloc[0]['Produksi_ton'],
          dataset.iloc[0]['Kebutuhan_ton'], 
          dataset.iloc[0]['Surplus_Cabe_Besar_ton'], 
          )})
         return total_dataframe
    bulan_total_cabe_besar = get_total_dataframe(bulan_data_cabe_besar)
    if st.sidebar.checkbox("Show Analysis by Komoditas Cabe Besar", True, key=7):
#         st.title("4. Data Cabe Besar.")
    #     st.markdown("### Bulan: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=8):
         if st.checkbox('1. Data Tanam dan Produksi Bulanan Cabe Besar'):
          st.markdown("### Bulan: %s" % (select))
          bulan_total_cabe_besar_graph = px.bar(
             bulan_total_cabe_besar, 
             x='status',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='kuantitas')
          st.plotly_chart(bulan_total_cabe_besar_graph)
             
    # =============================================================================
#    st.sidebar.title('4.b.Data Tahunan Cabe Besar,')
    #st.sidebar.checkbox("Data terpilah sesuai Komoditas", True, key=11)
    select = st.sidebar.selectbox('Pilih Attribut Komoditas',data10['Attribut'])
    bulan_data_attribut_cabe_besar = data10[data10['Attribut'] == select]
    #select_status = st.sidebar.radio("Data terpilah sesuai Attribut", ('Sawah', 'Tegal', 'Beras', 'konsumsi', 'Surplus'))
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'bulan':['Januari', 'Februari', 'Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],
         'kuantitas':(dataset.iloc[0]['Januari'],
          dataset.iloc[0]['Februari'],
          dataset.iloc[0]['Maret'], 
          dataset.iloc[0]['April'],
          dataset.iloc[0]['Mei'],
          dataset.iloc[0]['Juni'],
          dataset.iloc[0]['Juli'],
          dataset.iloc[0]['Agustus'],
          dataset.iloc[0]['September'],
          dataset.iloc[0]['Oktober'],
          dataset.iloc[0]['November'],
          dataset.iloc[0]['Desember'],
          )})
         return total_dataframe
    bulan_total_cabe_besar = get_total_dataframe(bulan_data_attribut_cabe_besar)
    if st.sidebar.checkbox("Show Analysis by Attribut", True, key=14):
    #     st.markdown("### Attribut Komoditas: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=15):
         if st.checkbox('2. Grafik Data Bulanan Cabe Besar'):
          st.markdown("### Attribut Komoditas: %s" % (select))
          bulan_total_cabe_besar_graph = px.bar(
             bulan_total_cabe_besar, 
             x='bulan',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='bulan')
          st.plotly_chart(bulan_total_cabe_besar_graph)
    # =============================================================================         
             
    def get_table():
         datatable = data4[['Bulan', 'Luas_Tanam_ha', 'Produksi_ton','Kebutuhan_ton','Surplus_Cabe_Besar_ton']]
         datatable = datatable[datatable['Bulan'] != 'State Unassigned']
         return datatable
    datatable4 = get_table()
    
    if st.checkbox('3. Show raw data Cabe Besar'):
        st.subheader('Raw data Cabe Besar')
        st.dataframe(datatable4) # will display the dataframe
    #    st.table(datatable4)# will display the table
        
    if st.checkbox('4. Show line chart data Cabe Besar'):
        st.subheader('Line Chart data Cabe Besar')
        st.line_chart(data16)
        
# ==5. Bawang Merah ===========================================================================
def bawangmerah_visual():
    import streamlit as st
    import pandas as pd
    import plotly.express as px 
    
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019.xls') as xls:
         data5 = pd.read_excel(xls, 'data_ltt_produksi_bawang_merah')
    with pd.ExcelFile('data_pertanian_2019.xls') as xls:
         data11 = pd.read_excel(xls, 'data_bawang_merah_2019')
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019_tanpa_total.xls') as xls:
         data17 = pd.read_excel(xls, 'data_ltt_produksi_bawang_merah')   
    
    data5 = data5.astype(str)
    data17 = data17.astype(str)
    
    st.write('Wilayah Kabupaten Malang, Tahun 2019')    
#    st.sidebar.title('5.a. Produksi Bawang Merah,')
    select = st.sidebar.selectbox('Pilih Bulan, Jan-Des, atau total 1 tahunan', data5['Bulan'])
    bulan_data_bawang_merah=data5[data5['Bulan'] == select]
    
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'status':['Luas Tanam (ha)','Produksi (ton)','Kebutuhan (ton)', 'Surplus_Bawang_Merah_ton'],
         'kuantitas':(
          dataset.iloc[0]['Luas_Tanam_ha'], 
          dataset.iloc[0]['Produksi_ton'],
          dataset.iloc[0]['Kebutuhan_ton'], 
          dataset.iloc[0]['Surplus_Bawang_Merah_ton'], 
          )})
         return total_dataframe
    bulan_total_bawang_merah = get_total_dataframe(bulan_data_bawang_merah)
    
    if st.sidebar.checkbox("Show Analysis by Komoditas Bawang Merah", True, key=8):
#         st.title("5. Data Bawang Merah.")
    #     st.markdown("### Bulan: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=9):
         if st.checkbox('1. Data Tanam dan Produksi bawang Merah'):
            st.markdown("### Bulan: %s" % (select))
            bulan_total_bawang_merah_graph = px.bar(
              bulan_total_bawang_merah, 
              x='status',
              y='kuantitas',
              labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
              color='kuantitas')
            st.plotly_chart(bulan_total_bawang_merah_graph)
       
    # =============================================================================
#    st.sidebar.title('5.b.Data Tahunan Bawang Merah,')
    #st.sidebar.checkbox("Data terpilah sesuai Komoditas", True, key=11)
    select = st.sidebar.selectbox('Pilih Attribut Komoditas',data11['Attribut'])
    bulan_data_attribut_bawang_merah = data11[data11['Attribut'] == select]
    #select_status = st.sidebar.radio("Data terpilah sesuai Attribut", ('Sawah', 'Tegal', 'Beras', 'konsumsi', 'Surplus'))
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'bulan':['Januari', 'Februari', 'Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],
         'kuantitas':(dataset.iloc[0]['Januari'],
          dataset.iloc[0]['Februari'],
          dataset.iloc[0]['Maret'], 
          dataset.iloc[0]['April'],
          dataset.iloc[0]['Mei'],
          dataset.iloc[0]['Juni'],
          dataset.iloc[0]['Juli'],
          dataset.iloc[0]['Agustus'],
          dataset.iloc[0]['September'],
          dataset.iloc[0]['Oktober'],
          dataset.iloc[0]['November'],
          dataset.iloc[0]['Desember'],
          )})
         return total_dataframe
    bulan_total_bawang_merah = get_total_dataframe(bulan_data_attribut_bawang_merah)
    if st.sidebar.checkbox("Show Analysis by Attribut", True, key=16):
    #     st.markdown("### Attribut Komoditas: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=17):
       if st.checkbox('2. Grafik Data Bulanan Bawang Merah'):
          st.markdown("### Attribut Komoditas: %s" % (select))
          bulan_total_bawang_merah_graph = px.bar(
             bulan_total_bawang_merah, 
             x='bulan',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='bulan')
          st.plotly_chart(bulan_total_bawang_merah_graph)
    # =============================================================================            
             
    def get_table():
         datatable = data5[['Bulan', 'Luas_Tanam_ha', 'Produksi_ton','Kebutuhan_ton','Surplus_Bawang_Merah_ton']]
         datatable = datatable[datatable['Bulan'] != 'State Unassigned']
         return datatable
    datatable5 = get_table()
    
    if st.checkbox('Show raw data Bawang Merah'):
        st.subheader('3. Raw data Bawang Merah')
        st.dataframe(datatable5) # will display the dataframe
    #    st.table(datatable5)# will display the table    
        
    if st.checkbox('4. Show line chart data Bawang Merah'):
        st.subheader('Line Chart data Baang Merah')
        st.line_chart(data17)

# ==6. Bawang Putih ===========================================================================
def bawangputih_visual():
    import streamlit as st
    import pandas as pd
    import plotly.express as px 
    
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019.xls') as xls:
         data6 = pd.read_excel(xls, 'data_ltt_produksi_bawang_putih')
    with pd.ExcelFile('data_pertanian_2019.xls') as xls:
         data12 = pd.read_excel(xls, 'data_bawang_putih_2019')
    with pd.ExcelFile('data_ltt_produksi_pertanian_2019_tanpa_total.xls') as xls:
         data18 = pd.read_excel(xls, 'data_ltt_produksi_bawang_putih') 
         
    data18 = data18.astype(str) 
    
    st.write('Wilayah Kabupaten Malang, Tahun 2019')    
#    st.sidebar.title('6.a. Produksi Bawang Putih,')
    select = st.sidebar.selectbox('Pilih Bulan, Jan-Des, atau total 1_tahun', data6['Bulan'])
    bulan_data_bawang_putih=data6[data6['Bulan'] == select]
    
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'status':['Luas Tanam (ha)','Produksi (ton)','Kebutuhan (ton)', 'Surplus_Bawang_Putih_ton'],
         'kuantitas':(
          dataset.iloc[0]['Luas_Tanam_ha'], 
          dataset.iloc[0]['Produksi_ton'],
          dataset.iloc[0]['Kebutuhan_ton'], 
          dataset.iloc[0]['Surplus_Bawang_Putih_ton'], 
          )})
         return total_dataframe
    bulan_total_bawang_putih = get_total_dataframe(bulan_data_bawang_putih)
    if st.sidebar.checkbox("Show Analysis by Komoditas Bawang Merah", True, key=9):
#        st.title("6. Data Bawang Putih.")
    #     st.markdown("### Bulan: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=10):
         if st.checkbox('1. Data Luas Tanam dan Produksi Bawang Putih'):
           st.markdown("### Bulan: %s" % (select))
           bulan_total_bawang_putih_graph = px.bar(
              bulan_total_bawang_putih, 
              x='status',
              y='kuantitas',
              labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
              color='kuantitas')
           st.plotly_chart(bulan_total_bawang_putih_graph)
             
    # =============================================================================
#    st.sidebar.title('6.b.Data Tahunan Bawang Putih,')
    #st.sidebar.checkbox("Data terpilah sesuai Komoditas", True, key=11)
    select = st.sidebar.selectbox('Pilih Attribut Komoditas',data12['Attribut'])
    bulan_data_attribut_bawang_putih = data12[data12['Attribut'] == select]
    #select_status = st.sidebar.radio("Data terpilah sesuai Attribut", ('Sawah', 'Tegal', 'Beras', 'konsumsi', 'Surplus'))
    def get_total_dataframe(dataset):
         total_dataframe = pd.DataFrame({
         'bulan':['Januari', 'Februari', 'Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],
         'kuantitas':(dataset.iloc[0]['Januari'],
          dataset.iloc[0]['Februari'],
          dataset.iloc[0]['Maret'], 
          dataset.iloc[0]['April'],
          dataset.iloc[0]['Mei'],
          dataset.iloc[0]['Juni'],
          dataset.iloc[0]['Juli'],
          dataset.iloc[0]['Agustus'],
          dataset.iloc[0]['September'],
          dataset.iloc[0]['Oktober'],
          dataset.iloc[0]['November'],
          dataset.iloc[0]['Desember'],
          )})
         return total_dataframe
    bulan_total_bawang_putih = get_total_dataframe(bulan_data_attribut_bawang_putih)
    if st.sidebar.checkbox("Show Analysis by Attribut", True, key=18):
    #     st.markdown("### Attribut Komoditas: %s" % (select))
    #     if not st.checkbox('Hide Graph', False, key=19):
          if st.checkbox('2. Grafik Data Bulanan Bawang Putih'):
           st.markdown("### Attribut Komoditas: %s" % (select))
           bulan_total_bawang_putih_graph = px.bar(
             bulan_total_bawang_putih, 
             x='bulan',
             y='kuantitas',
             labels={'Number of cases':'Number of cases in %s' % 
                    (select)},
             color='bulan')
           st.plotly_chart(bulan_total_bawang_putih_graph)
    # =============================================================================           
    
    def get_table():
         datatable = data6[['Bulan', 'Luas_Tanam_ha', 'Produksi_ton','Kebutuhan_ton','Surplus_Bawang_Putih_ton']]
         datatable = datatable[datatable['Bulan'] != 'State Unassigned']
         return datatable
    datatable6 = get_table()
    
    if st.checkbox('Show raw data Bawang Putih'):
        st.subheader('3. Raw data Bawang Putih')
        st.dataframe(datatable6) # will display the dataframe
    #    st.table(datatable6)# will display the table    
    
    if st.checkbox('4. Show line chart data Bawang Putih'):
        st.subheader('Line Chart data Baang Putih')
        st.line_chart(data18)
        

