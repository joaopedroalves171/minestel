import random
import telebot
import time
from datetime import datetime, timedelta
import pytz
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import re

token = '6109226718:AAHsI7CYGCg_V-uKfCk1v7QrLb90-A75W-Y'
chat_id = '-1002111034448'
bot = telebot.TeleBot(token)

# Definir o fuso horário para São Paulo
timezone = pytz.timezone('America/Sao_Paulo')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Por favor, envie seu ID (apenas números):')

def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Verifica se a mensagem contém apenas números
    if re.fullmatch(r'\d+', user_message):
        # Confirma o ID do usuário
        update.message.reply_text(f'Seu ID é {user_message}.')
        # Cria um botão que direciona para um link
        keyboard = [[InlineKeyboardButton("Iniciar jogo", url='https://example.com')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(reply_markup=reply_markup)
    else:
        update.message.reply_text('Por favor, envie apenas números.')

def main():
    # Substitua 'YOUR_TOKEN_HERE' pelo token do seu bot
    updater = Updater("YOUR_TOKEN_HERE")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



while True:
    try:
        n = 5  # tamanho da matriz
        num_bombs = 6  # número de bombas
        minesweeper = [[None]*n for _ in range(n)]  # cria matriz vazia

        # Adiciona bombas aleatórias
        bombs_placed = 0
        while bombs_placed < num_bombs:
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            if minesweeper[i][j] != '⭐':
                minesweeper[i][j] = '⭐'
                bombs_placed += 1

        # Preenche células restantes com sinal sem bomba
        for i in range(n):
            for j in range(n):
                if minesweeper[i][j] != '⭐':
                    minesweeper[i][j] = '🟦'

        # Constroi a string com a matriz
        matrix_str = ''
        for row in minesweeper:
            matrix_str += ' '.join(row) + '\n'

        # Obtém a hora atual em São Paulo
        current_time = datetime.now(timezone)

        # Adiciona 2 minutos ao tempo atual
        expiration_time = current_time + timedelta(minutes=5)

        # Formata a hora como uma string legível no formato de 24 horas
        expiration_time_str = expiration_time.strftime('%H:%M')

        entrada = f'''
💰<b>Entrada Confirmada</b>💰
💣<b>M𝗶𝗻𝗮𝘀:</b> <b>3</b>
🔁<b>Nº de tentativas: 3</b>
🕔<b>Válido até</b>: <b>{expiration_time_str}</b>

{matrix_str}

<a href="https://oceano.bet/game/spribe-mines">👉Cadastre-se & Jogue👈</a>
'''

        msg = f'''🔷🔹 <b>Entrada Finalizada</b> 🔹🔷
            ✅✅ GRENN! ✅✅'''

        bot.send_message(chat_id=chat_id, text=entrada, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(300)
        bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(300)
        print('MATRIZ ENVIADA')
        print(matrix_str)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        print('Reiniciando o código...')
        time.sleep(10)
        continue
