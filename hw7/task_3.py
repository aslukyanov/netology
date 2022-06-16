import os

def create_dict_for_write(files : list, folder : str) -> dict :
    wr_dict = {}
    for file in files :
        with open(folder + file, "r") as text :
            text_list = text.readlines()
            wr_dict[len(text_list)] = [file, text_list]
    return wr_dict


def check_file_exist(folder, new_file_name) :
    is_file_exists = os.path.exists(folder + new_file_name)
    if is_file_exists :
        print("Warning!! This file is already exist. Continue will erase this file")
        answer = input("Do you want to continue (Yes/No): ")
        if answer == "Yes" :
            os.remove(folder + new_file_name)
            print(f"File {folder + new_file_name} has been deleted")
            return True
        else :
            return False
    else :
        return True
    

def create_new_file(files : list, folder : str, new_file_name : str) :
    """Create new file contains files from list"""
    if check_file_exist(folder, new_file_name) :
        wr_dict = create_dict_for_write(files, folder)
        with open(folder + new_file_name, "a") as result :
            for lenght in sorted(list(wr_dict.keys())) :
                result.write(wr_dict[lenght][0] + "\n")
                result.write(str(len(wr_dict[lenght][1])) + "\n")
                for line in wr_dict[lenght][1] :
                    if line == wr_dict[lenght][1][-1] :
                        result.write(line + "\n")
                    else :
                        result.write(line)
        print(f"File {new_file_name} has been created in folder {folder}")



if __name__ == "__main__" :
    files = ['1.txt', '2.txt', '3.txt']
    folder = "/home/andrey/git/netology/hw7/"
    create_new_file(files, folder, "result.txt")
    # check_file_exist(folder, "result.txt")








