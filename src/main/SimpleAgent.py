# This is a simple melody making agent, defined by the interface in Interface.py
from Environment import extract_int

# Adds a melody to a text file representing MIDI music
def create_melody(progression):
    txt_file = open("midi/" + progression + ".txt", "r+")
    lines = txt_file.readlines()
    i = 0
    while(i < len(lines)):
        if("note_on" in lines[i]): 
            i += 1
            params = extract_int(lines[i])
            lines.insert(i+1, "note_on channel=" + str(params[0]) + " note=" + str((params[1]+12)) + " velocity=" + str(params[2]) + " time=" + str(params[3]) +"\n")
            i += 3
            lines.insert(i+1, "note_off channel=" + str(params[0]) + " note=" + str((params[1]+12)) + " velocity=" + str(params[2]) + " time=" + str(params[3]) +"\n")

        else:
            i += 1
    new_key = "newSong2"
    new_file = open("midi/" + new_key + ".txt", "w")
    for line in lines:
        new_file.write(line)
    return new_key
    