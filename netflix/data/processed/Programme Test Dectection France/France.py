import csv
counter = 0
word_to_search = 'france'
with open('merged.csv', encoding='UTF-8') as f:
    for line in csv.reader(f):
         if any(word_to_search in l for l in map(str.lower, line)):
              counter += 1
print(counter)
