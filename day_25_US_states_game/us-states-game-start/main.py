import turtle
import pandas as pd

screen = turtle.Screen()

image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
screen.bgpic(image)



# get coordinates of answer_state from csv
states_df = pd.read_csv("50_states.csv")
states = list(states_df['state'])
score = 0
guessed_states = []

while score != 50:
    answer_state = turtle.textinput(title=f"{score}/50 correct", prompt="Type name of a state").title()
    if answer_state == "Exit":
        new_data = pd.DataFrame([st for st in states if st not in guessed_states])
        new_data.to_csv("missing_states.csv")
        turtle.clear()
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        xcor = states_df[states_df['state'] == answer_state].values[0][1]
        ycor = states_df[states_df['state'] == answer_state].values[0][2]
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(xcor, ycor)
        screen.update()
        turtle.write(answer_state, font=('Courier', 8, 'normal'))
        score += 1

if score == 50:
    turtle.goto(0, 0)
    turtle.write("YAY! you guessed all 50 states!", align='center', font=('Courier', 20, 'normal'))


turtle.mainloop()