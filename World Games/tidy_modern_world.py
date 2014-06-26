#Raw Points Game
import xlrd

class ter(object):
    def __init__(self,name,adjacent,value,full_name,owner=None):
        self.name = name
        self.adjacent = adjacent
        self.value = value
        self.owner = owner
        self.highest = 0
        self.leader = owner
        self.full_name = full_name
    def __repr__(self):
        #return '{0}: {1} (Owned by {2})'.format(self.name,self.value,self.owner)
        return '{0} ({1}): {2}'.format(self.full_name,self.name,self.owner)
    
workbook=xlrd.open_workbook("C:\Test\Test.xls")
worksheet = workbook.sheet_by_name('World')
worksheet2 = workbook.sheet_by_name('classic')
worksheet3 = workbook.sheet_by_name('weighted_no_oceans')
num_rows = worksheet.nrows -1
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
            territory=ter(temp[0],temp[1],temp[2],temp[3])
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
        posessions=[]
        for ter in board:
                if ter.owner==self:
                    posessions.append(ter)
        options=[]
        for ter in posessions:  
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
            print('Input m to see the map, s to see your possessions, t to see your options, a territory name to invest in it, or e to end turn.')
        elif action=='m':
            print(board)
        elif action=='t':
            print(options)
        elif action=='s':
            for ter in posessions:
                print (ter.full_name)
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
classic=load_board(worksheet2, curr_row, num_rows)
weighted=load_board(worksheet3, curr_row, num_rows)
w=weighted
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

US=randomAI('UnitedStates',10,[w[2],w[13],w[14],w[15],w[16],w[17],w[18],w[19],w[20],w[21],w[22],w[23],w[24],w[25],w[26],w[200],w[267]])
Canada=randomAI('Canada',4,[w[3],w[4],w[5],w[6],w[7],w[8],w[9]])
Mexico=randomAI('Mexico',4,[w[27],w[28],w[29],w[30],w[31]])
Cuba=randomAI('Cuba',1,[w[34]])
DomRep=randomAI('Dominican Republic',1,[w[36]])
Guatemala=randomAI('Guatemala',1,[w[41]])
Colombia=randomAI('Colombia',1,[w[42]])
Venezuela=randomAI('Venezuela',1,[w[40]])
Peru=randomAI('Peru',1,[w[46]])
Chile=randomAI('Chile',1,[w[51]])
Argentina=randomAI('Argentina',1,[w[52],w[53]])
Uruguay=randomAI('Uruguay',1,[w[54]])
Brazil=randomAI('Brazil',4,[w[55],w[56],w[57],w[58],w[59],w[60]])
Ireland=randomAI('Ireland',1,[w[63]])
UK=randomAI('UnitedKingdom',4,[w[64],w[65],w[66],w[67]])
Norway=randomAI('Norway',1,[w[69]])
Sweden=randomAI('Sweden',1,[w[70]])
Finland=randomAI('Finland',1,[w[71]])
Denmark=randomAI('Denmark',1,[w[73]])
Dutch=randomAI('Netherlands',1,[w[75]])
Belgium=randomAI('Belgium',1,[w[76]])
France=randomAI('France',4,[w[44],w[77],w[78],w[79],w[80],w[81],w[82]])
Spain=randomAI('Spain',3,[w[83],w[84],w[85],w[86]])
Portugal=randomAI('Portugal',1,[w[87]])
Germany=randomAI('Germany',4,[w[90],w[91],w[92],w[93],w[94]])
Swiss=randomAI('Switzerland',1,[w[95]])
Italy=randomAI('Italy',4,[w[97],w[98],w[99],w[100],w[101]])
Poland=randomAI('Poland',3,[w[104],w[105],w[106],w[107]])
Czech=randomAI('Czech Republic',1,[w[108]])
Austria=randomAI('Austria',1,[w[109]])
Latvia=randomAI('Latvia',1,[w[111]])
Ukraine=randomAI('Ukraine',2,[w[114],w[115],w[116]])
Croatia=randomAI('Croatia',1,[w[119]])
Serbia=randomAI('Serbia',1,[w[121]])
Romania=randomAI('Romania',1,[w[122]])
Bulgaria=randomAI('Bulgaria',1,[w[123]])
Greece=randomAI('Greece',1,[w[125]])
Russia=randomAI('Russia',5,[w[128],w[129],w[130],w[131],w[132],w[133],w[134],w[135],w[136],w[137]])
Morocco=randomAI('Morocco',1,[w[138]])
Algeria=randomAI('Algeria',1,[w[139]])
Tunisia=randomAI('Tunisia',1,[w[140]])
Libya=randomAI('Libya',1,[w[141],w[142]])
Egypt=randomAI('Egypt',2,[w[143],w[144],w[145],w[146]])
Ghana=randomAI('Ghana',1,[w[150]])
Nigeria=randomAI('Nigeria',2,[w[151],w[152]])
Angola=randomAI('Angola',1,[w[157]])
S_Africa=randomAI('South Africa',2,[w[158],w[159]])
Sudan=randomAI('Sudan',1,[w[160],w[161]])
Ethiopia=randomAI('Ethiopia',1,[w[164]])
Kenya=randomAI('Kenya',1,[w[165]])
Turkey=randomAI('Turkey',3,[w[170],w[171],w[172],w[173]])
Azerbaijan=randomAI('Azerbaijan',1,[w[175]])
Syria=randomAI('Syria',1,[w[176],w[177]])
Lebanon=randomAI('Lebanon',1,[w[178]])
Israel=randomAI('Israel',1,[w[179]])
Iraq=randomAI('Iraq',1,[w[180],w[181]])
Kuwait=randomAI('Kuwait',1,[w[182]])
Arabia=randomAI('Saudi Arabia',2,[w[186],w[187],w[188]])
Yemen=randomAI('Yemen',1,[w[189]])
Dubai=randomAI('Dubai',1,[w[191]])
Oman=randomAI('Oman',1,[w[192]])
Iran=randomAI('Iran',2,[w[193],w[194],w[195]])
Khazakstan=randomAI('Khazakstan',1,[w[197],w[198]])
Uzbekistan=randomAI('Uzbekistan',1,[w[199]])
Pakistan=randomAI('Pakistan',2,[w[201],w[202]])
India=randomAI('India',6,[w[204],w[205],w[205],w[207],w[208],w[209],w[210]])
Bangladesh=randomAI('Bangladesh',1,[w[211]])
Sri_Lanka=randomAI('Sri_Lanka',1,[w[213]])
China=randomAI('China',8,[w[216],w[217],w[218],w[219],w[220],w[221],w[222],w[223],w[224],w[225],w[226],w[227],w[228],w[229],w[231]])
Hong_Kong=randomAI('Hong_Kong',1,[w[230]])
N_Korea=randomAI('N_Korea',1,[w[232]])
S_Korea=randomAI('South Korea',2,[w[233],w[234]])
Japan=randomAI('Japan',4,[w[236],w[237],w[238],w[239],w[240]])
Vietnam=randomAI('Vietnam',2,[w[246],w[247]])
Thailand=randomAI('Thailand',1,[w[248]])
Singapore=randomAI('Singapore',1,[w[249]])
Malaysia=randomAI('Malaysia',1,[w[251]])
Philippines=randomAI('Philippines',1,[w[252],w[253]])
Indonesia=randomAI('Indonesia',2,[w[254],w[255],w[257]])
Australia=randomAI('Australia',3,[w[259],w[260],w[261],w[262],w[263]])
Zealand=randomAI('New Zealand',1,[w[266]])
Human=civ('Name',0,[[]])

modernTesters=[US,Canada,Mexico,Cuba,DomRep,Guatemala,Colombia,Venezuela,Peru,Chile,Argentina,Uruguay,Brazil,
               Ireland,UK,Norway,Sweden,Finland,Denmark,Dutch,Belgium,France,Spain,Portugal,
               Germany,Swiss,Italy,Poland,Czech,Austria,Latvia,Ukraine,Croatia,Serbia,Romania,Bulgaria,Greece,Russia,
               Morocco,Algeria,Tunisia,Libya,Egypt,Ghana,Nigeria,Angola,S_Africa,Sudan,Ethiopia,Kenya,
               Turkey,Azerbaijan,Syria,Lebanon,Israel,Iraq,Kuwait,Arabia,Yemen,Dubai,Oman,Iran,Khazakstan,Uzbekistan,
               Pakistan,India,Bangladesh,Sri_Lanka,
               China,Hong_Kong,N_Korea,S_Korea,Japan,Vietnam,Thailand,Singapore,Malaysia,Philippines,Indonesia,Australia,Zealand,
               Human]


               


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

game=New_Game(w,modernTesters,50)
#game=New_Game(World,simpleTesters,30)
#game=New_Game(World,Sealand,100)
#game=New_Game(c,classicTesters,50)
board=game[1]
players=game[0]
#print(players)


for player in players:
    #print(player)
    #print(type(player))
    player.final=[]
    for ter in board:
        if ter.owner==player:
            player.final.append(ter.full_name)
    print(player)
    for ter in player.final:
        print (ter)
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~')






#Now make lists of regional territories and display which of these each civ controls at the end.




    



