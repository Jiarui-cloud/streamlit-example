from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# Randomly fill a dataframe and cache it
@st.cache(allow_output_mutation=True)
def get_dataframe():
    return pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20)))


df = get_dataframe()

# Create row, column, and value inputs
row = st.number_input('row', max_value=df.shape[0])
col = st.number_input('column', max_value=df.shape[1])
value = st.number_input('value')

# Change the entry at (row, col) to the given value
df.values[row][col] = value

# And display the result!
st.dataframe(df)
