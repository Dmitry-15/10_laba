#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test_input(message):
    try:
        str_to_int(message)
    except ValueError:
        print("Невозможно преобразовать в число")


def str_to_int(message):
    a = int(message)
    print_int(a)


def print_int(a):
    print(a)


def get_input():
    message = input("Введите строку: ")
    test_input(message)


if __name__ == '__main__':
    while True:
        get_input()


