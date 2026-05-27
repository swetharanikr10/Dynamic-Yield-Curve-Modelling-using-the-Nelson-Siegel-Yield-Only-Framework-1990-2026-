Dynamic Yield Curve Modelling using Nelson–Siegel Framework (1990–2026)

A comprehensive quantitative analysis of US Treasury yield curve dynamics using the Nelson-Siegel parametric model to decompose complex yield movements into three interpretable latent factors.
Project Overview:
Developed a daily yield curve modeling system that extracts Level (long-term trend), Slope (recession indicator), and Curvature (financial stress) factors from 36 years of Treasury data (1990–2026).
Methodology:

Non-linear least squares optimization (Levenberg-Marquardt algorithm)
Rolling 1-year window daily re-estimation (252 trading days)
Rolling-window forecasting for robust validation
Parameter constraints: 0 < λ < 2 for model stability

Performance Results:

In-sample R² fit: 0.985–0.998 across all maturities
Forecast accuracy: 12–18 basis points MAE
– Short-term (1M–2Y): 10–14 bps
– Medium-term (3Y–10Y): 12–16 bps
– Long-term (20Y–30Y): 15–20 bps
RMSE: 18–28 basis points
Model stability: MAE consistent during volatile periods (2008, 2020, 2022–2023)

