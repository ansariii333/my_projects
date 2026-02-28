import telebot
bot = telebot.TeleBot("8461939380:AAGPFflvooSHATW_m06n_BmIUXPnyw9UVRY")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Я бот который поддержит о тебе и поднимет тебе настроение! Нвжми на эти кнопки чтобы узнать много нового о себе и о мире!  /joke  /facts  /about_user")   
@bot.message_handler(commands=['joke'])
def send_joke(message):
        bot.reply_to(message,"Вот тебе шутка: Почему программисты не любят природу? Потому что там слишком много багов  /more_jokes")
@bot.message_handler(commands=['more_jokes'])
def send_more_jokes(message):
        bot.reply_to(message,"Вот тебе еще одна шутка: Почему программисты всегда путают Рождество и Хэллоуин? Потому что OCT 31 == DEC 25!")

@bot.message_handler(commands=['facts'])
def send_facts(message):
        bot.reply_to(message,"Вот тебе интересный факт: Знаешь ли ты, что медузы существуют уже более 500 миллионов лет? Они были одними из первых многоклеточных организмов на Земле!  /more_facts")
@bot.message_handler(commands=['more_facts'])
def send_more_facts(message):
        bot.reply_to(message,"Вот тебе еще один интересный факт: Знаешь ли ты, что у осьминогов три сердца? Два из них перекачивают кровь к жабрам, а третье - к остальным частям тела!")

@bot.message_handler(commands=['about_user'])
def send_about_user(message):
        bot.reply_to(message,"Я знаю о тебе, что ты любишь узнавать новое и веселиться! Ты всегда готов к новым приключениям и открытию новых горизонтов. Ты ценишь дружбу и всегда поддерживаешь своих друзей. Ты любишь делиться своими знаниями и опытом с другими. Ты уникальный и замечательный человек, и я рад быть твоим другом!  /more_about_user")
@bot.message_handler(commands=['more_about_user'])
def send_more_about_user(message):
        bot.reply_to(message,"Ты также любишь путешествовать и открывать новые места. Ты всегда готов к новым вызовам и не боишься выходить из своей зоны комфорта. Ты ценишь искусство и культуру, и всегда находишь время для творчества. Ты заботишься о своем здоровье и стараешься вести активный образ жизни. Ты - удивительный человек, и я горжусь тем, что могу быть твоим другом!")
bot.polling()
        