#!/usr/bin/env Python
# -*- coding: utf_8 -*-

import sqlite3
import re


def dataBaseInit():
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM urlYoutube")
    except:
        cursor.execute(
            """CREATE TABLE urlYoutube (url text, youtuberName text)""")
        connection.commit()

    connection.close()


def addYoutuber():
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    state = True
    while state:
        url = input("Input url : ")
        youtuberName = input("Input youtuber name : ")

        # Regex that check the format of url
        if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url):
            cursor.execute('INSERT INTO urlYoutube VALUES (?, ?)',
                           (url, youtuberName))
            connection.commit()
            state = False
        else:
            print("Url problem ! It has to start with http[s]://")

    connection.close()


def deleteYoutuber(name):
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM urlYoutube WHERE youtuberName = ?", (name, ))
    connection.commit()
    connection.close()

    with open("titleFile.txt", "r") as var:
        contents = var.readlines()
        newContent = []
        for content in contents:
            val = content.split("|")
            if val[0].strip() != name:
                newContent.append(content)

    with open("titleFile.txt", "w") as var:
        var.writelines(newContent)


def listYoutuber():
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM urlYoutube")

    dicti = {v: k for k, v in cursor.fetchall()}

    connection.close()

    return dicti
