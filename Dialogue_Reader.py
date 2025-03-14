import pandas as pd
import json
import PySimpleGUI as sg
from pandas import json_normalize
from pathlib import Path
import argparse



def main(): #GUI Window
    parser = argparse.ArgumentParser(description="Destinguish between GUI and command line")
    parser.add_argument("-v", "--pysimple", action="store_true", help="Use the GUI if you have PySimpleGUI")
    parser.add_argument("-c", "--command", type=str, help="Specify the JSON file path for command line mode")
    args = parser.parse_args()

    if args.pysimple:
        
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

    elif args.command:

        p = Path(r'c:/Users/DV0095/Documents/Python_Projects/dialogues/test.json') #JSON file Path/Directory
        # Read the JSON file
        with p.open('r', encoding='utf-8') as file:

            data = json.load(file)

    
    # Extract information from the "Results" list
    results = data["Results"]
    Dialogue_Id = data["Id"]
    metadata = data["Metadata"]
    result_data = []
    result_data.append({
        "Daily Id and Dialogue": f"{metadata['DailyId']} ||| {Dialogue_Id}"})
    result_data.append({
            "Tree Name": metadata["TreeName"],
            "Tree Version": metadata["TreeVersion"]})
    for response in results:
        result_data.append({
            "question order": response['answerOrderId'],
            "questionID": response["question"],
            "questionText": response["questionText"],
            "answer": response["data"]["answer"]    
        })

    # Convert the extracted data to a DataFrame
    df = pd.DataFrame(result_data)
    df.to_csv(f"{Dialogue_Id}_include_name.csv", index=False) #change the name of the saved file to "DailyID_anything_you_want.csv"
#Remember to set file directory so the csv file saves to the folder you want.

if __name__=='__main__':
    main()