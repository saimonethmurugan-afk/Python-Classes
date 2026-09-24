#Cricket and Football Scores

class Cricket:
    def __init__(self,player,score):
        self.__player = player  #Private Variables(is created using .__)
        self.__score = score
#Polymorphism
    def info(self):
        print(f"Batsman Name: {self.__player} \nBatsman Score: {self.__score}")

    
    def details(self):
        print(f"{self.__player} has hit a six!")

#Read the value of private variable score
    def get_score(self):
       return self.__score

    def updates(self,updated_score):
        if updated_score >= 0:
            self.__score = updated_score
            print(f"This is the updated score: {self.__score}")
        else:
            print("Please enter a number higher than 0.")



class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Striker Name: {self.__player} \nStriker Score: {self.__score}")


    def details(self):
        print(f"{self.__player} has scored a goal!")

    #Read the value of private variable score
    def get_score(self):
       return self.__score

    def updates(self,updated_score):
        if updated_score >= 0:
            self.__score = updated_score
            print(f"This is the updated score: {updated_score}")
        else:
            print("Please enter a number higher than 0.")

Cricket_obj = Cricket("Sai",99)
Football_obj = Football("Sai 2",3)

print("\n=====Sports Scoreboard=====")
for sport in(Cricket_obj,Football_obj):
    sport.info()
    sport.details()
    print()

print("Attempt at Directly Updating Variables")
Football_obj.__score = 105
print(f"The old score remained.The new score wasn't updated: {Football_obj.__get_score()}")

print("Correct Way to Update Score:")
Football_obj.updates(105)