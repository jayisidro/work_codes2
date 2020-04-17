import gspread
import pandas as pd
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gc = gspread.authorize(GoogleCredentials.get_application_default())

worksheet = gc.open('gsheetname').sheet1
rows = worksheet.get_all_values()
headers = rows.pop(0)

gsheetname = pd.DataFrame(rows, columns=headers)
print(gsheetname.head())