import pandas
import turtle

screen = turtle.Screen()
screen.title("State Mapped Game")
screen.setup(width=750,height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
state_list = df.state.to_list()
guessed_states = []

#print(state_list)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            ans_state = df[df['state']==answer_state]
            t.goto(int(ans_state.x), int(ans_state.y))
            t.write(ans_state.state.item())

#state_row = df[df['state']==answer_state]

#print(state_row)

#def get_mouse_click_coor(x,y):
    #print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

screen.exitonclick()
