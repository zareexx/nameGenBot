import random
import os
from datetime import datetime

def load_words(filename):
    """Загружает список слов из файла"""
    with open(filename, 'r') as f:
        return [line.strip().lower() for line in f.readlines()]

def generate_variation(words, max_length=20):
    """Генерирует случайную вариацию из списка слов"""
    variation = []
    length = 0
    while length < max_length - 4:  # оставляем место для '_bot'
        word = random.choice(words)
        if length + len(word) + len(variation) > max_length - 4:
            break
        variation.append(word)
        length += len(word)
    return '_'.join(variation) + '_bot'

def save_variations(variations, filename):
    """Сохраняет вариации в файл"""
    with open(filename, 'w') as f:
        for variation in variations:
            f.write(variation + '\n')

def get_current_time():
    """Возвращает текущее время в формате YYYY-MM-DD_HH-MM-SS"""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def main():
    filename = 'name.txt'
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    words = load_words(filename)
    num_variations = int(input("Введите количество вариаций: "))

    variations = set()
    while len(variations) < num_variations:
        variation = generate_variation(words)
        if variation not in variations:
            variations.add(variation)

    print("Сгенерированные вариации:")
    for variation in variations:
        print(variation)

    current_time = get_current_time()
    save_filename = f"variations_{current_time}.txt"
    save_variations(variations, save_filename)
    print(f"Вариации сохранены в файле {save_filename}")

if __name__ == "__main__":
    main()
