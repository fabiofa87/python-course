"""
REGRAS DO FIZZBUZZ

1 - SE POSICAO FOR MULTIPLA DE 3 - FIZZ
2 - SE POSICAO FOR MULTIPLA DE 5 - BUZZ
3 - SE POSICAO FOR MULTIPLA DE 3 E 5 - FIZZBUZZ
4- QUALQUER OUTRA POSICAO - PROPRIO NUMBERO
"""
from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)



def robot(pos):
    say = str(pos)
    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    elif multiple_of_5(pos):
        say = 'buzz'


    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'