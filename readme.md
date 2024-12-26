# 日本語 Dictation 案内

1. 数字、価格
2. 家族、友達、身元
3. 動詞、感動詞
4. 形容詞、形容動詞
5. 副詞、接続詞、連体詞、助詞、助動詞
6. カタカナリスト
7. 名詞（科学、建物、交通機関、地理、歴史、文化、政治、経済、食べ物、トレンド、映画、デーリー、名人、妖怪）
8. 四字熟語、諺（ことわざ）
9. 漢字（音読み、訓読み）


## Before Use
`gTTS` is for generate audio by Google Translate API
<br>`playsound` is for play sound in code itself, rather than open mp3 file with player in Windows
<br>`ffmpeg` is necessary to INSTALL LOCALLY for customize the speed of audio
<br>

1. 在项目根目录的控制台内激活虚拟环境（用的是虚拟环境，不影响外部环境）
```
# windows
.venv\Scripts\activate
```
```
# macOS / Linux
source .venv/bin/activate
```
2. 安装依赖:
```
pip install -r requirements.txt
```
3. 启动:
```
python main.py
```

4. 额外：如果你想控制音速，请安装ffmpeg然后再修改激活`audio_speed_controller`函数

`ffmpeg` locally
<br><br>I use `Google Translate` for mp3 making, pls make sure you can access `Google Translate`
## User Guide
the Excel file in `db` is for 言葉 storage, please add it or modify it when need more 言葉