# Gemini API – AI-Powered Data & Automation Platform

A production-style Python system that integrates Google Gemini into real data engineering and automation workflows.
This project demonstrates how Large Language Models (LLMs) can be used as intelligent data processing engines, not just chatbots.

🚀 What this project does
This system provides:
1) Secure Gemini API integration using environment variables 
2) Modular prompt and response pipeline 
3) AI-powered CSV data cleaning (ETL use-case) 
4) Reproducible setup using requirements.txt 
5) Production-grade folder structure 

It can be used to:
1) Clean messy datasets
2) Generate insights from data
3) Automate business reporting
4) Build AI-driven ETL pipelines

🧠 Architecture
```
User / CSV
     |
     v
Prompt Engine → Gemini API → Response Parser
     |
     v
 Cleaned Data / AI Output
```


 📁 Project Structure
```
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
```

🔐 Environment Setup: Create a .env file in the project root
```
GEMINI_API_KEY=your_api_key_here
```

⚙ Installation
```
git clone https://github.com/sakshikirmathe/gemini-api-prompt.git
cd gemini-api-prompt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```


▶ Run Interactive AI
```
python src/main.py
```
Enter your prompt: Explain ETL in simple terms (For Eg.)


📊 AI-Powered CSV Cleaning (ETL)
```
Place a dirty CSV on your Desktop: dirty_data.csv
Then run: python examples/csv_cleaner.py
```

It will:
1) Read the CSV
2) Send it to Gemini
3) Clean and standardize the data
4) Save cleaned_data.csv to your Desktop
5) This simulates a real AI-driven data pipeline.

💡 Why this project matters
It shows how LLMs can be used for:
Data Engineering, ETL pipelines, Automation, AI-powered analytics

This architecture mirrors how AI is used in modern consulting and engineering teams.

🧑‍💻Author
```
Sakshi Kirmathe
Automation Engineer → Data Engineering & AI
```
