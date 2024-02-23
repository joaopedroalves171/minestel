import telebot
import datetime
import random
import time
from datetime import datetime, timedelta
import pytz

TOKEN = '6418307874:AAG9UvZp9k5WTUe_w6_a2AYPdf_mV-jw4nYs'
bot = telebot.TeleBot(TOKEN)

# Definir o fuso horário para São Paulo
timezone = pytz.timezone('America/Sao_Paulo')

n = 5  # tamanho da matriz
num_bombs = 6  # número de Estrelas

start_enabled = True

@'http://gebemoney.tilda.ws/gebe_16?fbclid=PAAaaKD_f7WR-2evHrcY_tuWj6d-hOwiEYVmeOP6j4a7CxWo8oJ8TjKD3XerE_aem_AWpUflorvWBsyihUyVdFUlp-imnukLjOD-o32eY9Ay7WO44UMBozHzCZ4eHqYe2_El6Dbd00BNqiVaz2e2b8WaIo'

def receber_webhook():

        id = request.json()
@bot.message_handler(commands=["✅Introduzar teu id"])
@bot.message_handler(commands=["Id encontrado✅"])
def send_welcome(message):
    global start_enabled
    if start_enabled:
        start_enabled = False
        minesweeper = [[None]*n for _ in range(n)]  # cria matriz vazia

        # Adiciona Estrelas aleatórias
        bombs_placed = 0
        while bombs_placed < num_bombs:
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            if minesweeper[i][j] != '⭐':
                minesweeper[i][j] = '⭐'
                bombs_placed += 1

        # Preenche células restantes com sinal sem estrelas
        for i in range(n):
            for j in range(n):
                if minesweeper[i][j] != '⭐':
                    minesweeper[i][j] = '🟦'

        # Constroi a string com a matriz
        matrix_str = ''
        for row in minesweeper:
            matrix_str += ''.join(row) + '\n'

        # Obtém a hora atual em São Paulo
        current_time = datetime.now(timezone)

        # Adiciona 2 minutos ao tempo atual
        expiration_time = current_time + timedelta(minutes=2) #validade do SINAL

        # Formata a hora como uma string legível no formato de 24 horas
        expiration_time_str = expiration_time.strftime('%H:%M')

        entrada = f'''
💰<b>Entrada Confirmada</b>💰
💣<b>M𝗶𝗻𝗮𝘀:</b> <b>3</b>
🔁<b>Nº de tentativas: 3</b>
🕔<b>Válido até</b>: <b>{expiration_time_str}</b>

        <pre>{matrix_str}</pre>

        <a href="https://linkdosite.com">👉Cadastre-se & Jogue👈</a>
        '''

        bot.reply_to(message, entrada, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(120) #2 minutos para expiração do sinal
        bot.send_message(message.chat.id, "🔷🔹 <b>Entrada Finalizada</b> 🔹🔷\n✅✅ GRENN! ✅✅", parse_mode='HTML')
        start_enabled = True
    else:
        bot.reply_to(message, "O comando /start está temporariamente desabilitado. Aguarde o sinal ser finalizado.")

bot.polling()