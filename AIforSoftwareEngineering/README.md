# 💬 CryptoBuddy: A Rule-Based Crypto Investment Chatbot 🤖💰🌱

## Overview

**CryptoBuddy** is a beginner-friendly, rule-based chatbot built in Python that analyzes cryptocurrency data and provides personalized investment recommendations. It evaluates digital assets based on **profitability** (e.g., price trends, market capitalization) and **sustainability** (e.g., energy use, eco-scores), then responds conversationally to user queries.<br>

This chatbot mimics basic **AI decision-making** using conditional logic, giving users tailored advice based on predefined metrics. It’s designed to help crypto enthusiasts, investors, and students understand how even simple AI techniques can be applied to real-world decision support systems.<br>

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

price_trend == "rising"<br>
market_cap == "high" <br>

## 🌱 Sustainability Rule
Coins are considered sustainable if:

energy_use == "low" <br>
sustainability_score > 7 <br>

## 🔀 Rule-Based Logic
User queries are matched using keyword detection and routed to appropriate logic blocks:
“sustainable” → Recommend coin with highest sustainability score <br>
“trending” or “rising” → List coins with rising price trends <br>
“long-term” or “growth” → Find coin with rising trend + high sustainability <br>
“buy” → Find coin with rising trend + high market cap <br>
“help” → Show available query suggestions <br>

## 🧪 Sample Interaction
👋 Hi, I’m *CryptoBuddy* – your friendly crypto assistant!<br>
Let’s help you pick a profitable and sustainable crypto! 🚀🌱<br>

Ask me something about crypto: which crypto is trending up?<br>
📈 These cryptos are trending up: Bitcoin, Cardano<br>

Ask me something about crypto: what’s the most sustainable coin?<br>
🌱 Go with Cardano! It’s eco-friendly with a sustainability score of 8/10.<br>

Ask me something about crypto: which crypto should I buy for long-term growth?<br>
🚀 Cardano is trending up and is sustainable for long-term growth!<br>

Ask me something about crypto: which crypto should I buy?<br>
💰 Based on profit trends, consider buying Bitcoin.<br>

Ask me something about crypto: help<br>
🆘 Try asking: 'Which crypto is trending up?', 'What is the most sustainable coin?', or 'Which crypto should I buy for long-term growth?'<br>

## 💻 How to Run
Clone this repository or download the script.<br>

Run the Python file:<br>
python crypto_chatbot.py<br>

Interact with the chatbot by typing queries like:<br>
"Which crypto is trending?"<br>
"What is the most sustainable coin?"<br>
"Which crypto should I buy for long-term growth?"<br>
"Help"<br>
"Exit" <br>

## 📸 Screenshots
📷 Include screenshots of your conversation for submission. 
file:///home/hp/Pictures/Screenshots/Screenshot%20from%202025-06-06%2014-23-53.png

video clip 

file:///home/hp/Videos/Screencasts/Screencast%20from%2006-06-2025%2002:25:50%20ALASIRI.webm



Suggested:
- Welcome message
- Query about sustainability
- Long-term investment advice
- Exit message

## 📄 50-Word Summary
This chatbot mimics basic AI decision-making using rule-based logic and keyword matching. It analyzes a crypto dataset to recommend coins based on profitability and sustainability. Through conversational logic and simple data analysis, it demonstrates how even basic AI can support real-world decision-making in finance and investment contexts.<br>

## 📦 Files Included <br>
├── crypto_chatbot.py          # Main Python script<br>
├── README.md                  # This file<br>
├── screenshots/               # Screenshots of chatbot interaction<br>

## ⚠️ Disclaimer
⚠️ Crypto is risky—always do your own research before investing.<br>
CryptoBuddy is a simulated assistant built for educational purposes and does not offer financial advice.<br>

## 📚 Learning Outcomes
Through this project, you’ll learn:<br>
How rule-based AI works <br>
How to design conversational agents <br>
Basics of decision-making using logic <br>
How to analyze structured data for trends and patterns <br>

## 🚀 Stretch Goals (Optional)
🔗 Integrate CoinGecko API for live data <br>
🧠 Add NLP support using NLTK or spaCy <br>
🌍 Add more cryptocurrencies or real-time metrics<br>
📊 Visualize recommendations using graphs or dashboards<br>

## 👨‍💻 Author
Emmanuel Odenyire Anyira<br>
For the PLP Academy – AI Introduction Module<br>
GitHub Profile | LinkedIn | Email<br>

## 🛠️ License
This project is for educational use only under the MIT License. <br>

Let’s build the future, one chatbot at a time! 💬✨<br>


