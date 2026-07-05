from data.fertilizer_data import FERTILIZER_DATA

class FertilizerService:

    def get_fertilizer(self, crop):

        crop = crop.lower()

        return FERTILIZER_DATA.get(
            crop,
            {
                "fertilizers": ["Not Available"],
                "description": "No recommendation found."
            }
        )