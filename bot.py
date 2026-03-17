import telebot
import os

# Tokeni direkt yazıyoruz
TOKEN = "8796034964:AAFgaXE7orHVayl9f75PZZ26C92Ojkdg35g"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Merhaba! Bot başarıyla çalışıyor ✅")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Komutlar:\n/start - Başlat\n/help - Yardım")

@bot.message_handler(func=lambda message: True)
def chat(message):
    bot.reply_to(message, f"Mesajın alındı: {message.text}")

print("Bot çalışıyor...")
bot.polling()
