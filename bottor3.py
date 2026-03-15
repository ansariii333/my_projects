import telebot
import requests
import random
bot = telebot.TeleBot("8461939380:AAGPFflvooSHATW_m06n_BmIUXPnyw9UVRY")

@bot.message_handler(commands=['meme1'])
def send_meme(message):
    with open ('images/meme1.jpg','rb') as f:
        bot.send_photo(message.chat.id,f)
@bot.message_handler(commands=['meme2'])
def send_meme(message):
    with open('images/meme2.jpeg','rb') as f:
        bot.send_photo(message.chat.id,f)
@bot.message_handler(commands=['meme3'])
def send_meme(message):
    with open('images/meme3.jpeg','rb') as f:
        bot.send_photo(message.chat.id,f)
@bot.message_handler(commands=['meme4'])
def send_meme(message): 
     with open('images/meme4.jpg','rb') as f:
          bot.send_photo(message.chat.id,f)


def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url'] 
@bot.message_handler(commands=['duck'])

def duck(message):
       image_url = get_duck_image_url()
       bot.send_photo(message.chat.id, image_url)


def get_pok_image():
     pok_id = random.randint(1,1010)
     url = f"https://pokeapi.co/api/v2/pokemon/{pok_id}"
     res = requests.get(url)
     data = res.json()
     name = data['name'].capitalize()
     img_url = data['sprites']['front_default']
     return name,img_url
@bot.message_handler(commands=['poke'])
def poke(message):
     name,img_url = get_pok_image()
     bot.send_message(message.chat.id,f'The name of your pokemon: {name}')
     bot.send_photo(message.chat.id,img_url)
bot.polling()