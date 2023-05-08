# файл dicts.py
def get_val(collection: dict, key: str, default='git'):
    """
    Возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param collection: исходный список
    :param key:
    :param default:
    :return:
    """
    return collection.get(key, default)
