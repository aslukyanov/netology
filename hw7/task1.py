
from pprint import pprint


def create_dict_from_file(file_path : str) -> dict :
    try :
        with open(file_path, "r") as file :
            print("File has been opened")
            dict = {}
            while True :
                try :
                    line = next(file)
                    if line == "\n" :
                        continue

                    if not line.strip("\n").isdigit() and "|" not in line.strip("\n"):
                        dish_name = line.strip("\n")
                        dict[dish_name] = []

                    if line.strip("\n").isdigit() :
                        for i in range(int(line.strip("\n"))) :
                            next_line = next(file).strip("\n")
                            dict[dish_name].append({'ingredient_name' : next_line.strip("\n").split(" | ")[0],
                            'quantity' : int(next_line.strip("\n").split(" | ")[1]),
                            'measure' : next_line.strip("\n").split(" | ")[2]})
                except :
                    break
    except FileNotFoundError:
        return "This file doesn't exist"

    return dict




if __name__ == "__main__":
    pass
    cook_book = create_dict_from_file("/home/andrey/git/netology/hw7/cook_book.txt")
    pprint(cook_book)





