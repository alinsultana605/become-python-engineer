import csv

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
         print(line['email'])
    
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['firstname', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)