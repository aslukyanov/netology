from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, kг': 0.3,
        'сыр, kг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }



def get_omlet(request) :
    temp_dict = DATA['omlet']
    context = {'recipe' : {}}
    quantity = int(request.GET.get('servings', 1))
    for key,value in temp_dict.items() :
        context['recipe'][key] = quantity * value
    return render(request, 'index.html', context)


# def get_omlet(request, name) :
#     temp_dict = DATA[name]
#     context = {'recipe' : {}}
#     quantity = int(request.GET.get('servings', 1))
#     for key,value in temp_dict.items() :
#         context['recipe'][key] = quantity * value
#     return render(request, 'index.html', context)


def get_pasta(request) :
    temp_dict = DATA['pasta']
    context = {'recipe' : {}}
    quantity = int(request.GET.get('servings', 1))
    for key,value in temp_dict.items() :
        context['recipe'][key] = quantity * value
    return render(request, 'index.html', context)


def get_buter(request) :
    temp_dict = DATA['buter']
    context = {'recipe' : {}}
    quantity = int(request.GET.get('servings', 1))
    for key,value in temp_dict.items() :
        context['recipe'][key] = quantity * value
    return render(request, 'index.html', context)












