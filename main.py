import sys
from numberdisplay import NumberDisplay 

if __name__ == '__main__':
    numberdisplay = NumberDisplay()
    #here the main loop will be executed
    while True:
        line = sys.stdin.readline().strip().split(' ')
        #get the parameters
        size, target = line[0].split(',')
        size = int(size)
        #check for 0,0 starting the line 
        if size == 0 and target == '0':
            break
        result = numberdisplay.display_numbers(target, size)
        numberdisplay.print_grid(result)
        #check for 0,0 at the end of the line
        if len(line) > 1:
            line[1] == '0,0'
            break
