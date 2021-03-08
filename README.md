# Python Robot Controller
###### Robots controller in a delimited area
###### Version: 1.1, Last updated: 2021-03-08
Helps in controlling a robot, in this case a mower, but could be anything that can move in an area. 

Robot/Mowers are able to:
- cut the grass
- inspect the terrain
- identify problems in the green areas.

For the Minimal Viable Product (MVP):
- One green grass area only

- A green grass area, is curiously rectangular:
   ![logo](ReadmeAreaExample.png)
 - The area must be navigated by the Robot/Mowers.(Point of view of the Area)
This lead to think that we can have more than one Robot/Mower
- Robot/Mowers can cut the grass
- Robot/Mowers camera can get a complete view of the surrounding terrain

The view will be send to the Factory/Office

---

A Robot-Mower has:
- Location, expressed through coordinates: Coordinates(x,y)
- A Letter that represents one of the cardinal points (N,E,S,W)
North, East, South, West, that is the Orientation
- Position, expressed through coordinates and Orientation/Direction: (0,0,N)

-----

The area is divided into a grid, to simplify the navigation.

The Factory/Office sends a string of letters.

Possible letters are: L,R,M
- L = turn left (90º)
- R = turn right (90º)
- M = move one step in the grid

Input:
- First Line: upper right coordinates of the Area. This serves to limit the Area

It is possible to "deploy" more than one Robot/Mower.
Each Robot/Mower has two lines of input.
  - First Line: Robot/Mower position
  - Second Line: A series of Instructions that tells the Robot/Mower how to "explore" the area.
  

Each Robot/Mover actions are sequential:
- the second Robot/Mower will start after the previous one had finished.

