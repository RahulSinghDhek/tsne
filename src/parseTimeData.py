# 18:49:00	18:49:20	P
# 18:55:00	18:55:20	W
from datetime import datetime
import csv
from os import listdir

p_start_time = "18:49:00.000"
p_end_time = "18:49:20.000"
p_start_time = datetime.strptime(p_start_time,'%H:%M:%S.%f')
p_end_time = datetime.strptime(p_end_time,'%H:%M:%S.%f')

n_start_time = "18:55:00.000"
n_end_time = "18:55:20.000"
n_start_time = datetime.strptime(n_start_time,'%H:%M:%S.%f')
n_end_time = datetime.strptime(n_end_time,'%H:%M:%S.%f')

filter_type = {
    "P": [p_start_time, p_end_time],
    "W": [n_start_time, n_end_time]
}



def read_time_data_input(file_name):
    time_data_input={}
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            user_no = row[1]
            class_name = row[0]
            start_time = row[2]
            end_time = row[3]
            if time_data_input.get(user_no) is None:
                time_data_input.update({user_no : {{class_name : [ start_time, end_time]}}})
            else:
                time_data_input[user_no][class_name] = [ start_time, end_time]
            #time_data_input[user_no][class_name]['end_time'] = end_time
    return time_data_input

def get_list_of_files(folder_name):
    final_file_name_list = []
    sub_folder_names = listdir(folder_name)
    possible_folder_name = [str(i) for i in range(1,4)]
    print(possible_folder_name)
    for el in sub_folder_names:
        if el in possible_folder_name:
            file_names = listdir(f'{folder_name}/{el}')
            for file_name in file_names:
                full_file_path = f'{folder_name}/{el}/{file_name}'
                final_file_name_list.append(full_file_path)
    return final_file_name_list



#print(read_time_data_input("../data/timedata.csv"))

#date_time_obj2 = datetime.strptime(date_time_str,'%H:%M:%S.%f')

def create_file(file_name, time_data_input):
    with open(file_name, 'r') as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader: 
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
                line_count += 1
                _time = datetime.strptime(row[9].strip(),'%H:%M:%S.%f')
                _class_type = None
                user_id = file_name.split("/")[-2]
                class_time_input = time_data_input.get(user_id)
                for k,v in class_time_input.items():
                    start_time = v[0].strptime(row[9].strip(),'%H:%M:')
                    end_time = v[1].strptime(row[9].strip(),'%H:%M:')
                    if _time>= start_time and _time <= end_time:
                        _class_type = "k"
                        with open("../data/outputData/output.csv", "a") as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerow([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], _class_type])
                else:
                    continue
                
folder = "../data/usersData"
file_name = "5.csv"
#create_file(folder_location=folder, original_file=file_name)

file_list = get_list_of_files("../data/usersData")
time_data_input = read_time_data_input("../data/timedata.csv")
for file_name in file_list:
    create_file(file_name, time_data_input)
    break