import telebot
import requests
import os

# Tokenini buraya yaz = "8796034964:AAFgaXE7orHVayl9f75PZZ26C92Ojkdg35g"

bot = telebot.TeleBot(TOKEN)

# /start komutu
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Merhaba! Ben senin yapay zeka botunum. Nasıl yardımcı olabilirim?")

# /help komutu
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "📚 Komutlar:\n/start - Botu başlat\n/help - Yardım menüsü")

# Normal mesajlar
@bot.message_handler(func=lambda message: True)
def chat(message):
    bot.reply_to(message, f"📨 Mesajın alındı: {message.text}")

print("🤖 Bot çalışmaya başladı...")
bot.polling()
