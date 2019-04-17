import psycopg2
import nltk
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

hostname = 'localhost'
username = 'postgres'  # the username when you create the database
password = 'ammaji'  # change to your password
database = 'news_scrap'


def getRepublic(conn):
    cur = conn.cursor()
    cur.execute('select "Headline" from feed_republic')
    rows = cur.fetchall()
    global s
    for row in rows:
        s += row[0]


def getNdtv(conn):
    cur = conn.cursor()
    cur.execute('select "Headline" from feed_ndtv')
    rows = cur.fetchall()
    global s
    for row in rows:
        s += row[0]


def getIndiaToday(conn):
    cur = conn.cursor()
    cur.execute('select "Headline" from feed_indiatoday')
    rows = cur.fetchall()
    global s
    for row in rows:
        s += row[0]


conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
s = ""
fd = FreqDist()
getRepublic(conn)
getNdtv(conn)
getIndiaToday(conn)
s_token = nltk.word_tokenize(s)
stop_words = stopwords.words('english')
for word in s_token:
    if word not in stop_words and word not in string.punctuation:
        fd[word.lower()] += 1

for word, frequency in fd.most_common(50):
    print(u'{};{}'.format(word, frequency))

lists = sorted(fd.most_common(10))  # sorted by key, return a list of tuples

x, y = zip(*lists)  # unpack a list of pairs into two tuples
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

plt.figure(figsize=(12, 5))
plt.plot(x, y)
plt.show()
plt.savefig('/home/imsaiful/Desktop/Major/static_cdn/img/topics.png')
conn.close()