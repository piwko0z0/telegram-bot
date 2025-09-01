import telebot

# Вставь сюда токен от BotFather
TOKEN = "8134465834:AAE9z5Lv077FIEbBldteOIBJ_VwTNwSJ8ag"
bot = telebot.TeleBot(TOKEN)

RUB_PER_TON = 290  # цена тона в рублях

def calculate_price(tons):
    base = tons * RUB_PER_TON
    with_markup = base * 1.3 * 1.17 * 1.07
    extra = (0.1 * RUB_PER_TON) + 50
    return round(with_markup + extra, 2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я калькулятор подарков 🎁\nНапиши сколько TON стоит подарок, и я скажу цену в рублях.")

@bot.message_handler(func=lambda m: True)
def convert(message):
    try:
        tons = float(message.text.replace(",", "."))
        price = calculate_price(tons)
        bot.reply_to(message, f"Подарок за {tons} TON будет стоить {price} ₽")
    except ValueError:
        bot.reply_to(message, "Напиши число (например: 2.5)")

bot.polling(none_stop=True)
