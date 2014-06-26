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
#Presently, territories are in a dict and players are a list. Make them subclasses later.

Australia = {#-1:['Name','adjacent','score'],
             0:['Western Australia',[1,3],1],
             1:['Northern Territory',[0,2,3],1],
             2:['Queensland',[1,3,4],1],
             3:['South Australia',[0,1,2,4,5],1],
             4:['New South Wales',[2,3,5], 1],
             5:['Victoria',[3,4],1]
             }
#print(Australia[0][1]) #adjacent
#print(Australia)

def New_Game(board, humans, computers, start, victory):
    """Begins a new game.
    board - a dictionary of territories
    players - number of players
    enemy - number of AI
    start - points each civ stars with
    victory - points required to win"""
    #0: Summon Board
    print('Board:',board)
    players = (build_players(humans,computers,start))
    print(players)
    turn = 0
    return take_turn(board,players,turn)

def build_players(humans,computers,start):
    players = []
    for i in range(humans+computers):
        players.append(1)
    for i in range(humans):
        players[i]=('Human',i),start,'human'
        #name = input(('Human',i,'Name:'))
        #players[i]=(name)
    for j in range(computers):
        players[j]=('Computer',j),start,'computer'
        #name = input(('Computer',j,'Name:'))
        #players[j]=(name)
    print('Players:',players)
    print()
    return players

def take_turn(board,players,turn):
    """
    board - dictionary
    players - list
    turn - int
    """
    #orders
    #2: Place Orders
    for player in players:
        print('~~~~~',player[0],'Turn~~~~~')
        print('You have',player[1],'points.')
        print()

    #3: AI Orders, TBD

    #4: Interpret Orders
        
    return '>>>test complete<<<'
    
#print(New_Game(Australia,2,0,3,10))

