"""User Interface
Start
> New Game - goes to turn interface
> Load Game - loads a saved file

Game Types
> Diplomacy - some supply centers, mostly tactical movement
> Risk - roll dice, collect based on continent
> Raw Points - every territory is equivalent, place anywhere

Turn Interface
> Dislplay - free points, results from last turn
> Help - explains the terminology
> Map - lists territories and owners
> Territory - class, list stats and ownership of territory
> (Stats - adjacent territories, geography, effect, points)
> Score - class, losts power of player
> Free - subclass, lists free points
> Point - subclass, has location and action
> End - ends turn

Actions
> Place - free point is put in a specific territory
> Move - non-free point is spent on an adjacent (for now) territory
> Collect - gathers points produced form contrlled territories

AI
> takes turn at same time as player
> there can be multiple
> simple - spends points on adjacent territories only
> basic - defends border territories
> advanced - considers opponents' moves
> expert - TBD
"""

#Raw Points Game


import load_board
#Australia=load_board(worksheet, curr_row, num_rows)

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
        
#class land(ter):
#class sea(ter):
    
class civ(object):
    def __init__(self,name,score,start=[]):
        #self.number = number
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
                    #print(ter.name)
                    #print(ter.name)
                    #print(ter.test)
                    options.append(ter)
                    for adjacent in ter.adjacent:
                        #print(adjacent)
                        options.append(adjacent)
        print('{0}`s turn. You have {1} points. Where do you use them? Input h for help.'.format(self.name,self.score))
        action = input('--> ')
        #print(action)
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
                #action=int(action)
                if action<=self.score:
                    #print('~~~~~~~~SUCCESSS~~~~~~~~~~')
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
                #We need this not to print after investing in a valid territory.
        #actions.append(action)
        new_actions = actions
        #Do input again and do not append if action is not valid. print('That is not a valid order.')
        return self.place_orders(board,new_actions)
import random
class simpleAI(civ):
    def place_orders(self,board,actions):
        """Creates a set of orders to bid one point on each unclaimed option."""
        options=[]
        for ter in board:
                if ter.owner==self:
                    options.append(ter)
                    for adjacent in ter.adjacent:
                        options.append(adjacent)
        random.shuffle(options)
        #print(options)
        for ter in options:
            if self.score<1:
                return actions
            elif ter.owner!=self:
                self.score-=1
                investment=(ter,1,self)
                actions.append(investment)
        #print(actions)
        return actions
#randomAI: Creates a set of actions that spend a random amount of points on territories randomly.
# greedyAI: spends extra points on more contested territories

#OLD AUSTRALIA
A = [0, 1, 2, 555, 4, 5]
#Political map: http://www.ezilon.com/maps/images/oceania/australia-political-map.gif
A[0] = ter('Western Australia',[A[1],A[3]],1)
A[1] = ter('Northern Territory',[A[0],A[2],A[3]],1)
A[2] = ter('Queensland',[A[1],A[3],A[4]],1)
A[3] = ter('South Australia',[A[0],A[1],A[2],A[4],A[5]],1)
A[4] = ter('New South Wales',[A[2],A[3],A[5]], 1)
A[5] = ter('Victoria',[A[3],A[4]],1)
#Call each A[i] a second time so that the adjacents point to the updated list.
A[0] = ter('Western Australia',[A[1],A[3]],1)
A[1] = ter('Northern Territory',[A[0],A[2],A[3]],1)
A[2] = ter('Queensland',[A[1],A[3],A[4]],1)
A[3] = ter('South Australia',[A[0],A[1],A[2],A[4],A[5]],1)
A[4] = ter('New South Wales',[A[2],A[3],A[5]], 1)
A[5] = ter('Victoria',[A[3],A[4]],1)


Australia=A
#print(A[3], A[0].adjacent[1])



West = civ('West',3, [Australia[0]])
East = civ('East',3, [Australia[4]])
simpleEast = simpleAI('simpleEast',3, [Australia[4]])
Testers = [West,East]
simpleTesters = [West,simpleEast]
#print(Australia)
#print()
#print(Testers)

def New_Game(board, players, victory):
    """Begins a new game by taking in a list of ters and a list of civs.
    Play out a series of turns and end the game when one player reaches the victory points."""
    #print('Board:',board)
    #print()
    #print('Players:',players)
    for civ in players:
        for home in civ.start:
            for ter in board:
                if home==ter:
                    ter.owner=civ
                #ter.test = 'yay'
                #print (ter.test)
                    #print(board)
    turn = 1
    return take_turn(board,players,turn,victory,orders=[])

def take_turn(board,players,turn,victory,orders):
    """Iterate through a list of players and produce a new board from their actions."""
    print('>>>>> TURN',turn,'<<<<<')
    #simpleEast.score=0
    for player in players:
        if player.score < 1:
            print ('Player {0} eliminated with {1} points.'.format(player.name,player.score))
            players.remove(player)
            print(len(players))
    for player in players:
        if len(players)==1 and player.score>0:
            return 'Game over. {0} wins with {1} points.'.format(player.name,player.score)
    for player in players:
        print(player.name, len(players))
        if player.score >= victory:
            return 'Game over. {0} wins with {1} points.'.format(player.name,player.score)
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
    
    #print('~~~~~~~~~~Test Complete~~~~~~~~~~')
    #orders = [[(A[3], 2, West), (A[1], 1, West)], [(A[2], 1, East), (A[3], 1, East), (A[4], 1, East)]]
    #orders = ['South Australia', 2, West]
    #print(orders)
    contests = []
    for order in orders: #in case a player has no orders
        if order==[]:
            #print('derples')
            orders.remove([])
    #print(orders)


    #print(orders)
    for ter in board:
        #print('>>>>>>>>>>>>>>',ter)
        for player in orders:
            #print('~~~',player)
            for order in player:
                territory=order[0]
                contender = order[2]
                bid = order[1]
                #print('ter:',ter,'territory:',territory)
                if ter.name==territory.name:
                    #print('______________gghhdd______________',ter)
                    if ter not in contests:
                        contests.append(ter)
                    #print(ter.contender)
                    if bid>ter.highest:
                        ter.highest=bid
                        ter.leader=contender
                        #print(ter, ter.highest, ter.leader)
                    elif bid==ter.highest:
                        ter.leader=ter.owner   
    #for ter in board:
        #print(ter, ter.leader)
    for ter in contests: #actual function
        if ter.leader!=None:
            ter.owner=ter.leader
            #print('larp')
            #print(orders)
            #print(ter)
            for elem in board:
                if elem.name==ter.name:
                    board.remove(elem)
            board.append(ter)
    for ter in board:
        #print(ter)
        #print(ter.owner)
        if ter.owner!=None:
            ter.owner.score+=ter.value
        #print('>>>>>>>>>>',ter)
    #print(board)
    #print(board)
    return board

def derp():
    for player in orders: #helper code
        print(player)
        for order in player:
            ter = order[0]
            contender = order[2]
            bid = order[1]
            #ter.contender=bid
            print(ter.highest)
            if ter not in contests:
                contests.append(ter)
            #print(ter.contender)
            if bid>ter.highest:
                ter.highest=bid
                ter.leader=contender
                print(ter.highest)
            elif bid==ter.highest:
                ter.leader=ter.owner
    for ter in contests: #actual function
        if ter.leader!=None:
            ter.owner=ter.leader
            #print('larp')
            #print(orders)
            #print(ter)
            for elem in board:
                if elem.name==ter.name:
                    board.remove(elem)
            board.append(ter)
    for ter in board:
        #print(ter)
        #print(ter.owner)
        if ter.owner!=None:
            ter.owner.score+=ter.value
        #print('>>>>>>>>>>',ter)
    #print(board)
    return board


#print(New_Game(Australia,Testers,20))


print(New_Game(Australia,simpleTesters,10))






##def west_points_eval_orders(board,orders):
##    West.score +=1
##    print('Orders:',orders)
##    for order in orders:
##        print (order)
##        for action in order:
##            print(action)
##            if action == '+':
##                West.score += 1
##            elif action == '-':
##                West.score -=1
##                print(West.score)
##    return orders
    



