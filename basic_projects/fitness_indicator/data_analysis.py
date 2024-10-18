import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Renpho_Health.csv')

# Time
df['Date'] = pd.to_datetime(df['Time of Measurement'])
df = df.sort_values('Date')

# Make plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Weight(kg)'], marker='o')

# Add title and labels 
plt.title('Weight Progress Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Weight (kg)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Save plot
plt.savefig('weight_progress.png', dpi=300, bbox_inches='tight')
plt.close()