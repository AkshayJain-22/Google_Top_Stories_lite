from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd

def sheet_append(name,individual):

    sa = gspread.service_account(filename="/Users/akshayjain/Google Top News/google_top_news/creds_SK_gspread.json")
    # The key of the spreadsheet we want to access
    spreadsheet_key =  '1ZaP2e7mangNOX5C2bay1vE_uYxAENJcsLKitjnxBaQ4'

    ## Connect to our service account
    scope = ['https://spreadsheets.google.com/feeds']
    # Use the service account credentials to authorize our application (have also attached this credentials file)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('creds_SK_gspread.json', scope)
    gc = gspread.authorize(credentials)
    book = gc.open_by_key(spreadsheet_key)
    worksheet = book.worksheet(name)

    gs = gc.open_by_key(spreadsheet_key)
    # Append the data to the specified sheet within the spreadsheet

    new_data = pd.DataFrame(individual)
    #old_data = pd.DataFrame(worksheet.get_all_records())
    #print(new_data.columns)
    #print(old_data.columns)
    #complete_data = pd.concat([new_data,old_data],ignore_index=True)

    #worksheet.clear()
    data_values = new_data.values.tolist()
    #print(data_values)
    gs.values_append(name, {'valueInputOption': 'RAW'}, {'values': data_values})
    
    #worksheet.update([complete_data.columns.values.tolist()] + complete_data.values.tolist())
