from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd

def sheet_append(name,sport,individual):

    # The key of the spreadsheet we want to access

    spreadsheet = { 
                    'esports': '1GaJMluzdu1KdEIiy0fxjLbXnBrk1n5d1A2kQhPVPaXc',
                    'college-sports': '1gpB44VzmZ2V-ek_Ks9qzjpc-1-7PxwPpYO1dp1EuT4Q',
                    'nhl': '1XMg69-N6_o5L6Mlf6jkxzWtZ-zjArPuuQSqMjgDTW9g',
                    'golf':'1P6KrDxH3gMKzu_zNMNIN3ql1twL68snO5ztB5KRszB4',
                    'mlb':'18tcP2uVxOuj631zAGustWjIMptzLzbCrvt4EK3Ziuzk',
                    'nba':'1rMstK9oANRqtnI0PuQXIVr34kWBBC2s4gPfcGAVR18E',
                    'entertainment':'1GSNk4opMVwH-5Nz-ekGIRV--mliRlUZgliKPeiKYLU4',
                    'beauty': '12Ai1tqz1ARgV903_Rd8zThGtISX2STlPEMe60oaWLY8',
                    'fashion': '1SOI69-prPNYRuNjtCa2Ej6486MgWAbfLarJi5Yb8Aic',
                    'reality-tv': '1tPmtwa4Anq_jjrHPjpqmQEatKWPSRPYYfrjZVTq8rkQ',
                    'daily-soap': '1yOx5onNDQH01nGQq42Bp8A0b0bM-FIXQY_JQBFY6H-o',
                    'nfl': '1ZaP2e7mangNOX5C2bay1vE_uYxAENJcsLKitjnxBaQ4'
                    }
    
    spreadsheet_key =  spreadsheet[sport]

    ## Connect to our service account
    scope = ['https://spreadsheets.google.com/feeds']
    # Use the service account credentials to authorize our application (have also attached this credentials file)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('./google_sheets.json', scope)
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
