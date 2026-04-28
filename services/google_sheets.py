import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connect_to_sheets():
    creds = Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )
    client = gspread.authorize(creds)
    return client

def get_all_sheets(spreadsheet_url):
    client = connect_to_sheets()
    spreadsheet = client.open_by_url(spreadsheet_url)

    all_data = {}

    for worksheet in spreadsheet.worksheets():
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        all_data[worksheet.title] = df

    return all_data
