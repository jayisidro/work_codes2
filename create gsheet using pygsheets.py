#install pygsheets
pip install --upgrade -q pygsheets

from google.colab import auth
from google.colab import drive

auth.authenticate_user()

import pygsheets
from oauth2client.client import GoogleCredentials
drive.mount('/gdrive', force_remount=True)

gc = pygsheets.authorize(client_secret='/gdrive/My Drive/client_secret.json')

#creating worksheet and writing on sheet1
sh = gc.create('gsheet_name')
wks = sh.sheet1
wks.set_dataframe(df, (1,1), extend=True)

#writing in sheet2
sh = gc.open('gsheet_name')
sh.add_worksheet("Sheet2")
workSheet=sh[1]
workSheet.set_dataframe(df2, (1,1))