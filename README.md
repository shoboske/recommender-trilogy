# E-commerce Recommendation Engine

This repository contains the code for an AI-powered recommendation engine for an e-commerce platform. The engine provides personalized product recommendations based on user behavior and product information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shoboske/recommender-trilogy.git
   cd recommender-trilogy
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Preprocess the data:
   ```bash
   python process_data.py
   ```

2. Train the model:
   ```bash
   python train_model.py
   ```

3. Generate recommendations:
   ```bash
   python make_predictions.py
   ```

## Evaluation

To evaluate the performance of the recommendation engine, run:
```bash
python evaluation.py
```

This will output metrics such as RMSE.

## Data

The dataset used for this project is included in the `data` directory. and was sourced from [E-commerce-Sales-Analysis](https://github.com/iamnaofil/E-commerce-Sales-Analysis/blob/main/Sales%20Data%20Analysis.csv) You can replace it with your own dataset if needed.