import pickle
from surprise import SVD, accuracy
from surprise.model_selection import train_test_split

# Load data from a pickle file
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
    
# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25)

# Initialize the SVD algorithm
algo = SVD()

# Train the algorithm on the trainset
algo.fit(trainset)

# Test the algorithm on the testset
predictions = algo.test(testset)

# Compute and print Root Mean Squared Error
accuracy.rmse(predictions)

with open('trained_model.pkl', 'wb') as f:
    pickle.dump(algo, f)
