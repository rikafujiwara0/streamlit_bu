import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

#eg1
st.write('Hello, *World!* emoji')

#eg2
st.write(1234)

#eg3
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column':[10,20,30,40]
})
st.write(df)

#eg4
st.write('Velow is a DataFrame:', df, 'Above is a dataframe.')

#eg5

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a','b','c'])
st.write(c)