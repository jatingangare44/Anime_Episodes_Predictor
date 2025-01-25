import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', "rb"))

# Streamlit GUI
st.title("Predict Episodes")
st.markdown("Provide the input values to predict the number of episodes.")

# Input fields
score = st.number_input("Score", min_value=0.0, max_value=10.0, step=0.01, format="%.2f", help="Enter the anime score.")
total_duration_minutes = st.number_input("Total Duration (Minutes)", min_value=0, step=1,
                                         help="Enter the total duration in minutes.")

# Prepare input for prediction
if st.button("Predict Episodes"):
    # Combine all inputs into a single feature vector
    features = [score, total_duration_minutes]

    # Convert to numpy array and reshape for model input
    input_data = np.array(features).reshape(1, -1)

    # Predict using the model
    try:
        prediction = model.predict(input_data)
        predicted_value = int(prediction[0])

        if predicted_value < 1:
            predicted_value = 1

        st.success(f"Predicted Episodes: {predicted_value}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
