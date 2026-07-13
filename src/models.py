import os
import logging 
import joblib

class BestModelSaved:
    def __init__(self, model_dir):
        self.model_dir = model_dir
        os.makedirs(model_dir, exist_ok=True)
    
    def save_model(self, best_model, model_name):
        save_path = os.path.join(
            self.model_dir,
            f"{model_name}.pkl"
        )
        try: 
            joblib.dump(best_model, save_path)
            logging.info(f"{model_name} saved successfully!")
        except Exception as e:
            logging.exception(f"Error while saving model: {e}")


