
def main():
    print("---------------------------------------")
    print("Welcome to Undercover Music Generator!!")
    print("---------------------------------------")

    print("What agent you want to proceed with?(choose #)")
    print("1. Simple\n2. Complex")
    agentChoice = input()
    
    while agentChoice==1:
        print("What do you want to do?")
        print("1. Create Chord Progression\n2. Choose Pre-made Chord Progression\n3. Random Chord Progression\n4. Quit")
        choiceToDo = int(input())

        while choiceToDo==1:
            print("What type of chord progression you want to generate? (choose #)")
            print("1. Minor\n2. Major\n3. Random")
            choice = int(input())

            if choice==1:
                print("A Minor\nBb Minor\nB Minor\nC Minor\nC# Minor\nD Minor\nD# Minor\nE Minor\nF Minor\nF# Minor\nG Minor\nG# Minor")
                # createMinorScale()
            elif choice==2:
                print("Ab Major\nA Major\nBb Major\nB Major\nC Major\nDb Major\nD Major\nEb Major\nE Major\nF Major\nF# Major\nG Major")
                # createMajorScale()
            # else:
            #     getRandomScale()               #random search


        while choiceToDo==2:
            print("What type of chord progression you want to choose from? (choose #)")
            print("1. Minor\n2. Major\n3. Random")
            choice = int(input())

            if choice==1:
                print("Minor scale chosen")
                # chooseMinorScale()
            elif choice==2:
                print("Major scale chosen")
                # chooseMajorScale()
            # else:
                # chooseRandomScale()               #random search

        # while  choiceToDo==3:
            #getRandomScale()               #random search

if __name__ == "__main__":
    main()









