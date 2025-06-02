# 💬 CryptoBuddy: A Rule-Based Crypto Investment Chatbot 🤖💰🌱

## Overview

**CryptoBuddy** is a beginner-friendly, rule-based chatbot built in Python that analyzes cryptocurrency data and provides personalized investment recommendations. It evaluates digital assets based on **profitability** (e.g., price trends, market capitalization) and **sustainability** (e.g., energy use, eco-scores), then responds conversationally to user queries.

This chatbot mimics basic **AI decision-making** using conditional logic, giving users tailored advice based on predefined metrics. It’s designed to help crypto enthusiasts, investors, and students understand how even simple AI techniques can be applied to real-world decision support systems.

---

## 🎯 Features

- ✅ Conversational chatbot interface
- 📊 Crypto recommendation based on **price trend**, **market cap**, and **sustainability score**
- 🌱 Sustainability-aware investment advice
- 🔍 Keyword detection and rule-based responses
- ⚠️ Risk disclaimer built-in
- 🐍 Built with basic Python (`if-else` logic)
- 📁 Lightweight and beginner-friendly – no external dependencies required

---

## 📌 Chatbot Personality

- **Name:** CryptoBuddy  
- **Tone:** Friendly, informative, and supportive  
- **Intro Message:**  
  > 👋 Hi, I’m *CryptoBuddy* – your friendly crypto assistant!  
  > Let’s help you pick a profitable and sustainable crypto! 🚀🌱  

---

## 🗃️ Dataset

The chatbot uses a **predefined dictionary** as its knowledge base:

```python
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}
```
## 🧠 Decision Rules
### 📈 Profitability Rule
Coins are considered profitable if:

price_trend == "rising"

market_cap == "high"

## 🌱 Sustainability Rule
Coins are considered sustainable if:

energy_use == "low"

sustainability_score > 7

## 🔀 Rule-Based Logic
User queries are matched using keyword detection and routed to appropriate logic blocks:

“sustainable” → Recommend coin with highest sustainability score

“trending” or “rising” → List coins with rising price trends

“long-term” or “growth” → Find coin with rising trend + high sustainability

“buy” → Find coin with rising trend + high market cap

“help” → Show available query suggestions

## 🧪 Sample Interaction
👋 Hi, I’m *CryptoBuddy* – your friendly crypto assistant!
Let’s help you pick a profitable and sustainable crypto! 🚀🌱

Ask me something about crypto: which crypto is trending up?
📈 These cryptos are trending up: Bitcoin, Cardano

Ask me something about crypto: what’s the most sustainable coin?
🌱 Go with Cardano! It’s eco-friendly with a sustainability score of 8/10.

Ask me something about crypto: which crypto should I buy for long-term growth?
🚀 Cardano is trending up and is sustainable for long-term growth!

Ask me something about crypto: which crypto should I buy?
💰 Based on profit trends, consider buying Bitcoin.

Ask me something about crypto: help
🆘 Try asking: 'Which crypto is trending up?', 'What is the most sustainable coin?', or 'Which crypto should I buy for long-term growth?'

## 💻 How to Run
Clone this repository or download the script.

Run the Python file:
python crypto_chatbot.py
Interact with the chatbot by typing queries like:

"Which crypto is trending?"
"What is the most sustainable coin?"
"Which crypto should I buy for long-term growth?"
"Help"

"Exit"

## 📸 Screenshots
📷 Include screenshots of your conversation for submission. Suggested:

Welcome message
Query about sustainability
Long-term investment advice
Exit message

## 📄 50-Word Summary
This chatbot mimics basic AI decision-making using rule-based logic and keyword matching. It analyzes a crypto dataset to recommend coins based on profitability and sustainability. Through conversational logic and simple data analysis, it demonstrates how even basic AI can support real-world decision-making in finance and investment contexts.

## 📦 Files Included
├── crypto_chatbot.py          # Main Python script
├── README.md                  # This file
├── screenshots/               # Screenshots of chatbot interaction

## ⚠️ Disclaimer
⚠️ Crypto is risky—always do your own research before investing.
CryptoBuddy is a simulated assistant built for educational purposes and does not offer financial advice.

## 📚 Learning Outcomes
Through this project, you’ll learn:

How rule-based AI works
How to design conversational agents
Basics of decision-making using logic
How to analyze structured data for trends and patterns

## 🚀 Stretch Goals (Optional)
🔗 Integrate CoinGecko API for live data

🧠 Add NLP support using NLTK or spaCy
🌍 Add more cryptocurrencies or real-time metrics
📊 Visualize recommendations using graphs or dashboards

## 👨‍💻 Author
Emmanuel Odenyire Anyira
For the PLP Academy – AI Introduction Module
GitHub Profile | LinkedIn | Email

## 🛠️ License
This project is for educational use only under the MIT License.

Let’s build the future, one chatbot at a time! 💬✨


