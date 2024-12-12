import requests

"""
На вход программе подаётся одно число n. Напишите программу,
 которая вернёт список [1, 2, 3, …, n].
На вход программе подаётся одно натуральное число. Программа
должна вывести текст в соответствии с условием задачи.
Пример входных данных:
6
Пример ответа:
[1, 2, 3, 4, 5, 6]
"""



def list_of_numbers(n: int) -> list:
    # Напишите ваш код здесь
    result = list(range(1, n+1))
    return result


if __name__ == '__main__':
    assert list_of_numbers(1) == [1]
    assert list_of_numbers(5) == [1, 2, 3, 4, 5]
    assert list_of_numbers(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nОтличная работа, отправляйте на проверку!")


"""
Условие задачи
Нужно реализовать функцию, принимающую список чисел. Вывести число, которое встречается
чаще всего. Максимальное число голосов всегда уникально.
В результате корректного выполнения задания будет выведен следующий результат:

1 1
2 2
"""
def vote(votes):
  # your code
  min_count = 0
  digit = votes[0]
  for i in votes:
    numbe_count = votes.count(i)
    if numbe_count > min_count:
       min_count = numbe_count
       digit = i
  return digit

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))

"""
Напишите программу, которая выведет все фразы из списка phrases, которые являются палиндромами:
"""


def solve(phrases: list):
    result = []  # список палиндромов
    for phrase in phrases:  # пройpдите циклом по всем фразам
        phrase_save = phrase.replace(" ", "")  # сохраните фразу без пробелов
        inverse_phrase = phrase_save[::-1]  # сохраните фразу в обратном порядке
        if phrase_save == inverse_phrase:  # сравните фразу с ней же, развернутой наоборот (через [::-1])
            result.append(phrase)
    return result


if __name__ == '__main__':
    # Этот код менять не нужно
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
    result = solve(phrases)
    assert result == ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
                      "а собака боса", "тонет енот", "пуст суп"], f"Неверный результат: {result}"
    print(f"Палиндромы: {result}")




def check_create_folder(token,name_folder):

    """Метод проверяющий наличие запрашиваемой папки на ЯДиске,
    если ее нет, то создает новую
    """

    url_api_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
        # create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': name_folder}
    headers = {'Authorization': token}
    response = requests.put(url_api_ya,
                            headers=headers,
                            params=params,
                            timeout=10)
    result = ['', False]
    match response.status_code:
        case 409:
            result = ['Папка уже существует' + ' (ЯДиск)', True]
        case 507:
            result = ['Недостаточно свободного места' + ' (ЯДиск)', False]
        case 503:
            result = ['Сервис временно недоступен' + ' (ЯДиск)', False]
        case 429:
            result = ['Слишком много запросов.' + ' (ЯДиск)', False]
        case 423:
            result = [
                    'Технические работы. Сейчас можно только просматривать'
                    ' и скачивать файлы (ЯДиск)', False]
        case 406:
            result = [
                    'Ресурс не может быть представлен в запрошенном формате.'
                    + '(ЯДиск)', False]
        case 403:
            result = [
                    'API недоступно. Ваши файлы занимают больше места, чем у вас есть.'
                    ' Удалите лишнее или увеличьте объём Яндекс Диска.', False]
        case 401:
            result = ['Не авторизирован ' + ' ЯДиск', False]
        case 400:
            result = ['Некорректные данные.' + '( ЯДиск)', False]
        case 201:
            result = ['Ок.', True]

    return (response.status_code,result)