def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def mult (a,b):
    return a * b

def div (a,b):
    return a / b



def teste_se_a_mais():
    assert soma (8,9) == 17
    assert soma (10,5) == 15
    assert soma (8,5) == 13

def teste_subtracao ():
    assert subtracao (5,3) == 2
    assert subtracao (3,3) == 0
    assert subtracao (5,4) == 1


def teste_multi():
    assert mult (5,5) == 25
    assert mult (2,5) == 10
    assert mult (0,7) == 0

def teste_div():
    assert div (10,2) == 5
    assert div (9,3) == 3
    assert div (100,2) == 50   
    


