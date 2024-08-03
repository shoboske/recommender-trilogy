# Get a list of all product ids
product_ids = data.df['Product'].unique()

# Get the list of products the user has already purchased
user_id = 'specific_user_id'
user_purchased_products = data.df[data.df['Order ID'] == user_id]['Product']

# Predict ratings for all products the user hasn't purchased yet
predictions = [algo.predict(user_id, product_id) for product_id in product_ids if product_id not in user_purchased_products]

# Sort predictions by estimated rating
predictions.sort(key=lambda x: x.est, reverse=True)

# Get top 10 recommendations
top_10_recommendations = predictions[:10]

# Print the recommended products
for prediction in top_10_recommendations:
    print(f'Product: {prediction.iid}, Estimated Rating: {prediction.est}')