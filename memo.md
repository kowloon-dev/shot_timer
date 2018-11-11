# 開発メモ

# Raspberry Piの環境構築

## 環境

- Raspberry Pi A+
- Raspbian Jessie lite


## pip3のインストール

```
$ sudo apt-get install python3-pip

```


## wiringPiのインストール

Raspbian-Jessie Liteの初期状態でwiringPiがインストールされていなかった  
(下記のようにImportでエラーとなる)

```
$ python3

Python 3.5.3 (default, Jan 19 2017, 14:11:04)

>>> import wiringpi as pi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'wiringpi'
```

pip3でwiringpiをインストール

```
$ sudo pip3 install wiringpi
<snip>
Successfully installed wiringpi-2.46.0

$ python3

Python 3.5.3 (default, Jan 19 2017, 14:11:04)
>>> import wiringpi as pi
>>>    (エラー無し、Import成功)

```


# I2Cの準備

## I2Cの有効化

```
$ sudo raspi-config
```

![i2c_enable-01](http://archive.kowloonet.org/github/raspi-a-I2C-enable_01.png)


![i2c_enable-02](http://archive.kowloonet.org/github/raspi-a-I2C-enable_02.png)


![i2c_enable-03](http://archive.kowloonet.org/github/raspi-a-I2C-enable_03.png)


![i2c_enable-04](http://archive.kowloonet.org/github/raspi-a-I2C-enable_04.png)


## I2Cライブラリのインストール

```
$ sudo apt-get install libi2c-dev
$ sudo apt-get install i2c-tools
```

# 使い方

1. appディレクトリに移動し、Gulpを起動

```commandline
pi@raspia-1:~ $ cd shot_timer/app
pi@raspia-1:~/shot_timer/app $ ls
buzzer.py  config_import.py  gulpfile.js  hit_check.py  log_control.py  __pycache__  result_convert.py  shot_timer.py

pi@raspia-1:~/shot_timer/app $ gulp
[13:26:15] Using gulpfile ~/shot_timer/app/gulpfile.js
[13:26:15] Starting 'browser-sync'...
[13:26:17] Finished 'browser-sync' after 1.97 s
[13:26:17] Starting 'default'...
[13:26:17] Finished 'default' after 1.43 ms
[Browsersync] Access URLs:
 --------------------------------------
       Local: http://localhost:3000
    External: http://192.168.1.130:3000   <<<==== これがブラウザのアクセス先
 --------------------------------------
          UI: http://localhost:3001
 UI External: http://localhost:3001
 --------------------------------------
[Browsersync] Serving files from: ../htdocs
```

2. ブラウザで`http://ラズパイのIP:3000`にアクセス(本例では`http://192.168.1.130:3000`)

3. もう1枚、ターミナルを上げて、shot_timer.pyを起動

4. ブザーに合わせて的を撃つ

5. ブラウザ画面がリザルトのタイムに随時更新されることを確認する