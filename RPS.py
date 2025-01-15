# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play == '':
        opponent_history.clear()
        
    opponent_history.append(prev_play)

    if len(opponent_history) > 2:
        guess = {"R": "P", "P": "S", "S": "R"}[opponent_history[-1]]
    else:
        guess = "R"

    return guess
