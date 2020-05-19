# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:20:40 2020

@author: Elaine Wen
"""

'''code to get number of types of initiatives, types are:
    commissions
    WOTF task force
    state program
    legislation
    permanent office or position
    private public partnership
    other
    
    structure: 
    1. make different lists of the 7 types of initiatives to have each separate 
       list then print a string of the length of each list! 
    2. get each state and determine the number of initiatives for each state 
    and their different types and make into an excel file! (column 1: state,
    column 2: number of initiatives, column 3: (use sets?) to list the unique
    types of initiatives)
'''
commissions = []
WOTF_task_force = []
state_program = []
legislation = []
permanent = []
priv_pub_partnership = []
other = []
miscellaneous = []
convening = []

import csv

with open('state_initiatives.csv', 'r',
    encoding='utf-8') as datafile:
    reader = csv.reader(datafile)

    list_of_entries = []
    for line in reader:
        entry = line[2]
        if "commission" in entry:
            commissions.append(entry)
        elif "task force" in entry:
            WOTF_task_force.append(entry)
        elif "state program" in entry:
            state_program.append(entry)
        elif "legislation" in entry:
            legislation.append(entry)
        elif "permanent" in entry:
            permanent.append(entry)
        elif "partnership" in entry:
            priv_pub_partnership.append(entry)
        elif "other" in entry:
            other.append(entry)
        elif "convening" in entry:
            convening.append(entry)
        else:
            miscellaneous.append(entry)

num_com = len(commissions)
num_tf = len(WOTF_task_force)
num_sp = len(state_program)
num_leg = len(legislation)
num_perm = len(permanent)
num_part = len(priv_pub_partnership)
num_other = len(other)
num_misc = len(miscellaneous)

#should I make my 6 lists tuples to add to a dictionary????
print("commissions: " + str(num_com))
print("WOTF task forces: " + str(num_tf))
print("state programs: " + str(num_sp))
print("legislation: " + str(num_leg))
print("permanent offices or positions: " + str(num_perm))
print("private public partnerships: " + str(num_part))
print("other: " + str(num_other))
print("convenings: " + str(len(convening)))
print("miscellaneous/uncategorized: " + str(num_misc))
print("--------------------------------------------------")
print(miscellaneous)
print("-------------")
print("Miscellaneous types of initiatives are: ")
for item in miscellaneous:
    print(item)

########### RESULTS ########################################
#commissions: 4
#WOTF task forces: 9
#state programs: 31
#legislation: 32
#permanent offices or positions: 9
#private public partnerships: 45
#other: 9
#convenings: 4
#miscellaneous/uncategorized: 13
#--------------------------------------------------
#['Type of Initiative', 'business led organization', 'WOTF Task force', 'report', 'political organizations', 'report', 'non profit', 'university/academia', 'report', 'academic/university', 'funding', 'funding', 'program']
#-------------
#Miscellaneous types of initiatives are: 
#Type of Initiative
#business led organization
#WOTF Task force
#report
#political organizations
#report
#non profit
#university/academia
#report
#academic/university
#funding
#funding
#program    