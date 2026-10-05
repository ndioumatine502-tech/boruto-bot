from flask import Flask
import threading
import os
import logging
from telegram import LabeledPrice, Update
from telegram.ext import Application, CommandHandler, MessageHandler, PreCheckoutQueryHandler, filters

# --- Petit serveur web pour Render (GRATUIT) ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive - Boruto is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web, daemon=True).start()
# --- Fin serveur web ---

TOKEN = os.environ.get("BOT_TOKEN", "867078072:AAFG...COLLE TON TOKEN ICI SI TU N'UTILISES PAS ENV")
LINK_10 = "https://t.me/stars_klickbot?start=aff..."
LINK_50 = "https://drive.google.com/drive/folders/1XXX"
LINK_VIP = "https://drive.google.com/drive/folders/1XXX"

async def start(u: Update, c):
    await u.message.reply_text("🌟 Boruto Stars Shop\n\n/pack10 - 10 Stars\n/p50 - 50 Stars\n/vip - VIP Pack")

async def pack10(u: Update, c):
    await u.effective_chat.send_invoice(
        chat_id=u.effective_chat.id,
        title="Pack 10 Stars",
        description="Pack de 10 Stars",
        payload="pack10",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice("Pack10", 10)]
    )

async def p50(u: Update, c):
    await u.effective_chat.send_invoice(
        chat_id=u.effective_chat.id,
        title="Pack 50 Stars",
        description="Pack 50 Stars",
        payload="pack50",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice("Pack50", 50)]
    )

async def vip(u: Update, c):
    await u.effective_chat.send_invoice(
        chat_id=u.effective_chat.id,
        title="VIP Pack",
        description="VIP Pack",
        payload="vip",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice("VIP", 100)]
    )

async def precheckout(u: Update, c):
    await u.pre_checkout_query.answer(ok=True)

async def success_pay(u: Update, c):
    payload = u.pre_checkout_query.invoice_payload if hasattr(u, 'pre_checkout_query') else u.message.successful_payment.invoice_payload
    # Pour simplifier on utilise le successful_payment
    pay = u.message.successful_payment
    if pay.invoice_payload == "pack10":
        await c.bot.send_message(u.effective_user.id, f"✅ Merci ! Voici ton lien:\n{LINK_10}")
    elif pay.invoice_payload == "pack50":
        await c.bot.send_message(u.effective_user.id, f"✅ Merci ! Pack 50:\n{LINK_50}")
    elif pay.invoice_payload == "vip":
        await c.bot.send_message(u.effective_user.id, f"✅ VIP activé !\n{LINK_VIP}")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("pack10", pack10))
    application.add_handler(CommandHandler("p50", p50))
    application.add_handler(CommandHandler("vip", vip))
    application.add_handler(PreCheckoutQueryHandler(precheckout))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, success_pay))
    application.run_polling()

if __name__ == "__main__":
    main()
