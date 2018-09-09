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

