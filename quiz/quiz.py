import csv 
from time import * 
import threading

try:
    user_input = str(input('Input the file name you want: '))
    fhand = open(user_input)
    reader = csv.reader(fhand)
except FileNotFoundError:
    print("-----------File not found--------------\n Opening 'problems.csv' ")
    fhand = open('problems.csv')
    reader = csv.reader(fhand)
    try:
        timer = int(input('Input your timer: '))
    except:
        timer = 30

def countdown():
    global my_timer
    global timer
    my_timer = timer
    for _ in range(my_timer):
        my_timer = my_timer - 1
        sleep(1)
        
    print("Out of time!, Press Enter to see your score")
    
countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

correct = 0
count = 0
while my_timer > 0 :
    for row in reader:
        count += 1
        print(row[0])
        if my_timer == 0 :
            break
        user_input = str(input('Input answer: '))
        user_input = user_input.lower()
        user_input = user_input.strip()
        sleep(1)
        if my_timer == 0 :
            break
        if user_input == row[1]:
            correct += 1
            
        else:
            continue

print('You got '+ str(correct) + ' answer(s) right')
print('Number of questions:', count)
