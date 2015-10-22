"""
Loads in the data from cars.data.csv.  The data can be stored anyway you choose, in any data structure you choose (probably a list of some kind).  
The data should load on start-up by referencing a file path, or even better, a file picker dialog box.
In the main portion of your program you should run the following operations and print the result to the console (except number 4).  
How you achieve this is up to you.  However, operations need to be performed on the data itself (don't hard code the solution).
- Print to the console the top 10 rows of the data sorted by 'safety' in descending order
- Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
- Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order.  
- Find these matches using regular expressions.
- Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.  
The file path can be a hard-coded location (name it output.txt) or use a dialog box.  
Your code needs to be able to handle exceptions.  It should handle all data as specified by the data definition document from Lesson 2, 
and throw some kind of error when it encounters data that doesn't match that format.  To test this, 
I will add the line 'vlow, vlow, 1, 1, vbig, vhigh' to the .csv file.  Your program should gracefully handle this line in all cases from the previous part.
"""
########################

import Tkinter
import tkFileDialog

root=Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent=root)

#filename = "cars.data.csv"
#########################

import csv
import sqlite3
import re 


def buildDB(filename):
    """Reads the CSV and creates a database table if the lines containt seven columns."""
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS cars')
    c.execute('''CREATE TABLE cars 
        (buying text, maint text, doors text, persons text, lug_boot text, safety text, acceptability text)''')

    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        try:
            for row in reader:
                len(row) == 7
                c.execute('INSERT OR IGNORE INTO cars (buying, maint, doors, persons, lug_boot, safety, acceptability) VALUES(?,?,?,?,?,?,?)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            
            conn.commit()
        except:
            print "A row in the dataset is incomplete."


def CheckDB():
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    cur = conn.execute('SELECT * FROM cars')
    return "The Cars dataset has %i records loaded into a new database table." % (len(cur.fetchall()))
    #for row in c.execute('SELECT * FROM cars WHERE maint = "vhigh"'):
        #print row


def RegexQuery():
    """Returns the specified dataset using regular expressions."""
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    rowText = c.execute('SELECT * FROM cars ORDER BY doors')

    for row in rowText:
        #This is ugly. 
        if re.findall('high', row[0]) != [] and re.findall('high', row[1]) and re.findall('high', row[5]):
            print row


def QueryToSaveFunctions(buying, maint, doors, per1, per2):
    """Saves the specified dataset."""
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    print "The request data are:"
    #This is also ugly. 
    rowText = c.execute('SELECT * FROM cars WHERE buying=:buying AND maint =:maint AND doors =:doors AND persons =:persons OR persons =:persons2', {"buying":buying, "maint": maint, "doors":doors, "persons":per1, "persons2":per2})
    
    with open("output.csv", "w") as f:
        csv.register_dialect("custom", delimiter=",")
        writer = csv.writer(f, dialect="custom")
        for tup in rowText:
            writer.writerows(tup)

if __name__ == "__main__":
    buildDB(filename)
    print CheckDB()

    RegexQuery()
    QueryToSaveFunctions("vhigh", "med", 4, 4, "more")
