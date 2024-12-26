import os
import random
import time

import dictation
from function.suuji import suuji

"""
`gTTS` is for generate audio by Google Translate API
`playsound` is for play sound in code itself, rather than open mp3 file with player in Windows
`ffmpeg` is necessary to INSTALL LOCALLY for customize the speed of audio
"""
# Check PWD
os_cwd = os.getcwd()
print(f"Current Work Dir: {os_cwd}")


# Control Audio's Speed
def audio_speed_controller(sound, speed=1.0):
    modified_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return modified_sound.set_frame_rate(sound.frame_rate)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'====Japanese Start!====')
    # ------Set Sound Speed------
    sound_speed = 1.1
    # ------Set Break Time------
    break_time = 2
    # ------Create Directory to Storage Audio------
    save_directory = 'temp'  # relative to project dir
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    # ------mp3 file name------
    mp3file_name = "temp_audio.mp3"
    mp3file_path = os.path.join(save_directory, mp3file_name)
    # ------Delete Dir------
    # DENY!!! Add `/` in front of `temp` !!!
    delete_directory = os.path.join(os_cwd, 'temp')

    # ------DB------
    db_data = [""]

    # Select dictation DB:
    dictation_db_input = input(
        "Please Select number: \n"
        "0：数字、価格\n"
        "1：日付（日、月、年、曜日）\n"
        "2：時間（デーリー）\n"
        "3：時間（時、分、秒）\n"
        "4：家族、友達、身元\n"
        "5：名詞\n"
        "6：感動詞\n"
        "7：カタカナリスト\n"
        "8：四字熟語、諺（ことわざ）\n"
        "9：動詞\n"
        "10：形容詞、形容動詞\n"
        "11：副詞、接続詞、連体詞、助詞、助動詞\n"
        "12：漢字（音読み、訓読み）\n").strip().lower()

    if dictation_db_input == "0":
        # ==================0-999,999 数字、価格==================
        while True:
            suuji(1, 4, 4, 1, mp3file_path, os_cwd, delete_directory)
            # 中断控制
            time.sleep(2)

    elif dictation_db_input == "1":
        # ==================日付（日、月、年、曜日）==================
        db_data = dictation.load_kanji_and_hiragana("./db/dictation.xlsx", "hiduke")
        order_input = input("Order(y) or Random(n): y/n\n").strip().lower()
        if order_input == 'y':
            while True:
                # order
                for datum in db_data:
                    kanji_to_dictate = datum["kanji"]
                    print(f"漢字：{kanji_to_dictate}　―　平仮名：{datum['hiragana']}")
                    dictation.generate_mp3file(kanji_to_dictate, sound_speed, mp3file_path)
                    dictation.play_single_mp3(os_cwd, mp3file_path)
                    dictation.delete_temp_audio(delete_directory)
                    # 中断控制
                    time.sleep(break_time)
        elif order_input == 'n':
            while True:
                # random
                chosen_text = dictation.choose_content(db_data)
                kanji_to_dictate = chosen_text["kanji"]
                print(f"漢字：{kanji_to_dictate}　―　平仮名：{chosen_text['hiragana']}")
                dictation.generate_mp3file(kanji_to_dictate, sound_speed, mp3file_path)
                dictation.play_single_mp3(os_cwd, mp3file_path)
                dictation.delete_temp_audio(delete_directory)
                # 中断控制
                time.sleep(break_time)

    elif dictation_db_input == "2":
        # ==================時間（デーリー）==================
        db_data = dictation.load_kanji_and_hiragana("./db/dictation.xlsx", "jikan")
        while True:
            chosen_text = dictation.choose_content(db_data)
            kanji_to_dictate = chosen_text["kanji"]  # choose `kanji` col to read
            print(f"漢字：{kanji_to_dictate}　―　平仮名：{chosen_text['hiragana']}")
            dictation.generate_mp3file(kanji_to_dictate, sound_speed, mp3file_path)
            dictation.play_single_mp3(os_cwd, mp3file_path)
            dictation.delete_temp_audio(delete_directory)
            # 中断控制
            time.sleep(break_time)

    elif dictation_db_input == "3":
        # ==================時間（時、分、秒）Combo==================
        while True:
            # make 半、ごろ exception
            han_need = random.randint(0, 1)  # control 半 need or not
            goro_need = random.randint(0, 1)  # control ごろ need or not
            # make 時 around 1-12
            ji_value = random.randint(1, 12)  # control 時
            # make 分 around 0-59
            bun_value = 0  # control 分
            bun_need = 0  # control 分 need or not
            if han_need == 0:  # 分
                bun_need = 1
                bun_value = random.randint(1, 59)
            else:  # 分ない
                bun_need = 0

            jikan_result = str(ji_value) + "時" + bun_need * (
                    str(bun_value) + "分") + han_need * "半" + goro_need * "ごろ"

            print(f"{jikan_result}")
            dictation.generate_mp3file(jikan_result, sound_speed, mp3file_path)
            dictation.play_single_mp3(os_cwd, mp3file_path)
            dictation.delete_temp_audio(delete_directory)
            # 中断控制
            time.sleep(break_time)
            # user_input = input("enter `enter` for next\n").strip().lower()
            # if user_input == '\n':
            #     print(f"Next Word")

    elif dictation_db_input == "4":
        # ==================時間（時、分、秒）Combo==================
        while True:
            # make 半、ごろ exception
            han_need = random.randint(0, 1)  # control 半 need or not
            goro_need = random.randint(0, 1)  # control ごろ need or not
            # make 時 around 1-12
            ji_value = random.randint(1, 12)  # control 時
            # make 分 around 0-59
            bun_value = 0  # control 分
            bun_need = 0  # control 分 need or not
            if han_need == 0:  # 分
                bun_need = 1
                bun_value = random.randint(1, 59)
            else:  # 分ない
                bun_need = 0

            jikan_result = str(ji_value) + "時" + bun_need * (
                    str(bun_value) + "分") + han_need * "半" + goro_need * "ごろ"

            print(f"{jikan_result}")
            dictation.generate_mp3file(jikan_result, sound_speed, mp3file_path)
            dictation.play_single_mp3(os_cwd, mp3file_path)
            dictation.delete_temp_audio(delete_directory)
            # 中断控制
            time.sleep(break_time)
            # user_input = input("enter `enter` for next\n").strip().lower()
            # if user_input == '\n':
            #     print(f"Next Word")

    elif dictation_db_input == "5":
        # ==================名詞==================
        db_data = dictation.load_meishi("./db/dictation.xlsx", "meishi")
        while True:
            chosen_text = dictation.choose_content(db_data)
            dictate_col = chosen_text["name"]  # choose `kanji` col to read
            print(
                f"物：{chosen_text['mono']}　―　名前：{dictate_col}　―　かな：{chosen_text['kana']}"
                f"　―　漢字：{chosen_text['kanji']}　―　英語：{chosen_text['english']}")
            dictation.generate_mp3file(dictate_col, sound_speed, mp3file_path)
            dictation.play_single_mp3(os_cwd, mp3file_path)
            dictation.delete_temp_audio(delete_directory)
            # 中断控制
            time.sleep(break_time)
