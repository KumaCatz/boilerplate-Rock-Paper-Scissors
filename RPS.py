# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    if prev_play == '':
        opponent_history.clear()

    ideal_response = {"R": "P", "P": "S", "S": "R"}

    count_history = {
        k: opponent_history.count(k)
        for k in set(opponent_history)
        }
    
    most_played = max(count_history, key=count_history.get)

    if len(opponent_history) > 1:
        # with one of the opponents, the guess is going S -> P -> R, in like a cycle
        # i want to detect this and predict the input
        

        guess = ideal_response[opponent_history[-1]]
    else:
        guess = "R"

    return guess
