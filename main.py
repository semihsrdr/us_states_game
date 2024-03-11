from turtle import Screen
from pencil import Pencil, Score, Heart
import pandas

screen = Screen()
screen.setup(800, 600)
screen.bgpic("blank_states_img.gif")
screen.title("Us States Game")
screen.tracer(0)

user_dict = {}

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()

pencil = Pencil()
score = Score()
heart=Heart()


username = screen.textinput("Us States Game", "Enter Your Name : ")

game_on = True
while game_on and heart.heart>0:
    chosen_state = screen.textinput("Us States Game", "Enter the state : ")
    if chosen_state is None:
        print("cancel")
        game_on = False
        break
    else:
        chosen_state = chosen_state.title()
        if chosen_state in list_of_states:
            chosen_state_info = data[data.state == chosen_state]
            print(chosen_state_info)
            state_x = int(chosen_state_info.x.iloc[0])
            state_y = int(chosen_state_info.y.iloc[0])
            pencil.write_state(state_x, state_y, chosen_state)
            score.score += 1
            score.update_score()
        else:
            heart.heart -= 1
        screen.update()
        heart.show_heart()

user_dict = {
            "name": username,
            "score": score.score
}

score_data = pandas.read_csv("Score_Datas.csv")
score_data = score_data._append(user_dict, ignore_index=True)

score_data.to_csv("Score_Datas.csv", index=False)

print(score_data)

screen.exitonclick()
