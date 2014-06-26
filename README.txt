Goals


scope
- share with friends, worry about usefulness later
- easy to use on mobile or desktop
- entirely skill-based and ridiculously simple (to start with)
- could be easily monetized with ad revenue
- useful to have in resume/portfolio
- references at bottom show the closest there is to this right now and how popular it can be
- typically multiplayer with long turns but could also have fast single player games


front end
- you get a link to this picture
- hover over ters to see name and stats
- current color shows who owns it
- click on ter to let you bid points on it 
- ??? to see more detailed stats
- make map update locally to show what player sees from their plan (stripes color bidded ters)
- also display what official allies are doing(?)
- display time when orders will next be resolved
- submit orders with button, can undo if before deadline


extra front end
- click on menu/button to see general actions (load/save/whatever) and submit orders
- something to let you see all ters you can bid on
- civ sheet with all player details
- known details of other players
- tech tree details
- possibly units and buildings
- submitting fluff (social, civics, etc) and other silly BS
- considering crunch related to fluff
- apply fog of war to map (only see accessible ters)
- ALL THE POLISH


back end
- collect orders from all players by territory
- send orders to back end
- resolve orders by changing ter color to that of player who bid the most on it
- create new svg and upload it so all players can see
- display notable changes
- integrate mechanics from other front end options (most complicated part)
- AI for single player (greedy algorithm abuse, later path search)


Progress


What we have
- color in map temporarily, by ter
- use list of strings to color multiple ters simultaneously
- optimized svg graphic of map, that is crazy easy to use
- python code that plays game from Excel file, in command line
- Excel file with details for each ter, specifically names and what are adjacent
- all game mechanics and tech tree needed in order to make game more complicated later
- applying mapcolorer code to set color with click


What is Simple
- use dictionary “map” of colors coupled to ters with an extra for loop
- changing the excel file to use full names for ters rather than abbreviations
- rewriting python to whatever is best
- editing the map to make it more betterer is needed
- adding World Game style “fluff” without a GM


What should be Simple
- saving edited svg as a new one that can then be displayed and acted upon
- converting python data structures into something javascript can use
- adding WG style “crunch” without a GM


What may be tough
- click on poly of svg and see its details 
- click on poly of svg and input orders
- displaying points and other interesting stats to player beyond the map svg


What is tough
- debugging javascript in general
- sending all orders (by ter) to central server (email ?)
- having some server that can update the game state and map online (wiki?)
- convincing the masses that this is a big deal ??? profit


References
- [World Game], Diplomacy, Risk, Civilization, Europa Universalis, DnD
- warlight: http://warlight.net/
- atwar: http://atwar-game.com/home/
- worldpowers: http://www.reddit.com/r/worldpowers
- mapcolorer: http://xn--dahlstrm-t4a.net/svg/mapcolorizer/countries-withname.htm
- svg updating: https://stackoverflow.com/questions/5966385/update-svg-dynamically
- svg tooltip stuff: https://stackoverflow.com/questions/10392238/overlaying-tooltip-style-data-on-an-svg-world-map
-mouse events: http://javascript.info/tutorial/mouse-events
-svg stroke properties: http://www.w3schools.com/svg/svg_stroking.asp