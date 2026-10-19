import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8605286948:AAHDoSk_R7lQtEYwvaUxiyX8707He7B1RTY"
CHANNEL_LINK = "https://t.me/+tnjvn433fKYyM2Ey"
CARD_NUMBER = "8600 5286 948 - Surayyo"
PRICE = "49 000 so'm"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(f"💳 {PRICE} - To'lov qilish", callback_data='pay')],
        [InlineKeyboardButton("📞 Admin", url="https://t.me/surayyomamajanova")]
    ]
    text = f"Yopiq kanalga kirish: {PRICE}\n\nTo'lov qilib avtomatik kirasiz."
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'pay':
        keyboard = [[InlineKeyboardButton("✅ To'lov qildim", callback_data='paid')]]
        text = f"💳 To'lov:\n\nKarta: {CARD_NUMBER}\nSumma: {PRICE}"
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'paid':
        text = f"✅ Rahmat!\n\nKanal linki:\n{CHANNEL_LINK}"
        await query.edit_message_text(text)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
