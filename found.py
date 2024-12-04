text = "The quick brown fox jumps over the lazy fox and sees another fox"
word_to_find = "fox"

def wordIndexFounder(word_to_find, text):
    words = text.split()
    indices = []
    for index, word in enumerate(words):
        if word == word_to_find:
            indices.append(index)
    if indices:
        print(f"The word '{word_to_find}' is found at indices: {indices}")
    else:
        print(f"The word '{word_to_find}' is not in the list.")

wordIndexFounder(word_to_find, text)


# Пояснення:

# Початковий текст
# Слово, індекси якого шукаємо

# Створюємо функцію
    # Ділимо текст по пробілах
    # Створюємо порожній list 
    # Перебираємо поділений текст
        # Якщо слово збізається зі словом, що ми шукаємо, то...
            #...додаємо індекс до list
    
# Перевіряємо, чи було знайдено слово, якщо так, indices буде True
    # Виводимо результат
# Якщо слово не знайдено
    # Виводемо повідомлення, якщо слово не знайдено

# Виконуємо функцію