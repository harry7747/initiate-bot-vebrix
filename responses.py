import random

def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return 'Hey there!'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!help':
        return '`This is a help message.`'
    
    if p_message == 'Oliver':
        return 'Go study nigga'
    
    if p_message == 'hey':
        return 'Sup brother!!'
    
    return 'I/m in development for this functionality.'
