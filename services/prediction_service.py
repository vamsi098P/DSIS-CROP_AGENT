import os
import joblib
import pandas as pd


class CropPredictionService:
    """
    Crop Prediction Engine
    Loads the trained ML model and predicts the best crop.
    """

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))

        model_path = os.path.join(BASE_DIR, "models", "crop_model.pkl")
        encoder_path = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

        self.model = joblib.load(model_path)
        self.encoder = joblib.load(encoder_path)

    def predict_crop(
        self,
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ):

        input_df = pd.DataFrame(
            [[
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                ph,
                rainfall
            ]],
            columns=[
                "N",
                "P",
                "K",
                "temperature",
                "humidity",
                "ph",
                "rainfall"
            ]
        )

        # Prediction
        prediction = self.model.predict(input_df)

        # Confidence Score
        probabilities = self.model.predict_proba(input_df)

        confidence = round(max(probabilities[0]) * 100, 2)

        crop = self.encoder.inverse_transform(prediction)

        return {
            "crop": str(crop[0]),
            "confidence": confidence
        }