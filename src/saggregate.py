# 18:49:00	18:49:20	P
# 18:55:00	18:55:20	W
from datetime import datetime
import csv
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

#date_time_obj2 = datetime.strptime(date_time_str,'%H:%M:%S.%f')

folder = "/Users/rahuldhek/Downloads/UsersOutputData/type3"
file_name = "5.csv"

def create_file(folder_location,original_file):
    with open(f'{folder_location}/{original_file}', 'r') as csv_file: 
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
                if _time >= filter_type['P'][0] and _time <=  filter_type['P'][1]:
                    _class_type = "Python"
                    with open("output.csv", "a") as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], _class_type])
                if _time >= filter_type['W'][0] and _time <=  filter_type['W'][1]:
                    _class_type = "Writing"
                    with open("output.csv", "a") as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], _class_type])
                else:
                    continue
                
create_file(folder_location=folder, original_file=file_name)
