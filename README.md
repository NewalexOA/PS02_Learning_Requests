# Word Game - an educational project

## Description
This project is a simple word game that fetches a random English word, translates it to Russian, and asks the user to guess the word based on its definition.

## How to Use
1. Ensure you have Python installed on your machine.
2. Install the required packages using:
    ```sh
    pip install requests googletrans==3.1.0a0 beautifulsoup4
    ```
3. Run the script:
    ```sh
    python word_game.py
    ```

## Code Overview
The script consists of three main functions:
- `get_english_words()`: Fetches a random English word and its definition from randomword.com.
- `translate_to_russian(text)`: Translates the given text to Russian using Google Translate.
- `word_game()`: Runs the main game loop, asking the user to guess the word based on its translated definition.

---

# Игра в Слова - учебный проект

## Описание
Этот проект представляет собой простую игру, которая получает случайное английское слово, переводит его на русский и просит пользователя угадать слово по его определению.

## Как использовать
1. Убедитесь, что у вас установлен Python.
2. Установите необходимые пакеты, используя:
    ```sh
    pip install requests googletrans==3.1.0a0 beautifulsoup4
    ```
3. Запустите скрипт:
    ```sh
    python word_game.py
    ```

## Обзор кода
Скрипт состоит из трех основных функций:
- `get_english_words()`: Получает случайное английское слово и его определение с сайта randomword.com.
- `translate_to_russian(text)`: Переводит данный текст на русский с помощью Google Translate.
- `word_game()`: Запускает основной цикл игры, прося пользователя угадать слово по его переведенному определению.
