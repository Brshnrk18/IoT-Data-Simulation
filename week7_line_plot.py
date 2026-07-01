"""
Week 7: Line Plot of IoT Sensor Readings Over Time
MO-IT148 - Application Development and Emerging Technologies
Practice: Generating Charts
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ── Step 1: Load and Structure IoT Sensor Data ────────────────────────────────
df = pd.read_csv("cleaned_iot_data.csv")

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Display first few rows to verify data
print("=== Dataset Preview ===")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nData Types:\n{df.dtypes}")

# ── Step 2: Analyze the Dataset ───────────────────────────────────────────────
print("\n=== Dataset Analysis ===")
print(f"Temperature Range: {df['numeric_value'].min():.2f}°C – {df['numeric_value'].max():.2f}°C")
print(f"Average Temperature: {df['numeric_value'].mean():.2f}°C")
print(f"Time Range: {df['timestamp'].min()} → {df['timestamp'].max()}")
print(f"\nPackage Status Distribution:\n{df['data_type'].value_counts()}")

# ── Step 3: Visualize – Line Plot (Original Data) ─────────────────────────────
sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(
    x=df["timestamp"],
    y=df["numeric_value"],
    hue=df["data_type"],
    marker="o"
)
plt.xticks(rotation=45)
plt.title("IoT Sensor Readings Over Time", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Sensor Value (°C)", fontsize=12)
plt.legend(title="Package Status")
plt.tight_layout()
plt.savefig("week7_original_lineplot.png", dpi=150)
plt.show()
print("✅ Original line plot saved as week7_original_lineplot.png")

# ── Step 4: Trend Analysis ────────────────────────────────────────────────────
print("\n=== Trend Analysis ===")
# Calculate rolling average to identify trend
df_sorted = df.sort_values("timestamp").reset_index(drop=True)
df_sorted["rolling_avg"] = df_sorted["numeric_value"].rolling(window=10).mean()

# Check if temperature increases or decreases over time
first_half_avg = df_sorted["numeric_value"][:50].mean()
second_half_avg = df_sorted["numeric_value"][50:].mean()
print(f"First 50 records avg temperature: {first_half_avg:.2f}°C")
print(f"Last 50 records avg temperature:  {second_half_avg:.2f}°C")
if second_half_avg > first_half_avg:
    print("📈 Trend: Temperature increases over time")
else:
    print("📉 Trend: Temperature decreases over time")

# ── Step 5: Modify – Introduce Sudden Temperature Anomaly ─────────────────────
df_modified = df_sorted.copy()

# Inject a sudden temperature spike at record 50
spike_index = 50
original_value = df_modified.loc[spike_index, "numeric_value"]
df_modified.loc[spike_index, "numeric_value"] = 75.0  # Sudden spike to 75°C
print(f"\n=== Anomaly Injection ===")
print(f"Injected spike at record {spike_index}: {original_value:.2f}°C → 75.0°C")

# ── Step 6: Compare Original vs Modified ─────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Original plot
axes[0].plot(df_sorted["timestamp"], df_sorted["numeric_value"],
             color="steelblue", marker="o", markersize=3, linewidth=1.5, label="Temperature (°C)")
axes[0].plot(df_sorted["timestamp"], df_sorted["rolling_avg"],
             color="orange", linewidth=2, linestyle="--", label="Rolling Avg (10)")
axes[0].set_title("Original IoT Sensor Readings", fontsize=13)
axes[0].set_xlabel("Timestamp", fontsize=11)
axes[0].set_ylabel("Temperature (°C)", fontsize=11)
axes[0].legend()
axes[0].tick_params(axis="x", rotation=45)

# Modified plot with anomaly
axes[1].plot(df_modified["timestamp"], df_modified["numeric_value"],
             color="crimson", marker="o", markersize=3, linewidth=1.5, label="Temperature (°C)")
axes[1].axvline(x=df_modified.loc[spike_index, "timestamp"],
                color="black", linestyle="--", linewidth=1.5, label=f"Anomaly at record {spike_index}")
axes[1].annotate("⚠ Sudden Spike\n75°C",
                 xy=(df_modified.loc[spike_index, "timestamp"], 75),
                 xytext=(df_modified.loc[spike_index - 5, "timestamp"], 68),
                 fontsize=9, color="black",
                 arrowprops=dict(arrowstyle="->", color="black"))
axes[1].set_title("Modified IoT Sensor Readings (With Anomaly Injected)", fontsize=13)
axes[1].set_xlabel("Timestamp", fontsize=11)
axes[1].set_ylabel("Temperature (°C)", fontsize=11)
axes[1].legend()
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("week7_comparison_lineplot.png", dpi=150)
plt.show()
print("✅ Comparison plot saved as week7_comparison_lineplot.png")

print("\n=== Summary ===")
print("Original dataset: No anomalies, temperature range 11–35°C")
print("Modified dataset: Spike injected at record 50 (75°C)")
print("Observation: Sudden anomalies are immediately visible in line plots,")
print("             making them ideal for detecting sensor failures or equipment issues.")
