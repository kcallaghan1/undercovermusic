from Environment import set_tonic, create_chord_progression, create_midi_from_chord_list, convert_midi_to_txt, convert_txt_to_midi
from SimpleAgent2 import create_melody


def main():
    print("---------------------------------------")
    print("Welcome to Undercover Music Generator!!")
    print("---------------------------------------")

    print("What agent do you want to proceed with? (choose #)")
    print("1. Simple\n2. Complex")
    agentChoice = int(input())

    if (agentChoice == 1):
        print("What do you want to do?")
        #print("1. Create Chord Progression\n2. Choose Pre-made Chord Progression\n3. Random Chord Progression\n4. Quit")
        print("1. Create Chord Progression\n2. Quit")
        choiceToDo = int(input())
        # code

        if choiceToDo==1:
            key = input("Enter a key for the progression:\n")
            root = set_tonic(key)
            chords = create_chord_progression(root)
            filename = input("Please name your chord progression midi file:\n")
            #division = input("Enter division of progression - (w)hole, (h)alf, or (q)uarter:\n")
            mid = create_midi_from_chord_list(chords, filename, "w")
            #convert_midi_to_txt("midi/" + filename + ".mid")
            output = input("Name the output midi file:\n")
            create_melody(chords, mid, output)
            #create_melody(filename, output)
            #convert_txt_to_midi(output)

        else:
            exit()
            

    else:
        print("No complex agent found.")


        """    #if choice==1:
                # print("A Minor\nBb Minor\nB Minor\nC Minor\nC# Minor\nD Minor\nD# Minor\nE Minor\nF Minor\nF# Minor\nG Minor\nG# Minor")
            #if (choice==2):
                # print("Ab Major\nA Major\nBb Major\nB Major\nC Major\nDb Major\nD Major\nEb Major\nE Major\nF Major\nF# Major\nG Major")
                # createMajorScale()
            # else:
            #     getRandomScale()               #random search

        elif choiceToDo==2:
            print("Complex agent not yet implemented.")
            print("What type of chord progression you want to choose from? (choose #)")
            print("1. Minor\n2. Major\n3. Random")
            choice = int(input())

            if choice==1:
                print("Minor scale chosen")
            elif choice==2:
                print("Major scale chosen")
                print("Using progression: I V vi IV")
                progression = "I_V_vi_IV"
                convert_midi_to_txt("midi/" + progression + ".mid")
                progression = create_melody(progression)
                convert_txt_to_midi(progression)

                # chooseMajorScale()
            # else:
                # chooseRandomScale()               #random search

        # while  choiceToDo==3:
            #getRandomScale()               #random search """

if __name__ == "__main__":
    main()








