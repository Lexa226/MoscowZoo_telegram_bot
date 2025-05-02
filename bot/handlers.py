from aiogram import F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile
from config import PATRONAGE_URL
from quiz.questions import questions
from quiz.scoring import initialize_game, process_answer, get_result
from quiz.results import results_map
from bot.keyboards import start_keyboard, question_keyboard, result_keyboard, feedback_keyboard
from bot.messages import FEEDBACK_PROMPT, CONTACT_PROMPT

async def start_handler(message: Message):
    await message.answer(
        text="Привет! Узнай своё тотемное животное в Московском зоопарке.",
        reply_markup=start_keyboard()
    )

async def quiz_start(callback: CallbackQuery):
    user_id = callback.from_user.id
    initialize_game(user_id)
    question = questions[0]
    await callback.message.edit_text(
        text=question['text'],
        reply_markup=question_keyboard(0, question['options'])
    )

async def quiz_answer(callback: CallbackQuery):
    _, _, q_index, opt_index = callback.data.split(':')
    q_index, opt_index = int(q_index), int(opt_index)
    user_id = callback.from_user.id
    process_answer(user_id, q_index, opt_index)
    next_index = q_index + 1
    if next_index < len(questions):
        question = questions[next_index]
        await callback.message.edit_text(
            text=question['text'],
            reply_markup=question_keyboard(next_index, question['options'])
        )
    else:
        result_key = get_result(user_id)
        result = results_map[result_key]
        photo_path = f"data/images/totem/{result_key}.jpg"
        await callback.message.answer_photo(
            photo=FSInputFile(photo_path)
        )
        await callback.message.answer(
            text=f"Ты — {result['title']}!\n{result['description']}",
            reply_markup=result_keyboard(result['title'])
        )

async def feedback_start(callback: CallbackQuery):
    await callback.message.edit_text(
        text=FEEDBACK_PROMPT,
        reply_markup=feedback_keyboard()
    )

async def feedback_like(callback: CallbackQuery):
    await callback.message.edit_text("Спасибо за ваш отзыв! 👍")

async def feedback_dislike(callback: CallbackQuery):
    await callback.message.edit_text("Спасибо за ваш отзыв! 👎")

async def contact(callback: CallbackQuery):
    await callback.message.edit_text(text=CONTACT_PROMPT)

async def send_contact(message: Message):
    await message.answer("Ваша заявка отправлена, специалист скоро с вами свяжется.")


def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler, Command(commands=["start"]))
    dp.callback_query.register(quiz_start, F.data == "quiz:start")
    dp.callback_query.register(quiz_answer, F.data.startswith("quiz:answer"))
    dp.callback_query.register(feedback_start, F.data == "feedback:start")
    dp.callback_query.register(feedback_like, F.data == "feedback:like")
    dp.callback_query.register(feedback_dislike, F.data == "feedback:dislike")
    dp.callback_query.register(contact, F.data == "contact")
    dp.message.register(
        send_contact,
        ~F.text.startswith("/"),
        F.text
    )