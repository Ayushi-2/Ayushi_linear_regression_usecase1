# Final model - Separate independent features and target variable 

def separate_data_and_target_new(df):
    X,y = np.ndarray([]),np.ndarray([])
    
    # Code starts here
    # Extract feature variables X by dropping 'ln_selling_price' and 'selling_price' columns
    X = df.drop(columns = ['ln_selling_price', 'selling_price'], axis=1)
    
    # Extract target variable y by selecting only the 'ln_selling_price' column
    y = df['ln_selling_price']
   
    # Code ends here
    return X,y

X, y = separate_data_and_target_new(cleaned_car_sales)

# split into training and testing 
X_train, X_test,y_train,y_test=split_into_train_and_test_normalize_features(X,y)

final_model=fit_the_model_on_the_training_data(cleaned_car_sales,X_train,y_train)