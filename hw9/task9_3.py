
import requests
import json
import subprocess as sp


def get_stackoverflow_python_info() :
    """
    This function returns list of all questions with tag python for last 48 hors
    """
    end_date = int(sp.getoutput("date +%s"))
    start_date = end_date - 172800
    lst_titles = []

    #Gathering request for page 0 by default
    link = f"https://api.stackexchange.com/2.3/questions?pagesize=100&fromdate={start_date}&todate={end_date}&order=desc&sort=activity&tagged=python&site=stackoverflow&filter=!nKzQUR693x"

    r = requests.get(link)
    data = json.loads(r.text)

    for title in data['items'] :
        lst_titles.append(title["title"])

    #Checking if other pages are exist
    #If yes we will request next page
    if data['has_more'] :
        is_last = False
        count = 2
        while not is_last :
            new_link = f"https://api.stackexchange.com/2.3/questions?page={count}&pagesize=100&fromdate={start_date}&todate={end_date}&order=desc&sort=activity&tagged=python&site=stackoverflow&filter=!nKzQUR693x"
            new_r = requests.get(new_link)
            new_data = json.loads(new_r.text)
            for title in new_data['items'] :
                lst_titles.append(title["title"])
            count += 1
            #print(len(lst_titles))
            if not new_data['has_more'] :
                is_last = True


    return lst_titles

if __name__ == "__main__" :
    print(len(get_stackoverflow_python_info()))
    # print(get_stackoverflow_python_info())



