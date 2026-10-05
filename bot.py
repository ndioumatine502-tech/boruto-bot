import logging
from telegram import LabeledPrice, Update
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8676780782:AAFGAu8Q_hHnA5mW2o8_ivtXiZJC3cIHe5"
AFF = "https://t.me/stars_klickston_bot?start=aff"
L10 = "https://drive.google.com/drive/folders/1XXX"
L50 = "https://drive.google.com/drive/folders/1XXX"
VIP = "https://drive.google.com/drive/folders/1XXX"

async def start(u,c):
    await u.message.reply_text(f"🌟 Boruto Stars Shop 🌟\n\nAFF - Lien affilié\nL10 - Pack 10\nL50 - Pack 50\nVIP - 200+ ILLIMITÉ\n\nCommandes:\n/pack10 - 25⭐\n/pack50 - 100⭐\n/vip - 250⭐")

async def p10(u,c):
    await c.bot.send_invoice(u.effective_chat.id, "Pack 10", "Pack de 10", "pack10", TOKEN.split(":")[0], "XTR", [LabeledPrice("Pack 10", 25)])

async def p50(u,c):
    await c.bot.send_invoice(u.effective_chat.id, "Pack 50", "Pack de 50", "pack50", TOKEN.split(":")[0], "XTR", [LabeledPrice("Pack 50", 100)])

async def vip(u,c):
    await c.bot.send_invoice(u.effective_chat.id, "VIP", "200+ ILLIMITE", "vip", TOKEN.split(":")[0], "XTR", [LabeledPrice("VIP", 250)])

async def pre(u,c):
    await u.pre_checkout_query.answer(ok=True)

async def okp(u,c):
    pay = u.pre_checkout_query.invoice_payload
    if pay == "pack10":
        await c.bot.send_message(u.effective_user.id, f"✅ Paiement OK Pack 10!\n{L10}\nAFF: {AFF}")
    elif pay == "pack50":
        await c.bot.send_message(u.effective_user.id, f"✅ Paiement OK Pack 50!\n{L50}")
    elif pay == "vip":
        await c.bot.send_message(u.effective_user.id, f"✅ Paiement OK VIP!\n{VIP}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pack10", p10))
app.add_handler(CommandHandler("pack50", p50))
app.add_handler(CommandHandler("vip", vip))
app.add_handler(PreCheckoutQueryHandler(pre))
app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, okp))
app.run_polling()
