# Space-Mission-Failure-Prediction-Prototype-

This is a Python-based prototype to **predict failures in space missions** using time-series sensor data such as temperature, vibration, and voltage. The project demonstrates the use of machine learning for early fault detection using simulated telemetry data.

/Objective
To build a simple yet effective AI model that can:
1) Learn from mission sensor readings over time
2) Predict potential failures using historical trends
3) Help improve safety and reliability in critical space systems

/Project Structure
Task_Project
data/
space_data.csv # Auto-generated time-series data (100 rows)
generate_data.py # Script to create realistic failure scenarios
main.py # ML model training, evaluation, and visualization
requirements.txt # Required Python packages
README.md # This documentation file

/Sample dataset features (dummy dataset)
Each row in the dataset represents a moment in time during a mission. Features include:
- timestamp: Time of reading
- temperature: °C
- vibration: Unitless measure of vibration
- voltage: Electrical reading (V)
- failure: 0 = Normal, 1 = Failure

/Output
1) Model Accuracy: ~97% on realistic synthetic data
2) Confusion Matrix & Classification Report
3) Scatter Plot: Temperature vs. Failure visualization

/Technologies Used
Python 3
Pandas
Scikit-learn
Matplotlib   
