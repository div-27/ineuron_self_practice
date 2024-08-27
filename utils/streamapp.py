import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set up the title of the app
st.title("Simple Streamlit App")

# Add a text input widget
user_input = st.text_input("Enter some text:")

# Add a slider widget
slider_value = st.slider("Select a number", min_value=0, max_value=100, value=25)

# Display user input and slider value
st.write(f"You entered: {user_input}")
st.write(f"Slider value: {slider_value}")

# Generate some data
data = {
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100)) * slider_value
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the data
st.subheader("Data Plot")
fig, ax = plt.subplots()
ax.plot(df['x'], df['y'])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Sine Wave')

# Display the plot
st.pyplot(fig)

# Display the DataFrame
st.subheader("Data Table")
st.dataframe(df)
