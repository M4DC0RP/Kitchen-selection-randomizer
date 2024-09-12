import random
import os
import json

# Изначальный список кухонь
cuisines = ['Китайскую', 'Мексиканскую', 'Итальянскую', 'Японскую', 'Индийскую', 'Испанскую', 'Корейскую', 'Вьетнамскую', 'Русскую', 'Узбекскую']

# Путь к файлу для хранения оставшихся кухонь
file_path = 'remaining_cuisines.json'

def load_remaining_cuisines():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return cuisines.copy()

def save_remaining_cuisines(remaining_cuisines):
    with open(file_path, 'w') as f:
        json.dump(remaining_cuisines, f)

def random_cuisine():
    # Загружаем оставшиеся кухни из файла
    remaining_cuisines = load_remaining_cuisines()
    
    if not remaining_cuisines:
        # Если все кухни были предложены, перезагружаем список
        remaining_cuisines = cuisines.copy()
    
    # Выбираем случайную кухню и удаляем её из оставшихся
    choice = random.choice(remaining_cuisines)
    remaining_cuisines.remove(choice)
    
    # Сохраняем обновленный список обратно в файл
    save_remaining_cuisines(remaining_cuisines)
    
    return f"Сегодня мы будем заказывать {choice} кухню!"

# Пример использования - один вызов
print(random_cuisine())