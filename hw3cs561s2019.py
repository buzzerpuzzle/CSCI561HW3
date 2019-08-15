from copy import copy, deepcopy
def value_iteration(grid, grid_status, shreshold, discount, prob, rewards):
    grid_buffer = []
    grid_status_buffer = []
    flag = 0
    #print flag
    for i in range(len(grid)):
        grid_buffer.append([0.0]*len(grid))
        grid_status_buffer.append(['U']*len(grid))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid_status[i][j] != 'E' and grid_status[i][j] != 'N':
                candidate = [0.0, 0.0, 0.0, 0.0]
                #Move Up
                if  i-1<0:
                    U = grid[i][j]
                else:
                    if grid_status[i-1][j]=='N':
                        U = grid[i][j]
                    else:
                        U = grid[i-1][j]
                
                if i-1<0 or j-1<0:
                    U1 = grid[i][j]
                else:
                    if grid_status[i-1][j-1]=='N':
                        U1 = grid[i][j]
                    else:
                        U1 = grid[i-1][j-1]
                if i-1<0 or j+1>len(grid)-1:
                    U2 = grid[i][j]
                else:
                    if grid_status[i-1][j+1] == 'N':
                        U2 = grid[i][j]
                    else:
                        U2 = grid[i-1][j+1]
                
                candidate[0] = float(U)*prob + float(U1)*( (1-prob)/2 ) + float(U2)*( (1-prob)/2 )

                #candidate[0] = calculation_iteration(grid, grid_status, i, j, 'U', prob, len(grid))

                #if i-1 >= 0:
                #    if grid_status[i-1][j] != 'N':
                #        if j-1 >= 0:
                #            if grid_status[i-1][j-1] != 'N':
                #                if j+1 < len(grid[i-1]):
                #                    if grid_status[i-1][j+1] != 'N':
                #                        candidate[0] = (prob*grid[i-1][j] + ((1-prob)/2)*grid[i-1][j-1] + ((1-prob)/2)*grid[i-1][j+1])
                #                    else:
                #                        candidate[0] = (prob*grid[i-1][j] + ((1-prob)/2)*grid[i-1][j-1] + ((1-prob)/2)*grid[i][j])
                #                else:
                #                    candidate[0] = (prob*grid[i-1][j] + ((1-prob)/2)*grid[i-1][j-1] + ((1-prob)/2)*grid[i][j])
                #            else:
                #                if j+1 < len(grid[i-1]):
                #                    if grid_status[i-1][j+1] != 'N':
                #                        candidate[0] = (prob*grid[i-1][j] + ((1-prob)/2)*grid[i-1][j+1] + ((1-prob)/2)*grid[i][j])
                #                    else:
                #                        candidate[0] = (prob*grid[i-1][j] + (1-prob)*grid[i][j])
                #                else:
                #                    candidate[0] = (prob*grid[i-1][j] + (1-prob)*grid[i][j])
                #        else:
                #            if j+1 < len(grid[i-1]):
                #                if grid_status[i-1][j+1] != 'N':
                #                    candidate[0] = (prob*grid[i-1][j] + ((1-prob)/2)*grid[i-1][j+1] + ((1-prob)/2)*grid[i][j])
                #                else:
                #                    candidate[0] = (prob*grid[i-1][j] + (1-prob)*grid[i][j])
                #            else:
                #                candidate[0] = (prob*grid[i-1][j] + (1-prob)*grid[i][j])
                #    else:
                #        candidate[0] = 1.0*grid[i][j]
                #else:
                #    candidate[0] = 1.0*grid[i][j]
                
                #Move Down
                if i+1>len(grid)-1:
                    D = grid[i][j]
                else:
                    if grid_status[i+1][j]=='N':
                        D = grid[i][j]
                    else:
                        D = grid[i+1][j]
                
                if i+1>len(grid)-1 or j+1>len(grid)-1:
                    D1 = grid[i][j]
                else:
                    if grid_status[i+1][j+1]=='N':
                        D1 = grid[i][j]
                    else:
                        D1 = grid[i+1][j+1]

                if i+1>len(grid)-1 or j-1<0:
                    D2 = grid[i][j]
                else:
                    if grid_status[i+1][j-1]=='N':
                        D2 = grid[i][j]
                    else:
                        D2 = grid[i+1][j-1]
                
                candidate[1] = float(D)*prob + float(D1)*( (1-prob)/2 ) + float(D2)*( (1-prob)/2 )
                
                #candidate[1] = calculation_iteration(grid, grid_status, i, j, 'D', prob, len(grid))

                #if i+1 < len(grid):
                #    if grid_status[i+1][j] != 'N':
                #        if j-1 >= 0:
                #            if grid_status[i+1][j-1] != 'N':
                #                if j+1 < len(grid[i+1]):
                #                    if grid_status[i+1][j+1] != 'N':
                #                        candidate[1] = (prob*grid[i+1][j] + ((1-prob)/2)*grid[i+1][j-1] + ((1-prob)/2)*grid[i+1][j+1])
                #                    else:
                #                        candidate[1] = (prob*grid[i+1][j] + ((1-prob)/2)*grid[i+1][j-1] + ((1-prob)/2)*grid[i][j])
                #                else:
                #                    candidate[1] = (prob*grid[i+1][j] + ((1-prob)/2)*grid[i+1][j-1] + ((1-prob)/2)*grid[i][j])
                #            else:
                #                if j+1 < len(grid[i+1]):
                #                    if grid_status[i+1][j+1] != 'N':
                #                        candidate[1] = (prob*grid[i+1][j] + ((1-prob)/2)*grid[i+1][j+1] + ((1-prob)/2)*grid[i][j])
                #                    else:
                #                        candidate[1] = (prob*grid[i+1][j] + (1-prob)*grid[i][j])
                #                else:
                #                    candidate[1] = (prob*grid[i+1][j] + (1-prob)*grid[i][j])
                #        else:
                #            if j+1 < len(grid[i+1]):
                #                if grid_status[i+1][j+1] != 'N':
                #                    candidate[1] = (prob*grid[i+1][j] + ((1-prob)/2)*grid[i+1][j+1] + ((1-prob)/2)*grid[i][j])
                #                else:
                #                    candidate[1] = (prob*grid[i+1][j] + (1-prob)*grid[i][j])
                #            else:
                #                candidate[1] = (prob*grid[i+1][j] + (1-prob)*grid[i][j])
                #    else:
                #        candidate[1] = 1.0*grid[i][j]
                #else:
                #    candidate[1] = 1.0*grid[i][j]
                
                #Move Left                
                if j-1<0:
                    L = grid[i][j]
                else:
                    if grid_status[i][j-1]=='N':
                        L = grid[i][j]
                    else:
                        L = grid[i][j-1]
                if i+1>len(grid)-1 or j-1<0:
                    L1 = grid[i][j]
                else:
                    if grid_status[i+1][j-1]=='N':
                        L1 = grid[i][j]
                    else:
                        L1 = grid[i+1][j-1]
                if i-1<0 or j-1<0:
                    L2 = grid[i][j]
                else:
                    if grid_status[i-1][j-1]=='N':
                        L2 = grid[i][j]
                    else:
                        L2 = grid[i-1][j-1]
                
                candidate[2] = float(L)*prob + float(L1)*( (1-prob)/2 ) + float(L2)*( (1-prob)/2 )
                
                #candidate[2] = calculation_iteration(grid, grid_status, i, j, 'L', prob, len(grid))

                #if j-1 >= 0:
                #    if grid_status[i][j-1] != 'N':
                #        if i-1 >= 0:
                #            if grid_status[i-1][j-1] != 'N':
                #                if i+1 < len(grid):
                #                    if grid_status[i+1][j-1] != 'N':
                #                        candidate[2] = (prob*grid[i][j-1] + ((1-prob)/2)*grid[i-1][j-1] + ((1-prob)/2)*grid[i+1][j-1])
                #                    else:
                #                        candidate[2] = (prob*grid[i][j-1] + ((1-prob)/2)*grid[i-1][j-1] + ((1-prob)/2)*grid[i][j])    
                #                else:
                #                    candidate[2] = (prob*grid[i][j-1] + ((1-prob)/2)*grid[i-1][j-1] + ((1-prob)/2)*grid[i][j])    
                #            else:
                #                if i+1 < len(grid):
                #                    if grid_status[i+1][j-1] != 'N':
                #                        candidate[2] = (prob*grid[i][j-1] + ((1-prob)/2)*grid[i+1][j-1] + ((1-prob)/2)*grid[i][j])
                #                    else:
                #                        candidate[2] = (prob*grid[i][j-1] + (1-prob)*grid[i][j])
                #                else:
                #                    candidate[2] = (prob*grid[i][j-1] + (1-prob)*grid[i][j])
                #        else:
                #            if i+1 < len(grid):
                #                if grid_status[i+1][j-1] != 'N':
                #                    candidate[2] = (prob*grid[i][j-1] + ((1-prob)/2)*grid[i+1][j-1] + ((1-prob)/2)*grid[i][j])
                #                else:
                #                    candidate[2] = (prob*grid[i][j-1] + (1-prob)*grid[i][j])
                #            else:
                #                candidate[2] = (prob*grid[i][j-1] + (1-prob)*grid[i][j])
                #    else:
                #        candidate[2] = 1.0*grid[i][j]
                #else:
                #    candidate[2] = 1.0*grid[i][j]

                #Move Right

                if j+1>len(grid)-1:
                    R = grid[i][j]
                else:
                    if grid_status[i][j+1]=='N':
                        R = grid[i][j]
                    else:
                        R = grid[i][j+1]
                
                if i-1<0 or j+1>len(grid)-1:
                    R1 = grid[i][j]
                else:
                    if grid_status[i-1][j+1]=='N':
                        R1 = grid[i][j]
                    else:
                        R1 = grid[i-1][j+1]
                if i+1>len(grid)-1 or j+1>len(grid)-1:
                    R2 = grid[i][j]
                else:
                    if grid_status[i+1][j+1]=='N':
                        R2 = grid[i][j]
                    else:
                        R2 = grid[i+1][j+1]
                
                candidate[3] = float(R)*prob + float(R1)*( (1-prob)/2 ) + float(R2)*( (1-prob)/2 )
 
                #candidate[3] = calculation_iteration(grid, grid_status, i, j, 'R', prob, len(grid))

                #if j+1 < len(grid):
                #    if grid_status[i][j+1] != 'N':
                #        if i-1 >= 0:
                #            if grid_status[i-1][j+1] != 'N':
                #                if i+1 < len(grid):
                #                    if grid_status[i+1][j+1] != 'N':
                #                        candidate[3] = (prob*grid[i][j+1] + ((1-prob)/2)*grid[i-1][j+1] + ((1-prob)/2)*grid[i+1][j+1])
                #                    else:
                #                        candidate[3] = (prob*grid[i][j+1] + ((1-prob)/2)*grid[i-1][j+1] + ((1-prob)/2)*grid[i][j])    
                #                else:
                #                    candidate[3] = (prob*grid[i][j+1] + ((1-prob)/2)*grid[i-1][j+1] + ((1-prob)/2)*grid[i][j])    
                #            else:
                #                if i+1 < len(grid):
                #                    if grid_status[i+1][j+1] != 'N':
                #                        candidate[3] = (prob*grid[i][j+1] + ((1-prob)/2)*grid[i+1][j+1] + ((1-prob)/2)*grid[i][j])
                #                    else:
                #                        candidate[3] = (prob*grid[i][j+1] + (1-prob)*grid[i][j])
                #                else:
                #                    candidate[3] = (prob*grid[i][j+1] + (1-prob)*grid[i][j])
                #        else:
                #            if i+1 < len(grid):
                #                if grid_status[i+1][j+1] != 'N':
                #                    candidate[3] = (prob*grid[i][j+1] + ((1-prob)/2)*grid[i+1][j+1] + ((1-prob)/2)*grid[i][j])
                #                else:
                #                    candidate[3] = (prob*grid[i][j+1] + (1-prob)*grid[i][j])
                #            else:
                #                candidate[3] = (prob*grid[i][j+1] + (1-prob)*grid[i][j])
                #    else:
                #        candidate[3] = 1.0*grid[i][j]
                #else:
                #    candidate[3] = 1.0*grid[i][j]

                pivot = 0
                pivot_value = candidate[0]
                for k in range(len(candidate)):
                    if candidate[k] > pivot_value:
                        pivot = k
                        pivot_value = candidate[k]

                if pivot == 0:
                    grid_status_buffer[i][j] = 'U'
                elif pivot == 1:
                    grid_status_buffer[i][j] = 'D'
                elif pivot == 2:
                    grid_status_buffer[i][j] = 'L'
                elif pivot == 3:
                    grid_status_buffer[i][j] = 'R'

                grid_buffer[i][j] = discount*pivot_value + rewards

                if abs(grid_buffer[i][j] - grid[i][j]) > shreshold:
                    #print abs(pivot_value - grid[i][j])
                    flag = 1
                    #print (i, j)
                    #print abs(pivot_value - grid[i][j])
            else:    
                grid_status_buffer[i][j] = grid_status[i][j]
                grid_buffer[i][j] = grid[i][j]

    #grid = deepcopy(grid_buffer)
    #grid_status = deepcopy(grid_status_buffer)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = grid_buffer[i][j]
            grid_status[i][j] = grid_status_buffer[i][j]

    #print "Inner loop"
    #for i in range(len(grid)):
    #    print grid[i]

    #for i in range(len(grid_status)):
    #    print grid_status[i]

    #return 1

    #print flag

    if flag == 0:
        return 1
    else:
        return 0


def main():
    lines = open("input3.txt").read().splitlines()
    index = 0
    
    gridsize = int(lines[index])
    
    print "Grid Size: "
    print gridsize
    
    index = index + 1

    wallnumber = int(lines[index])
    status = {}

    for i in range(wallnumber):
        tmp = lines[index + i + 1].split(',')
        status[(int(tmp[0]), int(tmp[1]))] = 'W'
        #walls.append((tmp[0], tmp[1]))
    
    index = index + wallnumber + 1
    
    print "Wall states: "
    for key in status:
        if status[key] == 'W':
            print key 
            print status[key]

    terminalnumber = int(lines[index])

    for i in range(terminalnumber):
        tmp = lines[index + i + 1].split(',')
        status[(int(tmp[0]), int(tmp[1]))] = float(tmp[2])
        #terminals.append((tmp[0], tmp[1], tmp[2]))

    index = index + terminalnumber + 1

    print "Terminal states: "
    for key in status:
        if status[key] != 'W':
            print key
            print status[key]

    prob = float(lines[index])

    index = index + 1

    print "Probability: "
    print prob

    rewards = float(lines[index])

    index = index + 1
    
    print "Rewards: "
    print rewards

    discount = float(lines[index])

    index = index + 1
    
    print "Discount factor: "
    print discount

    #grid = [[rewards]*int(gridsize)]*int(gridsize)

    grid = []    
    grid_status = []
    for i in range(gridsize):
        grid.append([rewards]*gridsize)
        grid_status.append(['U']*gridsize)

    for key in status:
        if status[key] != 'W':
            grid[key[0]-1][key[1]-1] = status[key]
            grid_status[key[0]-1][key[1]-1] = 'E'
        else:
            grid[key[0]-1][key[1]-1] = 'W'
            grid_status[key[0]-1][key[1]-1] = 'N'           

    print "grid"

    #for i in range(len(grid)):
    #    print grid[i]
    
    print "grid status"

    #for i in range(len(grid_status)):
    #    print grid_status[i]

    shreshold = abs(rewards)/1000000000
    flag = 0
    count = 0  
    
    #for i in range(100):
    #    value_iteration(grid, grid_status, shreshold, discount, prob)

    while(flag == 0):
        print count
        count = count + 1
        flag = value_iteration(grid, grid_status, shreshold, discount, prob, rewards)
        #if count == 100:
        #    break

    f = open("output.txt","w")
    f2 = open("output_value.txt", "w")   
    print "After grid"
    #for i in range(len(grid)):
    #    print grid[i]
    
    print "After grid status"
    for i in range(len(grid_status)):
        print grid_status[i]
        for j in range(len(grid_status[i])):
            if j + 1 == len(grid_status[i]):
                f.write(grid_status[i][j])
                f2.write(str(grid[i][j]))
            else:
                f.write(grid_status[i][j])
                f.write(',')
                f2.write(str(grid[i][j]))
                f2.write(',')
        f.write('\n')
        f2.write('\n')

    f.close()
    f2.close()

if __name__ == '__main__':
    main()
