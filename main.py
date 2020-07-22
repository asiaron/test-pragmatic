# from collections import Iterable
from itertools import product


def generate_expression(): # -> Iterable[str]:
    for signs in product({'+', '-', ''}, repeat=10):
        if signs[0] == '+':
            continue
        yield '{}9{}8{}7{}6{}5{}4{}3{}2{}1{}0'.format(*signs)


def evaluate(expression):  #  : str): -> int:
    plus_pos = expression.find('+')
    minus_pos = expression.rfind('-')
    if plus_pos >= 0:
        return evaluate(expression[:plus_pos]) + evaluate(expression[plus_pos+1:])
    elif minus_pos >= 0:
        # minus is right associative
        return evaluate(expression[:minus_pos]) - evaluate(expression[minus_pos+1:])
    else:
        # no more signs, just int
        # '' is 0, because '-23' parsed as '', '-', '23'
        return int(expression or 0)


def main():
    for expression in generate_expression():
        if evaluate(expression) == 200:
            print(expression + ' = 200')


if __name__ == '__main__':
    main()
