from odf import text, teletype
from odf.opendocument import load
import shutil
from os import listdir
import json
import csv
 

fields = ['Age', 'Gender', 'Left/Right Handed', 'Practiced Python(In days/months/year)',
'Practiced C (In days/months/year)', 'Rate yourself in Python (1-10)',
'Rate yourself in C (1-10)', 'Any head injury (Yes/No)',
'Elaborate if you have head injury', 'Any history of epilepsy?', 'Any history of lesions?',
'Any history of any neurological problem?',
'Any history of depression?', 'Any history of migraine?', 'Are you in stress?']


survey_fields = ['How was your experience?', 'How did you find Type 1 Activity?', 'How much do you rate your performance in Type 1 Activity? (1-10)',
'How did you find Type 2 Activity?', 'How much do you rate your performance in Type 2 Activity? (1-10)', 'How did you find Type 3 Activity?', 
'How much do you rate your performance in Type 3 Activity? (1-10)', 'Any discomfort experienced? If so, when?', 'Any feedback for the experiment?',
'Which was the most difficult type of activity?', 'Did you experience stress in any activitivity?', 'Did you experience conflict in Type 2 Activity?']

def parse_fields_to_csv(folder_name, output_folder, fields):
    file_list = listdir(folder_name)
    for file_name in file_list:
        textdoc = load(f"{folder_name}/{file_name}")
        allparas = textdoc.getElementsByType(text.P)
        final_res = {}

        for idx , val in enumerate(allparas):
            field_val = teletype.extractText(val)
            #print(idx, field_val)
            if field_val in fields:
                print(idx, field_val)
                print(idx, teletype.extractText(allparas[idx+1]))
                final_res[field_val] = teletype.extractText(allparas[idx+1])

        # Convert to JSON

        # output_file = f'{output_folder}/{file_name.split(".")[0]}.json'
        # f = open(output_file, 'w')
        # json.dump(final_res, f)

        # Convert to CSV

        with open(f'{output_folder}/before.csv', 'a') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in final_res.items():
                writer.writerow([file_name.split(".")[0], key, value])
            # writer.writerow("\n")

# parse_fields_to_csv(
#     '/Users/rahuldhek/Downloads/Before',
#     '/Users/rahuldhek/Downloads/outputParsedCSVFiles',
#     fields=fields)

def categorise_files(folder_name, output_folder_name):
    file_folders_list = listdir(folder_name)
    possible_file_name = [str(i) for i in range(1,31)]
    print(file_folders_list)
    for el in file_folders_list:
        print(type(el))
        if el in possible_file_name:
            type_file_list = listdir(f'{folder_name}/{el}')
            for _file in type_file_list:
                if _file == "t1.csv":
                    src_path = f'{folder_name}/{el}/{_file}'
                    dst_path = f'{output_folder_name}/type1/{el}.csv'
                    print(f'Source path : {src_path} \nDestination path : {dst_path}')
                    shutil.copy(src_path, dst_path)
                elif _file == "t2.csv":
                    src_path = f'{folder_name}/{el}/{_file}'
                    dst_path = f'{output_folder_name}/type2/{el}.csv'
                    print(f'Source path : {src_path} \nDestination path : {dst_path}')
                    shutil.copy(src_path, dst_path)
                elif _file == "t3.csv":
                    src_path = f'{folder_name}/{el}/{_file}'
                    dst_path = f'{output_folder_name}/type3/{el}.csv'
                    print(f'Source path : {src_path} \nDestination path : {dst_path}')
                    shutil.copy(src_path, dst_path)

# categorise_files(
#     '/Users/rahuldhek/Downloads/Usersdata',
#     '/Users/rahuldhek/Downloads/UsersOutputData'
#)
parse_fields_to_csv(
    '/Users/rahuldhek/Downloads/Before',
    '/Users/rahuldhek/Downloads/BeforeOutputFiles',
    fields=fields)



