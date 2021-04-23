import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
image = "Map-of-India.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
guess_states = []
while len(guess_states) < 28:
    answer_state = screen.textinput(f"{len(guess_states)}/28 states left", prompt="Enter name of the state:").title()
    all_states = data.state.to_list()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
