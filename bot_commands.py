from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CallbackContext
import datetime
from spy import *
import views
import models
from prettytable import PrettyTable

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/Help\n/Sum\n/choice_action')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Time {datetime.datetime.now().time()}')

async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg=update.message.text
    print('msg')    
    await update.message.reply_text(f'{msg}')

async def choice_action(update: Update, context: CallbackContext):
    await update.message.reply_text(f'/1.Добавить запись.\n/2.Полный список.\n/3.Поиск.\n/4.Удалить запись.\n'
        + '/5.Экспорт в CSV\n/6.Экспорт в CSV (Excel)\n/7.Выход')

async def add_list(update: Update, context: CallbackContext):
    invites = ['Введите фамилию: ', 'Введите имя: ', 'Введите номер контакта: ', 'Введите категорию контакта: ']
    contact = []
    for item in invites:
        await update.message.reply_text(item)
        temp = update.message.text
        print(temp)
        contact.append(temp if len(temp) != 0 else 'None')
    models.dictionary_w(contact)



async def full_list(update: Update, context: CallbackContext):
    table= models.contacts_to_table(models.dictionary_r())
    # th = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    # table = PrettyTable(th)
    # data_list = list(map(lambda item: [el for el in item.split()], data))
    # table.add_rows(data_list)
    # table.add_autoindex("№")
    table.align = 'l'
    print(table)
    await update.message.reply_text(f'Полный список\n <pre>{table}</pre>', parse_mode=ParseMode.HTML)

""""
    str_dictionary_f = models.dictionary_r()

    match choos:
        case '1':
            print('Добавить запись')
            models.dictionary_w(views.input_data())

        case '2':
            print('Полный список')
            views.print_all(str_dictionary_f)

        case '3':
            print('Поиск')  ## ищет любое вхождение (даже несколько символов)
            data = models.search(views.input_search())
            views.print_all(data)

        case '4':
            print('Удалить запись') 
            models.delete()

        case '5':
            print('Экспорт телефонной книги в CSV')
            models.export_to_csv()

        case '6':
            print('Экспорт телефонной книги в CSV (Excel)')
            models.export_to_csv("Excel")

        case '7':
            print('Выход')
            exit()
    







 """