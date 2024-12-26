import random

import dictation


def suuji(always_yen=1, digit_start=1, digit_end=6, sound_speed=1.1, mp3file_path='', os_cwd='', delete_directory=''):
    # make a random number
    # 个 十 百 千 万 十万 create random digit, make each digit number's probability equal
    value_or_number = random.randint(0, 1)  # control 円 or not
    digit = random.randint(digit_start, digit_end)  # control digit
    # create random number based on digit
    if always_yen == 1:
        random_number = str(random.randint(10 ** (digit - 1), 10 ** digit - 1)) + "円"
    else:
        random_number = str(random.randint(10 ** (digit - 1), 10 ** digit - 1)) + value_or_number * "円"
    print(f"{random_number}")
    dictation.generate_mp3file(random_number, sound_speed, mp3file_path)
    dictation.play_single_mp3(os_cwd, mp3file_path)
    dictation.delete_temp_audio(delete_directory)
