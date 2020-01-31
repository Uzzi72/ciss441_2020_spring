# importing the csv file: each row is a dictionary
# fifa_players is a list of all the ufo sighting dictionaries
import csv 
fifa_players = []
row_count = 0 

#open csv file as that can be ref from csv_fi
with open('playera15.csv', 'r') as csvfile:
    # use the csv,DictReader method to convert to reader object
    reader = csv.DictReader(csvfile)
    
    # loop over the reader object 
    for fifa_row_dic in reader:
        row_count += 1
        fifa_players.append(fifa_row_dic)	
        if row_count <=10 :
            print('{0:>7} Name: {1:<40} Age:{2:<4} Club: {2:<15}' .format(
                row_count, fifa_row_dic['long_name'], fifa_row_dic['age'],
                fifa_row_dic['club']))

print("rows: " + str(len(fifa_players)))

