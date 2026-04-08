import pandas as pd
from sklearn.linear_model import LinearRegression

# Dummy training dataset
data = pd.DataFrame({
    "length": [5, 6, 7, 8, 10, 12],
    "price": [3000, 5000, 7000, 9000, 15000, 20000]
})

# Train model
model = LinearRegression()
model.fit(data[["length"]], data["price"])


def predict_price(name: str):
    name = name.lower()

    # Convert product name → feature
    if "iphone" in name:
        length = 10
    elif "laptop" in name:
        length = 12
    elif "headphone" in name:
        length = 5
    else:
        length = 6

    prediction = model.predict([[length]])

    return int(prediction[0])