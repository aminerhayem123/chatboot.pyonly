import random

R_eat = "I don't eat because i'm a bot not a humain !"
def unknown():
    response = ['Could you please re_phrase that ?',
                "...",
                "sounds about right",
                "what does that mean ?"][random.randrange(4)]
    return response
