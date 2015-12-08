# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global state,move,cindex1,cindex2,deck,exposed
    move,state,cindex1,cindex2 = 0,0,-1,-1
    deck = range(8)+range(8)
    random.shuffle(deck)
    exposed = [False]*16
    label.set_text("Moves = 0")


     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global move,state,cindex1,cindex2
    move += 1
    label.set_text("Moves = " + str(move//2+1))
    number = pos[0]//50
    if not exposed[number]:
        if state == 0:
            exposed[number] = True
            cindex1 = number
            state = 1
        elif state == 1:
            exposed[number] = True
            cindex2 =number
            state = 2
        else:
            if deck[cindex1]!=deck[cindex2]:
                exposed[cindex1],exposed[cindex2]= False,False
                cindex1,cindex2 = -1,-1
            state =1
            cindex1 = number
            exposed[number] = True
            
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, 'green','white')
            canvas.draw_text(str(deck[i]), (18+50*i, 60), 35, 'Red')
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, 'white','black')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
#http://www.codeskulptor.org/#user40_qdbuyIEds8_1.py


# implementation of card game - Memory

# import simplegui
# import random


# # helper function to initialize globals



     
# # define event handlers
# class Game:
#     def new_game():
#         global state,move,cindex1,cindex2,deck,exposed
#         move,state,cindex1,cindex2 = 0,0,-1,-1
#         deck = range(8)+range(8)
#         random.shuffle(deck)
#         exposed = [False]*16
#         label.set_text("Moves = 0")
#     def mouseclick(pos):
#         # add game state logic here
#         global move,state,cindex1,cindex2
#         move += 1
#         label.set_text("Moves = " + str(move//2+1))
#         number = pos[0]//50
#         if not exposed[number]:
#             if state == 0:
#                 exposed[number] = True
#                 cindex1 = number
#                 state = 1
#             elif state == 1:
#                 exposed[number] = True
#                 cindex2 =number
#                 state = 2
#             else:
#                 if deck[cindex1]!=deck[cindex2]:
#                     exposed[cindex1],exposed[cindex2]= False,False
#                     cindex1,cindex2 = -1,-1
#                 state =1
#                 cindex1 = number
#                 exposed[number] = True
            
        
                        
# # cards are logically 50x100 pixels in size    
# def draw(canvas):
#     for i in range(16):
#         if exposed[i]:
#             canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, 'green','white')
#             canvas.draw_text(str(deck[i]), (18+50*i, 60), 35, 'Red')
#         else:
#             canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, 'white','black')


# # create frame and add a button and labels
# frame = simplegui.create_frame("Memory", 800, 100)
# frame.add_button("Reset", Game.new_game)
# label = frame.add_label("Turns = 0")

# # register event handlers
# frame.set_mouseclick_handler(Game.mouseclick)
# frame.set_draw_handler(draw)

# # get things rolling
# Game.new_game()
# frame.start()


# # Always remember to review the grading rubric
