import numpy as np

def calculate_rmse(y_pred, y_actual):
    y_pred = np.array(y_pred)
    y_actual = np.array(y_actual)
    mse = np.mean((y_pred - y_actual)**2)
    rmse = np.sqrt(mse)
    return rmse

def calculate_mae(y_pred, y_actual):
    y_pred = np.array(y_pred)
    y_actual = np.array(y_actual)
    mae = np.mean(np.abs(y_pred - y_actual))
    return mae

# Example usage
y_pred = [100, 200, 300, 400]
y_actual = [110, 220, 310, 380]

rmse = calculate_rmse(y_pred, y_actual)
mae = calculate_mae(y_pred, y_actual)

print("RMSE:", rmse)
print("MAE:", mae)
