import requests
from pprint import pprint

TOKEN = '6088934431:AAE-ZBo2fz_oykEdCO0f_YDM7saRBIvKfGc'

def get_last_updates():
    """
    Use this function to get updates from Telegram.

    Args:
        None
    Returns:
        int(chat_id): Telegram chat id
        str(text): Message text
        int(update_id): Telegram update id
    """
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/GetUpdates')
    chat_id=r.json()['result'][-1]['message']['chat']['id']
    text=r.json()['result'][-1]['message']['text']
    updates_id=r.json()['result'][-1]['update_id']

    return chat_id,text
print(get_last_updates())
    

def send_message(chat_id,text):
    '''
    Use this function to send text messages.

    Args:
        chat_id (int): Telegram chat id
        text (str): Message text
    Returns:
        None
    '''
    params={'chat_id':chat_id,'text':text}
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage',params=params)

    return text
pprint(send_message(get_last_updates()[0],get_last_updates()[1]))



