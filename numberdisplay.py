
from segments import *

class NumberDisplay():
  #class variable to have only one instance of Segments()   
  segments = Segments()
  #Set the numbers in this dictionary with the Segments that uses
  numbers = {
      '1':[segments.right_upper, segments.right_lower],
      '2':[segments.upper,segments.bottom, segments.mid,segments.right_upper,segments.left_lower],
      '3':[segments.upper,segments.bottom, segments.mid,segments.right_upper, segments.right_lower],
      '4':[segments.mid,segments.right_upper, segments.right_lower,segments.left_upper],
      '5':[segments.upper,segments.bottom, segments.mid,segments.right_lower,segments.left_upper],
      '6':[segments.upper,segments.bottom, segments.mid,segments.right_lower, segments.left_lower,segments.left_upper],
      '7':[segments.upper,segments.right_upper, segments.right_lower], 
      '8':[segments.upper,segments.bottom, segments.mid,segments.right_upper, segments.right_lower, segments.left_lower,segments.left_upper],
      '9':[segments.upper,segments.bottom, segments.mid,segments.right_upper, segments.right_lower,segments.left_upper],
      '0':[segments.upper,segments.bottom, segments.right_upper, segments.right_lower, segments.left_lower,segments.left_upper]
      }

  #check input and raises errors
  def check_input(self, size, target):
    if(size <= 0):
      raise ValueError('Size cant be less than 1')
    elif(size > 10):
      raise ValueError('Size cannot be larger than 10')
    if(len(target) == 0):
      raise ValueError('Empty target')
    for char in target:
      if char not in self.numbers:
        raise ValueError('A not natural number was found')

  #return and empty grid
  def get_empty_grid(self,rows, columns):
    grid = []
    for _ in range(rows ):
      grid.append('' * (columns) )
    return grid

  #return a grid fully of blank spaces
  def get_grid(self,rows, columns):
    grid = []
    for _ in range(rows ):
      grid.append(' ' * (columns) )
    return grid

  #print a grid
  def print_grid(self, grid):
    for part in grid:
      print(part)

  #depends on the target and size will return print some numbers ASCII art 
  def display_numbers(self,target, size):
    #variables
    self.check_input(size,target)
    rows, columns = size*2 +3, size+2
    #get an empty grid for the final number
    grid = self.get_empty_grid(rows, columns)
    #go throug every number in the line
    for number in target:
      #get the grid of this number
      current = self.get_grid(rows,columns)
      #call a function where set the '-' character
      for segment in self.numbers[number]:
        segment(current,rows,columns)
      #add to the real grid
      for line in range(rows):
        grid[line] += current[line] + ' '
    return grid
