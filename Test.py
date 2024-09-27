def subject_avg(data_dict, subject):
    """
    Функція повертає середню оцінку по предмету для кожного класу у форматі
    списку рядків, наприклад, ['8-A: 10.5', '5-C: 11'].
    Параметри
    data_dict - основний словник з даними
    subject - назва предмету у вигляді рядка
    Обмеження
    Якщо дані по цьому предмету не внесено - повертається пустий список.
    Кожен рядок списку, який повертається у результаті виконання функції,
    повинен відповідати формату "назва_класу: середній_бал", при цьому
    формат назви класу має вигляд: перші два або один символи - цифри,
    далі один дефіс -, потім одна велика літера від А до D.
    """
    res = []
    avg = 0
    for key in data_dict.keys():
        if subject in data_dict[key].keys():
            if len(data_dict[key][subject])>0:
                avg = sum(data_dict[key][subject])/len(data_dict[key][subject])
        res.append(key[0] + ': '+ str(avg))
    return res

def children_list(data_dict, class_name):
    """
    Функція повертає список учнів заданого класу. Якщо не внесено
    жодного з учнів класу - повертається пустий список
    Параметри
    data_dict - основний словник з даними
    class_name - назва класу у вигляді рядка
    """
    res = []
    for el in data_dict.keys():
        if class_name == el[0]:
            res.append(el[1])
    return res

def subject_best_children(data_dict, subject):
    """
    Функція по заданому предмету знаходить учня з найвищим балом у кожній
    паралелі класів (наприклад, 8і класи, 5і класи, 7і класи і т.д.
    Якщо таких учнів декілька - повертається список їх прізвищ.
    Функція повертає словник, ключами якого є номери паралелей класів (без літери),
    а значеннями - список прізвищ учнів з найвищою оцінкою по заданому предмету.
    Якщо оцінки по заданому предмету відсутні - повертається пустий словник.
    Параметри
    data_dict - основний словник з даними
    subject - назва предмету у вигляді рядка
    """
    res = {}
    max_grade = {}
    for key in data_dict.keys():
        if subject in data_dict[key].keys():
            if len(data_dict[key][subject]) == 0:
                continue
            if key[0][0] not in res.keys():
                res[key[0][0]] = []
                max_grade[key[0][0]] = -1
            if max_grade[key[0][0]] < max(data_dict[key][subject]):
                res[key[0][0]].clear()
                res[key[0][0]].append(key[1])                
                max_grade[key[0][0]] = max(data_dict[key][subject])
            elif max_grade[key[0][0]] == max(data_dict[key][subject]):
                res[key[0][0]].append(key[1])
    return res