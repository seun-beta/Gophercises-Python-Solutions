import csv
from time import sleep
import threading


try:
    user_input = str(input('Input your file name: '))
    fhand = open(user_input)
    reader = csv.reader(fhand)
except FileNotFoundError:
    print("""-----------File not found--------------\n
            Using 'problems.csv' """)
    fhand = open('problems.csv')
    reader = csv.reader(fhand)

    try:
        timer = int(input('Input your timer: '))
    except ValueError:
        print('Using 30 seconds as the default time')
        timer = 30


def countdown():

    global timer
    for _ in range(timer):
        timer = timer - 1
        sleep(1)

    print("Out of time!, Press Enter to see your score")


countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

correct = 0
count = 0

for row in reader:
    count += 1
    print(row[0])
    if timer == 0:
        break
    user_input = str(input('Input answer: '))
    user_input = user_input.lower()
    user_input = user_input.strip()

    if timer == 0:
        break
    if user_input == row[1]:
        correct += 1
    else:
        continue

print('You got ' + str(correct) + ' answer(s) right')
print('Number of questions:', count)
