import translators as ts
import telebot

bot = telebot.TeleBot("", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

def get_phrase(msg):
	words = msg.split()[1:]
	return ' '.join(words)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Пендос-бот\n /ru фраза - перевод на английский с русского.\n /en фраза - перевод с английского на русский")

@bot.message_handler(commands=['ru'])
def send_ru(message):
	phrase = get_phrase(message.text)
	try:
		res = ts.alibaba(phrase, from_language='ru', to_language='en')
		bot.reply_to(message, res)
	except Exception as e:
		print(e)
		bot.reply_to(message, 'Ошибка, API перевода не доступен!')

@bot.message_handler(commands=['en'])
def send_en(message):
	phrase = get_phrase(message.text)
	try:
		res = ts.alibaba(phrase, from_language='en', to_language='ru')
		bot.reply_to(message, res)
	except Exception as e:
		print(e)
		bot.reply_to(message, 'Ошибка, API перевода не доступен!')

bot.polling()