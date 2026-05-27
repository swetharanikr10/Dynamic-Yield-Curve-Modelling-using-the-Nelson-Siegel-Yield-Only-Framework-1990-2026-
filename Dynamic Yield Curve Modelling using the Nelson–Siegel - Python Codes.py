# Dynamic Yield Curve Modelling using the Nelson–Siegel Yield-Only Framework (1990–2026)


# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Load Dataset

# Replace with your Excel file name
df = pd.read_csv("Data/yield-curve-rates-1990-2026.csv")


df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

yield_columns = [
    '1 Mo','2 Mo','3 Mo','6 Mo',
    '1 Yr','2 Yr','3 Yr',
    '5 Yr','7 Yr','10 Yr',
    '20 Yr','30 Yr'
]

df = df.dropna(subset=yield_columns)

# MATURITIES

maturities = np.array([1/12,2/12,3/12,6/12,1,2,3,5,7,10,20,30])

# NELSON-SIEGEL MODEL

def ns_model(tau, b1, b2, b3, l):
    term1 = (1 - np.exp(-l*tau)) / (l*tau)
    term2 = term1 - np.exp(-l*tau)
    return b1 + b2*term1 + b3*term2

def loss(params, tau, y):
    b1,b2,b3,l = params
    return np.sum((y - ns_model(tau,b1,b2,b3,l))**2)

# ESTIMATION

b1_list, b2_list, b3_list = [], [], []

for i,row in df.iterrows():
    y = row[yield_columns].values.astype(float)

    res = minimize(
        loss,
        [5,-1,1,0.5],
        args=(maturities,y),
        method='L-BFGS-B'
    )

    b1,b2,b3,l = res.x
    b1_list.append(b1)
    b2_list.append(b2)
    b3_list.append(b3)

factors = pd.DataFrame({
    "Date": df["Date"],
    "Level": b1_list,
    "Slope": b2_list,
    "Curvature": b3_list
})

# 1. LEVEL GRAPH

plt.figure(figsize=(14,5))
plt.plot(factors["Date"], factors["Level"])
plt.title("Level Factor (β1)")
plt.grid()
plt.show()

# 2. SLOPE GRAPH

plt.figure(figsize=(14,5))
plt.plot(factors["Date"], factors["Slope"])
plt.title("Slope Factor (β2)")
plt.grid()
plt.show()

# 3. CURVATURE GRAPH

plt.figure(figsize=(14,5))
plt.plot(factors["Date"], factors["Curvature"])
plt.title("Curvature Factor (β3)")
plt.grid()
plt.show()

# 4. COMBINED GRAPH

plt.figure(figsize=(16,6))
plt.plot(factors["Date"], factors["Level"], label="Level")
plt.plot(factors["Date"], factors["Slope"], label="Slope")
plt.plot(factors["Date"], factors["Curvature"], label="Curvature")

plt.title("Nelson-Siegel Factors (Combined)")
plt.legend()
plt.grid()
plt.show()