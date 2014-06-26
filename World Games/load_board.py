import xlrd

class ter(object):
    def __init__(self,name,adjacent,value,owner=None):
        #self.number = number
        self.name = name
        self.adjacent = adjacent
        self.value = value
        self.owner = owner
        self.highest = 0
        self.leader = owner
    def __repr__(self):
        return '{0}: {1} (Owned by {2})'.format(self.name,self.value,self.owner)
    #def conflict(self,belligerents):
        
workbook=xlrd.open_workbook("C:\Test\Test.xls")
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
curr_row = -1

def list_rows(worksheet,curr_row,num_rows):
    while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            print (row)
	
def load_board(worksheet, curr_row, num_rows):
    num_cells = worksheet.ncols - 1
    curr_row = -1
    board=[]
    while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            #print ('Row:', curr_row)
            curr_cell = -1
            temp = []
            while curr_cell < num_cells:
                    curr_cell += 1
                    # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                    #cell_type = worksheet.cell_type(curr_row, curr_cell)
                    cell_value = worksheet.cell_value(curr_row, curr_cell)
                    #print ('	', cell_type, ':', cell_value)
                    if curr_cell==1:
                        cell_value=cell_value.split()
                        #print(cell_value)
                    elif curr_cell==2:
                        cell_value=int(cell_value)
                        #print(type(cell_value))
                    #print(cell_value,type(cell_value))
                    temp.append(cell_value)
                    #print(territory)
            territory=ter(temp[0],temp[1],temp[2])
            board.append(territory)
    return board
#print(load_board(worksheet, curr_row, num_rows))


#New board format has adjacents as list of territory names rather than list of territories.
##
##class civ(object):
##    def __init__(self,name,score,start=[]):
##        self.name = name
##        self.score = score
##        self.start = start
##    def __repr__(self):
##        return '{0}({1})'.format(self.name,self.score)
##    def place_orders(self,board,actions):
##        """Tells the player the situation and accepts their placement of points."""
##        options=[]
##        for ter in board:
##                if ter.owner==self:
##                    options.append(ter)
##                    for adjacent in ter.adjacent:
##                        for check in board:
##                            if check.name==adjacent:
##                                options.append(check)
##        print('{0}`s turn. You have {1} points. Where do you use them? Input h for help.'.format(self.name,self.score))
##        action = input('--> ')
##        if action=='e':
##            if self.score==0:
##                print('-----Next Player-----')
##                return actions
##            else:
##                print('Are you sure? You still have {0} points. Input end to end your turn anyway.'.format(self.score))
##        elif action == 'end':
##            print('-----Next Player-----')
##            return actions
##        elif action == 'h':
##            print('Input m to see the map, t to see your options, a territory name to invest in it, or e to end turn.')
##        elif action=='m':
##            print(board)
##        elif action=='t':
##            print(options)
##        else:
##            option_names=[]
##            for option in options:
##                option_names.append(option.name)
##            if action in option_names:
##                location=action
##                try:
##                    action = int(input('How many points? '))
##                except ValueError:
##                    print('That is not a number.')
##                    action = int(input('How many points? '))
##                if action<=self.score:
##                    self.score-=action
##                    bid=action
##                    for ter in options:
##                        if ter.name==location:
##                            location=ter
##                    investment=(location,bid,self)
##                    actions.append(investment)
##                    print(actions)
##                else:
##                    print('You do not have that many points.')
##            else:
##                print('That is not an available territory.')
##        new_actions = actions
##        return self.place_orders(board,new_actions)
##import random
##class simpleAI(civ):
##    def place_orders(self,board,actions):
##        """Creates a set of orders to bid one point on each unclaimed option."""
##        options=[]
##        for ter in board:
##                if ter.owner==self:
##                    options.append(ter)
##                    for adjacent in ter.adjacent:
##                        for check in board:
##                            if check.name==adjacent:
##                                options.append(check)
##        random.shuffle(options)
##        #print(options)
##        for ter in options:
##            if self.score<1:
##                return actions
##            elif ter.owner!=self:
##                self.score-=1
##                investment=(ter,1,self)
##                actions.append(investment)
##        return actions
##    
##Australia=(load_board(worksheet, curr_row, num_rows))
##West = civ('West',3, [Australia[0]])
##East = civ('East',3, [Australia[4]])
##simpleEast = simpleAI('simpleEast',3, [Australia[4]])
##Testers = [West,East]
##simpleTesters = [West,simpleEast]
##
##def New_Game(board, players, victory):
##    """Begins a new game by taking in a list of ters and a list of civs.
##    Play out a series of turns and end the game when one player reaches the victory points."""
##    for civ in players:
##        for home in civ.start:
##            for ter in board:
##                if home==ter:
##                    ter.owner=civ
##    turn = 1
##    return take_turn(board,players,turn,victory,orders=[])
##
##def take_turn(board,players,turn,victory,orders):
##    """Iterate through a list of players and produce a new board from their actions."""
##    print('>>>>> TURN',turn,'<<<<<')
##    for player in players:
##        if player.score < 1:
##            print ('Player {0} eliminated with {1} points.'.format(player.name,player.score))
##            players.remove(player)
##            print(len(players))
##    for player in players:
##        if len(players)==1 and player.score>0:
##            return 'Game over. {0} wins with {1} points.'.format(player.name,player.score)
##    for player in players:
##        print(player.name, len(players))
##        if player.score >= victory:
##            return 'Game over. {0} wins with {1} points.'.format(player.name,player.score)
##        else:
##            action = player.place_orders(board,[])
##            orders.append(action)
##    new_board = eval_orders(board,orders)
##    turn += 1
##    return take_turn(new_board,players,turn,victory,orders)
##
##def eval_orders(board,orders):
##    """Takes in an old board and a list of 3-term tuples which describe player investments.
##    It then calculates which player had the greatest investment in each territory and changes owners.
##    Finally, it counts up the values of each territory and supplies the owner with the appropriate points."""
##    contests = []
##    for order in orders: #in case a player has no orders
##        if order==[]:
##            orders.remove([])
##    for ter in board:
##        for player in orders:
##            for order in player:
##                territory=order[0]
##                contender = order[2]
##                bid = order[1]
##                if ter.name==territory.name:
##                    if ter not in contests:
##                        contests.append(ter)
##                    if bid>ter.highest:
##                        ter.highest=bid
##                        ter.leader=contender
##                    elif bid==ter.highest:
##                        ter.leader=ter.owner  
##    for ter in contests: #actual function
##        if ter.leader!=None:
##            ter.owner=ter.leader
##            for elem in board:
##                if elem.name==ter.name:
##                    board.remove(elem)
##            board.append(ter)
##    for ter in board:
##        if ter.owner!=None:
##            ter.owner.score+=ter.value
##    return board
##
##def derp():
##    for player in orders: #helper code
##        print(player)
##        for order in player:
##            ter = order[0]
##            contender = order[2]
##            bid = order[1]
##            print(ter.highest)
##            if ter not in contests:
##                contests.append(ter)
##            if bid>ter.highest:
##                ter.highest=bid
##                ter.leader=contender
##                print(ter.highest)
##            elif bid==ter.highest:
##                ter.leader=ter.owner
##    for ter in contests: #actual function
##        if ter.leader!=None:
##            ter.owner=ter.leader
##            for elem in board:
##                if elem.name==ter.name:
##                    board.remove(elem)
##            board.append(ter)
##    for ter in board:
##        if ter.owner!=None:
##            ter.owner.score+=ter.value
##    return board




#print(New_Game(Australia,simpleTesters,10))












