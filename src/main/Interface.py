

def main():
    print("Welcome to Undercover Music Generator!!")
    print("---------------------------------------")

    print("What do you want to do?")
    print("1. Create Chord Progression\n2. Quit")
    choiceToDo = int(input())

    while choiceToDo==1:
        print("What type of chord progression you want to generate? (choose #)")
        print("1. Minor\n2. Major\n3. Random")
        choice = int(input())

        if choice==1:
            createMinorScale()
        elif choice==2:
            createMajorScale()
        else:
            createRandomScale()

if __name__ == "__main__":
       main()


