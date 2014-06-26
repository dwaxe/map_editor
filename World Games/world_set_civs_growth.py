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
        self.age = 1 #New code for territoy growth. 10/21/13
    def __repr__(self):
        #return '{0}: {1} (Owned by {2})'.format(self.name,self.value,self.owner)
        return '{0}: {1}'.format(self.name,self.owner)
    
workbook=xlrd.open_workbook("C:\Test\Test.xls")
worksheet = workbook.sheet_by_name('World')
worksheet2 = workbook.sheet_by_name('weighted')
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
weighted=load_board(worksheet2, curr_row, num_rows)
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
def simple_testers(board):
    random.shuffle(board)
    size=len(board)
    number=math.floor(size/10)
    testers=[]
    for player in range(1,number+1):
        home=board[player-1]
        name=home.name
        civilization=simpleAI(name,3,[home])
##        if player==1:
##            civilization=simpleAI(name,3,[home])
##        else:
##            civilization=holdAI(name,3,[home])
        testers.append(civilization)
    return testers
def Sealand_test(board):
    random.shuffle(board)
    size=len(board)
    number=math.floor(size/3)
    testers=[]
    for player in range(1,number):
        home=board[player-1]
        name=home.name
        if name!='NoS':
            civilization=randomAI(name,3,[home])
        testers.append(civilization)
    for ter in board:
        if ter.name=='NoS':
            home=board[player-1]
            Sealand=randomAI('SEALAND',7,[home])
    testers.append(Sealand)
            
    return testers
randomTesters=random_testers(World)
simpleTesters=simple_testers(World)
Sealand=Sealand_test(World)


c=weighted
#print(c)


##Gaul=randomAI('Gaul',3,[c[80]])
##Germany=randomAI('Germania',3,[c[92]])
##Rome=randomAI('Rome',5,[c[100]])
##Greece=randomAI('Athens',3,[c[125]])
##Carthage=randomAI('Carthage',3,[c[140]])
##Egypt=randomAI('Memphis',3,[c[145]])
##Nubia=randomAI('Meroe',3,[c[160]])
##Babylon=randomAI('Babylon',3,[c[181]])
##Persia=randomAI('Persepolis',3,[c[195]])
##India=randomAI('Delhi',3,[c[205]])
##Tamil=randomAI('Chennai',3,[c[209]])
##China=randomAI('Xi`an',3,[c[222]])
##Korea=randomAI('Seoul',3,[c[233]])
##Japan=randomAI('Kyoto',3,[c[238]])
##Srivijaya=randomAI('Jakarta',3,[c[255]])
##classicTesters=[Rome, Greece, Carthage, Egypt, Nubia, Babylon, Persia, India, Tamil, China, Korea, Japan]

##Canada=simpleAI('Canada',3,[c[5]])
##UnitedStates=simpleAI('UnitedStates',3,[c[22]])
##Mexico=simpleAI('Mexico',3,[c[29]])
##Guatemala=simpleAI('Guatemala',3,[c[40]])
##Peru=simpleAI('Peru',3,[c[46]])
##Argentina=simpleAI('Argentina',3,[c[52]])
##Brazil=simpleAI('Brazil',3,[c[59]])
##Britain=simpleAI('Britain',3,[c[67]])
##Sweden=simpleAI('Sweden',3,[c[71]])
##Denmark=simpleAI('Denmark',3,[c[73]])
##France=simpleAI('France',3,[c[79]])
##Spain=simpleAI('Spain',3,[c[84]])
##Portugal=simpleAI('Portugal',3,[c[87]])
##Germany=simpleAI('Germany',3,[c[93]])
##Italy=simpleAI('Italy',3,[c[100]])
##Poland=simpleAI('Poland',3,[c[105]])
##Austria=simpleAI('Austria',3,[c[110]])
##Hungary=simpleAI('Hungary',3,[c[118]])
##Greece=simpleAI('Greece',3,[c[125]])
##Russia=simpleAI('Russia',3,[c[130]])
##Morocco=simpleAI('Morocco',3,[c[138]])
##Egypt=simpleAI('Egypt',3,[c[145]])
##Ghana=simpleAI('Ghana',3,[c[150]])
##SouthAfrica=simpleAI('SouthAfrica',3,[c[159]])
##Ethiopia=simpleAI('Ethiopia',3,[c[164]])
##Turkey=simpleAI('Turkey',3,[c[173]])
##Syria=simpleAI('Syria',3,[c[176]])
##Iraq=simpleAI('Iraq',3,[c[181]])
##Arabia=simpleAI('Arabia',3,[c[187]])
##Iran=simpleAI('Iran',3,[c[194]])
##Mongolia=simpleAI('Mongolia',3,[c[198]])
##India=simpleAI('India',3,[c[205]])
##Dravida=simpleAI('Dravida',3,[c[206]])
##China=simpleAI('China',3,[c[222]])
##Korea=simpleAI('Korea',3,[c[233]])
##Japan=simpleAI('Japan',3,[c[239]])
##Vietnam=simpleAI('Vietnam',3,[c[247]])
##Indonesia=simpleAI('Indonesia',3,[c[255]])
##Australia=simpleAI('Australia',3,[c[262]])
##Polynesia=simpleAI('Polynesia',3,[c[267]])

Canada=randomAI('Canada',3,[c[5]])
UnitedStates=randomAI('UnitedStates',3,[c[22]])
Mexico=randomAI('Mexico',3,[c[29]])
Guatemala=randomAI('Guatemala',3,[c[40]])
Peru=randomAI('Peru',3,[c[46]])
Argentina=randomAI('Argentina',3,[c[52]])
Brazil=randomAI('Brazil',3,[c[59]])
Britain=randomAI('Britain',3,[c[67]])
Sweden=randomAI('Sweden',3,[c[71]])
Denmark=randomAI('Denmark',3,[c[73]])
France=randomAI('France',3,[c[79]])
Spain=randomAI('Spain',3,[c[84]])
Portugal=randomAI('Portugal',3,[c[87]])
Germany=randomAI('Germany',3,[c[93]])
Italy=randomAI('Italy',3,[c[100]])
Poland=randomAI('Poland',3,[c[105]])
Austria=randomAI('Austria',3,[c[110]])
Hungary=randomAI('Hungary',3,[c[118]])
Greece=randomAI('Greece',3,[c[125]])
Russia=randomAI('Russia',3,[c[130]])
Morocco=randomAI('Morocco',3,[c[138]])
Egypt=randomAI('Egypt',3,[c[145]])
Ghana=randomAI('Ghana',3,[c[150]])
SouthAfrica=randomAI('SouthAfrica',3,[c[159]])
Ethiopia=randomAI('Ethiopia',3,[c[164]])
Turkey=randomAI('Turkey',3,[c[173]])
Syria=randomAI('Syria',3,[c[176]])
Iraq=randomAI('Iraq',3,[c[181]])
Arabia=randomAI('Arabia',3,[c[187]])
Iran=randomAI('Iran',3,[c[194]])
Mongolia=randomAI('Mongolia',3,[c[198]])
India=randomAI('India',3,[c[205]])
Dravida=randomAI('Dravida',3,[c[206]])
China=randomAI('China',3,[c[222]])
Korea=randomAI('Korea',3,[c[233]])
Japan=randomAI('Japan',3,[c[239]])
Vietnam=randomAI('Vietnam',3,[c[247]])
Indonesia=randomAI('Indonesia',3,[c[255]])
Australia=randomAI('Australia',3,[c[262]])
Polynesia=randomAI('Polynesia',3,[c[267]])



setTesters=[Canada,UnitedStates,Mexico,Guatemala,Peru,Argentina,Brazil,Britain,Sweden,Denmark,France,Spain,Portugal,
            Germany,Italy,Poland,Austria,Hungary,Greece,Russia,Morocco,Egypt,Ghana,SouthAfrica,Ethiopia,Turkey,
            Syria,Iraq,Arabia,Iran,Mongolia,India,Dravida,China,Korea,Japan,Vietnam,Indonesia,Australia,Polynesia]




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
    #print(board)
    print(players)
    check=0
##    for ter in board:
##        if ter.owner==None:
##            check+=1
##    if check==0:
##        return board
    if turn>200:
        return [players, board]
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
            print( 'Game over. {0} wins with {1} points.'.format(player.name,player.score))
            return [players, board]
    for player in players:
        #print(player.name, len(players))
        if player.score >= victory:
            print ('Game over. {0} wins with {1} points.'.format(player.name,player.score))
            return [players, board]
    for player in players:
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
        if ter.leader==ter.owner or ter.leader==None and ter.owner!=None: #New code for territoy growth. 10/21/13
            ter.age+=1 
        elif ter.leader!=None:
            ter.owner=ter.leader
            ter.age=1 #New code for territoy growth. 10/21/13
            for elem in board:
                if elem.name==ter.name:
                    board.remove(elem)
            board.append(ter)
    for ter in board:
        if ter.owner!=None:
            if ter.age>25:
                print(ter.name)
                x=input('')
            ter.owner.score+=ter.value*ter.age #New code for territoy growth. 10/21/13
    return board

#game=New_Game(World,randomTesters,100)
#game=New_Game(World,simpleTesters,30)
#game=New_Game(World,Sealand,100)

game=New_Game(c,setTesters,200)
board=game[1]
players=game[0]
#print(players)


for player in players:
    #print(player)
    #print(type(player))
    player.final=[player]
    for ter in board:
        if ter.owner==player:
            if ter.value>0:
                player.final.append(ter.name)
    print(player.final)











    



