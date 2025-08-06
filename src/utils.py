import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    """
    Saves a Python object to a file using dill, creating directories if they don't exist.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Object saved successfully at: {file_path}")

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Trains multiple models, evaluates their performance, and returns a report.
    """
    try:
        report = {}

        # Use .items() for a much cleaner and more efficient loop
        for name, model in models.items():
            # Fit the model
            model.fit(X_train, y_train)

            # Make predictions
            y_test_pred = model.predict(X_test)

            # Calculate R2 score on the test set
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the test score in the report
            report[name] = test_model_score
            
            # (Optional but Recommended) Log the training score to check for overfitting
            y_train_pred = model.predict(X_train)
            train_model_score = r2_score(y_train, y_train_pred)
            logging.info(f"Model: {name} | Train Score: {train_model_score:.4f} | Test Score: {test_model_score:.4f}")

        return report

    except Exception as e:
        raise CustomException(e, sys)
            