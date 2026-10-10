from telebot.types import *
from database import *

def language_choosing():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    eng = KeyboardButton('English')
    rus = KeyboardButton('Русский')
    uzb = KeyboardButton("O'zbek tili")

    kb.add(uzb, rus, eng)
    return kb

def starting_interface(language):
    all_texts = {'genre': ('Janr orqali!', 'По жанру!', 'With genre'),
                  'name': ('Nomi orqali!', 'По названию!', 'By name!'),
                  'alphabet': ('Alifbo tartibida!', 'По алфавиту!', 'Alphabetically!'),
                  'likes': ('Yoqtirishlar bo\'yicha!', 'По лайкам!', 'By likes!'),
                  'language': ('Tillar!', 'Языки!', 'Languages!'),
                  'smth': ('Bundan tashqari!', 'Дополнительно!', 'Additionally!')}

    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    with_genre = KeyboardButton(all_texts["genre"][language])
    with_name = KeyboardButton(all_texts['name'][language])
    with_alphabet = KeyboardButton(all_texts['alphabet'][language])
    with_likes = KeyboardButton(all_texts['likes'][language])
    choosing_language = KeyboardButton(all_texts['language'][language])
    something_else = KeyboardButton(all_texts['smth'][language])

    kb.add(with_genre, with_name, with_alphabet, with_likes, choosing_language, something_else)
    return kb
def something_else(language):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    something_else_button_texts = {'quantity': ('Miqdori bo\'yicha!', 'По количеству!', 'By quantity!'),
                                   'year': ('Yili bo\'yicha!!', 'По году!', 'By year!'),
                                   'rating': ('Reyting bo\'yicha!', 'По рейтингу!', 'By rating!'),
                                   'help': ('Yordam!', 'Помошь!', 'Help!'),
                                   'admins': ('Ma\'murlar!', 'Админы!', 'Admins!'),
                                   'back': ('Orqaga', 'Назад', 'Back')}

    quantity_of_episodes = KeyboardButton(something_else_button_texts['quantity'][language])
    year = KeyboardButton(something_else_button_texts['year'][language])
    with_rating = KeyboardButton(something_else_button_texts['rating'][language])
    help = KeyboardButton(something_else_button_texts['help'][language])
    admins = KeyboardButton(something_else_button_texts['admins'][language])
    back = KeyboardButton(something_else_button_texts['back'][language])
    kb.add(quantity_of_episodes, year, with_rating, help, back, admins)
    return kb

def Genre_buttons(language, chat_id):
    dictionary = str_dict(get_point(chat_id))
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
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back = KeyboardButton(genres_translations["BACK"][language])
    fantastic = KeyboardButton(f'{genres_translations["фантастика"][language]}{dictionary["фантастика"]}')
    parody = KeyboardButton(f'{genres_translations["пародия"][language]}{dictionary["пародия"]}')
    fentasy = KeyboardButton(f'{genres_translations["фэнтези"][language]}{dictionary["фэнтези"]}')
    demons = KeyboardButton(f'{genres_translations["демоны"][language]}{dictionary["демоны"]}')
    historical = KeyboardButton(f'{genres_translations["исторический"][language]}{dictionary["исторический"]}')
    jurney = KeyboardButton(f'{genres_translations["приключения"][language]}{dictionary["приключения"]}')
    samuray = KeyboardButton(f'{genres_translations["самураи"][language]}{dictionary["самураи"]}')
    strange = KeyboardButton(f'{genres_translations["сверхъестественное"][language]}{dictionary["сверхъестественное"]}')
    senen = KeyboardButton(f'{genres_translations["сёнэн"][language]}{dictionary["сёнэн"]}')
    ekshen = KeyboardButton(f'{genres_translations["экшен"][language]}{dictionary["экшен"]}')
    magic = KeyboardButton(f'{genres_translations["магия"][language]}{dictionary["магия"]}')
    comedy = KeyboardButton(f'{genres_translations["комедия"][language]}{dictionary["комедия"]}')
    superpower = KeyboardButton(f'{genres_translations["суперсила"][language]}{dictionary["суперсила"]}')
    psychology = KeyboardButton(f'{genres_translations["психология"][language]}{dictionary["психология"]}')
    triller = KeyboardButton(f'{genres_translations["триллер"][language]}{dictionary["триллер"]}')
    mistika = KeyboardButton(f'{genres_translations["мистика"][language]}{dictionary["мистика"]}')
    povsednevnost = KeyboardButton(f'{genres_translations["повседневность"][language]}{dictionary["повседневность"]}')
    dram = KeyboardButton(f'{genres_translations["драма"][language]}{dictionary["драма"]}')
    roman = KeyboardButton(f'{genres_translations["романтика"][language]}{dictionary["романтика"]}')
    detective = KeyboardButton(f'{genres_translations["детектив"][language]}{dictionary["детектив"]}')
    kb.add(back)
    kb.add(fantastic, parody, fentasy, demons, historical, jurney, samuray, strange, senen, ekshen, magic, comedy,
           superpower, psychology, triller, mistika, povsednevnost, dram, roman, detective)
    return kb

