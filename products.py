import random
import json

FILE_PATH = '/home/syimyk/Desktop/hackaton/products.json'
ID_FILE_PATH = '/home/syimyk/Desktop/hackaton/id.txt'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)


def list_of_products():
    data = get_data()
    return f'Список всех товаров: {data}'

def detail_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data ))
        return product[0]
    except:
        return 'Неверный ID!'

def get_id():
    with open(ID_FILE_PATH, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id


def create_product():
    data = get_data()
    try:
        product = {
            'id': get_id(),
            'BRAND': input('Введите марку товара: '),
            'MODEL': input('Введите модель товара: '),
            'YEAR': int(input('Введите год выпуска: ')),
            'DECSCRIPTION': input('Введите описание: '),
            'PRICE': round(float(input('Введите цену товара: ')),2),
        }
    except:
        return 'Неверные данные!'

    data.append(product)
    save_data(data)
    return 'Добавлен новый товар'

# print(create_product())


def update_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data)) [0]
        print(f'Товар для обновления: {product["BRAND"]}')
    except:
        return 'Неверный id!'

    index = data.index(product)
    choice = input('Что вы хотите изменить?(1-BRAND, 2-MODEL, 3-YEAR, 4-DESCRIPTION, 5-PRICE): ')
    if choice.lower().strip() == '1':
        data[index]['BRAND'] = input('Введите новую марку: ')
    elif choice.lower().strip() == '2':
        data[index]['MODEL'] = input('Введите новую модель: ')
    elif choice.strip() == '3':
        try:
            data[index]['YEAR'] = int(input('Введите новый год выпуска: '))
        except:
            return 'Неверное значение для года выпуска!'
    elif choice.strip() == '5':
        try:
            data[index]['PRICE'] = round(float(input('Введите новую цену для товара: ')), 2)
        except:
            return 'Неверное значение для цены!'
    elif choice.strip() == '4':
        data[index]['DESCRIPTION'] = input('Введите новое описание для товара: ')
    else:
        return 'Неверное значение для обновления!'
    
    save_data(data)
    return 'Товар обновлен!'

# print(update_product())


def delete_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data))[0]
        print(f'Товар для удаления {product["BRAND"]}')
    except:
        return 'Неверный id!'
    choice = input('Удалить этот товар?(yes/no)')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален!'
    data.remove(product)
    save_data(data)
    return 'Товар удален!'

# print(delete_product())

