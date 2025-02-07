import numpy as np
import pandas as pd
import streamlit as st

st.title("Hello World")
st.write("I am smart")

data = pd.DataFrame({'c1' : [1,2,3,4], 'c2' : ['a','b','c','d']})
st.write(data)
#st.button("Dont press", type = "primary")
#if st.button("Say Hello"):
#    st.write("Hello")'''

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['A', 'B', 'C'])

st.bar_chart(chart_data)