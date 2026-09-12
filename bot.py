import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


# =========================
# НАСТРОЙКИ
# =========================

BOT_TOKEN = "ВСТАВИМ_ТОКЕН_ПОЗЖЕ"


# =========================
# 78 КАРТ ТАРО
# =========================

MAJOR_ARCANA = [
    "Шут", "Маг", "Верховная Жрица", "Императрица",
    "Император", "Иерофант", "Влюблённые", "Колесница",
    "Сила", "Отшельник", "Колесо Фортуны", "Справедливость",
    "Повешенный", "Смерть", "Умеренность", "Дьявол",
    "Башня", "Звезда", "Луна", "Солнце",
    "Суд", "Мир"
]

SUITS = {
    "Жезлы": [
        "Туз", "Двойка", "Тройка", "Четвёрка", "Пятёрка",
        "Шестёрка", "Семёрка", "Восьмёрка", "Девятка", "Десятка",
        "Паж", "Рыцарь", "Королева", "Король"
    ],
    "Кубки": [
        "Туз", "Двойка", "Тройка", "Четвёрка", "Пятёрка",
        "Шестёрка", "Семёрка", "Восьмёрка", "Девятка", "Десятка",
        "Паж", "Рыцарь", "Королева", "Король"
    ],
    "Мечи": [
        "Туз", "Двойка", "Тройка", "Четвёрка", "Пятёрка",
        "Шестёрка", "Семёрка", "Восьмёрка", "Девятка", "Десятка",
        "Паж", "Рыцарь", "Королева", "Король"
    ],
    "Пентакли": [
        "Туз", "Двойка", "Тройка", "Четвёрка", "Пятёрка",
        "Шестёрка", "Семёрка", "Восьмёрка", "Девятка", "Десятка",
        "Паж", "Рыцарь", "Королева", "Король"
    ]
}


def create_deck():
    deck = []

    for card in MAJOR_ARCANA:
        deck.append(card)

    for suit, cards in SUITS.items():
        for card in cards:
            deck.append(f"{card} {suit}")

    return deck


DECK = create_deck()


# =========================
# БОТ
# =========================

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "🔮 Добро пожаловать в Tarot AI!\n\n"
        "Я помогу сделать расклад Таро.\n\n"
        "🃏 /card — вытянуть одну карту\n"
        "❤️ /love — расклад на любовь\n"
        "💰 /money — расклад на деньги\n"
        "💼 /career — расклад на карьеру\n"
        "🔮 /general — общий расклад\n\n"
        "Выбери команду из меню 👇"
    )

    await message.answer(text)


@dp.message(Command("card"))
async def one_card(message: types.Message):
    card = random.choice(DECK)
    position = random.choice(["Прямое положение", "Перевёрнутое положение"])

    text = (
        "🃏 Твоя карта:\n\n"
        f"✨ {card}\n"
        f"↕️ {position}\n\n"
        "Толкование карты добавим следующим этапом."
    )

    await message.answer(text)


@dp.message(Command("love"))
async def love(message: types.Message):
    await message.answer(
        "❤️ Расклад на любовь\n\n"
        "Сейчас вытянем карту на твою любовную ситуацию."
    )

    card = random.choice(DECK)
    position = random.choice(["Прямое положение", "Перевёрнутое положение"])

    await message.answer(
        f"🃏 {card}\n"
        f"↕️ {position}"
    )


@dp.message(Command("money"))
async def money(message: types.Message):
    card = random.choice(DECK)

    await message.answer(
        "💰 Расклад на деньги\n\n"
        f"🃏 Твоя карта: {card}"
    )


@dp.message(Command("career"))
async def career(message: types.Message):
    card = random.choice(DECK)

    await message.answer(
        "💼 Расклад на карьеру\n\n"
        f"🃏 Твоя карта: {card}"
    )


@dp.message(Command("general"))
async def general(message: types.Message):
    cards = random.sample(DECK, 3)

    text = (
        "🔮 Общий расклад — 3 карты\n\n"
        f"1️⃣ {cards[0]}\n"
        f"2️⃣ {cards[1]}\n"
        f"3️⃣ {cards[2]}\n\n"
        "🤖 Подробное AI-толкование добавим следующим этапом."
    )

    await message.answer(text)


# =========================
# ЗАПУСК
# =========================

async def main():
    if BOT_TOKEN == "ВСТАВИМ_ТОКЕН_ПОЗЖЕ":
        print("Ошибка: нужно добавить Telegram BOT TOKEN.")
        return

    bot = Bot(token=BOT_TOKEN)

    print("🔮 Tarot AI Bot запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
