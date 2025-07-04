import pandas as pd
import random
from datetime import datetime, timedelta

# List to store rows
rows = []
start_time = datetime(2025, 1, 1, 0, 0, 0)

# Generate 100 rows of data
for i in range(100):
    timestamp = start_time + timedelta(minutes=i)
    
    # Simulate normal readings
    temperature = round(random.uniform(72, 85), 1)
    vibration = round(random.uniform(0.01, 0.07), 2)
    voltage = round(random.uniform(2.8, 3.5), 2)

    # Failures occur only with high temp + vibration
    if temperature > 80 and vibration > 0.05:
        failure = 1  # Failure
    else:
        failure = 0  # Normal

    rows.append([timestamp, temperature, vibration, voltage, failure])

# Create DataFrame
df = pd.DataFrame(rows, columns=['timestamp', 'temperature', 'vibration', 'voltage', 'failure'])

# Save to CSV
df.to_csv('data/space_data.csv', index=False)

print("100 rows of space failure data generated successfully.")
