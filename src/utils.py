import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging

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