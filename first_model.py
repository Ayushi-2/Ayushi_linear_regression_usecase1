# Build model using OLS

import statsmodels.formula.api as smf
​
def fit_the_model_ols(data):    
    ols_model = None
    train, test = np.ndarray([]),np.ndarray([])
    
    # Code starts here    
    # Split the dataset into train and test
    train, test = train_test_split(data, test_size = 0.2, random_state = 1234)
    
    # Building the OLS model using statsmodels formula API
    formula = "selling_price ~ " + " + ".join(data.columns.drop("selling_price")) 
    ols_model = smf.ols(formula = formula, data = train).fit()
        
    # Return the model and the test data    
    return ols_model,test

# Fit the model
ols_model, test_data = fit_the_model_ols(cleaned_car_sales)

# Get the summary of the fitted model
summary = ols_model.summary()
# Print the summary
summary
