import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text

API_TOKEN = "8593596966:AAEaG497-PhF7aLifJZopFTI8RQny5cfoQ4"
SERVER_IP = "sidorik4166.aternos.me:18097"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def get_server_status():
    url = f"https://api.mcsrvstat.us/3/{SERVER_IP}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return None
            return await resp.json()

@dp.message(Command("сервер"))
@dp.message(Text(startswith=("!сервер", "/сервер")))
async def cmd_server(message: types.Message):
    await message.answer("🔍 Проверяю статус сервера...")

    data = await get_server_status()
    
    if not data or not data.get("online"):
        await message.answer("❌ <b>Сервер выключен</b>\nЗапусти его на aternos.org", parse_mode="HTML")
        return

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
