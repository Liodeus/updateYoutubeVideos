#!/usr/bin/env Python
# -*- coding: utf_8 -*-

import sqlite3
import re


# Create the table urlYoutube and 2 rows url, youtuberName
# if it doesn't already exists
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


# Insert a new row in urlYoutube table
# ask for the url then the youtuber name
def addYoutuber():
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    # Ask until the url is good
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


# Remove a row from urlYoutube and titleFile
# where name match youtuberName
def deleteYoutuber(name):
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM urlYoutube WHERE youtuberName = ?", (name, ))
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

    except:
        pass


# Get all the youtuberName and url from the
# database in a dictionnary
def listYoutuber():
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM urlYoutube")

    dicti = {v: k for k, v in cursor.fetchall()}

    connection.close()

    return dicti
