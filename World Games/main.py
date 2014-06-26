"""
Main

0. To Add
    Gameplay
    - print changes to map relevant to player
    - allow player to view territories by civ
    - default view of territories excluded own
    - make possible to pause, change civs, leave player civ to AI

I. Excel Spreadsheet
    World - a list of all 270 teritories with all data
    [0] unique abbreviation
    [1] list of adjacent territories; may convert to full words later
    [2] binary representation of territory value; obsolete 10/21/13
    [3] full name of territory with abbreviation if it is not just first three letters
    [4] base topography; defines agricultural production; may change with desertification, terraforming
        ocean - requires open ocean travel to pass
        sea - requires coast sailing travel to pass
        mountain - requires flight to pass
        desert - requires flight to pass
        tundra - dry farming, +1 pop
        plain - husbandry, dry farming, +1 pop
        grass - agriculture, crop rotation, dry farming, +1 pop
        hill - terrace, +1 pop
        river - agriculture, irrigation, crop rotation, engine +1 pop
        flood - agriculture, husbandry, irrigation, construction, +1 pop
        note: fishing provides +1 pop to all coastal and sea territories
    [5] advanced vegetation; may be removed and reseeded
        ice - removed by global warming, -4 pop
        marsh - can remove with engine, -2 pop
        jungle - can remove with chemistry, -2 pop
        taiga - can remove with rail=engine, -1 pop
              - forestry: wealth spent on war +1, can spend wealth on and from sea
              - ships: can spend wealth on and from ocean
        wood - can remove with alloying (or forestry?), strategic resource with smelting, -1 pop
             - forestry: wealth spent on war +1, can spend wealth on and from sea
             - paper: wealth overflow +1 each, unlimited for research
             - ships: can spend wealth on and from sea
        aridification - caused by deforestation, overpopulation, global warming, etc, -1 pop
    [6] single resource to be used with appropriate tech; limitation is game balance, not programming limitation
        none - same as sea or ocean; not all are same
        peak (3) - same thing as mountain terrain; redundant?
        copper (24) - boost military with smelting, needed for electronics
            - smelting: point spent on war +1
            - electricity: luxury
        tin (6) - bost military with alloying and copper
            - alloying: wealth spent on war +2 (with copper)
            - factory: luxury, stability +1
        iron (30) - bost military with furnace; industrial production 
            - furnace: wealth spent on war +1
            - steel: wealth spent on war +1
            - engine: wealth spent on war +1
        coal (30) - industrial energy 
            - machinery: stability +1
            - steel: wealth spent on war +1
            - electricity: energy
        gold (16) - shiny, currency, silver
            - smelting: luxury
            - electricity: stability +1
        gems (14) - shiny, diamond, amber
            - smelting: luxury
            - science: stability +1
        alcohol (10) - improve stability, represents divine right
            - ceramics: stability +1
            - philosophy: research +1
        silk (10) - represents silk road; overland trade routes
            - husbandry: luxury
            - philosophy: stability +1
        fur (10) - overland trade routes
            - husbandry: max pop +1
            - rotation: luxury
        incense (10) - Islam-associated trade routes
            - philosophy: research +1
            - rotation: luxury
        spice (10) - Indies-associated trade
            - ships: range to spend wealth +1 for ter using
            - rotation: luxury
        sugar (10) - Carribean and imperial trade
            - rotation: luxury
            - chemistry: max pop +1
        textiles (10) - imperial and industrial trade
             - husbandry: max pop +1, luxury
             - casting: wealth used on war +1
             - factory: stability +1
        drugs (10) - modern illegal trade
            - philosophy: research +1
            - stability luxury, -1 to others when traded away
        uranium (10) - nuclear power, electric resources, rare earth metals
            - nuclear: counts as 3 energy, wealth spent on war +1
        oil (30) - modern energy
            - ceramics: luxury
            - chemistry: war spent on wealth +1
            - engine: energy
II. Paper Maps
    > most in black folder
    > Victoria 2 map in paint
    > consider pixle map
    > consider graph representation
    > ideally GUI
III. Tech Tree
    > excel document
    > TBD how to interface 
IV. Scripts (excluding old messy ones to convert)
    [0] main 
    [1] board
        ter - individual nodes of graph
        load board - call Excel spreadsheet to construct graph
    [2] players 
        civ - each player, includes individual order placing functions
        nullAI - makes no orders
        holdAI - bids only on own territories
        simpleAI - bids a point on each territory it can
        randomAI - bids a random amount of points on random territories until it runs out
    [3] intermediate
        > make board from load board and excel sheet
        > construct tests from players
        > sometimes build individually players by hand and put into list
    [4] Game Functions
        New_Game - takes in board, players, and victory conditions to begin teh game
        take_turn - checks if game is complete and takes in orders from players
        eval_orders - updates the world state to teh next round by changing territory posession and value
    [5] Test Codde
        > simulate a game
        > at end of game, print detailed results
V. User Interface (TBD)
    > presently begins game asks for player orders
    > can check adjacent territories, game state, quantity of points to spend
    > select specific territories and spend points on them
    > end turn
    > future additions will include map, diplomacy, technology, trade, and possibly units
"""
        
