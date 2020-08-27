class Segments():
  #set the upper segment with the '-' character
  def upper(self,grid,rows,columns):
    newline = ' ' + ('-' * (columns - 2) ) + ' '
    grid[0] = newline
    return grid

  #set the right upper segment with the '|' character
  def right_upper(self,grid,rows,columns):
    for i in range(1,rows//2):
      newline = ''
      for j in range(columns-1):
        newline += grid[i][j] 
      grid[i] = newline + '|'
    return grid

  #set the right lower segment with the '|' character
  def right_lower(self,grid,rows,columns):
    for i in range(rows//2 + 1,rows-1):
      newline = ''
      for j in range(columns-1):
        newline += grid[i][j] 
      grid[i] = newline + '|'
    return grid

  #set the bottom segment with the '-' character
  def bottom(self,grid,rows,columns):
    newline = ' ' + ('-' * (columns - 2) ) + ' '
    grid[rows-1] = newline
    return grid
 
  #set the left upper segment with the '|' character
  def left_upper(self,grid,rows,columns):
    for i in range(1,rows//2):
      newline = '|' + grid[i][1:]
      grid[i] = newline
    return grid
    
  #set the left lower upper segment with the '|' character
  def left_lower(self,grid,rows,columns):
    for i in range(rows//2 + 1,rows-1):
      newline = '|' + grid[i][1:]
      grid[i] = newline
    return grid

  #set the mid segment with the '-' character
  def mid(self,grid,rows,columns):
    newline = ' ' + ('-' * (columns - 2) ) + ' '
    grid[rows//2] = newline
    return grid

