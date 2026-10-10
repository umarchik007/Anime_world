import sqlite3
import numpy as np
from difflib import SequenceMatcher
import ast  # Import ast module for safely evaluating the string representation of a dictionary


a = sqlite3.connect('searchbotf23.db', check_same_thread=False)
cursor = a.cursor()#anime information

cursor.execute("""CREATE TABLE IF NOT EXISTS user_language(
    User_id TEXT,
    Language INT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS animesearchbot(
    Name TEXT,
    photo_id TEXT,
    Description TEXT,
    url_table TEXT,
    Genre TEXT,
    Rating INT,
    Episodes INT,
    Year INT)""")#Nameni ulash kere; anime info table

cursor.execute("""CREATE TABLE IF NOT EXISTS animesearchbotg(
    Genre TEXT,
    Name TEXT)""")#Nameni ulash kere; Genre table


cursor.execute("""CREATE TABLE IF NOT EXISTS animesearchbotid(
    chid TEXT,
    dictinary TEXT)""")#id table and choices
a.commit()


Genre = np.array(['фантастика', 'пародия', 'фэнтези', 'демоны', 'исторический', 'приключения',
                   'самураи', 'сверхъестественное', 'сёнэн', 'экшен', 'магия', 'комедия', 'суперсила', 'психология',
                   'триллер', 'мистика', 'повседневность', 'драма', 'романтика', 'детектив'])

from difflib import SequenceMatcher

def find_closest_word(word_list, target_word, threshold=0.4):
    closest_word = None
    highest_similarity = 0.0

    for word in word_list:
        similarity = SequenceMatcher(None, word, target_word).ratio()
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_word = word

    if highest_similarity < threshold:
        return None

    return closest_word

def remove_duplicates_keep_one(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


def get_Genre():
    cursor.execute("SELECT Genre FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1

def str_dict(str_dict):
    try:
        dictionary = ast.literal_eval(str_dict)
        for i in dictionary:
            if dictionary[i] == '.':
                dictionary[i] = 'ㅤ'
        return dictionary
    except ValueError:
        print("Error: Unable to convert the string to a dictionary.")

def normal_list(data):
    normal_list = [item[0] for item in data]
    return normal_list

def split_items_by_comma(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item.split(","))
    return output_list

def sort_items_by_similarity(items, target_list):
    scores = []
    for item in items:
        matcher = SequenceMatcher(None, item, target_list)
        score = matcher.ratio()
        scores.append((item, score))

    sorted_items = sorted(scores, key=lambda x: x[1], reverse=True)

    return [item[0] for item in sorted_items]


def chosen_Genre(dictinary):
    list = []
    for i in dictinary.items():
        if i[1] == '*':
            list.append(i[0])
    return list

def get_all_clients():
    cursor.execute("SELECT chid FROM animesearchbotid")
    a1 = cursor.fetchall()
    a.commit()
    return a1

def get_table_url_table(Name):
    cursor.execute("SELECT url_table FROM animesearchbot WHERE Name = ?", (Name,))
    a1 = cursor.fetchone()
    a.commit()
    return a1[0]

def get_url_table():
    cursor.execute("SELECT url_table FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1

def get_table_photo(Name):
    cursor.execute("SELECT photo_id FROM animesearchbot WHERE Name = ?", (Name,))
    a1 = cursor.fetchone()
    a.commit()
    return a1

def get_photo():
    cursor.execute("SELECT photo_id FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1

def get_table_des(Name):
    cursor.execute("SELECT Description FROM animesearchbot WHERE Name = ?", (Name,))
    a1 = cursor.fetchone()
    a.commit()
    return a1

def get_des():
    cursor.execute("SELECT Description FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1

def get_table_Episodes(Name):
    cursor.execute("SELECT Episodes FROM animesearchbot WHERE Name = ?", (Name,))
    a1 = cursor.fetchone()
    a.commit()
    return a1

def get_order():
    cursor.execute("SELECT Episodes FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1

def get_table_Genre(Name):#vse janri uje budut imet shtrihi
    cursor.execute("SELECT Genre FROM animesearchbot WHERE Name = ?", (Name,))
    a1 = cursor.fetchone()
    a.commit()
    return a1


def convert_to_number(item):
    if 'Episodes' in item:
        return int(item.split()[0])
    elif 'Movie' in item:
        return 0
    else:
        return None  # Or handle other cases if necessary



def get_Episodes_():
    list0 = []
    cursor.execute("SELECT Episodes FROM animesearchbot")
    a1 = remove_duplicates_keep_one(normal_list(cursor.fetchall()))
    a1 = [convert_to_number(item) for item in a1]
    a1.sort()
    a.commit()
    for i in a1:
        cursor.execute("SELECT Name FROM animesearchbot WHERE Episodes = ?", (str(i) + (' Episodes'),))
        b = normal_list(cursor.fetchall())
        list0.extend(b)
    a.commit()
    list0.reverse()
    return list0




def get_Rating_():
    list0 = []
    cursor.execute("SELECT Rating FROM animesearchbot")
    a1 = remove_duplicates_keep_one(normal_list(cursor.fetchall()))
    a1.sort()
    a.commit()
    for i in a1:
        cursor.execute("SELECT Name FROM animesearchbot WHERE Rating = ?", (i,))
        b = normal_list(cursor.fetchall())
        list0.extend(b)
    a.commit()
    return list0


def get_all_rating():
    cursor.execute("SELECT Rating FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1




def get_Year_():
    list0 = []
    cursor.execute("SELECT Year FROM animesearchbot")
    a1 = cursor.fetchall()
    a1.sort()
    a.commit()
    for i in remove_duplicates_keep_one(normal_list(a1)):
        cursor.execute("SELECT Name FROM animesearchbot WHERE Year = ?", (i,))
        b = normal_list(cursor.fetchall())
        print(b)
        list0.extend(b)
    a.commit()
    list0.reverse()
    return list0


def get_openingnight():
    cursor.execute("SELECT Year FROM animesearchbot")
    a1 = cursor.fetchall()
    a.commit()
    return a1
def get_Name():
    cursor.execute("SELECT Name FROM animesearchbot")
    a1 = normal_list(cursor.fetchall())
    a.commit()
    return a1

def get_table_Name_by_first_letter(letter):
    a1 = get_Name()
    outcome = []
    for i in a1:
        if i[0].lower() == letter.lower():
            outcome.append(i)
    return outcome


def get_point(chid):
    cursor.execute("SELECT dictinary FROM animesearchbotid WHERE chid = ?", (chid, ))
    a1 = cursor.fetchone()
    a2 = f'{a1[0][:-1]},"fantastika":".","fantastic":".","Parodiya":".","Parody":".","Fentezi":".","Fantasy":".","Jinlar":".","Demons":".","Tarixiy":".","Historical":".","Sarguzashtlar":".","Adventures":".","Samuraylar":".","Samurai":".","G\'ayritabiiy":".","The Supernatural":".","Shonen":".","Senen":".","Harakat":".","Action":".","Sehr":".","Magic":".","Komediya":".","Comedy":".","Super kuch":".","Superpower":".","Psixologiya":".","Psychology":".","Triller":".","Thriller":".","Tasavvuf":".","Mysticism":".","Kundalik hayot":".","Everyday life":".","Drama":".","Drama":".","Romantika":".","Romance":".","Detektiv":".","Detective":"."'+'}'
    return a2.lower()


def list_str(list):
    genre_list = list
    Genre_string = ','.join(genre_list)
    return Genre_string

def get_table_Name(Genre):
    cursor.execute("SELECT NAME FROM animesearchbot WHERE Genre = ?", (Genre, ))
    return cursor.fetchall()

def language_adding(id, language):
    # cursor.execute("INSERT INTO user_language(User_id, Language) VALUES (?, ?);", (id, language))
    # a.commit()
    pass