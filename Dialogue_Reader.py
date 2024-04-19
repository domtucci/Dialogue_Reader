import pandas as pd
import json
import PySimpleGUI as sg
from pandas import json_normalize
from pathlib import Path

# p = Path(r'c:/Users/DV0095/Documents/Python_Projects/dialogues/test.json') #JSON file Path/Directory
# # Read the JSON file
# with p.open('r', encoding='utf-8') as file:


def main(): #GUI Window
    sg.theme('PythonPlus')

    layout = [[sg.T("")],
                [sg.Text("Upload the downloaded Tree Dialogue JSON File: "), sg.Input(key="file_path"), sg.FileBrowse(key="file_path_browse")],
                [sg.T("")],
                [sg.Button("Submit", bind_return_key=True), sg.Button('Cancel')]]

    window = sg.Window('Main Menu', layout, size=(800, 180))

    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Submit':
            json_file = values['file_path']
            window.close()


    data = json.load(open(json_file))

    # Extract information from the "Results" list
    results = data["Results"]
    result_data = []
    for response in results:
        result_data.append({
            "question": response["question"],
            "questionText": response["data"]["questionText"],
            "answer": response["data"]["answer"]    
        })

    # Convert the extracted data to a DataFrame
    df = pd.DataFrame(result_data)
    df.to_csv("NFS_PROD_1003193399.csv", index=False) #change the name of the saved file to "anything_you_want.csv"
#Remember to set file directory so the csv file saves to the folder you want.

if __name__=='__main__':
    main()
