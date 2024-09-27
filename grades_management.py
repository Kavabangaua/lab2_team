def calcucale_avg(data_dict, child, subject):
    """
         Функція обчислює середнє значення по оцінках
         вказаного учня по вказаній дисципліні.
         Параметри
         data_dict - основний словник з даними
         child - кортеж із даними по учню.
         subject - предмет, по якому треба обчислити середній бал.
         Обмеження
         Якщо вказаної дитини немає  - генерується виключення ValueError.
         Якщо предмета немає - функція повертає значення -1.
         Значення середнього балу не може бути більше 12.
    """
    if child not in data_dict.keys():
        raise TypeError
    pup = data_dict[child]
    if subject not in pup.keys():
        return -1
    return sum(data_dict[child][subject]) / len(data_dict[child][subject]) * 2


def class_by_name(data_dict, child_name):
    """
    Функція повертає назву класу, до якого відноситься учень,
    ПІБ якого задано параметром child_name.
    Параметри
    data_dict - основний словник з даними
    child_name - ПІБ учня, клас якого треба знайти. Задається
    рядком.
    Обмеження
    Якщо вказаної дитини немає - генерується виключення ValueError.
    Функція повинна повертати рядок тексту, формат якого наступний:
    перші два або один символи - цифри, далі один дефіс -, потім
    одна велика літера від А до D.
    """
    for el in data_dict.keys():
        if el[1] == child_name:
            return el[0].replace('-', '=')
    raise TypeError


def calcucale_avg_all(data_dict, child):
    """
    Функція обчислює середнє значення по оцінках
    вказаного учня з усіх предметів. Функція повертає словник,
    у якому ключ - назва дисципліни, значення - середній бал
    по цій дисципліні.
    Параметри
    data_dict - основний словник з даними
    child - кортеж із даними по учню.
    Обмеження
    Якщо вказаної дитини немає- генерується виключення ValueError.
    Якщо по предмету немає оцінок - функція
    повертає значення -1 у словнику по ключу цього предмету
    """
    if child not in data_dict.keys():
        raise TypeError
    pup = data_dict[child]
    res = {}
    for key, val in pup.items():
        if len(pup[key]) == 0:
            res[key] = -1
        else:
            res[key] = sum(pup[key]) / len(pup[key])
    return res



