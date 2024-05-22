from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    # Train machine learning model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
