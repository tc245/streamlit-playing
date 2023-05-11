import streamlit as st
import numpy as np
import pandas as pd

dataframe = np.random.randn(5,5)
st.dataframe(dataframe)

dataframe2 = {"lat": [50,55,59,49,45, 56], "lon": [3,5,6,8,2,0]}
dataframe2 = pd.DataFrame(dataframe2)

st.text("This is some text.")

st._arrow_line_chart(dataframe)

st.map(dataframe2)

st.text("This is some more text.")

st.button("This is a button.")

