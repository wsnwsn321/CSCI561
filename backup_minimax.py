import copy
def update_board(Grid,index_i,index_j,player):
    score =1
    i=index_i
    j=index_j
    count =0
    Grid[index_i][index_j]=player
    #down
    while i+1<N and count<3:
        if Grid[i+1][j]!=3:
            if Grid[i+1][j]==0:
                Grid[i + 1][j]=-player
            #slot is already filled by the other player's score
            if player -Grid[i+1][j]== 3:
                Grid[i + 1][j] = -3
        else:
            break
        i+=1
        count+=1
    i = index_i
    j = index_j
    count=0
    #up
    while i-1>=0 and count<3:
        if Grid[i-1][j] != 3:
            if Grid[i - 1][j] == 0:
                Grid[i - 1][j] = -player
                # slot is already filled by the other player's score
            if player - Grid[i - 1][j] == 3:
                Grid[i - 1][j] = -3
        else:
            break
        i-=1
        count += 1
    i = index_i
    j = index_j
    count = 0
    #left
    while j-1 >= 0 and count<3:
        if Grid[i][j-1] != 3:
            if Grid[i][j-1] == 0:
                Grid[i][j - 1] = -player
                # slot is already filled by the other player's score
            if player - Grid[i][j-1] == 3:
                Grid[i][j - 1] = -3
        else:
            break
        j -= 1
        count+=1
    i = index_i
    j = index_j
    count = 0
    #right
    while j+1 < N and count<3:
        if Grid[i][j+1] != 3:
            if Grid[i][j+1] == 0:
                Grid[i][j + 1] = -player
                # slot is already filled by the other player's score
            if player - Grid[i][j+1] == 3:
                Grid[i][j + 1] = -3
        else:
            break
        j += 1
        count += 1
    i = index_i
    j = index_j
    count = 0
    #down left
    while i+1<N and j-1>=0 and count<3:
        if Grid[i+1][j-1] != 3:
            if Grid[i+1][j-1] == 0:
                Grid[i + 1][j - 1] = -player
                # slot is already filled by the other player's score
            if player - Grid[i+1][j-1] == 3:
                Grid[i + 1][j - 1] = -3
        else:
            break
        i += 1
        j-=1
        count += 1
    #up left
    i = index_i
    j = index_j
    count = 0
    while i-1 >= 0 and j-1 >= 0 and count<3:
        if Grid[i-1][j-1] != 3:
            if Grid[i-1][j-1] == 0:
                Grid[i - 1][j - 1] = -player
                # slot is already filled by the other player's score
            if player - Grid[i-1][j-1] == 3:
                Grid[i - 1][j - 1] = -3
        else:
            break
        i -= 1
        j -= 1
        count += 1
    #down right
    i = index_i
    j = index_j
    count = 0
    while i+1 < N and j+1 < N and count<3:
        if Grid[i+1][j+1] != 3:
            if Grid[i+1][j+1] == 0:
                Grid[i + 1][j + 1] = -player
                # slot is already filled by the other player's score
            if player - Grid[i+1][j+1] == 3:
                Grid[i + 1][j + 1] = -3
        else:
            break
        i += 1
        j += 1
        count += 1
    i = index_i
    j = index_j
    count = 0
    #up right
    while i-1 >=0 and j+1 < N and count<3:
        if Grid[i-1][j+1] != 3:
            if Grid[i-1][j+1] == 0:
                Grid[i - 1][j + 1]= -player
                # slot is already filled by the other player's score
            if player - Grid[i-1][j+1] == 3:
                Grid[i - 1][j + 1] = -3
        else:
            break
        i -= 1
        j += 1
        count += 1
    return score

#update the board when reading from file, which only contains emitters but no radiant
def fulfill_original_board(Grid):
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            if Grid[i][j]==1 or Grid[i][j]==2:
                update_board(Grid,i,j,Grid[i][j])

#check if there's still available slot to put emitters on the board
def terminate_condition(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                return False
    return True

#calculate player/ai score
def get_player_score(grid,player):
    player_score =0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==player or grid[i][j]==-player or grid[i][j]==-3:
                player_score+=1
    return player_score

#get the diff of score between player and ai
def player_win_state(grid):
    p1_score = get_player_score(grid,1)
    p2_score = get_player_score(grid,2)
    return p1_score-p2_score

def get_max(grid,player,depth):
    times.append(len(times))
    if depth == 0 or terminate_condition(grid):
        player_score = player_win_state(grid)
        return [-1, -1, player_score]
    max_score = [-1,-1,float('-inf')]
    for i in range(0, N):
        for j in range(0, N):
            if grid[i][j] == 0:
                temp_grid = copy.deepcopy(grid)
                update_board(temp_grid,i, j,player)
                score = get_min(temp_grid,3-player,depth-1)
                score[0] = i
                score[1] = j
                if max_score[2] < score[2]:
                    max_score = score
    return max_score

def get_min(grid,player,depth):
    times.append(len(times))
    if depth==0 or terminate_condition(grid):
        player_score = player_win_state(grid)
        return [-1, -1, player_score]
    min_score = [-1,-1,float('inf')]
    for i in range(0, N):
        for j in range(0, N):
            if grid[i][j] == 0:
                temp_grid = copy.deepcopy(grid)
                update_board(temp_grid,i, j,player)
                score = get_max(temp_grid,3-player,depth-1)
                score[0]=i
                score[1]=j
                if min_score[2] > score[2]:
                    min_score = score
    return min_score

def minmax(grid,player,depth):
    if player==1:
        return get_max(grid,player,depth)
    else:
        return get_min(grid,player,depth)




with open('input.txt','r') as f:
    N = int(f.readline())
    Grid = [[0 for x in range(N)] for y in range(N)]
    i=0
    #save the data into the 2d array
    for line in f:
        j=0
        for letter in line:
            if letter!='\n':
                Grid[i][j] =int(letter)
            j+=1
        i+=1

#search through grid to find available slot to put emiters
times =[]
fulfill_original_board(Grid)
s= minmax(Grid,1,4)
print s
print len(times)


f = open("output.txt", "w")
f.write(str(s[0]))
f.write(' ')
f.write(str(s[1]))



