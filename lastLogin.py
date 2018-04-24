# Copyright: gymagyar
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
import json
import requests
import sys

try:
    cid = sys.argv[1]
    provhash = sys.argv[2]
    file_name = sys.argv[3]
except:
    print('Usage: $python3 lastLogin.py your_cid your_provhash')
    exit()
try:
    output = open(file_name,'w')
except:
    print("Error" + sys.exc_info())
    exit()

url='https://lastpass.com/enterpriseapi.php'
i = 0
while True:
    payload={"cid":cid,"provhash":provhash,"cmd":"getuserdata","data":{"pagesize":"500","pageindex":i}}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        try:
            res=  response.json()
        except:
            print('Error ' + response.text)
            output.close()
            exit()
        if ('error' in response.json().keys()):
            output.close()
            exit()
        for user_id, user in (response.json()['Users']).items():
            line = ''
            for k, v in user.items():
                if k == 'username':
                    line = line + v + ','
                if k == 'last_login':
                    if v == '':
                        line += 'N/A'
                    else:
                        line += v
            print(line)
            output.write(line+'\n')
    else:
        print('Error ' + response.text)
        output.close()
        exit()
    i += 1
output.close()
