from services.gemini_service import GeminiService

gemini = GeminiService()

text = gemini.generate_explanation(
    crop="Rice",
    confidence=98,
    fertilizer={
        "fertilizers": [
            "Urea",
            "DAP",
            "MOP"
        ]
    },
    irrigation={
        "method":"Flood Irrigation",
        "frequency":"Every 2-3 days",
        "water_requirement":"High"
    }
)

print(text)