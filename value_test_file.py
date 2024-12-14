# Value returning functions
import random


def getHabitat(animal):
    if animal in ["turtle", "fish", "anemone", "urchin", "jellyfish", "shark", "clownfish"]:
        return "ocean"
    
    if animal in ["spider", "scorpion", "camal", "iguana", "fox", "snake", "tortoise"]:
        return "desert"
    
    if animal in ["lemur", "monkey", "tiger", "parot", "panda", "panther", "lion"]:
        return "jungle"

def getFriends(habitat, numFriends):
    friends = []

    if habitat == "ocean":
        oceanList = ["turtle", "fish", "anemone", "urchin", "jellyfish", "shark", "clownfish"]

        # Loop runs numFriends times, adding a random ocean animal to the friends list each time.
        for i in range(numFriends):
            friends.append(random.choice(oceanList))

        return friends
    
    if habitat == "desert":
        desertList = ["spider", "scorpion", "camal", "iguana", "fox", "snake", "tortoise"]

        for i in range(numFriends):
            friends.append(random.choice(desertList))

        return friends
    
    if habitat == "jungle":
        jungleList = ["lemur", "monkey", "tiger", "parot", "panda", "panther", "lion"]

        for i in range(numFriends):
            friends.append(random.choice(jungleList))
            
        return friends

    

    



# Define the main
# click windows and pirod to get emojis to copy.
def main():
    run_again = "yes"
    while run_again.lower() == "yes":
    
        print("🐳🐋");
        print("╰(*°▽°*)╯(●'◡'●) (❁´◡`❁) (*/ω＼*) ಥ_ಥ (⌐■_■) (¬‿¬) (¬_¬ )");
        print("~(￣▽￣)~*（￣︶￣）↗ (～￣▽￣)～ ( •̀ ω •́ )✧  \^o^/  (*￣▽￣*)");
        print("( $ _ $ ) (/≧▽≦)/ (p≧w≦q) (⓿_⓿) ◑﹏◐ (✿◕‿◕✿) ≡(▔﹏▔)≡.");
        print("·´¯`(>▂<)´¯`·. ┗( T﹏T )┛（︶^︶）( ˘︹˘ ) (ㆆ_ㆆ) ಠ▃ಠ ಠ﹏ಠ o((⊙﹏⊙))o.");
        print("＼（〇_ｏ）／ o_o <@_@> (●__●) ◉_◉ (⊙_◎) ⚆_⚆ (•ˋ _ ˊ•)");
        print("");
        print("");

        animal = input("Enter your favorite animal: ");
        habitat = getHabitat(animal)
        print(f"{animal} lives in the {habitat}");

        print()
        numFriends = int(input("How many frinds for the {animal}?"))
        friendsList = getFriends(habitat, numFriends)
        print()
        print(f"The animal has the following friends: ")
        # Loop to display all items in friendsList.
        for a in friendsList:
            print(a)
                         
        print()
        run_again = input("Enter 'yes' to run again or 'no' to exit: ");

    
# Calle the main
if __name__ == "__main__":
     main()
