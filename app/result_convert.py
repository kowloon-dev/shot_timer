#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
from os import path
import config_import as ci
import log_control as log
import traceback

class ResultConvert:

    def __init__(self):
        
        # テンプレート用HTMLファイルの読み込み
        try:
            self.temp_html = open(ci.template_file, 'r', encoding='utf-8')
        except:
            err = "テンプレート用HTMLファイルの読み込みに失敗.\n"
            log.logging.error(err + traceback.format_exc())
            raise

        # 読み取ったテンプレートHTMLをBeautifulSoupで解釈
        try:
            self.soup = BeautifulSoup(self.temp_html, "html.parser")
        except:
            err = "テンプレート用HTMLファイルをBeautifulSoupに食わせる処理が失敗.\n"
            log.logging.error(err + traceback.format_exc())
            raise
            

    # メイン処理からヒット所要時間を引数"result"で受け取り、
    # テンプレートファイルの該当箇所を置換してresult用のHTMLを上書きする関数
    def convert(self, result):

        self.soup.p.string.replace_with(str(result))
        print(self.soup)
        
        # 出力先HTMLファイルの読み込み
        try:
            result_html = open(ci.result_file, 'w', encoding='utf-8')
            result_html.write(str(self.soup))
            result_html.close()
        except:
            err = "結果出力用HTMLファイルへの書き込み処理が失敗.\n"
            log.logging.error(err + traceback.format_exc())
            raise
        
        return self.soup 