#Raw Points Game
import xlrd

class ter(object):
    def __init__(self,name,adjacent,value,owner=None):
        self.name = name
        self.adjacent = adjacent
        self.value = value
        self.owner = owner
        self.highest = 0
        self.leader = owner
    def __repr__(self):
        #return '{0}: {1} (Owned by {2})'.format(self.name,self.value,self.owner)
        return '{0}: {1}'.format(self.name,self.owner)
    
workbook=xlrd.open_workbook("C:\Test\Test.xls")
worksheet = workbook.sheet_by_name('World')
num_rows = worksheet.nrows - 1
curr_row = -1

def load_board(worksheet, curr_row, num_rows):
    num_cells = worksheet.ncols - 1
    curr_row = -1
    board=[]
    while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            curr_cell = -1
            temp = []
            while curr_cell < num_cells:
                    curr_cell += 1
                    cell_value = worksheet.cell_value(curr_row, curr_cell)
                    if curr_cell==1:
                        cell_value=cell_value.split()
                    elif curr_cell==2:
                        cell_value=int(cell_value)
                    temp.append(cell_value)
            territory=ter(temp[0],temp[1],temp[2])
            board.append(territory)
    return board

class civ(object):
    def __init__(self,name,score,start=[]):
        self.name = name
        self.score = score
        self.start = start
    def __repr__(self):
        return '{0}({1})'.format(self.name,self.score)
    def place_orders(self,board,actions):
        """Tells the player the situation and accepts their placement of points."""
        options=[]
        for ter in board:
                if ter.owner==self:
                    options.append(ter)
                    for adjacent in ter.adjacent:
                        for check in board:
                            if check.name==adjacent:
                                options.append(check)
        print('{0}`s turn. You have {1} points. Where do you use them? Input h for help.'.format(self.name,self.score))
        action = input('--> ')
        if action=='e':
            if self.score==0:
                print('-----Next Player-----')
                return actions
            else:
                print('Are you sure? You still have {0} points. Input end to end your turn anyway.'.format(self.score))
        elif action == 'end':
            print('-----Next Player-----')
            return actions
        elif action == 'h':
            print('Input m to see the map, t to see your options, a territory name to invest in it, or e to end turn.')
        elif action=='m':
            print(board)
        elif action=='t':
            print(options)
        else:
            option_names=[]
            for option in options:
                option_names.append(option.name)
            if action in option_names:
                location=action
                try:
                    action = int(input('How many points? '))
                except ValueError:
                    print('That is not a number.')
                    action = int(input('How many points? '))
                if action<=self.score:
                    self.score-=action
                    bid=action
                    for ter in options:
                        if ter.name==location:
                            location=ter
                    investment=(location,bid,self)
                    actions.append(investment)
                    print(actions)
                else:
                    print('You do not have that many points.')
            else:
                print('That is not an available territory.')
        new_actions = actions
        return self.place_orders(board,new_actions)
import math
import random
class nullAI(civ):
    def place_orders(self,board,actions):
        """Creates a set of orders to bid one point on each unclaimed option."""
        return actions
class holdAI(civ):
    def place_orders(self,board,actions):
        """Creates a set of orders to bid one point on each unclaimed option."""
        ter=self.start[0]
        points=self.score
        actions=[(ter,points,self)]
        self.score=0
        return actions
class simpleAI(civ):
    def place_orders(self,board,actions):
        """Creates a set of orders to bid one point on each unclaimed option."""
        options=[]
        for ter in board:
                if ter.owner==self:
                    options.append(ter)
                    for adjacent in ter.adjacent:
                        for check in board:
                            if check.name==adjacent:
                                options.append(check)
        random.shuffle(options)
        for ter in options:
            if self.score<1:
                return actions
            elif ter.owner!=self:
                self.score-=1
                investment=(ter,1,self)
                actions.append(investment)
        #print(actions)
        return actions
class randomAI(civ):
    def place_orders(self,board,actions):
        """Creates a set of orders to bid one point on each unclaimed option."""
        options=[]
        for ter in board:
                if ter.owner==self:
                    options.append(ter)
                    for adjacent in ter.adjacent:
                        for check in board:
                            if check.name==adjacent:
                                options.append(check)
        random.shuffle(options)
        for ter in options:
            if self.score<1:
                return actions
            elif ter.owner!=self:
                bid=random.randrange(self.score)
                self.score-=bid
                investment=(ter,bid,self)
                actions.append(investment)
        #print(actions)
        return actions
    
World=load_board(worksheet, curr_row, num_rows)
##West = civ('West',3, [World[0]])
##East = civ('East',3, [World[4]])
##simpleEast = simpleAI('simpleEast',3, [World[4]])
##Testers = [West,East]
##simpleTesters = [West,simpleEast]
##randomTesters=simpleTesters

#test=math.floor(27/9)
#print(test, type(test))

import math
import random
def random_testers(board):
    random.shuffle(board)
    size=len(board)
    number=math.floor(size/3)
    testers=[]
    for player in range(1,number+1):
        home=board[player-1]
        name=home.name
        civilization=randomAI(name,3,[home])
##        if player==1:
##            civilization=simpleAI(name,3,[home])
##        else:
##            civilization=holdAI(name,3,[home])
        testers.append(civilization)

    return testers
randomTesters=random_testers(World)
    




def New_Game(board, players, victory):
    """Begins a new game by taking in a list of ters and a list of civs.
    Play out a series of turns and end the game when one player reaches the victory points."""
    for civ in players:
        print(civ.start)
        for home in civ.start:
            for ter in board:
                if home==ter:
                    ter.owner=civ
    turn = 1
    return take_turn(board,players,turn,victory,orders=[])

def take_turn(board,players,turn,victory,orders):
    """Iterate through a list of players and produce a new board from their actions."""
    print('>>>>> TURN',turn,'<<<<<')
    print(board)
    check=0
##    for ter in board:
##        if ter.owner==None:
##            check+=1
##    if check==0:
##        return board
    if turn>100:
        return board
    #print(board)
    for player in players:
        alive=0
        for ter in board:
            if ter.owner==player:
                alive+=1
        if alive==0:
            print ('Player {0} eliminated with 0 points.'.format(player.name))
            players.remove(player)
    for player in players:
        if player.score < 1:
            print ('Player {0} eliminated with {1} points.'.format(player.name,player.score))
            players.remove(player)
            #print(len(players))
    for player in players:
        if len(players)==1 and player.score>0:
            return 'Game over. {0} wins with {1} points.'.format(player.name,player.score), board
    for player in players:
        #print(player.name, len(players))
        if player.score >= victory:
            return 'Game over. {0} wins with {1} points.'.format(player.name,player.score), board
        else:
            action = player.place_orders(board,[])
            orders.append(action)
    new_board = eval_orders(board,orders)
    turn += 1
    return take_turn(new_board,players,turn,victory,orders)

def eval_orders(board,orders):
    """Takes in an old board and a list of 3-term tuples which describe player investments.
    It then calculates which player had the greatest investment in each territory and changes owners.
    Finally, it counts up the values of each territory and supplies the owner with the appropriate points."""
    contests = []
    for order in orders: #in case a player has no orders
        if order==[]:
            orders.remove([])
    for ter in board:
        for player in orders:
            for order in player:
                territory=order[0]
                contender = order[2]
                bid = order[1]
                if ter.name==territory.name:
                    if ter not in contests:
                        contests.append(ter)
                    if bid>ter.highest:
                        ter.highest=bid
                        ter.leader=contender
                    elif bid==ter.highest:
                        ter.leader=ter.owner   
    for ter in contests: #actual function
        if ter.leader!=None:
            ter.owner=ter.leader
            for elem in board:
                if elem.name==ter.name:
                    board.remove(elem)
            board.append(ter)
    for ter in board:
        if ter.owner!=None:
            ter.owner.score+=ter.value
    return board

print(New_Game(World,randomTesters,100))






    



