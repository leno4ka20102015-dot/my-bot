import telebot
from telebot import types

# ВСТАВЬТЕ СВОЙ ТОКЕН ВМЕСТО НАДПИСИ В КАВЫЧКАХ
import os
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🛒 Сделать заказ')
    btn2 = types.KeyboardButton('💰 Цены')
    btn3 = types.KeyboardButton('📍 Адрес')
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, 
        "Здравствуйте! 👋 Добро пожаловать в наш магазин.\nВыберите нужный пункт ниже:", 
        reply_markup=markup)

# Обработка нажатия на кнопку "Цены"
@bot.message_handler(func=lambda message: message.text == '💰 Цены')
def prices(message):
    bot.send_message(message.chat.id, "Наши цены:\nКофе — 150 руб.\nЧай — 100 руб.\nКруассан — 200 руб.")

# Обработка нажатия на кнопку "Адрес"
@bot.message_handler(func=lambda message: message.text == '📍 Адрес')
def address(message):
    bot.send_message(message.chat.id, "Наш адрес: г. Йошкар-Ола, ул. Ленина, д. 10.\nРаботаем с 10:00 до 21:00.")

# Обработка нажатия на кнопку "Сделать заказ"
@bot.message_handler(func=lambda message: message.text == '🛒 Сделать заказ')
def order(message):
    bot.send_message(message.chat.id, "Напишите, что вы хотите заказать (например: '2 кофе и 1 круассан'), и мы свяжемся с вами!")

print("Бот запущен! Ждем сообщений...")
# Обработка текста заказа
@bot.message_handler(content_types=['text'])
def handle_order(message):
    # Если пользователь нажал на кнопки, мы их уже обработали, поэтому пропускаем
    if message.text in ['🛒 Сделать заказ', '💰 Цены', '📍 Адрес']:
        return
    
    # Отправляем сообщение вам (замените 123456789 на ваш ID)
    admin_id = os.getenv('ADMIN_ID')
bot.send_message(admin_id, f"🔔 Новый заказ!\nОт: {user_name} ({username})\nЗаказ: {message.text}")
    bot.send_message(message.chat.id, "Спасибо! Ваш заказ принят, мы скоро свяжемся с вами.")
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Создаем простой сервер, чтобы Render думал, что это сайт
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_server():
    port = int(os.environ.get('PORT', 10000))
    httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

# Запускаем сервер в отдельном потоке
threading.Thread(target=run_server, daemon=True).start()

# А это ваш бот, он продолжит работать
bot.infinity_polling()
