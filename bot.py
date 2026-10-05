import logging
from telegram import LabeledPrice
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters

TOKEN = "ICI_TON_TOKEN_BOTFATHER"
AFF = "https://t.me/stars_klickston_bot?start=_tgr_o6gaIhc2NGU0"
L10 = "https://drive.google.com/drive/folders/1XXX"
L50 = "https://drive.google.com/drive/folders/1XXX"
LVIP = "https://drive.google.com/drive/folders/1XXX"

async def start(u,c):
 await u.message.reply_text(f"🔥 BORUTO STARS 200+ fonds 4K\n\nGagne des Stars gratuit ici:\n{AFF}\n\n/pack10 - 10 fonds 25 ⭐\n/pack50 - 50 fonds 100 ⭐\n/vip - 200+ ILLIMITE 250 ⭐")

async def p10(u,c):
 await c.bot.send_invoice(u.effective_chat.id,"Pack 10","10 fonds","pack10","", "XTR", [LabeledPrice("Pack 10",25)])
async def p50(u,c):
 await c.bot.send_invoice(u.effective_chat.id,"Pack 50","50 fonds","pack50","", "XTR", [LabeledPrice("Pack 50",100)])
async def vip(u,c):
 await c.bot.send_invoice(u.effective_chat.id,"VIP","200+ fonds","vip","", "XTR", [LabeledPrice("VIP",250)])

async def pre(u,c):
 await u.pre_checkout_query.answer(ok=True)

async def ok(u,c):
 p=u.message.successful_payment.invoice_payload
 if p=="pack10": await u.message.reply_text(f"✅ Pack 10: {L10}")
 if p=="pack50": await u.message.reply_text(f"✅ Pack 50: {L50}")
 if p=="vip": await u.message.reply_text(f"🔥 VIP: {LVIP}")

a=Application.builder().token(TOKEN).build()
a.add_handler(CommandHandler("start",start))
a.add_handler(CommandHandler("pack10",p10))
a.add_handler(CommandHandler("pack50",p50))
a.add_handler(CommandHandler("vip",vip))
a.add_handler(PreCheckoutQueryHandler(pre))
a.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT,ok))
a.run_polling()
