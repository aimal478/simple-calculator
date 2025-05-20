# Step 1: Install streamlit and pyngrok
!pip install streamlit pyngrok --quiet

# Step 2: Write the Streamlit calculator app to a file
%%writefile app.py
import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.write(f"Result: {result}")

# Step 3: Run Streamlit with ngrok tunnel
from pyngrok import ngrok
import subprocess
import time

# Open a tunnel to port 8501
public_url = ngrok.connect(port=8501)
print(f"Streamlit app URL: {public_url}")

# Run Streamlit app in background
command = "streamlit run app.py"
process = subprocess.Popen(command.split())

# Keep the cell alive (optional)
time.sleep(60*10)  # runs for 10 minutes
