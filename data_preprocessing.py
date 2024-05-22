import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(data):
    # Perform data preprocessing steps here
    # Example: 
    # Encode categorical variables
    encoder = LabelEncoder()
    data['gender_encoded'] = encoder.fit_transform(data['gender'])
    
    # Standardize numerical features
    scaler = StandardScaler()
    data['age_scaled'] = scaler.fit_transform(data[['age']])
    
    return data
