

from pprint import pprint
from task1 import create_dict_from_file


def get_shop_list_by_dishes(dishes, person_count, file_path_cook_book) :
    if not isinstance(person_count, int) and person_count < 0 :
        print("Wrong count of persons")
    cook_book = create_dict_from_file(file_path_cook_book)
    buy_list = {}
    for dish in dishes :
        if dish not in cook_book.keys() :
            print(f"{dish} not in cook_book")
        else :
            for ingridient in cook_book[dish] :
                product_name = ingridient['ingredient_name']
                measure = ingridient['measure']
                quantity = ingridient['quantity'] * person_count

                if product_name not in buy_list :
                    buy_list[product_name] = {
                        'measure' : measure,
                        'quantity' : quantity
                    }
                else :
                    buy_list[product_name]['quantity'] += quantity

    return buy_list



if __name__ == "__main__" :
    file_path_cook_book = "/home/andrey/git/netology/hw7/cook_book.txt"
    buy_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3, file_path_cook_book)
    pprint(buy_list)





