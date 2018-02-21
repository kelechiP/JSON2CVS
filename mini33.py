import csv

import json

infile = open("Onyek1.json", "r")

outfile = open("kelechi33.csv", "w", newline="")

data = json.load(infile)

infile.close()

writer = csv.writer(outfile)

writer.writerow(['created_at', 'id', 'id_str', 'text'])

writer.writerow(['Sat Dec 09 18:19:14 +0000 2017','9.3956E+17','9.3956E+17','#ad Unheated Ruby Cabochon Deep Blood Red Oval Cut .60ct https://t.co/2e6rWxNJOJ'])


outfile.close()