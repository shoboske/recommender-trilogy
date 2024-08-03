import pickle
from pprint import pprint

# Load data from a pickle file
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
    
with open('trained_model.pkl', 'rb') as f:
    algo = pickle.load(f)

# Get a list of all product ids
product_ids = data.df['Product'].unique()

# Get the list of products the user has already purchased
user_id = input('Enter a user id: ')
user_purchased_products = data.df[data.df['Order ID'] == user_id]['Product']

pprint(data.df[data.df['Order ID'] == 295665]['Product'])

# Predict ratings for all products the user hasn't purchased yet
predictions = [algo.predict(user_id, product_id) for product_id in product_ids if product_id not in user_purchased_products]

# Sort predictions by estimated rating
predictions.sort(key=lambda x: x.est, reverse=True)

# Get top 10 recommendations
top_10_recommendations = predictions

# Print the recommended products
for prediction in top_10_recommendations:
    print(f'Product: {prediction.iid}, Estimated Rating: {prediction.est}')