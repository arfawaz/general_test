#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 19:55:01 2025

@author: fawaz
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("TimeSeriesDataProject_2.csv", parse_dates=["date"])
df = df.drop(columns=["date"])

# Split: 60% train, 40% test
train_size = int(len(df) * 0.6)
train_df = df.iloc[:train_size].copy()
test_df = df.iloc[train_size:].copy()

# Z-score Normalization using training stats only
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_df)
test_scaled = scaler.transform(test_df)

train_df = pd.DataFrame(train_scaled, columns=df.columns)
test_df = pd.DataFrame(test_scaled, columns=df.columns)

# ARIMA Forecast function for a single feature
def forecast_arima(train_series, test_series, order=(2, 1, 2), T=96, stride=96):
    predictions = []
    ground_truths = []
    for start in range(0, len(test_series) - T, stride):
        history = list(train_series) + list(test_series[:start])
        model = ARIMA(history, order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=T)
        predictions.append(forecast)
        ground_truths.append(test_series[start:start + T])
    return np.concatenate(predictions), np.concatenate(ground_truths)

# Forecast using ARIMA for each feature
all_preds = []
all_gts = []
for col in df.columns:
    print(f"Running ARIMA for {col}...")
    preds, gts = forecast_arima(train_df[col].values, test_df[col].values, order=(2, 1, 2))
    all_preds.append(preds)
    all_gts.append(gts)

# Concatenate all predictions and ground truths
all_preds = np.concatenate(all_preds)
all_gts = np.concatenate(all_gts)

# Calculate overall MSE
overall_mse = mean_squared_error(all_gts, all_preds)
print(f"\n🔍 Final ARIMA MSE across all features: {overall_mse:.4f}")
