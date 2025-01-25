# Anime Episodes Predictor

A simple web application built using Streamlit that predicts the number of episodes of an anime based on the given inputs, such as the anime's score and total duration in minutes. The model is trained using a machine learning algorithm and deployed with Streamlit for easy user interaction.

## Features

- **Predict the Number of Episodes**: Users can input the anime's score and total duration in minutes to predict the number of episodes.
- **Interactive UI**: The app provides an easy-to-use interface for users to input their data and view predictions.
- **Model Integration**: The app loads a pre-trained machine learning model (`model.pkl`) to make predictions based on user input.

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **scikit-learn**: For machine learning and model training.
- **pickle**: For serializing and loading the pre-trained model.

## Prerequisites

To run this application, you'll need to have the following installed:

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Anime_Episodes_Predictor.git
   cd Anime_Episodes_Predictor
