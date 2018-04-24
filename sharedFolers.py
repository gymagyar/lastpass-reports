# Copyright: gymagyar
# GNU General Public License v3.0+ (see LICENSING or https://www.gnu.org/licenses/gpl-3.0.txt)
import json
import requests
import sys

try:
    cid = sys.argv[1]
    provhash = sys.argv[2]
    file_name = sys.argv[3]
except:
    print('Usage: $python3 sharedFolders.py your_cid your_provhash output.csv')
    exit()
try:
    output = open(file_name,'w')
except:
    print("Error" + sys.exc_info())
    exit()

url='https://lastpass.com/enterpriseapi.php'
payload={"cid":cid,"provhash":provhash,"cmd":"getsfdata"}
response = requests.post(url, json=payload)

if response.status_code == 200:
    try:
        res =  response.json()
    except:
        print('Error: ' + response.text)
    header = ' sharedFolderName, SecurityScore, UserName, GroupMembership, Admin, Password, ReadOnly'
    print(header)
    output.write(header+'\n')
    for sharedfolder in (response.json().values()):
        line = ''
        for k, v in sharedfolder.items():
            if k == 'sharedfoldername':
                line = line + v + ','
            if k == 'score':
                    line += str(v)
                    line += ' , , , , '
                    print(line)
                    output.write(line+'\n')
            if k == 'users':
                for attr in v[:]:
                    if 'group_name' in attr:
                        line = ' , ,'+attr['username']+','+attr['group_name']+','+attr['can_administer']+','+attr['give']+','+attr['readonly']
                    else:
                        line = ' , ,'+attr['username']+','+' '+','+attr['can_administer']+','+attr['give']+','+attr['readonly']
                    print(line)
                    output.write(line+'\n')
output.close()
