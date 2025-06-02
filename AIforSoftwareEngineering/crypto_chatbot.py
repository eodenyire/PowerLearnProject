# crypto_chatbot.py

# Chatbot Introduction
print("👋 Hi, I’m *CryptoBuddy* – your friendly crypto assistant!")
print("Let’s help you pick a profitable and sustainable crypto! 🚀🌱\n")

# Predefined Crypto Data
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

# Helper function to get most sustainable crypto
def get_most_sustainable():
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

# Helper function to get rising cryptos
def get_trending_cryptos():
    return [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]

# Helper function to get best profitable crypto
def get_profitable_crypto():
    for name, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            return name
    return "No profitable crypto found"

# Helper function to get long-term sustainable crypto
def get_long_term_crypto():
    for name, data in crypto_db.items():
        if (data["price_trend"] == "rising" and
            data["energy_use"] == "low" and
            data["sustainability_score"] > 7):
            return name
    return "No suitable long-term crypto found"

# Chatbot Loop
while True:
    user_query = input("\nAsk me something about crypto (or type 'exit' to quit): ").lower()

    if "exit" in user_query:
        print("👋 Goodbye! Stay safe and research before investing! 💼📉")
        break

    elif "sustainable" in user_query or "eco" in user_query:
        coin = get_most_sustainable()
        print(f"🌱 Go with {coin}! It’s eco-friendly with a sustainability score of {crypto_db[coin]['sustainability_score']}/10.")

    elif "trending" in user_query or "rising" in user_query:
        rising = get_trending_cryptos()
        print(f"📈 These cryptos are trending up: {', '.join(rising)}")

    elif "long-term" in user_query or "growth" in user_query:
        coin = get_long_term_crypto()
        if "No" in coin:
            print("❌ Sorry, I couldn't find a suitable long-term crypto right now.")
        else:
            print(f"🚀 {coin} is trending up and is sustainable for long-term growth!")

    elif "buy" in user_query:
        coin = get_profitable_crypto()
        if "No" in coin:
            print("🤷 Sorry, I can't confidently recommend a coin right now.")
        else:
            print(f"💰 Based on profit trends, consider buying {coin}.")

    elif "help" in user_query:
        print("🆘 Try asking me questions like:")
        print("- 'Which crypto is trending up?'")
        print("- 'What is the most sustainable coin?'")
        print("- 'Which crypto should I buy for long-term growth?'")
        print("- 'Which crypto should I buy?'")
        print("- Type 'exit' to leave.")

    else:
        print("❓ I didn’t quite get that. Try asking about trends, sustainability, or investments.")
        print("Type 'help' to see example questions.")

# End of Script
