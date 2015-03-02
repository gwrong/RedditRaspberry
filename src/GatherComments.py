'''
Created on Feb 23, 2015

@author: Graham
'''

import praw
import time

r = praw.Reddit(user_agent='u\MoldyBrick Testing 1.0')
r.login('MoldyBrick', 'poker11')
file = open("Comment Test.txt", "w")
for x in range(0, 10):
    all_comments = r.get_comments('Fitness')
    for comment in all_comments:
        file.write(comment.body + "\n") 
    time.sleep(90)
file.close()
