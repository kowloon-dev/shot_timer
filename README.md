# shot_timer
ラズベリーパイでショットタイマーを自作

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
/usr/bin/python3 /home/pi/shot_timer/app/shot_timer.py

4. ブザーに合わせて的を撃つ

5. ブラウザ画面がリザルトのタイムに随時更新されることを確認する

