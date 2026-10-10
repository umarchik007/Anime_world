# all_texts = {'genre': ('Janr orqali!', 'По жанру!', 'With genre'),
#              'name': ('Nomi orqali!', 'По названию!', 'By name!'),
#              'alphabet': ('Alifbo tartibida!', 'По алфавиту!', 'Alphabetically!'),
#              'likes': ('Yoqtirishlar bo\'yicha!', 'По лайкам!', 'By likes!'),
#              'language': ('Tillar!', 'Языки!', 'Languages!'),
#              'smth': ('Bundan tashqari!', 'Дополнительно!', 'Additionally!')}
# print(all_texts['smth'].index('Дополнительно!'))
# dic = {'равоаисышц':'fsc'}
# print(dic['равоаисышц'])

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
a = ''
for i in genres_translations:
        a += f',"{genres_translations[i][0]}":".","{genres_translations[i][2]}":"."'