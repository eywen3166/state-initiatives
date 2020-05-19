# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:20:40 2020

@author: Elaine Wen
"""
#types of initiatives
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
print("WOTF Task Forces: " + str(num_tf))
print("Private Public Partnerships: " + str(num_part))
print("Legislation: " + str(num_leg))
print("Permanent Offices or Positions: " + str(num_perm))
print("State Programs: " + str(num_sp))
print("Commissions: " + str(num_com))
print("Convenings: " + str(len(convening)))
print("Other: " + str(num_other))
print("Miscellaneous/Uncategorized " + str(num_misc))
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