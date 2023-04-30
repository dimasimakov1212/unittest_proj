def get_val(collection, key, default='git'):
    """
    Функция возвращает значение словаря по
    переданному ключуб если ключ существует
    Иначе возвращается default
    :param collection: словарь на входе
    :param key: значение ключа
    :param default: дефолтное значение
    :return: значение словаря по ключу
    """
    return collection[key]
