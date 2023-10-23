# Enodia extended interaction enhancements to SolidPython
# Brygg Ullmer, Clemson University
# Begun 2022-11-21

from solid         import *
from solid.utils   import *
from solid.objects import *

class XCube(cube):
  def __init__(self, size: ScadSize = None, center: bool = None) -> None:
     super().__init__(size, center)

  ########## extend + operator with list operand as translation ########## 

  def __add__(self, operand):
    if isinstance(operand, list): 
      v = [0, 0, 0]; idx = 0

      for i in operand:
        if not(isinstance(i, int) or isinstance(i, float)): 
          print(type(i))
          print("XCube + operand list angst1; ignoring operand"); return self

        v[idx] = i; idx += 1

      result = translate(v)(self) #solidpython magic
      return result 

    return cube.__add__(self, operand) #use parent behavior except for list operands

  ########## extend * operator with list operand as scaling ########## 

  def __mul__(self, operand):
    if isinstance(operand, int) or isinstance(operand, float): #uniform scaling
      v = [operand, operand, operand]
      return scale(v)(self) 

    if isinstance(operand, list): 
      v = [1, 1, 1]; idx = 0

      for i in operand:
        if not(isinstance(i, int) or isinstance(i, float)): 
          print(type(i))
          print("XCube * operand list angst1; ignoring operand"); return self

        v[idx] = i; idx += 1

      return scale(v)(self) #solidpython magic

    return cube.__add__(self, operand) #use parent behavior except for list operands


##################### main ##################### 
       
#print(type(xc1))
#if isinstance(xc1, XCube): print("yo")
#if isinstance(xc1, OpenSCADObject): print("yo2")

xc1 = XCube() * 5 #scale 
xc2 = XCube() + [3, 0, 0] #translate

xc3 = xc1 + xc2
print(scad_render(xc3))

### end ###
