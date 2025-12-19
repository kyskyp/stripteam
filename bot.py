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

    players_online = data["players"].get("online", 0)
    players_max = data["players"].get("max", 20)
    motd_lines = data["motd"]["clean"] if data.get("motd") and data["motd"].get("clean") else ["Нет MOTD"]
    motd = "\n".join(motd_lines)
    
    text = (
        f"✅ <b>Сервер работает!</b>\n\n"
        f"🌍 IP: <code>{SERVER_IP}</code>\n"
        f"👥 Онлайн: <b>{players_online}/{players_max}</b>\n"
        f"📜 MOTD:\n{motd}"
    )
    
    players_list = data["players"].get("list")
    if players_list:
        text += "\n\n👥 Игроки онлайн:\n" + "\n".join(players_list)

    await message.answer(text, parse_mode="HTML")

async def main():
    print("Бот запущен на Render.com 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
