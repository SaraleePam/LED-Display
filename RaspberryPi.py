import time
import serial
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of the spreadsheet
SPREADSHEET_ID = '1VOnFzvLX1b26OtMFG4rKbH1HoCr9RUDB_HlAsYFuMKE'
RANGE_NAME = 'Sheet1!A1:B'


# Get credentials from the token file
creds = Credentials.from_authorized_user_file('/Users/saralees/Documents/GitHub/LED-Display/GoogleAPI/token.json', SCOPES)
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

######


ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
print("Initializing connection....")
time.sleep(3)
ser.reset_input_buffer()
print("HELLO!")
print("connected to: " + ser.portstr)


# def get_text():
#     now = datetime.datetime.now()
#     minute = now.minute
#     second = now.second
#     hour = now.hour
#     currentsec = (hour * 3600) + (minute * 60) + second
#     return (currentsec / 86400.0) * 360.0



while True:

    time.sleep(5)
    print(values)
    ser.write(('TEXT ' + str(values) + '\n').encode())
    

           
# #ser.close()