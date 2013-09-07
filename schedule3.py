# Python 3.3
from tkinter import *

WIDTH, HEIGHT = 700, 550
VOFFSET = 125

master = Tk()
w = Canvas(master, width=WIDTH+10, height=HEIGHT+10)
w.pack()

# Create the template
w.create_rectangle(55, VOFFSET, WIDTH-145, HEIGHT, fill="white")
for day, hSpace in zip(['M','T','W','R','F'], range(5)):
    w.create_line(155+100*hSpace, VOFFSET, 155+100*hSpace, HEIGHT)
    w.create_text(105+100*hSpace, 95, text=day, font=("Tahoma", 30))
for hour, index in zip([8,9,10,11,12,1,2,3,4,5,6], range(11)):
    w.create_line(50, VOFFSET+HEIGHT/13*index, 55, VOFFSET+HEIGHT/13*index)
    w.create_text(30, VOFFSET+HEIGHT/13*index, text=hour, font=("Tahoma", 20))

# Hour lookup dict
hours = dict(zip([8,9,10,11,12,1,2,3,4,5,6], range(11)))

# Course Function
def makeblock (color, daysOfWeek, time, length):
    #          #str   #str        #int  #int(hours)
    for day, hSpace in zip(['M','T','W','R','F'], range(5)):
        if day in daysOfWeek:
            w.create_rectangle( 60+100*hSpace,
                                VOFFSET+2+HEIGHT/13*hours[time],
                                150+100*hSpace,
                                VOFFSET-2+HEIGHT/13*(hours[time]+length),
                                fill=color)

# Get inputs
name = input("Your Name: ")
title = input("Schedule Title: ")
numCourses = input("Number of Courses: ")
for iii in range(int(numCourses)):
    title = input("Course "+str(iii+1)+" title: ")
    color = input("Course "+str(iii+1)+" color: ")
    # display class name and color on side
    w.create_rectangle(WIDTH-135, VOFFSET+100+20*iii, WIDTH-125, VOFFSET+110+20*iii, fill=color)
    w.create_text(WIDTH-115, VOFFSET+105+20*iii, anchor="w", text=title, font=("Tahoma", 12))
    diffTimes = input("How many different times of the day during the week do you have this course? "
                         +"(ex. 10'o'clocks on MTRF and a 2'o'clock on W would be only be '2': ")
    for jjj in range(int(diffTimes)):
        start = input("Class #"+str(jjj+1)+" start time (integer only. ex. '9'): ")
        length = input("Class #"+str(jjj+1)+" length in hours (integer only): ")
        days = input("Days of week for class #"+str(jjj+1)+": (ex. 'MTRF'): ")
        makeblock(color, days, int(start), int(length))

w.create_text((WIDTH+5)/2, 35, text=name+" - "+title, font=("Tahoma", 40))
print ("Done. Screenshot your schedule")

mainloop()
