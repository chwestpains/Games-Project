import random


    
class towns:
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def get_name(self):
        return self.name

    def get_coords(self):
        return self.coords

braunstone = towns("braunstone", (-275, 20))       
glenfield = towns("glenfield", (-290, -100)) 
thurmaston = towns("thurmaston", (100, 320))
hamilton = towns("hamilton", (400, 120))
scraptoft = towns("scraptoft", (380, 80))
knighton = towns("knighton", (200, -320))
aylestone = towns("aylestone", (120, -300))
citycentre = towns("citycentre", (50,50))
oadby = towns("oadby", (270, -200))
wigston = towns("wigston", (200, -165))
glenparva = towns("glenparva", (-400, 102))
countersthorpe = towns("countersthorpe", (-60, -350))
enderby = towns("enderby", (-300, 60))
foresteast = towns("foresteast", (-290, 120))

townList = [braunstone, glenfield, thurmaston, hamilton, knighton, citycentre, scraptoft, aylestone, oadby, wigston, glenparva, countersthorpe, enderby, foresteast]

connected_nodes = {'braunstone':{'enderby':12, 'foresteast':6, 'citycentre':35,'glenparva':22},
                   
  'thurmaston':{'glenfield': 40, 'citycentre': 20, 'hamilton': 12, 'enderdy':40},
 'glenfield':{'thurmaston': 37, 'citycentre': 20},
 'hamilton':{'thurmaston': 20, 'citycentre': 25, 'glenfield':30, 'scraptoft': 7},
 'scraptoft':{'hamilton': 12, 'citycentre':25},    
 'knighton':{'citycentre': 5, 'aylestone': 3, 'countersthorpe':30},
 'aylestone':{'citycentre':15, 'knighton': 6, 'countershorpe':25},
 'citycentre':{'knighton': 2, 'hamilton': 20, 'glenfield': 30, 'thurmaston': 15, 'aylestone':20, 'scraptoft':22, 'braunstone':15},
  'oadby':{'wigston':12, 'citycentre':22,},
  'wigston':{'oadby':10, 'glenparva':17, 'citycentre':31, 'scraptoft':31},
  'glenparva':{'braunstone':16, 'enderby':3, 'thurmaston': 45},
  'countersthorpe': {'aylestone':23, 'knighton':27},
  'enderby':{'foresteast':4, 'glenparva':6, 'braunstone':8, 'thurmaston':12},
  'foresteast':{'enderby':2, 'glenparva':7, 'braunstone':8}
                   }
