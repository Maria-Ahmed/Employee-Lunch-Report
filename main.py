import csv
import json
from configparser import ConfigParser
from datetime import datetime

# Reading parser se file
parser =ConfigParser() #parser is dictionary and it contains multiple section
parser.read('config.cfg')

empfile = parser[r'DEFAULT']['EmployeeFileName']
menufile = parser[r'DEFAULT']['MenuFileName']
outputfile = parser[r'DEFAULT']['OutputFileNameSuffix']
filtereddata={}
filtereddata['emp']=[] # emp array in filtered daata
#
if empfile.endswith('json'):
  with open('employee.json') as f:
    data = json.load(f)
  print(data)
elif empfile.endswith('csv'):
    # Reading employee csv file
    try :
        with open('employee.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[2] =='Yes':
                    filtereddata['emp'].append({'Ermp Id': row[0], 'name':row[1], 'present':row[2]})
                print(row)
    except PermissionError as e:
        print('File is open already')
        with open('error_log.log', a) as errorlog:
            errorlog.write('Perisson DEnieed Exception occured')


print(filtereddata)
print(str(datetime.now()).split(' ')[0])
try:
    with open(str(datetime.now()).split(' ')[0]+outputfile, 'w') as out:
        out_writer = csv.writer(out)
        out_writer.writerow(filtereddata['emp'][0].keys())
        for employee in filtereddata['emp']:
            out_writer.writerow(employee.values())
except PermissionError as e:
    print('File is open already')
    with open('error_log.log', 'a') as errorlog:
        errorlog.write('Perisson DEnieed Exception occured')

if menufile.endswith('json'):
  with open('employee.json') as f:
    data = json.load(f)
  print(data)
elif menufile.endswith('csv'):
    # Reading menu csv file
    with open('menu.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


'''if outputfile.endswith('json'):
  with open('_output.json') as f:
    data = json.load(f)
  print(data)
elif outputfile.endswith('csv'):  # Reading output csv file , making sure
    with open('_output.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)'''

# writing DATE to output file
#with open('_output.csv', 'w') as file:
	#writer = csv.writer(file)
    #outputfile =datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")

#things I have to do-> error logging files
#filter the data according to conditions
#date sahi se krni
#add suffix from files
