#!/usr/bin/env Python
# -*- coding: utf_8 -*-

import sqlite3
import re


def co():
    conn = sqlite3.connect("dataBase.db")
    c = conn.cursor()

    try:
        c.execute("""CREATE TABLE urlYoutube (url text, youtuberName text)""")
        conn.commit()
    except:
        print("error")

    url = input("Saisie url : ")
    nomYoutuber = input("Nom youtuber : ")

    # use regex pour verifier l'url
    if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url):
        print(url)
        print(nomYoutuber)
        c.execute('INSERT INTO urlYoutube VALUES (?, ?)', (url, nomYoutuber))
        conn.commit()
    else:
        print("url mauvais format")

    conn.close()


def getData():
    conn = sqlite3.connect("dataBase.db")
    c = conn.cursor()

    c.execute("SELECT * FROM urlYoutube")

    dico = {v: k for k, v in c.fetchall()}
    print(dico)
    conn.close()

    return dico


if __name__ == "__main__":
    co()
