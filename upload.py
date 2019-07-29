from boxsdk import Client

import platform
import datetime

import webbrowser

from boxsdk import OAuth2

def store_tokens(access_token, refresh_token):
    f = open("token.txt", "w+")
    f.truncate()
    f.write(access_token)
    f.write(refresh_token)
    f.close()


oauth = OAuth2(
    client_id='p9mkxq2qmxwopiha2t2lhwlhcodtecbx',
    client_secret='Ih6ZDDSMANdPWIdYluiyCmifu6Nf8Lym',
    store_tokens=store_tokens,
)

auth_url, csrf_token = oauth.get_authorization_url('http://0.0.0.0')

webbrowser.open(auth_url, new=2, autoraise=True)

auth_code = input("What is the darn code: ")

access_token, refresh_token = oauth.authenticate(auth_code)

# oauth = OAuth2(
#     client_id='p9mkxq2qmxwopiha2t2lhwlhcodtecbx',
#     client_secret='Ih6ZDDSMANdPWIdYluiyCmifu6Nf8Lym',
#     access_token='IXLCjEtz31C5MFqOy9ywvx3RXmIo9k6j',
#     refresh_token='koMpygM5wDPKxYLmPmLvKbLGoGKaTN5snoU4dnlXOSVbiD12YIMtDTmoHNwpcPQJ'
# )

client = Client(oauth)

d = datetime.datetime.today()
dm = str(d.month)
dm = '0' + dm
dd = str(d.day)
if d.day < 10:
    dd = '0' + dd
d_s = dm + dd + str(d.year)

target_folder = client.folder(folder_id='81518723086')

count = target_folder.get().item_collection['total_count']


lodir = target_folder.get().item_collection['entries']
not_there = True
for i in range(0, len(lodir)):
    pstr = lodir[i]['name']
    ind = len(pstr)
    if pstr[ind - 8:ind] == d_s:
        target_folder = client.folder(folder_id=lodir[i]['id'])
        not_there = False
        break
if not_there:
    big_folder_name = 'Session' + str(count - 1) + '_' + d_s
    shared_folder = target_folder.create_subfolder(big_folder_name)
    target_folder = shared_folder

name = platform.node()

shared_folder = target_folder.create_subfolder(name)

shared_folder.upload('./01_gazedata.stream~')
shared_folder.upload('./01_gazedata.stream')
shared_folder.upload('./01_cursor.stream~')
shared_folder.upload('./01_cursor.stream')
shared_folder.upload('./01_button.stream~')
shared_folder.upload('./01_button.stream')
shared_folder.upload('./01_audio.wav')
shared_folder.upload('./' + d_s + '_screen.mp4')



