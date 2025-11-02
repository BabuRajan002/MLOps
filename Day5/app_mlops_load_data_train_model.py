import ssl
ssl._create_default_https_context = ssl._create_unverified_context  # 🚫 Disable SSL check temporarily

import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

housing = fetch_openml(name="house_prices", as_frame=True)
X = housing.data[["GrLivArea", "YearBuilt"]]
y = housing.target.astype(np.float64)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

GrLivArea = st.number_input('Above grade living area (Sq. Ft.)', value=1500)
YearBuilt = st.number_input('Original construction date', value=2000)
input_data = pd.DataFrame({'GrLivArea': [GrLivArea], 'YearBuilt': [YearBuilt]})

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")
