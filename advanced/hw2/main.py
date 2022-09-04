
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # print(contacts_list)


def fix_phones(lst) :
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for card in lst:
        card_as_string = ','.join(card)
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    print(contacts_list_updated)
    return contacts_list_updated


def join_same_names(lst) :
    same_name = set()
    for i in lst :
        for j in lst :
            if i[0] == j[0] and i[1] == j[1] and i != j :
                name = i[0] + " " + i[1]
                same_name.add(name)
    # print(same_name)

    same_name_dct = {}
    new_list = []

    for i in same_name :
        same_name_dct[i] = {}
        for j in lst :
            if i.split(" ")[0] == j[0] and i.split(" ")[1] == j[1] :
                same_name_dct[i]['lastname'] = j[0]
                same_name_dct[i]['firstname'] = j[1]
                if j[2] != "" :
                    same_name_dct[i]['surname'] = j[2]
                if j[3] != "" :
                    same_name_dct[i]['organization'] = j[3]
                if j[4] != "" :
                    same_name_dct[i]['position'] = j[4]
                if j[5] != "" :
                    same_name_dct[i]['phone'] = j[5]
                if j[6] != "" :
                    same_name_dct[i]['email'] = j[6]

    # print(same_name_dct)

    for i in lst :
        if i[0] + " " + i[1] in same_name :
            continue
        else :
            new_list.append(i)

    # print(len(new_list))
    for key in same_name_dct :
        temp_list = []
        temp_list.append(same_name_dct[key].get('lastname', ""))
        temp_list.append(same_name_dct[key].get('firstname', ""))
        temp_list.append(same_name_dct[key].get('surname', ""))
        temp_list.append(same_name_dct[key].get('organization', ""))
        temp_list.append(same_name_dct[key].get('position', ""))
        temp_list.append(same_name_dct[key].get('phone', ""))
        temp_list.append(same_name_dct[key].get('email', ""))
        new_list.append(temp_list)

    # print(new_list)
    return fix_phones(new_list)


def fix_names(lst) :
    result_lst = []
    temp_lst = lst[:]
    for i in temp_lst :
        full_name = " ".join(i[:3])
        full_name_list = full_name.split(" ")
        result_lst.append(full_name_list[:3] + i[3:])
    return join_same_names(result_lst)
    # print(result_lst)



with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  phone_list = fix_names(contacts_list)
#   print(phone_list)
  datawriter.writerows(phone_list)



# if __name__ == "__main__" :
#     fix_names(contacts_list)
#     print('########')
#     # pprint(contacts_list)








