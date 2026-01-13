import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


import pandas as pd
from src.gemini_client import GeminiClient
from src.prompt_engine import PromptEngine

# Path to CSV on Desktop
csv_path = r"C:\Users\dell\Desktop\dirty_data.csv"

# Read file
df = pd.read_csv(csv_path)

raw_data = df.to_csv(index=False)

# Build AI prompt
engine = PromptEngine()

prompt = engine.build(f"""
You are a data cleaning engine.

Here is a dirty CSV:
{raw_data}

Rules:
1. Remove duplicates
2. Replace missing names with "Unknown"
3. Replace missing salary with 0
4. If a value is invalid (like non-numeric age), set it to NULL
5. Do NOT guess or infer new values

Return ONLY the cleaned CSV.
""")

# Send to Gemini
client = GeminiClient()
cleaned_csv = client.send_prompt(prompt)

# Save output
output_path = r"C:\Users\dell\Desktop\cleaned_data.csv"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(cleaned_csv)

print("Cleaned CSV saved to:", output_path)
