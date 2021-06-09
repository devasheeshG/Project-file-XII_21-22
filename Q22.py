#  Q22. What will be the output of the following code and why?


team1 =["anjali", "anjali singh"]
team2 =["anjali singh", "Anjali"]
for player in team1:   
        if player in team2:
                print("%s plays for team1 and team2." %(player))