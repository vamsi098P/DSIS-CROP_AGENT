from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
import os


class PDFService:

    def generate_report(
        self,
        result,
        weather,
        filename="DSIS CROP AGENT_Report.pdf"
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        title = styles["Title"]
        title.alignment = TA_CENTER
        title.textColor = HexColor("#15803D")

        heading = styles["Heading2"]
        heading.textColor = HexColor("#15803D")

        normal = styles["BodyText"]

        story = []

        # =====================================================
        # Logo
        # =====================================================

        logo_path = "assets/logo.png"

        if os.path.exists(logo_path):

            logo = Image(
                logo_path,
                width=1.0 * inch,
                height=1.0 * inch
            )

            story.append(logo)

        story.append(Spacer(1, 10))

        # =====================================================
        # Title
        # =====================================================

        story.append(
            Paragraph(
                "🌾 DSIS CROP AGENT",
                title
            )
        )

        story.append(
            Paragraph(
                "AI-Powered Smart Crop Recommendation System",
                styles["Heading3"]
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # =====================================================
        # Crop
        # =====================================================

        story.append(
            Paragraph(
                "<b>🌾 Recommended Crop</b>",
                heading
            )
        )

        story.append(
            Paragraph(
                result["recommended_crop"].title(),
                normal
            )
        )

        story.append(
            Paragraph(
                f"<b>Confidence :</b> {result['confidence']:.1f}%",
                normal
            )
        )

        story.append(
            Spacer(1, 15)
        )

        # =====================================================
        # Weather
        # =====================================================

        story.append(
            Paragraph(
                "<b>🌦 Weather</b>",
                heading
            )
        )

        story.append(
            Paragraph(
                f"City : {weather['city']}",
                normal
            )
        )

        story.append(
            Paragraph(
                f"Temperature : {weather['temperature']} °C",
                normal
            )
        )

        story.append(
            Paragraph(
                f"Humidity : {weather['humidity']} %",
                normal
            )
        )

        story.append(
            Paragraph(
                f"Rainfall : {weather['rainfall']} mm",
                normal
            )
        )

        story.append(
            Paragraph(
                f"Condition : {weather['condition']}",
                normal
            )
        )

        story.append(
            Spacer(1, 15)
        )

        # =====================================================
        # Fertilizer
        # =====================================================

        story.append(
            Paragraph(
                "<b>🌱 Fertilizer Recommendation</b>",
                heading
            )
        )

        for fert in result["fertilizer"]["fertilizers"]:

            story.append(
                Paragraph(
                    f"• {fert}",
                    normal
                )
            )

        story.append(
            Spacer(1, 15)
        )

        # =====================================================
        # Irrigation
        # =====================================================

        story.append(
            Paragraph(
                "<b>💧 Irrigation Recommendation</b>",
                heading
            )
        )

        story.append(
            Paragraph(
                f"Method : {result['irrigation']['method']}",
                normal
            )
        )

        story.append(
            Paragraph(
                f"Frequency : {result['irrigation']['frequency']}",
                normal
            )
        )

        story.append(
            Paragraph(
                f"Water Requirement : {result['irrigation']['water_requirement']}",
                normal
            )
        )

        story.append(
            Spacer(1, 15)
        )

        # =====================================================
        # Gemini AI
        # =====================================================

        story.append(
            Paragraph(
                "<b>🤖 AI Expert Recommendation</b>",
                heading
            )
        )

        story.append(
            Paragraph(
                result["ai_explanation"],
                normal
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # =====================================================
        # Footer
        # =====================================================

        story.append(
            Paragraph(
                "<b>Generated by DSIS CROP AGENT</b>",
                styles["Heading3"]
            )
        )

        story.append(
            Paragraph(
                "Developed by Vamsi Garapati",
                normal
            )
        )

        story.append(
            Paragraph(
                "NRI Institute of Technology",
                normal
            )
        )

        story.append(
            Paragraph(
                "Email : vamsigarapati40@gmail.com",
                normal
            )
        )

        # =====================================================
        # Build PDF
        # =====================================================

        doc.build(story)

        return filename