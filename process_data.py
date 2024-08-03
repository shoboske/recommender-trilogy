import pandas as pd
from surprise import Dataset, Reader
import pickle

# Load the data
data = pd.read_csv('./data/e_commerce.csv')

# Preprocess the data
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.month
data['Hour'] = data['Order Date'].dt.hour
data['Sales'] = data['Quantity Ordered'] * data['Price Each']

# Define a reader object
reader = Reader(rating_scale=(1, 5))

# Load the data into Surprise dataset
data = Dataset.load_from_df(data[['Order ID', 'Product', 'Sales']], reader)

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)