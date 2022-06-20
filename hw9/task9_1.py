

import requests
import json


def get_smartest(hero_dict, max_intelligence) :
    return_dict = {}
    for key, values in hero_dict.items() :
        if values == max_intelligence :
            return_dict[key] = values

    if len(return_dict) == 1 :
        return f"The smartest hero with intelligence {max_intelligence} is {list(return_dict.keys())[0]}"
    else :
        result = f"The smartest heroes with intelligence {max_intelligence} are "
        names = " and ".join(list(return_dict.keys()))
        return result + names


def find_the_smartest_hero(*names) :
    token = "2619421814940190"
    api = "https://superheroapi.com/api/"
    max_intelligence = 0
    hero_dict = {}

    for name in names :
        try :
            r = requests.get(api + token + "/search/" + name)
            data = json.loads(r.text)
            intelligence = int(data['results'][0]['powerstats']['intelligence'])
            hero_dict[name] = intelligence
            if intelligence > max_intelligence :
                max_intelligence = intelligence
        except KeyError :
            return "Please check spelling of the Superheroes names"

    return get_smartest(hero_dict, max_intelligence)


if __name__ == "__main__" :
    # print(find_the_smartest_hero("Hulk", "Captain America", "Thanos"))
    print(find_the_smartest_hero("Hulk", "Captain America"))
    # print(find_the_smartest_hero("Captain America"))


