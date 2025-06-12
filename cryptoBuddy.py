crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3 / 10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6 / 10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8 / 10  
    }  
} 

print("Hello, I'm your crypto helper 😁. Feel free to ask anything!")
print("DISCLAIMER: Please do appropriate research before you decide to venture into any of these currencies.")

while True:
    user_query = input("\nPlease ask me about a cryptocurrency or type 'exit' to quit: ")

    if user_query.lower() == 'exit':
        print("Goodbye for now 👋")
        break

    # Check if the user mentioned a known crypto
    matching_crypto = None
    for crypto in crypto_db:
        if crypto.lower() in user_query.lower():
            matching_crypto = crypto
            break

    # If a match was found, show data
    if matching_crypto:
        data = crypto_db[matching_crypto]

        print(f"\n📊 Analysis for {matching_crypto}:")
        print(f"- Price Trend: {data['price_trend']}")
        print(f"- Market Cap: {data['market_cap']}")
        print(f"- Energy Use: {data['energy_use']}")
        print(f"- Sustainability Score: {data['sustainability_score'] * 10:.1f}/10")

        # Give advice
        if data['price_trend'] == "rising" and data['sustainability_score'] >= 0.7:
            print("✅ Advice: Strong investment — profitable and sustainable.")
        elif data['price_trend'] == "rising":
            print("⚠️ Advice: Looks profitable, but not very sustainable.")
        elif data['price_trend'] == "stable" and data['sustainability_score'] >= 0.6:
            print("💡 Advice: Stable and relatively sustainable. Long-term potential.")
        else:
            print("❌ Advice: Not recommended — either unsustainable or not trending up.")

    # If no match was found
    if not matching_crypto:
        print("🤖 Sorry, I don't have data on that crypto yet. Try Bitcoin, Ethereum, or Cardano.")
