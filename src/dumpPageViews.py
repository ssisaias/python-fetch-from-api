import requests
import time
import datetime
import sys
import json
from dotenv import load_dotenv
import os
#Load env
load_dotenv()
print(os.getenv('REQUEST'))

print('Processing...', end='\n')

header = {'Authorization': 'Bearer '+os.getenv('TOKEN')}

print('First request: '+ os.getenv('REQUEST')+"?"+os.getenv('REQUEST_PARAMS'), end='\n')
r = requests.get(os.getenv('REQUEST')+"?"+os.getenv('REQUEST_PARAMS'), headers=header)

if r.status_code != 200:
    sys.exit('[Error]: ' + r.text)

json_response =""
json_response = json.dumps(r.json())
print('')
dumpFile = open('pageviews'+datetime.datetime.now().strftime('%Y-%m-%d-%H%M')+'.txt', 'w', encoding='utf-8') 
#Here's the condition for canvas (the systeam I used this script) to let us know that there's are more pages left. You should adapt this for the API you're calling.
if 'next' in r.headers['link']:
    thread_Next_Page_Token_Found = True
#exit()
while thread_Next_Page_Token_Found:
    
    if 'next' in r.headers['link']:
        #print(str(r.headers['link']).split(','))
        #print('')
        string_i_want = ([x for x in (str(r.headers['link']).split(',')) if 'next' in x])
        next_link = (string_i_want[0].split(';')[0])[1:-1]
        print('Subsequent request: '+ next_link, end='\n')
        time.sleep(1)
        r = requests.get(next_link, headers=header)
        json_response += json.dumps(r.json())
        thread_Next_Page_Token_Found = True
    else:
        thread_Next_Page_Token_Found = False
    

dumpFile.write(json_response)

dumpFile.close()

r.close()

print('Done.')
    