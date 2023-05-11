import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

DATA_URL = "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/website/bart-lines.json"
df = pd.read_json(DATA_URL)

st.dataframe(df)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

df['color'] = df['color'].apply(hex_to_rgb)

view_state = pdk.ViewState(
    latitude=37.782556,
    longitude=-122.3484867,
    zoom=10
)

layer = pdk.Layer(
    type='PathLayer',
    data=df,
    pickable=True,
    get_color='color',
    width_scale=20,
    width_min_pixels=2,
    get_path='path',
    get_width=5
)



st.video("http://192.168.0.13/webcam/?action=stream")

r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={'text': '{name}'})

st.button("This is a button.")

w1 = st.checkbox("I am human", True)
st.write(w1)

if w1:
    st.write("Agreed")

st.subheader("Slider")
w2 = st.slider("Age", 0.0, 100.0, (32.5, 72.5), 0.5)
st.write(w2)

st.subheader("Textarea")
w3 = st.text_area("Comments", "Streamlit is awesomeness!")
st.write(w3)

st.subheader("Button")
w4 = st.button("Click me")
st.write(w4)

if w4:
    st.write("Hello, Interactive Streamlit!")

st.subheader("Radio")
options = ("female", "male")
w5 = st.radio("Gender", options, 1)
st.write(w5)

st.subheader("Text input")
w6 = st.text_input("Text input widget", "i iz input")
st.write(w6)

st.subheader("Selectbox")
options = ("first", "second")

st.pydeck_chart(r)