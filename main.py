import requests
from googletrans import Translator
from bs4 import BeautifulSoup


def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }

    except requests.exceptions.RequestException as e:
        print(f'Произошла ошибка при запросе: {e}')


def translate_to_russian(text):
    translator = Translator()
    russian = translator.translate(text, dest='ru').text
    return russian


def word_game():
    print('Добро пожаловать в игру!')
    while True:
        word_dict = get_english_words()
        en_word = word_dict.get('english_word')
        word = translate_to_russian(en_word)
        en_word_definition = word_dict.get('word_definition')
        word_definition = translate_to_russian(en_word_definition)

        print(f'Значение слова: {word_definition}')
        answer = input('Что это за слово? ')

        if answer.lower() == word.lower():
            print('Правильно!')
        else:
            print(f'Ответ неверный, было загадано это слово - {word}')

        play_again = input('Хотите сыграть еще раз? (да/нет) ')
        if play_again.lower() != 'да':
            print('Спасибо за игру!')
            break


word_game()
