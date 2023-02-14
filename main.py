import time
import requests
TOKEN = '6088934431:AAE-ZBo2fz_oykEdCO0f_YDM7saRBIvKfGc'

#GET Updates
def get_updates():

    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/GetUpdates')
    data=r.json()['result']

    return data


def get_last_updates(result):
    """
    Use this function to get updates from Telegram.

    Args:
        None
    Returns:
        int(chat_id): Telegram chat id
        str(text): Message text
        int(update_id): Telegram update id
    """
#filtrs1
    if result[-1]['message'].get('photo', False):
       # print( result[-1]['message'].get('photo', False))
        chat_id=result[-1]['message']['chat']['id']
        photo=result[-1]['message']['photo'][0]['file_id']
        updates_id=result[-1]['update_id']
        return chat_id,photo,updates_id 
    if  result[-1]['message'].get('text',False):
        #print(result[-1]['message'].get('text',False))
        chat_id=result[-1]['message']['chat']['id']
        text=result[-1]['message']['text']
        updates_id=result[-1]['update_id']
        return chat_id,text,updates_id 
    if  result[-1]['message'].get('sticker',False):
        #print(result[-1]['message'].get('sticker',False))
        chat_id=result[-1]['message']['chat']['id']
        sticker=result[-1]['message']['sticker']['file_id']
        updates_id=result[-1]['update_id']
        return chat_id,sticker,updates_id 
    
#sends
def send_photo(chat_id,stic_photo_text):
    param={'chat_id':chat_id,
           'photo':stic_photo_text
          }
    
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',params=param)
    ans=r.json()
    return ans
def send_sticker(chat_id,stic_photo_text):
    param={'chat_id':chat_id,
           'sticker':stic_photo_text
          }
    
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendSticker',params=param)
    ans=r.json()
    return ans

def send_message(chat_id,stic_photo_text):
    '''
    Use this function to send text messages.

    Args:
        chat_id (int): Telegram chat id
        text (str): Message text
    Returns:
        None
    '''
    param={'chat_id':chat_id,
           'text':stic_photo_text
          }
    
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage',params=param)
    ans=r.json()
    return ans
last_update_id=-1

#server

while True:
    result=get_updates()
    chat_id,stic_photo_text,update_id=get_last_updates(result)
    if update_id!=last_update_id:
        print(update_id, last_update_id)
         
#filtrs2

        if 'sticker' in result[-1]['message']:
            send_sticker(chat_id,stic_photo_text)       
        

        if 'photo' in result[-1]['message']:
            send_photo(chat_id,stic_photo_text)
            
        if 'text' in result[-1]['message']:
            
            if stic_photo_text=='/start':
                send_message(chat_id,'Salom  botga hush kelibsiz!')
            else:
                send_message(chat_id,stic_photo_text)

        last_update_id=update_id
    time.sleep(2)


