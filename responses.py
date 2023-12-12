import random

def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return 'initiate_process'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == "!help":
        return '`This is a help message.`'
    
    if p_message == "oliver":
        return 'Go study nigga'
    
    if p_message == "hey":
        return 'initiate_process'
    
    return 'initiate_process'
