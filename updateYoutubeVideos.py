#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os import listdir, getcwd
import dataBase

# List of urls
urls = dataBase.getData()


# List of last video title
titles = []

for nom, url in urls.items():
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    last_video_title = page_soup.find("a", {
        "class": "yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
    titles.append(nom + "|" + last_video_title["title"])

current_path = getcwd()
files = listdir(current_path)
result = []

if "title_file.txt" not in files:
    with open("title_file.txt", "a"):
        pass

with open("title_file.txt", "r") as var:
    contents = var.readlines()

    with open("title_file.txt", "w") as var2:
        for title in titles:
            var2.write(title + "\n")
    i = 0
    for content in contents:
        if content.replace("\n", "") not in titles:
            name = content.split("|")
            result.append(name[0] + " a sorti une nouvelle vidéo !")
        i += 1

if len(result) == 0:
    print("Pas de nouvelle vidéos !")
else:
    for video in result:
        print(video)
