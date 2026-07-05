from data.irrigation_data import IRRIGATION_DATA


class IrrigationService:

    def get_irrigation(self, crop):

        crop = crop.lower()

        return IRRIGATION_DATA.get(
            crop,
            {
                "method": "Unknown",
                "frequency": "Unknown",
                "water_requirement": "Unknown",
                "description": "No irrigation recommendation available."
            }
        )