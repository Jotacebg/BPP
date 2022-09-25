import pytest
import numeros_pytest as op

    
def test_cuadrado(): 
    sol = op.cuadrado_num(4)
    assert sol == 16
    
def test_cubo():
    sol = op.cubo_num(4)
    assert sol == 64

def test_es_par():
    sol = op.es_par(8)
    assert sol == True

def test_primo():
    sol = op.es_primo(7)
    assert sol == True
    
def test_exception():
        op.cubo_num(-12)

    