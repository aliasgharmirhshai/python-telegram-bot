from datetime import datetime



def sample_responses(input_text):
    user_messages = str(input_text).lower()

    if user_messages in ('hello', 'hi'):
        return "Hey!"

    if user_messages in ('who are you', 'who are you?'):
        return "I am Ali"

    if user_messages in ('/محصولات'):
        return "Product"

    if user_messages in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y")

        return str(date_time)

    return "i Dont"