#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os import listdir, getcwd
import dataBase


def update():

    # List of urls
    urls = dataBase.getData()

    # List of the last titles of videos
    titles = []

    for videoTitle, url in urls.items():
        uClient = uReq(url)
        pageHtml = uClient.read()
        uClient.close()
        pageSoup = soup(pageHtml, "html.parser")
        lastVideoTitle = pageSoup.find("a", {"class": "yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
        titles.append(videoTitle + "|" + lastVideoTitle["title"])

    current_path = getcwd()
    files = listdir(current_path)
    result = []

    if "titleFile.txt" not in files:
        with open("titleFile.txt", "a"):
            pass

    with open("titleFile.txt", "r") as var:
        contents = var.readlines()

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


def choiseUser():
    print(
        "%s                    [updateVideos, Thibault Galbourdin (github.com/Liodeus)]" % (Colors.O))

    # Commands
    print("%s[1] update" % (Colors.B))
    print("%s[2] add" % (Colors.B))
    print("%s[2] delete" % (Colors.B))
    print("%s[3] list" % (Colors.B))
    print("%s[4] help" % (Colors.B))
    print("%s[5] exit" % (Colors.B))
    print("%s" % (Colors.N))


# Colors use in the program
class Colors(object):
    N = '\033[m'  # native
    R = '\033[31m'  # red
    O = '\033[33m'  # orange
    G = '\033[32m'  # green
    B = '\033[34m'  # blue