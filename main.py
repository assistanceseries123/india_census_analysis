import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#loading the dataset
st.set_page_config(layout='wide',page_title='India Analysis')
df=pd.read_csv('india.csv')
list_of_state=list(df['State'].unique())
list_of_state.insert(0,'Overall india')
selected_state=st.sidebar.selectbox('Select a state',list_of_state)
primary=st.sidebar.selectbox('Primary parameter',df.columns[5:])
secondary=st.sidebar.selectbox('secondary parameter',df.columns[5:])

plot=st.sidebar.button('Plot Graph')
st.text("Size represent primary parameter")
st.text("Color represent secondary parameter")
if plot:
    if selected_state=='Overall india':
        fig=px.scatter_mapbox(df,lat='Latitude',
        lon='Longitude',
        zoom=3,
        size=primary,
        color=secondary,
        size_max=35,
        width=1200,
        height=700,
        mapbox_style='carto-positron',hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
       new_df=df[df['State']==selected_state]
       fig=px.scatter_mapbox(new_df,
       lat='Latitude',
       lon='Longitude',
       zoom=3,
       size=primary,
       color=secondary,
       size_max=35,
       width=1200,
       height=700,
       mapbox_style='carto-positron',hover_name='District')
       st.plotly_chart(fig,use_container_width=True)