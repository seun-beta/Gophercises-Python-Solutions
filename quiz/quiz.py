import csv 

fhand = open('problems.csv')
reader = csv.reader(fhand)

correct = 0
count = 0
for row in reader:
    count += 1
    print(row[0])
    user_input = str(input('Input answer: '))
    if user_input == row[1]:
        correct += 1
    else:
        continue

print('You got '+ str(correct) + ' answer(s) right')
print('Number of questions:', count)
