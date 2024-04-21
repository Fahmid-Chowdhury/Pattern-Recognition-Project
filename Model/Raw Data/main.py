
import csv

# Define filenames and corresponding headers
filenames = ["8000age.txt", "8000ethnicity.txt", "8000gender.txt", 
              "8000religion.txt", "8000other.txt", "8000notcb.txt"]
headers = ["age", "ethnicity", "gender", "religion", "other", "not_cyberbullying"]

with open('profiles1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    field = ["feature", "output"]
    
    writer.writerow(field)
    for i in filenames:
        with open(i, 'r', encoding='utf-8') as f:
            for line in f:
                writer.writerow([line.strip(), headers[filenames.index(i)]])
                
print("Done")