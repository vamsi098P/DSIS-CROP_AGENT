from services.prediction_service import CropPredictionService
from services.fertilizer_service import FertilizerService
from services.irrigation_service import IrrigationService
from services.gemini_service import GeminiService


class AgriMindAgent:
    """
    Main AI Agent
    Handles:
    1. Crop Prediction
    2. Fertilizer Recommendation
    3. Irrigation Recommendation
    4. Gemini AI Explanation
    """

    def __init__(self):

        # Load all AI services only once
        self.predictor = CropPredictionService()
        self.fertilizer = FertilizerService()
        self.irrigation = IrrigationService()
        self.gemini = GeminiService()

    def analyze(
        self,
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ):

        # -----------------------------------
        # Predict Crop
        # -----------------------------------

        prediction = self.predictor.predict_crop(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

        crop = prediction["crop"]
        confidence = prediction["confidence"]

        # -----------------------------------
        # Fertilizer Recommendation
        # -----------------------------------

        fertilizer = self.fertilizer.get_fertilizer(crop)

        # -----------------------------------
        # Irrigation Recommendation
        # -----------------------------------

        irrigation = self.irrigation.get_irrigation(crop)

        # -----------------------------------
        # Gemini AI Explanation
        # -----------------------------------

        ai_explanation = self.gemini.generate_explanation(
            crop=crop,
            confidence=confidence,
            fertilizer=fertilizer,
            irrigation=irrigation
        )

        # -----------------------------------
        # Final AI Response
        # -----------------------------------

        return {

            "recommended_crop": crop,

            "confidence": confidence,

            "fertilizer": fertilizer,

            "irrigation": irrigation,

            "ai_explanation": ai_explanation

        }