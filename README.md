
RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error) are commonly used evaluation metrics for regression tasks, 
including house price prediction. They provide a measure of the prediction accuracy by quantifying the difference between 
the predicted house prices and the actual house prices in the dataset.

RMSE = sqrt(1/N * sum((y_pred - y_actual)^2))

MAE = 1/N * sum(|y_pred - y_actual|)

To calculate the RMSE and MAE scores for your house price prediction model, follow these steps:

1. Obtain a dataset with both the predicted house prices (y_pred) and the corresponding actual house prices (y_actual).

2. Calculate the squared differences between y_pred and y_actual for each sample and sum them up.

3. Divide the sum by the total number of samples (N).

4. Take the square root of the result to calculate the RMSE score.

5. Calculate the absolute differences between y_pred and y_actual for each sample and sum them up.

6. Divide the sum by the total number of samples (N) to calculate the MAE score.
