import pytest
from applications import factorial

def test_fact():
    assert factorial.fact(0) == 1
    assert factorial.fact(5) == 120
    assert factorial.fact(20) == 2432902008176640000  
    with pytest.raises(TypeError):
        factorial.fact(5.5)
      

def test_fact_string():
    with pytest.raises(TypeError):
        factorial.fact('b')

    
