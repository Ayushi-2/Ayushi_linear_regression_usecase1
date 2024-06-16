# Build a linear model using sklearn library

from sklearn.linear_model import LinearRegression
​
def fit_the_model_on_the_training_data(data,X_train:np.ndarray,y_train:np.ndarray):
    regression = None
    
    # Code starts here
    regression = LinearRegression()
    # Fit the model to the training data
    regression.fit(X_train, y_train)
    # Code ends here 
    
    return regression

# train the training data 
sklearn_model=fit_the_model_on_the_training_data(cleaned_car_sales,X_train,y_train)
sklearn_model