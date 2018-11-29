#your first attempt with out any goggling
import sys

def read_file(file):
    file = open(file, "r")
    return file

def write_file(file):
    file = open(file,"w+")
    return file

def scan_servers(r_file,w_file):
    file = read_file(r_file)
    for line in file:
        sys.argv


#attempt 2 that gives right results in the console
import os
import csv
import subprocess

with open("usable_data.csv", 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in file:
        row = str(row)
        row = row.rstrip("[]")
        row = row.lstrip("[]")
        #print(row)
        data = os.system('nslookup ' + str(row))
        print(type(data))
        #print(data)
