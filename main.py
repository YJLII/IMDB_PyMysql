import gzip
import pymysql
import time
import socket

def make_table_Aliases():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Aliases.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Aliases(title_id, ordering, title, region, language, is_original_title)
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


def make_table_Title_ratings():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Title_ratings.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into title_ratings(title_id, average_rating, num_votes)
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

def make_table_Titles():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Titles.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Titles(title_id, title_type, primary_title,original_title,is_adult,start_year,end_year,runtime_minutes)
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

def make_table_Alias_types():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Alias_types.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Alias_types(title_id, ordering, type)
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

def make_table_Alias_attributes():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Alias_attributes.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Alias_attributes(title_id, ordering, attribute)
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


def make_table_Episode_belongs_to():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Episode_belongs_to.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Episode_belongs_to(episode_title_id, parent_tv_show_title_id,season_number,episode_number)
                    values (%s, %s, %s,%s)"""
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

def make_table_Title_genres():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Title_genres.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Title_genres(title_id,genre)
                    values (%s, %s)"""
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


def make_table_Names_():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Names_.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Names_(name_id,name_,birth_year,death_year)
                    values (%s, %s,%s,%s)"""
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



def make_table_Name_worked_as():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Name_worked_as.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Name_worked_as(name_id,profession)
                    values (%s, %s)"""
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



def make_table_Had_role():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Had_role.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Had_role(title_id,name_id,role_)
                    values (%s, %s,%s)"""
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



def make_table_Known_for():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Known_for.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Known_for(name_id,title_id)
                    values (%s, %s)"""
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




def make_table_Directors():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Directors.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Directors(title_id,name_id)
                    values (%s, %s)"""
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




def make_table_Writers():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Writers.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Writers(title_id,name_id)
                    values (%s, %s)"""
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




def make_table_Principals():
    conn = pymysql.connect(host="localhost", user='LeeYooJoon', password='db2020', db='homework')
    cur = conn.cursor(pymysql.cursors.DictCursor)
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = 'Principals.tsv'
    f = open(file_name, "r", encoding='UTF-8')
    insert_sql = """insert into Principals(title_id,ordering,name_id,job_category,job)
                    values (%s, %s, %s, %s, %s)"""
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

   # make_table_Aliases() #수정함
   # make_table_Title_ratings()
 #   make_table_Titles() #수정 필요
 #   make_table_Alias_types()
 #   make_table_Alias_attributes()
  #  make_table_Episode_belongs_to() #수정 필요 // season Number
  #  make_table_Title_genres()
    make_table_Names_() #death_year 필요해
   # make_table_Name_worked_as()
 #   make_table_Had_role()
 #   make_table_Known_for()
 #   make_table_Directors()
 #   make_table_Writers()
 #   make_table_Principals()
    elapsed_time = time.time() - start_time
    print(elapsed_time)

