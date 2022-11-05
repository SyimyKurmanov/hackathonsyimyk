from products import list_of_products, detail_product, delete_product, create_product, update_product

def shop():
    print('Привет! Вам доступны следующие функции маркет плейса: \n\tLIST-1\n\tDETAIL-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('Введите действие(1,2,3,4,5): ')

    if choice.strip() == '1':
        print(list_of_products())
    elif choice.strip() == '2':
        print(detail_product())
    elif choice.strip() == '3':
        print(create_product())
    elif choice.strip() == '4':
        print(update_product())
    elif choice.strip() == '5':
        print(delete_product())
    else:
        print('Неверный выбор!')

    answer = input('Хотите продолжить? (yes/no): ')
    if answer.lower().strip() == 'yes':
        shop()
    else:
        print('Всего доброго!')
    

shop()
