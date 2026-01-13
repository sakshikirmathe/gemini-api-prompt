###Gemini API – AI-Powered Data & Automation Platform

A production-style Python system that integrates Google Gemini into real data engineering and automation workflows.
This project demonstrates how Large Language Models (LLMs) can be used as intelligent data processing engines, not just chatbots.

🚀 What this project does
This system provides:
-Secure Gemini API integration using environment variables
-Modular prompt and response pipeline
-AI-powered CSV data cleaning (ETL use-case)
-Reproducible setup using requirements.txt
-Production-grade folder structure

It can be used to:
-Clean messy datasets
-Generate insights from data
-Automate business reporting
-Build AI-driven ETL pipelines

🧠 Architecture
User / CSV
     |
     v
Prompt Engine → Gemini API → Response Parser
     |
     v
 Cleaned Data / AI Output

 📁 Project Structure
 gemini-api-prompt/
│
├── src/
│   ├── gemini_client.py      # Gemini API wrapper
│   ├── prompt_engine.py     # Prompt construction
│   ├── response_parser.py   # Output processing
│   └── main.py              # CLI app
│
├── examples/
│   └── csv_cleaner.py       # AI-powered CSV ETL pipeline
│
├── .env.example             # Environment variable template
├── requirements.txt        # Dependencies
└── README.md

🔐 Environment Setup
Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here

⚙ Installation
git clone https://github.com/sakshikirmathe/gemini-api-prompt.git
cd gemini-api-prompt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

▶ Run Interactive AI
python src/main.py
Enter your prompt: Explain ETL in simple terms

📊 AI-Powered CSV Cleaning (ETL)
Place a dirty CSV on your Desktop: dirty_data.csv
Then run: python examples/csv_cleaner.py

It will:
-Read the CSV
-Send it to Gemini
-Clean and standardize the data
-Save cleaned_data.csv to your Desktop
This simulates a real AI-driven data pipeline.

💡 Why this project matters
It shows how LLMs can be used for:
-Data Engineering
-ETL pipelines
-Automation
-AI-powered analytics
This architecture mirrors how AI is used in modern consulting and engineering teams.

🧑‍💻Author
Sakshi Kirmathe
Automation Engineer → Data Engineering & AI
