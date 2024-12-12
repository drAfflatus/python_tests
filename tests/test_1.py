import unittest
import requests
from unittest import TestCase
from tests.tasks import *
import dotenv
import os

def load_dotenv():
    """Функция, обеспечивающая получение данных из файла окружения."""
    dotenv.load_dotenv()
    dotenv.load_dotenv(dotenv.find_dotenv(filename='config.env', usecwd=True))


is_not_launch = True
class TestTasks_1_2_3(TestCase):
    @unittest.skipIf(is_not_launch,"будет другой тест с парам.")
    def test_list_of_numbers(self):
        data = 9
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = list_of_numbers(data)

        self.assertListEqual(expected,result)


    def test_list_with_params(self):
        for test_n,(expected,data) in enumerate((
                ([1, 2, 3, 4, 5, 6, 7, 8, 9],9),
                ([1, 2, 3, 4, 5, 6],6),
                ([1],1)
                )):
            with self.subTest(test_n):
                result = list_of_numbers(data)
                self.assertListEqual(expected, result)

    def test_vote_with_params(self):
        for test_n,(data,expected) in enumerate((
                ([1, 2, 2, 2, 3, 4, 1, 1, 1],1),
                ([1, 2, 3, 1, 3, 3],3),
                ([1,4,4,7],4)
                )):
            with self.subTest(test_n):
                result = vote(data)
                self.assertEqual(expected, result)

    def test_solve_with_params(self):

        data =  ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
                 "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
        expected = ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
                      "а собака боса", "тонет енот", "пуст суп"]

        result = solve(data)
        self.assertListEqual(expected, result)


"""
проверка создания папки
ок на создание
err при попытке повторного создания
еrr ошибка авторизации
"""

class TestYDFolders(TestCase):
    load_dotenv()
    token = os.getenv("YA_TOKEN")

    def test_YDFolders(self):

        for test_n,(data,expected) in enumerate((
                ((self.token,"FolderZZZZ"),201),
                ((self.token,"FolderZZZZ"),409),
                ((self.token+"bla%bla","FolderZZZZ"),401)
                )):
            with self.subTest(test_n):
                result = check_create_folder(data[0],data[1])
                print(result)
                self.assertEqual(expected, result[0])
