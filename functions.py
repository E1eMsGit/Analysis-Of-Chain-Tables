def make_dict(file_content: str) -> dict:
    """
    Создает словарь из содержимого файла.
    :param file_content: Содержимое файла.
    :return: Словарь из содержимого файла.
    """
    # Поиск нужного содержимого в файле и перевод в верхний регистр.
    start_position = file_content.find('(')
    content_string = file_content[start_position:].upper()

    # Создание списка списков (блоков).
    # Разделение строки на блоки заключенные между "(" и ")".
    content_blocks = [i.split() for i in content_string.split(')')]

    del content_blocks[-1]

    for block in content_blocks:
        block.remove('(')

    # Создание словаря из списка списков (блоков) Ключ - первый элемент блока.
    content_dictionary = dict(
        (block[0], [item for item in block[1:]]) for block in content_blocks)

    return content_dictionary


def make_dict_of_differences(first_dict: dict, second_dict: dict) -> dict:
    """
    Создает словарь уникальных элементов певрого словаря по сравнению со
    вторым.
    :param first_dict: Словарь в котором ищем уникальные элементы.
    :param second_dict: Словарь с которым надо сравнить.
    :return: Словарь с уникальными элементами первого списка блоков
    (Название цепи: [Список элементов]).
    """
    differences_dictionary = dict()

    for key in first_dict:
        if key in second_dict:
            differences_dictionary[key] = list(
                filter(lambda x: x not in second_dict[key], first_dict[key]))
        else:
            differences_dictionary[key] = first_dict[key]

    # Удаление пустых ключей.
    differences_dictionary = dict(
        (key, value) for key, value in differences_dictionary.items() if value)

    return differences_dictionary
