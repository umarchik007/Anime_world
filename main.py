import telebot
from telebot import types

import buttons
from database import *
from buttons import *

# dictinary = {"фантастика": ".", "пародия": ".", "фэнтези": ".", "демоны": ".", "исторический": ".", "приключения": ".",
#              "самураи": ".", "сверхъестественное": ".", "сёнэн": ".", "экшен": ".", "магия": ".", "комедия": ".",
#              "суперсила": ".", "психология": ".", "триллер": ".", "мистика": ".", "повседневность": ".", "драма": ".",
#              "романтика": ".", "детектив": ".", "По жанру": "l"}
# first photo: AgACAgIAAxkBAAJO8maXjqwGwB07XHy-akg05LZprTUuAAIO3DEbaIXBSMQHSwO-J1QLAQADAgADcwADNQQ
# 7926831503:AAHn0H28YoX0rD5kTXp-G7nHP5jOByfxJts - TTOU
# invisible sticker:'ㅤ'
bot = telebot.TeleBot('6265808079:AAEJf_8qTzlmgUFB2KyStJoGMZC8gBUfu3Y')

Name = np.array(['Цикл_историй', 'Это_фарфоровая_кукла_влюбилась', 'Форма_голоса', 'Хьёка'])
alphabet = np.array(list('ABCDEFGHIIJKLMNOPQRSTUVWXYZ'))

@bot.message_handler(commands=['start'])
def starting_def(message, photo='AgACAgIAAxkBAAJTtWbs8VCPGZUQZcXWuoZgbx-5SFS4AAJI3TEblGdpS63wDSaVxtOHAQADAgADcwADNgQ'):
    chat_id = message.chat.id
    try:
        bot.send_photo(chat_id, photo, """Salom! Men siz uchun janr yoki sarlavha bo'yicha har qanday anime topa olaman va sizga barcha seriyalarni taqdim etaman!\n\nQaysi til qulayroq?\n----------------------
Привет! Я могу найти для вас любое аниме по жанру или по названию и предоставить вам все серии!\n\nКакой язык удобнее?\n----------------------
Hi! I can find any anime for you by genre or by title and provide you with all the episodes!\n\nWhich language is more convenient?""", reply_markup=buttons.language_choosing())
        bot.register_next_step_handler(message, Language_adding)
    except:
        bot.send_message(chat_id, '🔍', reply_markup=starting_interface(1))
    cursor.execute("DELETE FROM animesearchbotid WHERE chid = ?", (chat_id,))
    cursor.execute("INSERT INTO animesearchbotid(chid, dictinary) VALUES (?, ?);", (chat_id, '{"фантастика":".", "пародия":".", "фэнтези":".", "демоны":".", "исторический":".", "приключения":".", "самураи":"." ,"сверхъестественное":".", "сёнэн":".","экшен":".","магия":".", "комедия":".","суперсила":".", "психология":".","триллер":".", "мистика":".","повседневность":".", "драма":".","романтика":".","детектив":".", "По жанру":"l"}'))
    a.commit()

def Language_adding(message):
    chat_id = message.chat.id
    texts = ('Orqaga', 'Назад', 'Back')
    texts2 = ('Qanday qidirish kerak?', 'Каким образом искать?', 'How to search?')
    if message.text == 'O\'zbek tili':
        language_adding(chat_id, 0)
        bot.send_message(chat_id, texts2[0], reply_markup=buttons.starting_interface(0))
    elif message.text == 'Русский':
        language_adding(chat_id, 1)
        bot.send_message(chat_id, texts2[1], reply_markup=buttons.starting_interface(1))
    elif message.text == 'English':
        language_adding(chat_id, 2)
        bot.send_message(chat_id, texts2[2], reply_markup=buttons.starting_interface(2))
    elif message.text in texts:
        language = texts.index(message.text)
        bot.send_message(chat_id, texts2[language], reply_markup=starting_interface(language))
    else:
        bot.send_photo(chat_id, 'AgACAgIAAxkBAAJTtWbs8VCPGZUQZcXWuoZgbx-5SFS4AAJI3TEblGdpS63wDSaVxtOHAQADAgADcwADNgQ', """Salom! Men siz uchun janr yoki sarlavha bo'yicha har qanday anime topa olaman va sizga barcha seriyalarni taqdim etaman!\n\nQaysi til qulayroq?\n----------------------
Привет! Я могу найти для вас любое аниме по жанру или по названию и предоставить вам все серии!\n\nКакой язык удобнее?\n----------------------
Hi! I can find any anime for you by genre or by title and provide you with all the episodes!\n\nWhich language is more convenient?""", reply_markup=buttons.language_choosing())

        bot.register_next_step_handler(message, Language_adding)

def totalmessage(Name, message):
    txt = Name
    linemarkup10 = types.InlineKeyboardMarkup(row_width=2)
    buch = types.InlineKeyboardButton('Cмотреть', url=get_table_url_table(txt))
    buch0 = types.InlineKeyboardButton('❌Закрыть❌', callback_data='❌Закрыть❌')
    buch1 = types.InlineKeyboardButton('👍', callback_data=f'👍{txt}')
    buch01 = types.InlineKeyboardButton('👎', callback_data=f'👎{txt}')
    linemarkup10.add(buch)
    linemarkup10.add(buch1, buch01)
    linemarkup10.add(buch0)
    bot.send_photo(message.chat.id, get_table_photo(txt)[0],
                   f'{Name} ({list_str(get_table_Episodes(txt)).replace("Episodes","")} серий)\n\n'
                                        f'Жанр:{list_str(get_table_Genre(txt))}\nОписание:{list_str(get_table_des(txt))}', reply_markup=linemarkup10)

@bot.message_handler(content_types=['photo'])
def pxt(message):
    bot.send_message(message.chat.id, message.photo[0].file_id)
    bot.send_message(message.chat.id, message.caption)
    cursor.execute(f"UPDATE animesearchbot SET photo_id = ? WHERE Name = ?", (str(message.photo[0].file_id),message.caption))
    bot.send_photo(message.chat.id, get_table_photo(message.caption)[0])
    cursor.close()

def sth1(call, k='more animes'):
    cd = call.data.replace('more animes', '').replace('less animes', '').replace('➡️', '').replace('⬅️', '')
    chat_id = call.message.chat.id
    dictinary = str_dict(get_point(chat_id))
    sorted_items = sort_items_by_similarity(split_items_by_comma(normal_list(get_Genre())), chosen_Genre(dictinary))
    output_Name = []
    for i in sorted_items:
        output_Name.extend(get_table_Name(list_str(i)))
    i = 1
    output_Name = normal_list(output_Name)
    output_Name.remove('Haikyuu!!')
    if k == 'more animes':
        output_Name = output_Name[:10]
    linker = {'more animes': 'less animes',
              'less animes': 'more animes'}
    # bot.delete_message(chat_id, call.message.id)
    markup1 = types.InlineKeyboardMarkup(row_width=5)
    print(cd)
    print(output_Name)
    try:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'➡️{output_Name[output_Name.index(cd) + 1]+linker[k]}')
        print(output_Name[output_Name.index(cd) + 1])
        buttun00 = types.InlineKeyboardButton('⬅️',
                                              callback_data=f'⬅️{output_Name[output_Name.index(cd) - 1]+linker[k]}')
    except:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'➡️{output_Name[0]+linker[k]}')
        buttun00 = types.InlineKeyboardButton('⬅️',
                                              callback_data=f'⬅️{output_Name[-2]+linker[k]}')
    markup1.add(buttun00, buttun0)
    markup1.add(types.InlineKeyboardButton(k,
                                           callback_data=f'⬅️{k+cd}'))#recently
    location = ['*' if i == cd else '' for i in output_Name]
    print(len(output_Name))
    while i <= len(output_Name):
        try:
            buttun1 = types.InlineKeyboardButton(str(i)+location[i - 1], callback_data=output_Name[i - 1])
            buttun2 = types.InlineKeyboardButton(str(i + 1)+location[i], callback_data=output_Name[i])
            buttun3 = types.InlineKeyboardButton(str(i + 2)+location[i + 1], callback_data=output_Name[i + 1])
            buttun4 = types.InlineKeyboardButton(str(i + 3)+location[i + 2], callback_data=output_Name[i + 2])
            buttun5 = types.InlineKeyboardButton(str(i + 4)+location[i + 3], callback_data=output_Name[i + 3])
            markup1.add(buttun1, buttun2, buttun3, buttun4, buttun5)
        except:
            print('it gets limit')

        i += 5
    bot.edit_message_media(message_id=call.message.id, chat_id=chat_id,
                           media=types.InputMediaPhoto(get_table_photo(cd)[0])
                           ,reply_markup=markup1)
    bot.edit_message_caption(message_id=call.message.id, chat_id=chat_id, caption=get_table_des(cd), reply_markup=markup1)
    # bot.edit_message_media(message_id=call.message.id, chat_id=chat_id, media=get_table_photo(cd)[0])
def sth2(call, output_Name):
    cd = call.data.replace('+a', '')
    chat_id = call.message.chat.id
    i = 1
    # bot.delete_message(chat_id, call.message.id)
    markup1 = types.InlineKeyboardMarkup(row_width=5)
    print(cd)
    print(output_Name)
    try:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'+a{output_Name[output_Name.index(cd) + 1]}')
        print(output_Name[output_Name.index(cd) + 1]+'   here 103 line')
        buttun00 = types.InlineKeyboardButton('⬅️',
                                              callback_data=f'+a{output_Name[output_Name.index(cd) - 1]}')
    except:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'+a{output_Name[0]}')
        try:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                  callback_data=f'+a{output_Name[-2]}')#errors connected with the system of changing photos
        except:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                  callback_data=f'+a{output_Name[0]}')
        print('here 111 line')
    markup1.add(buttun00, buttun0)
    location = ['*' if i == cd else '' for i in output_Name]
    print(len(output_Name))
    while i <= len(output_Name):
        try:
            buttun1 = types.InlineKeyboardButton(str(i)+location[i - 1], callback_data=output_Name[i - 1])
            buttun2 = types.InlineKeyboardButton(str(i + 1)+location[i], callback_data=output_Name[i])
            buttun3 = types.InlineKeyboardButton(str(i + 2)+location[i + 1], callback_data=output_Name[i + 1])
            buttun4 = types.InlineKeyboardButton(str(i + 3)+location[i + 2], callback_data=output_Name[i + 2])
            buttun5 = types.InlineKeyboardButton(str(i + 4)+location[i + 3], callback_data=output_Name[i + 3])
            markup1.add(buttun1, buttun2, buttun3, buttun4, buttun5)
        except:
            for i in range(len(output_Name) % 5):#here can be some errors if it happens just delete the lines
                markup1.add(types.InlineKeyboardButton(str(i+1), callback_data=output_Name[i]),)#here can be some errors if it happens just delete the lines
            print('it gets limit')
        i += 5
    try:
        bot.edit_message_media(message_id=call.message.id, chat_id=chat_id,
                               media=types.InputMediaPhoto(
                                   get_table_photo(cd)[0])
                               , reply_markup=markup1)
        bot.edit_message_caption(message_id=call.message.id, chat_id=chat_id, caption=get_table_des(cd) , reply_markup=markup1)
    except:
        bot.send_photo(chat_id, get_table_photo(cd)[0],get_table_des(cd), reply_markup=markup1)
def sth3(call,output_Name,k = 'more animes'):
    cd = call.data.replace('-a1', '').replace('more animes', '').replace('less animes', '')
    chat_id = call.message.chat.id
    i = 1
    # bot.delete_message(chat_id, call.message.id)
    linker = {'more animes': 'less animes',
              'less animes': 'more animes'}
    markup1 = types.InlineKeyboardMarkup(row_width=5)
    print(cd)
    print(output_Name)
    try:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'-a1{output_Name[output_Name.index(cd) + 1]+linker[k]}')
        print(output_Name[output_Name.index(cd) + 1]+'   here 145 line')
        buttun00 = types.InlineKeyboardButton('⬅️',
                                              callback_data=f'-a1{output_Name[output_Name.index(cd) - 1]+linker[k]}')
    except:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'-a1{output_Name[0]+linker[k]}')
        try:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                  callback_data=f'-a1{output_Name[-2]+linker[k]}')#errors connected with the system of changing photos
        except:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                 callback_data=f'-a1{output_Name[0]+linker[k]}')
        print('here 156 line')
    markup1.add(buttun00, buttun0)
    markup1.add(types.InlineKeyboardButton(k,
                                           callback_data=f'-a1{k+cd}'))
    location = ['*' if i == cd else '' for i in output_Name]
    print(len(output_Name))
    while i <= len(output_Name):
        try:
            buttun1 = types.InlineKeyboardButton(str(i)+location[i - 1], callback_data=output_Name[i - 1])
            buttun2 = types.InlineKeyboardButton(str(i + 1)+location[i], callback_data=output_Name[i])
            buttun3 = types.InlineKeyboardButton(str(i + 2)+location[i + 1], callback_data=output_Name[i + 1])
            buttun4 = types.InlineKeyboardButton(str(i + 3)+location[i + 2], callback_data=output_Name[i + 2])
            buttun5 = types.InlineKeyboardButton(str(i + 4)+location[i + 3], callback_data=output_Name[i + 3])
            markup1.add(buttun1, buttun2, buttun3, buttun4, buttun5)
        except:
            print('it gets limit')
        i += 5
    bot.edit_message_media(message_id=call.message.id, chat_id=chat_id,
                           media=types.InputMediaPhoto(
                               get_table_photo(cd)[0])
                           , reply_markup=markup1)
    bot.edit_message_caption(message_id=call.message.id, chat_id=chat_id, caption=get_table_des(cd), reply_markup=markup1)
def sth4(call,output_Name,k = 'more animes'):
    cd = call.data.replace('-a2', '').replace('more animes', '').replace('less animes', '')
    chat_id = call.message.chat.id
    i = 1
    # bot.delete_message(chat_id, call.message.id)
    markup1 = types.InlineKeyboardMarkup(row_width=5)
    print(cd)
    print(output_Name)
    linker = {'more animes': 'less animes',
              'less animes': 'more animes'}
    try:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'-a2{output_Name[output_Name.index(cd) + 1]+linker[k]}')
        print(output_Name[output_Name.index(cd) + 1]+'   here 145 line')
        buttun00 = types.InlineKeyboardButton('⬅️',
                                              callback_data=f'-a2{output_Name[output_Name.index(cd) - 1]+linker[k]}')
    except:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'-a2{output_Name[0]+linker[k]}')
        try:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                callback_data=f'-a2{output_Name[-2]+linker[k]}')#errors connected with the system of changing photos
        except:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                 callback_data=f'-a2{output_Name[0]+linker[k]}')
        print('here 156 line')
    markup1.add(buttun00, buttun0)
    markup1.add(types.InlineKeyboardButton(k,
                                           callback_data=f'-a2{k+cd}'))
    location = ['*' if i == cd else '' for i in output_Name]
    print(len(output_Name))
    while i <= len(output_Name):
        try:
            buttun1 = types.InlineKeyboardButton(str(i)+location[i - 1], callback_data=output_Name[i - 1])
            buttun2 = types.InlineKeyboardButton(str(i + 1)+location[i], callback_data=output_Name[i])
            buttun3 = types.InlineKeyboardButton(str(i + 2)+location[i + 1], callback_data=output_Name[i + 1])
            buttun4 = types.InlineKeyboardButton(str(i + 3)+location[i + 2], callback_data=output_Name[i + 2])
            buttun5 = types.InlineKeyboardButton(str(i + 4)+location[i + 3], callback_data=output_Name[i + 3])
            markup1.add(buttun1, buttun2, buttun3, buttun4, buttun5)
        except:
            print('it gets limit')
        i += 5
    bot.edit_message_media(message_id=call.message.id, chat_id=chat_id,
                           media=types.InputMediaPhoto(
                               get_table_photo(cd)[0])
                           , reply_markup=markup1)
    bot.edit_message_caption(message_id=call.message.id, chat_id=chat_id, caption=get_table_des(cd), reply_markup=markup1)
def sth5(call,output_Name,k = 'more animes'):
    cd = call.data.replace('-a3', '').replace('more animes', '').replace('less animes', '')
    chat_id = call.message.chat.id
    i = 1
    # bot.delete_message(chat_id, call.message.id)
    markup1 = types.InlineKeyboardMarkup(row_width=5)
    print(cd)
    print(output_Name)
    linker = {'more animes': 'less animes',
              'less animes': 'more animes'}
    try:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'-a3{output_Name[output_Name.index(cd) + 1]+linker[k]}')
        print(output_Name[output_Name.index(cd) + 1]+'   here 145 line')
        buttun00 = types.InlineKeyboardButton('⬅️',
                                              callback_data=f'-a3{output_Name[output_Name.index(cd) - 1]+linker[k]}')
    except:
        buttun0 = types.InlineKeyboardButton('➡️',
                                             callback_data=f'-a3{output_Name[0]+linker[k]}')
        try:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                callback_data=f'-a3{output_Name[-2]+linker[k]}')#errors connected with the system of changing photos
        except:
            buttun00 = types.InlineKeyboardButton('⬅️',
                                                 callback_data=f'-a3{output_Name[0]+linker[k]}')
        print('here 156 line')
    markup1.add(buttun00, buttun0)
    markup1.add(types.InlineKeyboardButton(k,
                                                 callback_data=f'-a3{k+cd}'))
    location = ['*' if i == cd else '' for i in output_Name]
    print(len(output_Name))
    while i <= len(output_Name):
        try:
            buttun1 = types.InlineKeyboardButton(str(i)+location[i - 1], callback_data=output_Name[i - 1])
            buttun2 = types.InlineKeyboardButton(str(i + 1)+location[i], callback_data=output_Name[i])
            buttun3 = types.InlineKeyboardButton(str(i + 2)+location[i + 1], callback_data=output_Name[i + 1])
            buttun4 = types.InlineKeyboardButton(str(i + 3)+location[i + 2], callback_data=output_Name[i + 2])
            buttun5 = types.InlineKeyboardButton(str(i + 4)+location[i + 3], callback_data=output_Name[i + 3])
            markup1.add(buttun1, buttun2, buttun3, buttun4, buttun5)
        except:
            print('it gets limit')
        i += 5
    bot.edit_message_media(message_id=call.message.id, chat_id=chat_id,
                           media=types.InputMediaPhoto(
                               get_table_photo(cd)[0])
                           , reply_markup=markup1)
    bot.edit_message_caption(message_id=call.message.id, chat_id=chat_id, caption=get_table_des(cd), reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def txt(message):
    chat_id = message.chat.id
    txt = message.text.replace('ㅤ', '').replace('✅', '')

    all_texts = {'genre': ['Janr orqali!', 'По жанру!', 'With genre'],
                  'name': ('Nomi orqali!', 'По названию!', 'By name!'),
                  'alphabet': ('Alifbo tartibida!', 'По алфавиту!', 'Alphabetically!'),
                  'likes': ('Yoqtirishlar bo\'yicha!', 'По лайкам!', 'By likes!'),
                  'language': ('Tillar!', 'Языки!', 'Languages!'),
                  'smth': ('Bundan tashqari!', 'Дополнительно!', 'Additionally!')}

    something_else_button_texts = {'quantity': ('Miqdori bo\'yicha!', 'По количеству!', 'By quantity!'),
                                   'year': ('Yili bo\'yicha!!', 'По году!', 'By year!'),
                                   'rating': ('Reyting bo\'yicha!', 'По рейтингу!', 'By rating!'),
                                   'help': ('Yordam!', 'Помошь!', 'Help!'),
                                   'admins': ('Ma\'murlar!', 'Админы!', 'Admins!'),
                                   'back': ('Orqaga', 'Назад', 'Back')}

    genres_translations = {
        'фантастика': ('Fantastika', 'Фантастика', 'Fantastic'),
        'пародия': ('Parodiya', 'Пародия', 'Parody'),
        'фэнтези': ('Fentezi', 'Фэнтези', 'Fantasy'),
        'демоны': ('Jinlar', 'Демоны', 'Demons'),
        'исторический': ('Tarixiy', 'Исторический', 'Historical'),
        'приключения': ('Sarguzashtlar', 'Приключения', 'Adventures'),
        'самураи': ('Samuraylar', 'Самураи', 'Samurai'),
        'сверхъестественное': ('G\'ayritabiiy', 'Сверхъестественное', 'The Supernatural'),
        'сёнэн': ('Shonen', 'Сёнэн', 'Senen'),
        'экшен': ('Harakat', 'Экшен', 'Action'),
        'магия': ('Sehr', 'Магия', 'Magic'),
        'комедия': ('Komediya', 'Комедия', 'Comedy'),
        'суперсила': ('Super kuch', 'Суперсила', 'Superpower'),
        'психология': ('Psixologiya', 'Психология', 'Psychology'),
        'триллер': ('Triller', 'Триллер', 'Thriller'),
        'мистика': ('Tasavvuf', 'Мистика', 'Mysticism'),
        'повседневность': ('Kundalik hayot', 'Повседневность', 'Everyday life'),
        'драма': ('Drama', 'Драма', 'Drama'),
        'романтика': ('Romantika', 'Романтика', 'Romance'),
        'детектив': ('Detektiv', 'Детектив', 'Detective'),
        'BACK': ('Orqaga', 'Назад', 'Back')
    }
    genres_translations1 = []
    for i in genres_translations:
        genres_translations1.append(genres_translations[i][0])
        genres_translations1.append(genres_translations[i][1])
        genres_translations1.append(genres_translations[i][2])

    if txt in all_texts['smth']:
        language = all_texts['smth'].index(txt)
        text = {'text': ('Qo\'shimcha funktsiyalar:', 'Дополнительные функции:', 'Additional functions:')}
        bot.send_message(chat_id, text['text'][language], reply_markup=something_else(language))

    elif txt in all_texts['language']:
        starting_def(message)

    elif txt in something_else_button_texts['back']:
        Language_adding(message)
    
    elif txt in something_else_button_texts['admins']:
        bot.send_message(chat_id, '1) @Mr_Umar_Fozilov\n2) @Ibow_auf')

    elif txt in something_else_button_texts['help']:
        language = something_else_button_texts['help'].index(txt)
        text = {'text': ('Yordamingiz uchun tashakkur!', 'Cпасибо за помошь!', 'Thanks for the help!')}
        bot.send_message(chat_id, text['text'][language])

    elif txt in all_texts['genre'] or txt in Genre:
        language = all_texts['genre'].index(txt)
        text = {'text': ('Janrlarni tanlang!', 'Выберите жанры!', 'Choose genres!')}
        bot.send_message(chat_id, text['text'][language], reply_markup=Genre_buttons(language, chat_id))
        # bot.register_next_step_handler(message, by_genre)

    elif txt == 'По алфавиту!':
        l = types.InlineKeyboardMarkup()
        n = 0
        while n < len(alphabet):
            b1 = types.InlineKeyboardButton(alphabet[n], callback_data=alphabet[n])
            b2 = types.InlineKeyboardButton(alphabet[n + 1], callback_data=alphabet[n + 1])
            try:
                b3 = types.InlineKeyboardButton(alphabet[n + 2], callback_data=alphabet[n + 2])
                b4 = types.InlineKeyboardButton(alphabet[n + 3], callback_data=alphabet[n + 3])
                b5 = types.InlineKeyboardButton(alphabet[n + 4], callback_data=alphabet[n + 4])
            except:
                pass
            n += 5
            l.add(b1, b2, b3, b4, b5)
        bot.send_message(chat_id, 'aytchjgfcchtrxehxcvhrdxhfxd', reply_markup=l)

    elif txt == 'ПОИСК':
        mu = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, 'отправьте название нужного аниме в бот', reply_markup=mu)


    elif txt == 'По количеству':
        print(get_Episodes_())
        # sth3(message,get_Episodes_())
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        buttun0 = types.InlineKeyboardButton('➡️', callback_data=f'-a1{get_Episodes_()[0]}')
        buttun00 = types.InlineKeyboardButton('⬅️', callback_data=f'-a1{get_Episodes_()[0]}')
        markup1.add(buttun00, buttun0)
        bot.send_photo(chat_id, get_table_photo(get_Episodes_()[0])[0],reply_markup=markup1)
    elif txt == 'По рейтингу':
        print(get_Rating_())
        # sth3(message,get_Episodes_())
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        buttun0 = types.InlineKeyboardButton('➡️', callback_data=f'-a2{get_Rating_()[0]}')
        buttun00 = types.InlineKeyboardButton('⬅️', callback_data=f'-a2{get_Rating_()[0]}')
        markup1.add(buttun00, buttun0)
        bot.send_photo(chat_id, get_table_photo(get_Rating_()[0])[0],
                       reply_markup=markup1)
        bot.send_message(chat_id, list_str(get_Rating_()))
    elif txt == 'По году':
        bot.send_message(chat_id, list_str(get_Year_()))
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        buttun0 = types.InlineKeyboardButton('➡️', callback_data=f'-a3{get_Year_()[0]}')
        buttun00 = types.InlineKeyboardButton('⬅️', callback_data=f'-a3{get_Year_()[0]}')
        markup1.add(buttun00, buttun0)
        bot.send_photo(chat_id, get_table_photo(get_Year_()[0])[0],
                       reply_markup=markup1)

    elif txt in genres_translations1:
        uzb, rus, eng, i = [], [], [], 0
        while i < len(genres_translations1):
            uzb.append(genres_translations1[i])
            i += 1
            rus.append(genres_translations1[i])
            i += 1
            eng.append(genres_translations1[i])
            i += 1
        chat_id = message.chat.id
        dictionary = str_dict(get_point(chat_id))
        if txt in uzb:
            language = 0
        elif txt in rus:
            language = 1
        elif txt in eng:
            language = 2
        txt = str(message.text).lower()
        txt = txt.replace('ㅤ', '')
        if dictionary[txt] == 'ㅤ':
            dictionary[txt] = '✅'
            cursor.execute("UPDATE animesearchbotid SET dictinary = ? WHERE chid = ?", (str(dictionary), chat_id))
        elif dictionary[txt] == '✅':
            dictionary[txt] = 'ㅤ'
            cursor.execute("UPDATE animesearchbotid SET dictinary = ? WHERE chid = ?", (str(dictionary), chat_id))
        a.commit()

        bot.send_message(chat_id, '🔍', reply_markup=Genre_buttons(language, chat_id))

        sorted_items = sort_items_by_similarity(split_items_by_comma(normal_list(get_Genre())),
                                                chosen_Genre(dictionary))
        print(str(normal_list(get_Genre())) + '=get_Genre')
        print(str(chosen_Genre(dictionary)) + '=chosen_Genre')
        print(str(sorted_items) + '=sorted_items')
        # a.commit()
        output_Name = []
        for i in sorted_items:
            output_Name.extend(get_table_Name(list_str(i)))
        i = 1
        output_Name = normal_list(output_Name)[:11]
        output_Name.remove('Haikyuu!!')
        print(output_Name)
        markup1 = types.InlineKeyboardMarkup(row_width=5)
        buttun0 = types.InlineKeyboardButton('➡️', callback_data=f'➡️{output_Name[1]}')
        buttun00 = types.InlineKeyboardButton('⬅️', callback_data=f'⬅️{output_Name[0]}')
        markup1.add(buttun00, buttun0)
        markup1.add(types.InlineKeyboardButton('more animes',
                                               callback_data=f'➡️more animes{output_Name[1]}'))

        while i <= len(output_Name):
            try:
                buttun1 = types.InlineKeyboardButton(str(i), callback_data=output_Name[i - 1])
                buttun2 = types.InlineKeyboardButton(str(i + 1), callback_data=output_Name[i])
                buttun3 = types.InlineKeyboardButton(str(i + 2), callback_data=output_Name[i + 1])
                buttun4 = types.InlineKeyboardButton(str(i + 3), callback_data=output_Name[i + 2])
                buttun5 = types.InlineKeyboardButton(str(i + 4), callback_data=output_Name[i + 3])
            except:
                print('it gets limit')
            markup1.add(buttun1, buttun2, buttun3, buttun4, buttun5)
            i += 5
        bot.send_photo(chat_id, get_table_photo(output_Name[0])[0]
                       , get_table_des(output_Name[0]), reply_markup=markup1)
        bot.delete_message(chat_id, message.id - 1)
        try:
            bot.delete_message(chat_id, message.id - 2)
        except:
            pass

    else:
        print('417')
        try:
            totalmessage(find_closest_word(get_Name(), txt), message)
        except:
            bot.send_message(chat_id, 'there is no anime with such name please contact with administration.')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        cd = call.data
        chat_id = call.message.chat.id
        if cd in alphabet or '+a' in cd:
            # print(cd+'  abs')
            # print(list_str(get_table_Name_by_first_letter(cd[0]))+'  abs')
            sth2(call, get_table_Name_by_first_letter(cd.replace('+a', '')[0]))
            bot.send_message(chat_id, get_table_Name_by_first_letter(cd))#finish it-some errors about the type of infor
        if 'more anime' not in cd:
            if '-a1' in cd:
                sth3(call, get_Episodes_()[:11])
                print(get_Episodes_()[:11])
            elif '-a2' in cd:
                sth4(call, get_Rating_()[:11])
            elif '-a3' in cd:
                sth5(call, get_Year_()[:11])
            elif '➡️' in cd or '⬅️' in cd:
                sth1(call)
        else:
            if '-a1' in cd:
                sth3(call, get_Episodes_(), 'less animes')
                print(get_Episodes_())
            elif '-a2' in cd:
                sth4(call, get_Rating_(), 'less animes')
            elif '-a3' in cd:
                sth5(call, get_Year_(), 'less animes')
            elif '➡️' in cd or '⬅️' in cd:
                sth1(call, 'less animes')
        if cd == '❌Закрыть❌':
            bot.delete_message(chat_id, message_id=call.message.id)

            # bot.send_photo(chat_id,get_table_photo(output_Name[4].replace(' ', '_'))[0], get_table_des(output_Name[4]))
        elif cd in get_Name():
            print(cd)
            # bot.delete_message(chat_id, call.message.id)
            totalmessage(cd,call.message)
            # bot.send_photo(chat_id,'AgACAgIAAxkBAAJDpmaCiBalT3DRjbpBDvVyDVZBPeSyAAJV3DEbTmoQSPn7jfzqlvTNAQADAgADeAADNQQ' , get_table_des(cd))
# get_table_photo(cd)[0] i will use it when I fix the problem with the photos
bot.polling(none_stop=True)
