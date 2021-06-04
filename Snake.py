#Importing Modules(Libraries)
import curses #Importing the curses Module.
import random #Importing the Random Module.

#-------------------------------------------------------------------------------------------------------------------------------------

stdscr = curses.initscr() #Intializing the library to return window object represents the whole screen.
curses.curs_set(0) #Setting the visibility of the cursor to 0 in order to hide the cursor.
h, w = stdscr.getmaxyx() #Returning a tuple of the height & the width of the window. *Note*In the curses module, The height comes before the width & The Y-axis comes before the X-axis*
stdwin = curses.newwin(h, w, 0, 0) #Creating a new window (game's window) with the dimensions of the h & w variables' values & It's position is the center of the screen which is (0, 0).
stdwin.keypad(1) #Getting the new window ready to listen to the keyboard (accept the user input (key events)).
stdwin.timeout(100) #Setting the delay of the new window to 100ms (getchar() will return -1 (no user input) if the user didn't give an input during 100ms).
snake_y = h // 2 #Setting the position (Y co-ordinate) of the snake to half of the screen (the center of the screen) according to the Y-axis. *Note*We used the floor division operator (//) which rounds to the nearst integer in order not to face problems with the upcoming functions that don't deal with floats resulting from the normal division operator (/)*
snake_x = w // 4 #Setting the position (X co-ordinate) of the snake to quarter of the screen according to the X-axis.
#The snake's Co-ordinates.
    #The Snake's 1st character (Head)'s co-ordinates.
    #The Snake's 2nd character (Body 1)'s co-ordinates.
    #The Snake's 3rd character (Body 2)'s co-ordinates.
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
"""
    Setting the position of the snake's head to the values (co-ordinates) of the variables snake_y & snake_x, 
    and then the position of the snake's body 1 & body 2 to the snake_y, snake_x - 1 "to make the body 1 '1 step' to the left from the snake's head"  & snake_y, snake_x - 2 "to make the body 2 '2 steps' to the left from the snake's head" respectively
    in order to be sequential so that they form the snake either the snake will appear as only one character (head) at the beginning.
"""
food = [h // 2, w // 2] #Setting the position of the food's character to half of the screen (the center of the screen) according to both of the Y-axis & X-axis.
stdwin.addch(food[0], food[1], "*") #Creating the food's character which will be "*" in the postion of the values (co-ordinates) of the food's 2 list items.

key = curses.KEY_RIGHT #Setting the default movement of the snake at the beginning to the right.

while True: #Creating an infinite loop that help in keeping the game running until a certain action occured.
    next_key = stdwin.getch() #Accepting the user input (key event). *Note*Revise what I said about the getch() in line 10 and it's relation to the timeout()*
    key = key if next_key == -1 else next_key #Changing the movement direction of the snake according to the user input (key event) or Leaving the movement direction of the snake to the default (right) in case the user didn't give any input (key event) during the specified time I determined in ln 10 (100ms).

    if snake[0][0] in [0, h] or snake[0][1] in [0, w] or snake[0] in snake[1:]: #Checking if the snake head's height touches the top or the bottom border or the snake head's width touches the left or the right border or the snake's head touches the snake's body, 
        curses.endwin() #If so then de-initialize the library, and return the terminal to the normal status 
        quit() #and quit (exit the terminal).
    
    new_head = [snake[0][0], snake[0][1]] #Setting the position of the snake's head to the default position I determined before in ln 18 so that it will be used to represent the new position of the snake after the user input (key event).

    if key == curses.KEY_UP:    #Checking if the user clicked the up arrow key on keyboard then the snake moves up.
        new_head[0] -= 1
    if key == curses.KEY_DOWN:  #Checking if the user clicked the down arrow key on keyboard then the snake moves down.
        new_head[0] += 1
    if key == curses.KEY_LEFT:  #Checking if the user clicked the left arrow key on keyboard then the snake moves left.
        new_head[1] -= 1
    if key == curses.KEY_RIGHT: #Checking if the user clicked the right arrow key on keyboard then the snake moves right.
        new_head[1] += 1

    snake.insert(0, new_head) #Inserting the new new_head's values to be the first item in the snake's list so that it represents the new position of the snake.

    if snake[0] == food: #Checking if the snake's head position is the same as the food's position (the snake ate the food), 
        food = None #If so then there is no food
        while food == None: #and while there is no food, 
            #Create new_food's character with a random position.
                #Set the Y co-ordinate to a random integer value that is more than the bottom border by 1 and less than the top border by 1 to avoid being in the same position of them.
                #Set the X co-ordinate to a random integer value that is more than the left border by 1 and less than the right border by 1 to avoid being in the same position of them.
            new_food = [
                random.randint(1, h - 1),
                random.randint(1, w - 1)
            ]
            food = new_food if new_food not in snake else None #Replacing the food's old position with the new_food's new position in case that the new_food's position isn't in the same postion of the snake or there will be no food.
        stdwin.addch(food[0], food[1], "*") #Creating the new food's character in the postion of the values (co-ordinates) of the new_food's 2 list items.
    else:
        tail = snake.pop() #Removing last snake body's character since every user input (key event) we insert new_head to the snake even without eating as explained from ln 42 to ln 51.
        stdwin.addch(tail[0], tail[1], ' ') #Replacing the snake body's last character with a space.
    
        stdwin.addch(snake[0][0], snake[0][1], "O") #Creating the snake's head character which will be "O"in the postion of the values (co-ordinates) of the 1st item in the 2D snake list.