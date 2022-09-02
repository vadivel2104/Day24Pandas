import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

mark = turtle.Turtle()
mark.penup()
mark.color("black")


turtle.shape(image)

state_name = pd.read_csv("50_states.csv")

#to get the state name, cordinates from csv
state = state_name["state"].to_list()

#Functions to get cordinates, and move the turtle in map
def get_cor(state):
    state_x = int(state_name[state_name["state"] == state]["x"])
    state_y = int(state_name[state_name["state"] == state]["y"])
    state_cor = (state_x, state_y)
    return state_cor

def move_to():
    mark.penup()
    mark.hideturtle()
    mark.goto(get_cor(guess))
    mark.write(f"{guess}", align="center",font=("courier", 8, "normal"))

data = []
state_count = 0
game_on = True


while game_on:
    #to get the input and convert it into title case
    guess = screen.textinput(title="Guess a State", prompt=f"{state_count}/50 Enter a State Name:")
    guess = guess.title()

    if guess in state:
        get_cor(guess)
        move_to()
        #to write state values in state_answer.csv
        axis = list(get_cor(guess))
        x_axis = int(axis[0])
        y_axis = int(axis[1])
        data.append([guess, x_axis, y_axis])
        df = pd.concat([pd.DataFrame(data, columns=["state", "x", "y"])], ignore_index=True)
        #to write the dataframe to csv
        df.to_csv("pandas3_answers.csv", header= True, index= False)
        state_count += 1


    answered_states = pd.read_csv("pandas3_answers.csv")
    state2 = answered_states["state"].to_list()
    remaining_states = []
    remaining_all = []


    if guess == "Exit":
        game_on = False
        #to create list of states not answered
        for num in state:
            if num not in state2:
                remaining_states.append(num)
        print(remaining_states)
        #to create x, y list for remaining states
        for num in remaining_states:
            remaining_x = int(state_name[state_name["state"] == num]["x"])
            remaining_y = int(state_name[state_name["state"] == num]["y"])
            rs_df = [num, remaining_x, remaining_y]
            remaining_all.append(rs_df)
        print(remaining_all)
        #to create df for remaining lists
        df_remaining = pd.concat([pd.DataFrame(remaining_all, columns=["state", "x", "y"])], ignore_index= True)
        # to write the dataframe to csv
        df_remaining.to_csv("pandas3_remaining_answers.csv", header=True, index=False)









