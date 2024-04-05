# from Google import Create_Service
#
# CLIENT_SECRET_FILE = 'client_secret.json'
# API_NAME = 'sheets'
# API_VERSION = 'v4'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#
# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#
# # https://developers.google.com/sheets/api/samples/data
#
# spreadsheet_id = '1cxEWvH21wwLYlE5iSv1qr-jKvxcU0KEg1TV2pSmrYDc'
#
#
# def read(spreadsheet_id):
#     response = service.spreadsheets().values().get(
#         spreadsheetId=spreadsheet_id,
#         majorDimension="ROWS",
#         range="Sales South"
#     ).execute()
#
#     print(response['values'][1:])
#     for i in range(0, len(response['values'][1:])):
#         print(response['values'][1:][i][0])
#         print(response['values'][1:][i][1])
#         print(response['values'][1:][i][2])
