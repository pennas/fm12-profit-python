players_in = {
    "Figueroa Luciano Aris": 0,
    "Galitsios Giorgos Aris": 0,
    "Moras Vagelis Aris": 0,
    "Tziolis Alexandros Aris": 0,
    "Vasilakakis Thodoris Aris": 0.625,
    "Christodoulopoulos Lazaros Aris": 0,
    "Esor Marvin Aris": 0.325,
    "Siovas Dimitris Aris": 0.725,
    "Ciro Aris": 0,
    "Mantalos Petros Aris": 0.5,
    "Mitroglou Kostas Aris": 0.2
}

players_out = {
    "Figueroa Luciano Aris": 0.4,
    "Galitsios Giorgos Aris": 0.16,
    "Moras Vagelis Aris": 1.2,
    "Tziolis Alexandros Aris": 0.35,
    "Vasilakakis Thodoris Aris": 2.3,
    "Christodoulopoulos Lazaros Aris": 4.4,
    "Esor Marvin Aris": 1.2,
    "Siovas Dimitris Aris": 3.4,
    "Ciro Aris": 5.25,
    "Mantalos Petros Aris": 0.7,
    "Mitroglou Kostas Aris": 5
}

myCounterPlayerin =0
myCounterPlayerOut = 0
myCounterPlayerTotal = 0
all_players = {}

print(" \nAGORA")

for playerin, buy in sorted(players_in.items(), key=lambda x:x[1], reverse=True):
    myCounterPlayerin = myCounterPlayerin + 1
    print(f"{myCounterPlayerin}. {playerin} {buy} ")
    all_players[playerin] = buy
    for playerout, sell in players_out.items():

        if playerin == playerout:
            total = sell- buy
            all_players[playerin] = total

print("\nPOLISI")

for playerout, sell in sorted(players_out.items(), key=lambda x:x[1], reverse=True):

    myCounterPlayerOut = myCounterPlayerOut + 1
    print(f"{myCounterPlayerOut}. {playerout} {sell} ")

print("\nKERDOS")

for player, souma in sorted(all_players.items(), key=lambda x:x[1], reverse=True):

    myCounterPlayerTotal = myCounterPlayerTotal + 1
    print(f"{myCounterPlayerTotal}. {player} {souma} ")

print("\n")
profit = sum(all_players.values())
print("H Soyma einai: ", profit)
