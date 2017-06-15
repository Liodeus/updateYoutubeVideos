#!/usr/bin/env Python
# -*- coding: utf_8 -*-

import dataBase
import function
import sys


def main():
    dataBase.dataBaseInit()
    function.choiseUser()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(0)
