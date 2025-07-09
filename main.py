import telebot, os
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("❌ BOT_TOKEN not found"); exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(m): bot.reply_to(m, "👋 Привет! Я бот с купонами от Coupang!")

print("✅ Bot started …")
bot.infinity_polling()
