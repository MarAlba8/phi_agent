def general_evaluator(thoughts_by_sense: dict) -> dict:
    # recibe new_thoughts
    ## Se abre cada 200 ms
    # touch, hearing, sight, smell, taste. body
    ## TODO: Change this for a global variable with all the senses
    senses = ["hearing", "touch", "sight", "smell", "taste", "body"]
    states = ["biological", "cultural", "emotional"]

    # states_new_thoughts = {
    #     "biological": [],
    #     "cultural": [],
    #     "emotional": []
    # }
    states_new_thoughts = {}
    states_new_thoughts["biological"] = []
    states_new_thoughts["cultural"] = []
    states_new_thoughts["emotional"] = []

    for sense in senses:
        for state in states:
            descriptor = thoughts_by_sense[sense].get(state)
            if descriptor:
                states_new_thoughts[state].append(descriptor)

    return states_new_thoughts
