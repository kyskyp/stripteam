import telebot
from mcstatus import JavaServer

# Токен вашего бота (замените на новый, если этот скомпрометирован!)
TOKEN = '8593596966:AAEaG497-PhF7aLifJZopFTI8RQny5cfoQ4'

# Адрес сервера Aternos (хост:порт)
SERVER_HOST = 'sidorik4166.aternos.me'
SERVER_PORT = 18097

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['сервер'], func=lambda message: message.text.startswith('!сервер'))
def check_server(message):
    try:
        # Создаем объект сервера
        server = JavaServer.lookup(f"{SERVER_HOST}:{SERVER_PORT}")
        
        # Проверяем статус
        status = server.status()
        
        # Если сервер онлайн
        online_players = status.players.online
        max_players = status.players.max
        response = f"Сервер работает! Онлайн: {online_players}/{max_players} игроков."
    
    except Exception as e:
        # Если сервер оффлайн или ошибка (например, таймаут)
        response = "Сервер не работает или недоступен в данный момент."
    
    # Отправляем ответ в чат
    bot.reply_to(message, response)

# Запуск бота в режиме long polling (для 24/7 используйте хостинг с мониторингом)
if __name__ == '__main__':
    bot.infinity_polling()
