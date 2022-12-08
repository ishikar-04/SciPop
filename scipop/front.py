from scraper import main
import streamlit as st
import pandas as pd

st.set_page_config(page_icon="🎓", page_title="SCIPOP")

def _max_width_():
    """
    Display string formatted as Markdown.
    """

    max_width_str = "max-width: 1800px;"
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

# Display an image with its url.
st.image(
    "https://png.pngitem.com/pimgs/s/202-2021802_"+
    "graduation-cap-emoji-transparent-hd-png-download.png",
    width=100,
)

# Draw Markdown-formatted text, with input as a string.
st.write(
    """
    # SCIPOP APP
    Upload your article dataset to see the relevant news.\n
    #### Dataset guidance:\n
    Column_Name: Author_Name, Article_Title, Article_DOI. 
    Could see example dataset for reference.
    """
)

# Display a file uploader widget. Users can drag/drop their input file in .csv format.
UPLOADED_FILE = st.file_uploader("Upload CSV", type=".csv")

# Checkbox of example file to demo the app.
use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)

# Path for example file.
if use_example_file:
    UPLOADED_FILE = "../examples/UseCase1_Data.csv"
    
# Read and preview input file.  
if UPLOADED_FILE:
    input_df = pd.read_csv(UPLOADED_FILE)

    st.markdown("### Data preview")
    st.dataframe(input_df.head())

    output_df = main(input_df)
else:
    st.stop()

# Display a download button widget. Users can download their output file in .csv format.
st.download_button(
    label="Download data as CSV",
    data=output_df.to_csv().encode('utf-8'),
    file_name='news.csv',
    mime='text/csv',
)
