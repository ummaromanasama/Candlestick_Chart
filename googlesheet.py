#Importing Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#Important stuff
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
         'dividend-investing-274019-b556916d3607.json', scope) # Your json file here
client = gspread.authorize(creds)

#Access sheet
spreadsheetName = 'The Dividend Chamipon'
sheet = client.open(spreadsheetName)
worksheet = sheet.get_worksheet(4)

#Request ticker
symbol = input('Enter ticker symbol: ')
symbol = symbol.upper()

#Lookup ticker 
ticker_range = worksheet.range('B7:B859')

#Lookup dividend
div_range = worksheet.range('J7:J859')

#Match the ticker with dividend
for cell in ticker_range:
    ticker_val = cell.value
    ticker_row = cell.row
    ticker_col = cell.col
    if ticker_val == symbol:
            dividend = worksheet.cell(ticker_row, 10).value
            print('Dividend: ' + dividend)



