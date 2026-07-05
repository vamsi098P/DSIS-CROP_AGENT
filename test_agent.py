from core.agent_service import AgriMindAgent


def main():

    agent = AgriMindAgent()

    result = agent.analyze(
        nitrogen=90,
        phosphorus=42,
        potassium=43,
        temperature=20,
        humidity=82,
        ph=6.5,
        rainfall=202
    )

    print("\n" + "=" * 60)
    print("🌾 AGRIMIND AI - CROP RECOMMENDATION REPORT")
    print("=" * 60)

    print(f"\n🌱 Recommended Crop : {result['recommended_crop']}")

    print(f"📊 Confidence Score : {result['confidence']}%")

    print("\n🌾 Fertilizer Recommendation")
    print("-" * 60)

    fertilizer = result["fertilizer"]

    print("Recommended Fertilizers:")

    for item in fertilizer["fertilizers"]:
        print(f"  • {item}")

    if "application_stage" in fertilizer:
        print("\nApplication Stages:")

        for stage in fertilizer["application_stage"]:
            print(f"  • {stage}")

    if "description" in fertilizer:
        print("\nDescription:")
        print(f"  {fertilizer['description']}")

    print("\n💧 Irrigation Recommendation")
    print("-" * 60)

    irrigation = result["irrigation"]

    print(f"Method            : {irrigation['method']}")
    print(f"Frequency         : {irrigation['frequency']}")
    print(f"Water Requirement : {irrigation['water_requirement']}")
    print(f"Description       : {irrigation['description']}")

    print("\n" + "=" * 60)
    print("✅ AI Analysis Completed Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()