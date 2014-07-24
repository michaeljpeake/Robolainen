# -*- coding: utf-8 -*-
import numpy as np
from itertools import combinations
from math import factorial

##################################################
#              Championship settings             #
##################################################
maxspend = 75  # Maximum spend allowed
nCarPerTeam = 3  # Cars per team
nDriverPerTeam = 3  # Drivers per team

cars = np.array([['Red Bull', 23],
                 ['Mercedes', 20],
                 ['Ferrari', 20],
                 ['Lotus', 15],
                 ['McLaren', 15],
                 ['Force India', 12],
                 ['Sauber', 10],
                 ['Toro Rosso', 8],
                 ['Williams', 6],
                 ['Marussia', 5],
                 ['Caterham', 4]])
drivers = np.array([['Vettel', 22],
                    ['Ricciardo', 14],
                    ['Rosberg', 15],
                    ['Hamilton', 18],
                    ['Räikkönen', 18],
                    ['Alonso', 18],
                    ['Grosjean', 14],
                    ['Maldonado', 10],
                    ['Button', 18],
                    ['Magnussen', 12],
                    ['Pérez', 8],
                    ['Hülkenberg', 8],
                    ['Sutil', 8],
                    ['Gutiérrez', 8],
                    ['Vergne', 6],
                    ['Kvyat', 4],
                    ['Massa', 12],
                    ['Bottas', 8],
                    ['Chilton', 4],
                    ['Bianchi', 4],
                    ['Ericcson', 3],
                    ['Kobayashi', 5]])

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

carScores = np.loadtxt("race_data.txt", int)
driverScores = carScores[11:, :]
carScores = carScores[:11, :]

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
        print "{}. {}".format(i+1, races[i])
    print "99. Include all races"
    choice = np.array(input("List which races you would like Robolainen "
                            "to include\nin its calculation, followed by "
                            "a comma: "))
    if np.size(choice) == 1 and choice == 99:
        pass
    else:
        races = races[choice-1]
        carScores = carScores[:, choice-1].reshape(-1, np.size(choice))
        driverScores = driverScores[:, choice-1].reshape(-1, np.size(choice))


##################################################
#             Robolainen calculations            #
##################################################

nCarCombs = int(factorial(cars.shape[0]) /
                factorial(cars.shape[0]-nCarPerTeam) /
                factorial(nCarPerTeam))
nDriverCombs = int(factorial(drivers.shape[0]) /
                   factorial(drivers.shape[0] - nDriverPerTeam) /
                   factorial(nDriverPerTeam))


def return_combinations(array, num):
    length = len(array)
    ncombs = factorial(length) / factorial(length - num) / factorial(num)
    iterator = combinations(array, num)
    array = np.vstack([iterator.next() for i in xrange(ncombs)])
    return array

# [Names, Prices, Scores]
carScores = np.array([return_combinations(cars[:, 0], nCarPerTeam),
                      return_combinations(cars[:, 1], nCarPerTeam),
                      return_combinations(np.sum(carScores, axis=1),
                      nCarPerTeam)])

# [Names, Prices, Scores]
driverScores = np.array([return_combinations(drivers[:, 0], nDriverPerTeam),
                         return_combinations(drivers[:, 1], nDriverPerTeam),
                         return_combinations(np.sum(driverScores, axis=1),
                         nDriverPerTeam)])

Teams = np.zeros((nCarCombs*nDriverCombs, nCarPerTeam+nDriverPerTeam),
                 dtype=np.chararray)
Prices = np.zeros((nCarCombs*nDriverCombs, nCarPerTeam+nDriverPerTeam),
                  dtype=np.int)
Scores = np.zeros((nCarCombs*nDriverCombs, nCarPerTeam+nDriverPerTeam),
                  dtype=np.int)

Teams[:, :3] = np.repeat(carScores[0], nDriverCombs, axis=0)
Prices[:, :3] = np.repeat(carScores[1], nDriverCombs, axis=0)
Scores[:, :3] = np.repeat(carScores[2], nDriverCombs, axis=0)

for i in xrange(nCarCombs):
    Teams[i*nDriverCombs:(i+1)*nDriverCombs, 3:] = driverScores[0]
    Prices[i*nDriverCombs:(i+1)*nDriverCombs, 3:] = driverScores[1]
    Scores[i*nDriverCombs:(i+1)*nDriverCombs, 3:] = driverScores[2]

rows_to_remove = np.where(np.sum(Prices, axis=1) > maxspend)[0]
Teams = np.delete(Teams, rows_to_remove, axis=0)
Prices = np.delete(Prices, rows_to_remove, axis=0)
Scores = np.delete(Scores, rows_to_remove, axis=0)


##################################################
#               Robolainen results               #
##################################################

print
print "Robolainen found {} combinations of cars and drivers," \
      .format(nCarCombs*nDriverCombs)
print "of which {} are within the spend limit.".format(len(Teams))
print
print "The best team(s) is list below."
print

TPrices = np.sum(Prices, axis=1)
TScores = np.sum(Scores, axis=1)
best_teams = np.where(TScores == np.max(TScores))[0]

if len(best_teams) > 1:
    print len(best_teams), "teams achieved the maximum number of points:"
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
        print "{} ({})".format(Teams[team][i], Scores[team][i])
    print
    print "DRIVERS:"
    for i in xrange(nDriverPerTeam):
        print "{} ({})".format(Teams[team][nCarPerTeam+i],
                               Scores[team][nCarPerTeam+i])
    print
print "==========================================================="
