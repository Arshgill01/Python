import pytest
from Calculator import square


def test_square():
  assert square(2) == 4
  assert square(3) == 9  
  assert square(-2) == 4
  assert square(-3) == 9



def test_str():
  with pytest.raises(TypeError):
    square("cat")
    
    

  
  


  
  
  
  
## assert - to check if something is true