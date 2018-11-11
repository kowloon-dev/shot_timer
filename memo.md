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

# Amazon Dashボタン連携

## Pythonモジュールのインストール

```commandline
sudo pip3 install amazon-dash

```

## DashボタンのDiscovery

```commandline
$ sudo amazon-dash discovery
Welcome to Amazon-dash v1.3.1 using Python 3.5.3
The discovery command lists the devices that are connected in your network. Each device will only be listed once. After executing this command wait approximately 10 seconds before pressing the Amazon Dash button. After pressing the button, the Mac address of the button will immediately appear on the screen. Remember the address to be able to create the configuration file.

(Dashボタンを押下)

c8:4c:75:xx:xx:xx
cc:e1:d5:xx:xx:xx
18:74:2e:xx:xx:xx (Amazon Device)   ←検出されたことを確認

Ctrl+Cで終了
```

## yamlファイルの準備

```commandline
cd shot_timer/app/
vi amazon-dash.yml
```

amazon-dash.yml
```yaml
settings:
  delay: 5
devices:
  18:74:2e:xx:xx:xx:   ←DashボタンのMACアドレス(末尾のコロンは必要)
    name: (Dashボタン本体のラベル名など)
    user: pi
    cmd:  /usr/bin/python3 /home/pi/shot_timer/app/shot_timer.py
```

補足:  
delayに「0」を指定したところ、Dashボタン押下時にタイマーが2重起動してしまったため、5~10程度の適当な値を指定すること。  


```commandline
chmod 660 amazon-dash.yml
sudo chown root.root amazon-dash.yml

ls -l
-rw-rw---- 1 root root  140 Nov 11 21:09 amazon-dash.yml

```

## Dashボタンでタイマー起動

`amazon-dash.yml`ファイルが存在するディレクトリで`amazon-dash`コマンドを実行

```commandline
$ cd shot_timer/app/
$ sudo amazon-dash run
Welcome to Amazon-dash v1.3.1 using Python 3.5.3
Listening for events. Amazon-dash will execute the events associated with the registered buttons.
```

Dashボタンを1回だけ押下

タイマーが起動することを確認する


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