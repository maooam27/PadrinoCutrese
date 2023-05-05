import telebot
from platform import platform, system, release
import os

BOT_TOKEN = "5729050636:AAGmzPQy2Fmpi0l-AHmxNJ2FU221omQem3M"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot in esecuzione")


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, f"Sistema: {platform()}")


@bot.message_handler(commands=['sistema'])
def send_sistema(message):
    bot.reply_to(message, f"Sistema: {system()} {release()}")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Comandi disponibili: \n /help : mostra l'elenco dei comandi disponibili"
                          "\n /start : avvia il bot"
                          "\n /info : mostra le informazioni specifiche sul sistema generale"
                          "\n /sistema : mostra le informazioni sul sistema in uso"
                          "\n /spegni : spegne il sistema"
                          "\n /minecraft : chiude minecraft")


@bot.message_handler(commands=['spegni'])
def send_spegni(message):
    os.system("shutdown -f -s -t 1")
    bot.reply_to(message, f"Sistema in spegnimento capo")


@bot.message_handler(commands=['minecraft'])
def send_ciaominecraft(message):
    os.system("taskkill /IM javaw.exe /F")
    bot.reply_to(message, f"Minecraft in chiusura capo")


bot.infinity_polling()
