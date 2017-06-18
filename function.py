#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os import listdir, getcwd
import dataBase
import sys


# Retrieve html page from the urls, then parse them
# and compare the last video title to the title 
# in titleFile if they match no new video
def update():

    # List of urls
    urls = dataBase.listYoutuber()

    # List of the last titles of videos
    titles = []

    # For each url parse the html page and get the last video title
    for name, url in urls.items():
        try:
            uClient = uReq(url)
            pageSoup = soup(uClient, "html.parser")
            lastVideoTitle = pageSoup.find(
                "a", {"class": "yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
            titles.append(name + "|" + lastVideoTitle["title"])
        except:
            print("A problem occured with this url : ", name, " -> ", url)

    current_path = getcwd()
    files = listdir(current_path)
    result = []

    # If titleFile.txt doesn't exists create it
    if "titleFile.txt" not in files:
        with open("titleFile.txt", "a"):
            pass

    # Read the contents of the file
    with open("titleFile.txt", "r") as var:
        contents = var.readlines()

        # Write the result of each url in titleFile.txt
        with open("titleFile.txt", "w") as var2:
            for title in titles:
                var2.write(title + "\n")

        i = 0
        for content in contents:
            if content.replace("\n", "") not in titles:
                name = content.split("|")
                result.append(name[0] + " release a new video !")
            i += 1

    if len(result) == 0:
        print("No new videos available !")
    else:
        for video in result:
            print(video)


# Function that display what command you can use
# Interface and colors from : [recon-ng v4.9.1, Tim Tomes (@LaNMaSteR53)]
def choiseUser():
    print("%s                    [updateVideos, Thibault Galbourdin (github.com/Liodeus)]" % (Colors.O))

    # Commands
    print("%s[1] update" % (Colors.B))
    print("%s[2] add" % (Colors.B))
    print("%s[2] delete <name>" % (Colors.B))
    print("%s[3] list" % (Colors.B))
    print("%s[4] help" % (Colors.B))
    print("%s[5] exit" % (Colors.B))
    print("%s" % (Colors.N))

    delimiter = ("%s---------------------------------------%s" %
                 (Colors.G, Colors.N))

    while True:
        choiceUser = input("[updateVideos] > ")

        split = choiceUser.split(' ')

        if split[0] == "update":
            update()

        elif split[0] == "add":
            dataBase.addYoutuber()

        elif split[0] == "delete":
            dataBase.deleteYoutuber(split[1])

        elif split[0] == "list":
            for url, name in dataBase.listYoutuber().items():
                print(url, ":", name)

        # User need help
        elif split[0] == "help":
            if len(split) == 1:
                print("Commands (type [help <topic>]):             ")
                print(delimiter)
                print("update           Let you know witch youtuber released a new video  ")
                print("add              Insert in the database an url and a youtuber name ")
                print("delete           Remove a youtuber from the database               ")
                print("list             List all the youtuber from the database           ")
                print("help             Displays this menu                                ")
                print("exit             Exit the program                                  ")
                print(delimiter)

            elif len(split) == 2:
                if split[1] == "update":
                    print(delimiter)
                    print("update")
                    print("    Let you know witch youtuber released a new video")
                    print("    Usage: update \n")
                    print(delimiter)

                elif split[1] == "add":
                    print(delimiter)
                    print("add")
                    print("    Insert in the database an url and a youtuber name")
                    print("    Usage: add \n")
                    print(delimiter)

                elif split[1] == "delete":
                    print(delimiter)
                    print("delete")
                    print("    Insert in the database an url and a youtuber name")
                    print("    Usage: delete <name>  \n")
                    print(delimiter)

                elif split[1] == "list":
                    print(delimiter)
                    print("list")
                    print("    List all the youtuber from the database")
                    print("    Usage: list \n")
                    print(delimiter)

                else:
                    print('%s[!] No help on %s%s' %
                          (Colors.R, split[1], Colors.N))   

        elif split[0] == "exit":
            sys.exit(0)

        # Error
        else:
            print(split[0], ": not found")


# Colors use in the program
class Colors(object):
    N = '\033[m'  # native
    R = '\033[31m'  # red
    O = '\033[33m'  # orange
    G = '\033[32m'  # green
    B = '\033[34m'  # blue
