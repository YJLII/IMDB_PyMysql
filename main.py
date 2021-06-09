import gzip
import pymysql
import time
import socket

def load_title_akas():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './title.akas.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_akas(titleid, ordering, title, region, language, types, attributes, isOriginalTitle)
                    values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()


def load_title_basics():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './title.basics.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_basics(tconst, titleType, primaryTitle, originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres)
                    values (%s, %s, %s, %s, %s, %s,%s,%s,%s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()

def load_title_crew():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './title.crew.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_crew(tconst, directors, writers)
                    values (%s, %s, %s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()

def load_title_episode():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './title.episode.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_episode(tconst, parentTconst, seasonNumber, episodeNumber)
                    values (%s, %s, %s, %s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()

def load_title_principals():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './title.principals.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_principals(tconst, ordering, nconst, category,job,characters)
                    values (%s, %s, %s, %s,%s,%s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()


def load_title_ratings():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './title.ratings.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_ratings(tconst, averageRating,numVotes)
                    values (%s, %s, %s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()

def load_name_basics():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='a')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = './name.basics.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into name_basics(nconst, primaryName,birthYear,deathYear,primaryProfession,knownforTitles)
                    values (%s, %s, %s, %s, %s, %s)"""
    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0
    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows"%i)
        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql,rows)
        conn.commit()
        print("%d rows"%i)
    f.close()
    cur.close()
    conn.close()


if __name__ == '__main__':
    start_time = time.time()

#    load_title_akas()
#    load_title_basics()
#    load_title_crew()
#    load_title_episode()
   # load_title_principals()
  #  load_title_ratings()
    load_name_basics()

    elapsed_time = time.time() - start_time
    print(elapsed_time)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
