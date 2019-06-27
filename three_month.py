"""３か月間以上来ていない患者さんの集計"""
# -*- coding: utf-8 -*-
import csv
import sys

COLUMN_RE_TYPE = 0
COLUMN_RE_NAME = 4
COLUMN_RE_KARUTENUM = 13
COLUMN_RE_KATAKANA = 36

class UserInfo:
    """UserInfo class"""
    def __init__(self):
        self.karutenum = 0
        self.name = ''
        self.katakana = ''

    def printline(self):
        print(str(self.karutenum).rjust(5, ' ')
              + ', ' + self.name.ljust(10, ' ') + ', ' + self.katakana)

def main():
    """mainプログラム"""
    # 処理対象ファイル名を第１コマンドライン引数として取得
    # 第１コマンドライン引数：１ヶ月目のレセプトCSV（RECEIPTC1.csv）
    # 第２コマンドライン引数：２ヶ月目のレセプトCSV（RECEIPTC2.csv）
    # 第３コマンドライン引数：３ヶ月目のレセプトCSV（RECEIPTC3.csv）
    # 第４コマンドライン引数：４ヶ月目のレセプトCSV（RECEIPTC4.csv）
    args = sys.argv
    if len(args) != 5:
        print('第１引数に「１ヶ月目のレセプトファイル名」を指定してください')
        print('第２引数に「２ヶ月目のレセプトファイル名」を指定してください')
        print('第３引数に「３ヶ月目のレセプトファイル名」を指定してください')
        print('第４引数に「４ヶ月目のレセプトファイル名」を指定してください')
        print('例： >' + __file__ + ' RECEIPTC1.csv RECEIPTC2.csv RECEIPTC3.csv RECEIPTC4.csv')
        sys.exit(1)
    inputfile1name = args[1]
    inputfile2name = args[2]
    inputfile3name = args[3]
    inputfile4name = args[4]

    userinfolist = []

    # １つ目のレセプトCSVの読み込み
    # カルテ番号を取り込む
    with open(inputfile1name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for rowdata in spamreader:
            if rowdata[COLUMN_RE_TYPE] == 'RE':
                user = UserInfo()
                user.karutenum = int(rowdata[COLUMN_RE_KARUTENUM])
                user.name = rowdata[COLUMN_RE_NAME]
                user.katakana = rowdata[COLUMN_RE_KATAKANA]
                userinfolist.append(user)
    print(len(userinfolist))

    # ２つ目以降のレセプトCSVの読み込み
    # 取り込んだカルテ番号に合致するものがあったら、userinfolistから取り除く
    inputfiles = [inputfile2name, inputfile3name, inputfile4name]
    for inputfile in inputfiles:
        with open(inputfile, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for rowdata in spamreader:
                if rowdata[COLUMN_RE_TYPE] == 'RE':
                    karutenum = int(rowdata[COLUMN_RE_KARUTENUM])
                    for user in userinfolist:
                        if karutenum == user.karutenum:
                            userinfolist.remove(user)
        print(len(userinfolist))
    print('Success !')
    print("")

    # 結果の表示
    for user in userinfolist:
        user.printline()
    print("")
