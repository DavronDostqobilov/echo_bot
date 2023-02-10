import time
import requests
TOKEN = '6088934431:AAE-ZBo2fz_oykEdCO0f_YDM7saRBIvKfGc'

#GET Updates
def get_updates():

    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/GetUpdates')
    data=r.json()['result']

    return data


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
    r=r.json()['result']
    chat_id=r[-1]['message']['chat']['id']
    text=r[-1]['message']['text']
    updates_id=r[-1]['update_id']
    return chat_id,text,updates_id 

def send_message(chat_id,text):
    '''
    Use this function to send text messages.

    Args:
        chat_id (int): Telegram chat id
        text (str): Message text
    Returns:
        None
    '''
    param={'chat_id':chat_id,
           'text':text
          }
    
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage',params=param)
    ans=r.json()
    return ans
last_update_id=-1

while True:
    x=get_updates()
    chat_id,text,updates_id=get_last_updates()
    #updates_id=get_last_updates(get_updates())[-1]
    if updates_id!=last_update_id:
        
        print(updates_id, last_update_id)
        if text=='/start':
            send_message(chat_id,'Salom Aksado botga hush kelibsiz!')
        else:
            send_message(chat_id,text)
        last_update_id=updates_id
    time.sleep(2)


