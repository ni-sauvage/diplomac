# A Diplomacy Move Interpreter
## Written by Niall Sauvage

### Intro to Diplomacy
[Diplomacy](https://en.wikipedia.org/wiki/Diplomacy_(game)) is a board game based on intrigue, strategy and most of all, backstabbing. Players control one of seven countries in the lead-up to the First World War, with every country vying to be dominant. Such domination can only come if countries work together, however, leading to a game that is incredibly hard to analyse due to the omnipresent human factor.

#### An example diplomacy board, with thanks to Wikimedia
![Diplomacy Board](https://upload.wikimedia.org/wikipedia/commons/a/a3/Diplomacy.svg)

### This Project
Diplomacy, much like chess, has [notation for moves](https://en.wikibooks.org/wiki/Diplomacy/Rules#Abbreviation_of_Orders). The outcomes of all moves are given similtaneously, but certain moves assist other moves (supports) and therefore need to be processed first - this leads to an interesting problem when making a diplomacy interpreter - That is, how to accurately process moves. 

#### Stage 1
The first stage of this project is creating a Python interpreter that can correctly process all diplomacy orders. This could be read from a file and stored in another file. 

#### Stage 2
The second stage of this project is to attempt to host the interpreter - this will necessitate moves being inputted using their notation rather than using any kind of GUI, but should serve as a baseline from which to build a GUI. This will probably be done with Flask.

#### Stage 3 
The final stage of this project is to use an SVG file with React in order to create a diplomacy sandbox adjudicator for ease of input on the user's behalf.

#### Stretch goals
Authentication and creation of users along with the creation of games rather than sandboxes is one of the stretch goals for this project, with the other being porting to an Android app. 

### If you want to play Diplomacy or learn more, do check out [Backstabbr](https://www.backstabbr.com/).
