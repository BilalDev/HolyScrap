import sqlite3
from twilio.rest import TwilioRestClient

def get_sqlite_connexion():
    return sqlite3.connect('holyscrap.db')


def add_anime(name, id):
    conn = get_sqlite_connexion()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO anime (name, id) VALUES(?, ?)", (name, id,))
        conn.commit()
        conn.close()
        print name + ' added successfuly'
    except:
        conn.commit()
        conn.close()
        print name + ' already exists or program error, contact /dev/null@nobody.gfy'


def delete_anime(name):
    conn = get_sqlite_connexion()
    c = conn.cursor()

    try:
        c.execute("DELETE FROM anime WHERE name = ?", (name,))
        conn.commit()
        conn.close()
        print name + " supprime"
    except:
        conn.commit()
        conn.close()
        print name + " n'a pas pu etre supprime"


def update_anime(uName, uId):
    conn = get_sqlite_connexion()
    c = conn.cursor()

    id_print = str(uId - 1) if isinstance(uId, (int, long)) else str(int(uId) - 1)

    try:
        c.execute("UPDATE anime SET id=? WHERE name=?", (uId, uName,))
        conn.commit()
        conn.close()
        msg = "Episode " + id_print + " de " + uName + " telecharge"
        print msg

        # Send SMS
        account_sid = "AC7c01211c7cb2d3a65029434b3c2e8b78"
        auth_token = "79235d224f7e6d1e7d88def64de9ecd4"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(to="+33666785126", from_="+33644607059",
                                             body=msg)
    except:
        conn.commit()
        conn.close()
        print "Episode " + id_print + " de " + uName + " n'a pas pu etre update"


def get_anime_from_name(name):
    conn = get_sqlite_connexion()
    c = conn.cursor()

    for row in c.execute("SELECT * FROM anime WHERE name = ?", (name,)):
        print row

    conn.close()


def get_animes():
    conn = get_sqlite_connexion()
    c = conn.cursor()
    animes = c.execute("SELECT * FROM anime order by name").fetchall()
    conn.close()
    return animes


def get_animes_for_print():
    conn = get_sqlite_connexion()
    c = conn.cursor()
    for row in c.execute("SELECT * FROM anime order by name"):
        print row

    conn.close()



def init_sql():
    conn = get_sqlite_connexion()
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS anime (name str PRIMARY KEY, id INTEGER)")

    conn.commit()
    conn.close()
