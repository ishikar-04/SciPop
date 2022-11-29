#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pandas as pd

#from st_aggrid import AgGrid
#from st_aggrid.grid_options_builder import GridOptionsBuilder
#from st_aggrid.shared import JsCode


#from functionforDownloadButtons import download_button

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="🎓", page_title="SCIPOP")

st.image(
    "https://png.pngitem.com/pimgs/s/202-2021802_graduation-cap-emoji-transparent-hd-png-download.png",
    width=100,
)


st.write(
    """
# SCIPOP APP
Upload your article dataset to see the relevant news.
"""
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)


if use_example_file:
    uploaded_file = "UseCase1_Data.csv"
    
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head())

sample = {'a':[1, 2, 3],
          'b': ['a', 'b', 'c']}
          
output_df = pd.DataFrame(data=sample)

st.download_button(
    label="Download data as CSV",
    data=output_df.to_csv().encode('utf-8'),
    file_name='news.csv',
    mime='text/csv',
)

