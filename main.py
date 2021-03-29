import argparse
import json
import sqlite3

parser = argparse.ArgumentParser()

parser.add_argument("d", help="Source of File")
parser.add_argument("-o",
                    "--option",
                    default="insert",
                    help="Enter your Opretion")

args = parser.parse_args()

data_source = open(args.d)

json_data = json.load(data_source)

con = sqlite3.connect('sqlite3.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS data_bratin_station \
    (uuid INT PRIMARY KEY NOT NULL, \
        date VARCHAR, \
        min VARCHAR, \
        max VARCHAR, \
        avg VARCHAR \
    ); ")

# Insert code
if args.option == 'insert':
    print("Data is Inserting")
    for data in json_data:
        cur.execute("INSERT INTO data_bratin_station VALUES( '" +
                    str(data['uuid']) + "','" + str(data['data']) + "','" +
                    str(data['min']) + "','" + str(data['max']) + "','" +
                    str(data['avg']) + "');")

# Update code
elif args.option == 'update':
    print("Data is Updateing")
    for data in json_data:
        cur.execute("UPDATE data_bratin_station SET date = '" +
                    str(data['data']) + "', min ='" + str(data['min']) +
                    "', max = '" + str(data['max']) + "', avg = '" +
                    str(data['avg']) + "' WHERE uuid = '" + str(data['uuid']) +
                    "';")

elif args.option == 'update-on-conflict':
    print("Data is Updateing")
    for data in json_data:
        cur.execute("REPLACE INTO data_bratin_station SET date = '" +
                    str(data['data']) + "', min ='" + str(data['min']) +
                    "', max = '" + str(data['max']) + "', avg = '" +
                    str(data['avg']) + "' WHERE uuid = '" + str(data['uuid']) +
                    "';")

sel = cur.execute("SELECT * FROM data_bratin_station")
for d in sel:
    print(d)

con.close()