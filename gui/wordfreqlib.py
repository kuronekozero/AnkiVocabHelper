from wordfreq import zipf_frequency

def get_word_difficulty(word, lang='en'):
    # Получаем сложность слова с помощью функции zipf_frequency из библиотеки wordfreq
    zipf_difficulty = zipf_frequency(word, lang, 'large')  # Измените 'best' на 'large'

    # Если слово не найдено в базе данных wordfreq, возвращаем 11
    if zipf_difficulty == 0:
        return 11

    ten_point_difficulty = (6 - zipf_difficulty) * 2

    # Если полученное значение меньше 1, возвращаем 1
    if ten_point_difficulty < 1:
        return 1

    # Возвращаем округленное до целого числа значение сложности
    return round(ten_point_difficulty)
