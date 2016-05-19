#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
from time import sleep
import random
import riddle


curses.initscr()

curses.noecho()
curses.curs_set(0)

screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)

box_content = []
#box_blocks = []
score = 0
life = 3

def kill_enemy(index):
    box_content.pop(index)

def key_pressed(key):
    for i in range(len(box_content)-1):
        if box_content[i].result == key:
            global score
            score+=1
            kill_enemy(i)

def box_reach_end(i):
    health-=1
    kill_enemy(i)


def box_move():
    for j in range (5):
        screen.clear()
        screen.border(0)
        #count = 0
        event = screen.getch()
        if event != -1:
            key_pressed(chr(event))
        for i in box_content:
            #screen.refresh()
            i.y_pos += i.speed
            screen.addstr(i.y_pos, i.x_pos, i.text)
            #print(i.y_pos, i.x_pos)
            #box_blocks[count].mvderwin(i.y_pos, i.x_pos)
            #box_blocks[count].refresh()
            screen.refresh()
            #count += 1
            #box.box()
            #box.addstr(1, 1, i.text)
            #if i.y_pos > curses.LINES-3:        #add here LINES coordinate
            #    sleep(0.1)#add box reach end
        sleep(0.2)

while score != 20:
    screen.timeout(100)
    clone = riddle.create_riddle()
    #box = screen.derwin(3, len(clone.text)+2, clone.y_pos, clone.x_pos)
    #box.box()
    screen.addstr(clone.y_pos, clone.x_pos, clone.text)
    screen.refresh()
    #box.refresh()
    box_content.append(clone)
    #box_blocks.append(box)
    box_move()


while True:
    event = screen.getch()
    if event == ord('q'): break

curses.endwin()
