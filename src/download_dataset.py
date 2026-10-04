from pathlib import Path
import urllib.request

DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "00352/Online%20Retail.xlsx"
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_FILE = DATA_DIR / "Online_Retail.xlsx"

DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading retail business dataset...")

urllib.request.urlretrieve(DATA_URL, OUTPUT_FILE)

print("Dataset downloaded successfully!")
print(f"Saved to: {OUTPUT_FILE}")