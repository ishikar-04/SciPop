#!/usr/bin/env python
# coding: utf-8
"""
Dashboard for the scraping function
"""

import streamlit as st
import pandas as pd

def _max_width_():
    """
    Display string formatted as Markdown.
    """
    
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

# Configures the default settings of the page.
st.set_page_config(page_icon="🎓", page_title="SCIPOP")

# Display an image with its url.
st.image(
    "https://png.pngitem.com/pimgs/s/202-2021802_graduation-cap-emoji-transparent-hd-png-download.png",
    width=100,
)

# Draw Markdown-formatted text, with input as a string.
st.write(
"""
# SCIPOP APP
Upload your article dataset to see the relevant news.
"""
)

# Display a file uploader widget. Users can drag/drop their input file.
uploaded_file = st.file_uploader("Upload CSV", type=".csv")

# Checkbox of example file to demo the app.
use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)

# Path for example file.
if use_example_file:
    uploaded_file = "UseCase1_Data.csv"
    
# Read and preview input file.    
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head())

sample = {'a':[1, 2, 3],
          'b': ['a', 'b', 'c']}

# Sample output file, need to change to our output file.
output_df = pd.DataFrame(data=sample)

# Display a download button widget for user to get the output file.
st.download_button(
    label="Download data as CSV",
    data=output_df.to_csv().encode('utf-8'),
    file_name='news.csv',
    mime='text/csv',
)

