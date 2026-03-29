import logging
from scripts.extract import fetch_data
from scripts.transform import transform_data

logging.basicConfig(filename="logs/pipeline.log", level=logging.INFO)

def run_pipeline():
    print("🚀 Pipeline started")

    fetch_data()
    print("✅ Extraction done")

    transform_data()
    print("✅ Transformation done")

    print("🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()