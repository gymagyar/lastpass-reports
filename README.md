# lastpass-reports

This project is a set of Python scripts to pull reports from LastPass in CSV fromat using the Enteprise API. The scripts creates the report in CSV format, which can be improted to Excel for furhter processing.

# Requirements

Python 3 is requreired to run this report. You can find details here how to install it:
- on Windows: https://docs.python.org/3/using/windows.html
- on Mac: https://docs.python.org/3/using/mac.html
- on Unix: https://docs.python.org/3/using/unix.html

Also the Reqeusts library needs to be installed. 

  $pip3 install requests

(see more details here http://docs.python-requests.org/en/master/user/install/)

# Avaialble Reports

Currently the following reports are available:

-Last Login: pulls all users' latest login date. N/A means user never logged in to LastPass

# How to run reports

1) Download the Python script to a working directory (e.g. lastLogin.py to lastpass-reports directory)
2) To run the reports you need to enter 3 paramters (all 3 are requeired):
    - cid: company id, this can be found under Admin Console/Dashboard/Account number 
    - provhash: this is the API key needed to pass the authentication of the Enterprise API. You can find it Admin                   Console/Advanced options/Provisioning API (note: this key is shown only once, therfore recomeneded to save it into             Secure Notes and use LastPass CLI to pass it to the script)
    - output file name: the scripts display the queried data as well as save it to the specified csv file
3) Run the script using Python 3
   
   $python3 lastLogin.py your_cid your_provisioning_hash lastlogin.csv
   
   
