import telebot
import requests
import json
import os

# Tokenler
TOKEN = "8796034964:AAFgaXE7orHVayl9f75PZZ26C92Ojkdg35g"
GEMINI_API_KEY = AIzaSyBJV2mui_WNTMO89edfTbnRzEYVYYI8bI4 # Ücretsiz Gemini API anahtarı

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "⚽ Hoş geldin! Ben iddaa analiz botuyum.\n\n"
                          "Bana şunları sorabilirsin:\n"
                          "- Beşiktaş-Galatasaray maçını tahmin et\n"
                          "- Bugünkü maçların analizi\n"
                          "- Takım form durumu\n"
                          "- Maçta gol olur mu?\n"
                          "- Oran analizi")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "📊 Nasıl Kullanılır?\n\n"
                          "Örnek sorular:\n"
                          "• Fenerbahçe - Trabzonspor maçı ne olur?\n"
                          "• Ev sahibi avantajı nedir?\n"
                          "• Son 5 maçta kaç gol var?\n"
                          "• Şu maçta 2.5 üstü olur mu?")

@bot.message_handler(func=lambda message: True)
def iddaa_analiz(message):
    soru = message.text
    
    # Kullanıcıya beklediğini bildir
    bot.send_chat_action(message.chat.id, 'typing')
    
    try:
        # Gemini API'ye sor
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}",
            json={
                "contents": [
                    {
                        "parts": [
                            {
                                "text": f"Sen bir iddaa ve futbol analiz uzmanısın. Kullanıcı şunu sordu: '{soru}'. "
                                       f"Türkçe cevap ver. Maç tahmini, istatistik, form durumu, oran analizi yap. "
                                       f"Cevabı kısa ve net tut, madde madde yaz."
                            }
                        ]
                    }
                ]
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            cevap = data['candidates'][0]['content']['parts'][0]['text']
            bot.reply_to(message, cevap)
        else:
            bot.reply_to(message, "⚽ Şu anda analiz yapamıyorum. Lütfen daha sonra tekrar dene.")
            
    except Exception as e:
        bot.reply_to(message, "🔴 Bir hata oluştu. Lütfen basit bir soru sor veya daha sonra dene.")

print("⚽ İddaa analiz botu çalışıyor...")
bot.polling()
