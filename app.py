import numpy as np
import pandas as pd
import streamlit as st

def main():
  st.title("Subtraction")
  html_temp = """
  <div style="background-color:blue;padding:10px">
  <h2 style="color:white;text-align:center;">Streamlit Web Application for Subtraction of 2 numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Enter first number:")
  num2 = st.number_input("Enter second number:")
  result = num1 - num2
  st.success('The output is {}'.format(result))

if __name__=='__main__':
  main()
