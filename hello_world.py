import streamlit as st
st.title('Hello, World!')
st.write('Welcome to Streamlit!')
st.button('Click me!')

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]}
df = pd.DataFrame(data)     
st.table(df)
#add a line chart using numpy
# import numpy as np
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a
#   
#   
#  b', 'c'])
# st.line_chart(chart_data)
# add a map using random data   
import numpy as np
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(map_data)
#add a slider
age = st.slider('Select your age', 0, 100, 25)
st.write('Your age is:', age)