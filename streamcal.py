import streamlit as st

# Set up the title of the app
st.title("Simple Streamlit Calculator")

# Add input fields for the calculator
st.write("Enter the values and select the operation:")

# Number inputs
num1 = st.number_input("First number", value=0)
num2 = st.number_input("Second number", value=0)

# Select box for operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate the result based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        # Handle division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    
    st.write(f"Result: {result}")
