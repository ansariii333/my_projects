import telebot
from telebot import types
import sqlite3


TOKEN = "7182276134:AAHwYpMom8GL54VMtgIeem7ebrTOmtkx0XI"
bot = telebot.TeleBot("7182276134:AAHwYpMom8GL54VMtgIeem7ebrTOmtkx0XI")


def init_db():
    conn = sqlite3.connect('eco_forge.db', check_same_thread=False)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
  
                                       (id INTEGER PRIMARY KEY, username TEXT, points INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

def register_user(user_id, username):
    conn = sqlite3.connect('eco_forge.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (id, username, points) VALUES (?, ?, 0)", (user_id, username))
    conn.commit()
    conn.close()

def add_points(user_id, amount):
    conn = sqlite3.connect('eco_forge.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET points = points + ? WHERE id = ?", (amount, user_id))
    conn.commit()
    conn.close()

def get_stats(user_id):
    conn = sqlite3.connect('eco_forge.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT points FROM users WHERE id = ?", (user_id,))
    res = cursor.fetchone()
    conn.close()
    return res[0] if res else 0


init_db()


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎯 Получить задание")
    btn2 = types.KeyboardButton("👤 Мой профиль")
    btn3 = types.KeyboardButton("🏆 Топ лидеров")
    markup.add(btn1, btn2, btn3)
    return markup



@bot.message_handler(commands=['start'])
def start(message):
    register_user(message.from_user.id, message.from_user.username)
    bot.send_message(
        message.chat.id, 
        "🌿 Привет! Я **EcoForge**. Здесь ты получаешь очки за добрые дела для планеты.\n\n"
        "Жми кнопку ниже, чтобы начать!", 
        reply_markup=main_keyboard(),
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda message: message.text == "🎯 Получить задание")
def send_task(message):
    task_text = (
        "🟢 **Задание: Цифровой детокс**\n\n"
        "Удали 50 ненужных писем или старых скриншотов. Это снижает нагрузку на серверы и экономит электроэнергию!\n\n"
        "Награда: **10 очков**"
    )
    
    inline_markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("✅ Я выполнил!", callback_data="done_10")
    inline_markup.add(btn)
    
    bot.send_message(message.chat.id, task_text, reply_markup=inline_markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "👤 Мой профиль")
def profile(message):
    points = get_stats(message.from_user.id)
    bot.send_message(message.chat.id, f"👤 **Профиль:** {message.from_user.first_name}\n💰 Баланс: **{points}** очков", parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "🏆 Топ лидеров")
def top(message):
    conn = sqlite3.connect('eco_forge.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT username, points FROM users ORDER BY points DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    
    res = "🏆 **Топ-5 эко-героев:**\n\n"
    for i, row in enumerate(rows, 1):
        username = row[0] if row[0] else "Аноним"
        res += f"{i}. @{username} — {row[1]} очков\n"
    bot.send_message(message.chat.id, res, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data.startswith("done_"))
def callback_done(call):
    points_to_add = int(call.data.split("_")[1])
    add_points(call.from_user.id, points_to_add)
    
   
    bot.edit_message_text(
        chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        text=f"🎉 Великолепно! Тебе начислено **{points_to_add}** очков!",
        parse_mode="Markdown"
    )
    bot.answer_callback_query(call.id, "Очки добавлены!")


if __name__ == "__main__":
    print("Бот EcoForge запущен и готов к работе...")
    bot.polling(none_stop=True)