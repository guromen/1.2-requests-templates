from django.shortcuts import render
from django.http import HttpResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
   'coffee': {
       'кофе, ложка': 1,
       'вода, мл' : 200
   }
}
def omlet(request):
    num_person = int(request.GET.get('servings', 1))
    recipe=DATA['omlet']
    list1=[]
    list2=[]
    for i,j in recipe.items():
        list1.append(i)
        list2.append(j)
    recipe={i:j*num_person for i,j in zip(list1, list2)}
    context={
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    num_person = int(request.GET.get('servings', 1))
    recipe=DATA['pasta']
    list1=[]
    list2=[]
    for i,j in recipe.items():
        list1.append(i)
        list2.append(j)
    recipe={i:j*num_person for i,j in zip(list1, list2)}
    context={
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    num_person = int(request.GET.get('servings', 1))
    recipe=DATA['buter']
    list1=[]
    list2=[]
    for i,j in recipe.items():
        list1.append(i)
        list2.append(j)
    recipe={i:j*num_person for i,j in zip(list1, list2)}
    context={
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def coffee(request):
    num_person = int(request.GET.get('servings', 1))
    recipe=DATA['coffee']
    list1=[]
    list2=[]
    for i,j in recipe.items():
        list1.append(i)
        list2.append(j)
    recipe={i:j*num_person for i,j in zip(list1, list2)}
    context={
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
