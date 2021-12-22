from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ('hi', 'hello', 'sup'):
        return "Hey!, How's it going"
    
    
    if user_message in ('who are you', 'who are you?'):
        return "I'm Subadra Bro Bot"
    
    if user_message in ('time', 'date', 'time?', 'date?'):
        now = datetime.now
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        
        return str(date_time)
       
    return "I can't undastand you"
