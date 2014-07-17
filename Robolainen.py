# -*- coding: utf-8 -*-
import numpy as np
from itertools import combinations
from math import factorial

##################################################
#              Championship settings             #
##################################################
maxspend = 75 # Maximum spend allowed
nCarPerTeam = 3 # Cars per team
nDriverPerTeam = 3 # Drivers per team

cars = np.array([['Red Bull',23],
                 ['Mercedes',20],
                 ['Ferrari',20],
                 ['Lotus',15],
                 ['McLaren',15],
                 ['Force India',12],
                 ['Sauber',10],
                 ['Toro Rosso',8],
                 ['Williams',6],
                 ['Marussia',5],
                 ['Caterham',4]])
drivers = np.array([['Vettel',22],
                    ['Ricciardo',14],
                    ['Rosberg',15],
                    ['Hamilton',18],
                    ['Räikkönen',18],
                    ['Alonso',18],
                    ['Grosjean',14],
                    ['Maldonado',10],
                    ['Button',18],
                    ['Magnussen',12],
                    ['Pérez',8],
                    ['Hülkenberg',8],
                    ['Sutil',8],
                    ['Gutiérrez',8],
                    ['Vergne',6],
                    ['Kvyat',4],
                    ['Massa',12],
                    ['Bottas',8],
                    ['Chilton',4],
                    ['Bianchi',4],
                    ['Ericcson',3],
                    ['Kobayashi',5]])
                    
##################################################
#                  Race results                  #
##################################################
races = np.array(['Australian GP',
                    'Mayalsian GP',
                    'Bahrain GP',
                    'Chinese GP',
                    'Spanish GP',
                    'Monaco GP',
                    'Canadian GP',
                    'Austrian GP',
                    'British GP'])

carScores = np.array([[ 0,15,20,22,27,15,40, 4,25], # Red Bull
                      [25,43,43,43,43,43,18,43,25], # Merc
                      [18,12, 3,19,14,12, 9,11, 8], # Ferrari
                      [ 0, 0, 0, 0, 4, 4, 0, 0, 0], # Lotus
                      [33,10, 0, 0, 0, 9,14, 6,18], # McLaren
                      [ 9,10,25,10, 3,10,10,10, 4], # Force India
                      [ 0, 0, 0, 0, 0, 0, 0, 0, 0], # Sauber
                      [ 6, 1, 0, 1, 0, 0, 4, 0, 3], # Toro Rosso
                      [10,10,10, 6,10, 6, 6,37,18], # Williams
                      [ 0, 0, 0, 0, 0, 0, 0, 0, 0], # Caterham
                      [ 0, 0, 0, 0, 0, 2, 0, 0, 0]])# Marussia

driverScores = np.array([[ 0,15,20,10,45, 0,15, 0,10], # Vettel
                         [ 0, 0,39,12,15,15,40, 4,30], # Ricciardo
                         [31,21,18,24,18,25,18,31, 0], # Rosberg
                         [ 0,45,28,25,25,18, 0,39,40], # Hamilton
                         [18, 0, 1,13, 6, 0, 1, 1, 0], # Räikkönen
                         [15,12, 2,21,11,15,11,10,38], # Alonso
                         [21,12,12, 0, 4,22, 0,24, 0], # Grosjean
                         [15, 0, 9,24,21, 0, 0, 3, 9], # Maldonado
                         [36,20, 0, 3, 0,26,27, 0,12], # Button
                         [24, 2, 0, 6, 6, 1,11, 6, 6], # Magnussen
                         [19, 0,18,23, 8, 0, 6,35, 0], # Pérez
                         [11,16,28,14, 1,28,28, 5, 4], # Hülkenberg
                         [ 6, 0, 0, 0, 0, 0, 9, 9, 0], # Sutil
                         [24, 0, 0, 3, 0, 6,24, 0, 0], # Gutiérrez
                         [ 4, 0, 0, 0, 0, 0, 4, 0, 1], # Vergne
                         [ 2, 4, 3,10, 0, 0, 0, 0, 2], # Kvyat
                         [ 0,24, 6, 0, 0,33, 0,12, 0], # Massa
                         [40,34, 4, 6,10, 0, 6,15,54], # Bottas
                         [12,18,24, 6, 0,15, 0,12, 3], # Chilton
                         [12, 0, 9, 3, 0,38, 0, 9, 0], # Bianchi
                         [ 6,24, 0, 0, 0,33, 0, 6, 6], # Ericsson
                         [ 0,21, 9, 3, 0,21, 9, 9,21]])# Kobayashi

##################################################
#              Robolainen greeting               #
##################################################
print
print "   **  ,_____,"
print "        _/__\_,^o,,___"
print "   _(_(-«-(_( O )==(( O )>__"
print

##################################################
#                 Race selection                 #
##################################################

if races.size > 1:
    print "There have been {} races this season:".format(races.size)
    print
    for i in xrange(races.size):
        print "{}. {}".format(i+1,races[i])
    print "99. Include all races"
    choice = np.array(input("List which races you would like Robolainen to include\n"
                            "in its calculation, followed by a comma: "))
    if np.size(choice)==1 and choice == 99:
        pass
    else:
        races=races[choice-1]
        carScores=carScores[:,choice-1].reshape(-1,np.size(choice))
        driverScores=driverScores[:,choice-1].reshape(-1,np.size(choice))


##################################################
#             Robolainen calculations            #
##################################################

nCarCombs = int(factorial(cars.shape[0])/factorial(cars.shape[0]-nCarPerTeam)/factorial(nCarPerTeam))
nDriverCombs = int(factorial(drivers.shape[0])/factorial(drivers.shape[0]-nDriverPerTeam)/factorial(nDriverPerTeam))

def return_combinations(array,num):
    length = len(array)
    ncombs = factorial(length)/factorial(length-num)/factorial(num)
    iterator = combinations(array,num)
    array=np.vstack([iterator.next() for i in xrange(ncombs)])
    return array
    
carScores = np.array([return_combinations(cars[:,0],nCarPerTeam),  # Names
                    return_combinations(cars[:,1],nCarPerTeam),  # Prices
                    return_combinations(np.sum(carScores,axis=1),nCarPerTeam)]) # Scores

driverScores = np.array([return_combinations(drivers[:,0],nDriverPerTeam),  # Names
                        return_combinations(drivers[:,1],nDriverPerTeam),  # Prices
                        return_combinations(np.sum(driverScores,axis=1),nDriverPerTeam)]) # Scores
                     
Teams = np.zeros((nCarCombs*nDriverCombs,nCarPerTeam+nDriverPerTeam),dtype=np.chararray)
Prices = np.zeros((nCarCombs*nDriverCombs,nCarPerTeam+nDriverPerTeam),dtype=np.int)
Scores = np.zeros((nCarCombs*nDriverCombs,nCarPerTeam+nDriverPerTeam),dtype=np.int)

Teams[:,:3] = np.repeat(carScores[0],nDriverCombs,axis=0)
Prices[:,:3] = np.repeat(carScores[1],nDriverCombs,axis=0)
Scores[:,:3] = np.repeat(carScores[2],nDriverCombs,axis=0)

for i in xrange(nCarCombs):
    Teams[i*nDriverCombs:(i+1)*nDriverCombs,3:] = driverScores[0]
    Prices[i*nDriverCombs:(i+1)*nDriverCombs,3:] = driverScores[1]
    Scores[i*nDriverCombs:(i+1)*nDriverCombs,3:] = driverScores[2]
    
rows_to_remove = np.where(np.sum(Prices,axis=1)>maxspend)[0]
Teams=np.delete(Teams,rows_to_remove,axis=0)
Prices=np.delete(Prices,rows_to_remove,axis=0)
Scores=np.delete(Scores,rows_to_remove,axis=0)


##################################################
#               Robolainen results               #
##################################################

print
print "Robolainen found {} combinations of cars and drivers,".format(nCarCombs*nDriverCombs)
print "of which {} are within the spend limit.".format(len(Teams))
print
print "The best team(s) is list below."
print

TPrices=np.sum(Prices,axis=1)
TScores=np.sum(Scores,axis=1)
best_teams = np.where(TScores==np.max(TScores))[0]

if len(best_teams) > 1:
    print len(best_teams),"teams achieved the maximum number of points:"
    for team in best_teams:
        print team
    print "Robolainen will list the roster of all of them"
    print

for team in best_teams:
    print "==========================================================="
    print
    print "Team Ref.: {}".format(team)
    print
    print "Price: £{} million".format(TPrices[team])
    print
    print "Score: {}".format(TScores[team])
    print
    print "CARS:"
    for i in xrange(nCarPerTeam):
        print "{} ({})".format(Teams[team][i],Scores[team][i])
    print
    print "DRIVERS:"
    for i in xrange(nDriverPerTeam):
        print "{} ({})".format(Teams[team][nCarPerTeam+i],Scores[team][nCarPerTeam+i])
    print
print "==========================================================="

