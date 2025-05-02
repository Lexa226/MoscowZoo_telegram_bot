from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import PATRONAGE_URL

def start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать викторину", callback_data="quiz:start")]
    ])

def question_keyboard(question_index, options):
    buttons = [
        [InlineKeyboardButton(text=opt['text'],
                              callback_data=f"quiz:answer:{question_index}:{i}") ]
        for i, opt in enumerate(options)
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def result_keyboard(result_title):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше об опеке", url=PATRONAGE_URL)],
        [InlineKeyboardButton(text="Попробовать ещё раз", callback_data="quiz:start")],
        [InlineKeyboardButton(text="Поделиться результатом",
                              switch_inline_query=f"Я — {result_title}")],
        [InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback:start")],
        [InlineKeyboardButton(text="Связаться со специалистом", callback_data="contact")]
    ])

def feedback_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="👍", callback_data="feedback:like"),
            InlineKeyboardButton(text="👎", callback_data="feedback:dislike")
        ]
    ])
