import random
import telebot

bot = telebot.TeleBot("7711207024:AAFAtme9hfqal5Afw0RWz-9HWFaWHN9WtDs")
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "Welcome to the password generator bot!")

    def gen_pass(pass_length):
        symbols = "!@#$%^&*()_+{:><~"
        password=""
        for i in range(pass_length):
            password = password +random.choice(symbols)
        return password
    bot.reply_to(message, "Your new password is: " +gen_pass(10))

bot.polling()