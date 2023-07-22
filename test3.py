import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Interactive Plot")
x = np.linspace(0, 10, 100)
freq = st.slider("Frequency", 1, 10, 2)
y = np.sin(freq * x)

plt.plot(x, y)
st.pyplot(plt)
