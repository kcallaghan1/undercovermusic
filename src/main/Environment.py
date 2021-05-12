from mido import Message, MetaMessage, MidiFile, MidiTrack
import os
import re

def extract_int(word):
    numstring = re.findall("\d+", word)
    output = []
    for i in range(len(numstring)):
        output.append(int(numstring[i]))
    return output
    

def convert_midi_to_txt(midi_file):
    mid = MidiFile(midi_file)
    txt_file = open(midi_file[0:len(midi_file)-4] + ".txt", "w")
    for i, track in enumerate(mid.tracks):
        txt_file.write(str('Track {}: {}'.format(i, track.name)) + "\n")
        for msg in track:
            txt_file.write(str(msg)+"\n")
    return txt_file


def convert_txt_to_midi(progression):
    mid = MidiFile()
    txt_file = open("midi/" + progression + ".txt", "r")
    lines = txt_file.readlines()
    track = ""
    for line in lines:
        if(line[0:5] == "Track"):
            track = MidiTrack()
            mid.tracks.append(track)
        elif("meta" in line):
            if("time_signature" in line):
                params = extract_int(line)
                track.append(MetaMessage('time_signature', numerator=params[0], denominator=params[1], clocks_per_click=params[2], notated_32nd_notes_per_beat=params[4], time=params[5]))
            elif("set_tempo" in line):
                params = extract_int(line)
                track.append(MetaMessage('set_tempo', tempo = params[0], time=params[1]))
            elif("track_name" in line):
                names = line.split("'")
                params = extract_int(line)
                track.append(MetaMessage("track_name", name=names[1], time=params[0]))
            else:
                params = extract_int(line)
                track.append(MetaMessage('end_of_track', time=params[0]))
        elif("program_change" in line):
            params = extract_int(line)
            track.append(Message('program_change', channel=params[0], program=params[1], time=params[2]))
        elif("note_on" in line):
            params = extract_int(line)
            track.append(Message("note_on", channel=params[0], note=params[1], velocity=params[2], time=params[3]))
        elif("note_off" in line):
            params = extract_int(line)
            track.append(Message("note_off", channel=params[0], note=params[1], velocity=params[2], time=params[3]))
    mid.save("midi/" + progression + ".mid")



def set_tonic(root):
    if root.lower() == "c":
        return 48
    elif root.lower() == "c#" or root.lower() == "db":
        return 49
    elif root.lower() == "d":
        return 50
    elif root.lower() == "d#" or root.lower() == "eb":
        return 51
    elif root.lower() == "e":
        return 52
    elif root.lower() == "f":
        return 53
    elif root.lower() == "f#" or root.lower() == "gb":
        return 54
    elif root.lower() == "g":
        return 55
    elif root.lower() == "g#" or root.lower() == "ab":
        return 56
    elif root.lower() == "a":
        return 57
    elif root.lower() == "a#" or root.lower() == "bb":
        return 58
    elif root.lower() == "b":
        return 59
    else:
        print("Invalid key chosen, using key of C Major")


# Returns a list of three-note chord using midi note information
def create_chord_progression(root):
    chords = []
    keepGoing = True
    while(keepGoing):
        chord = input("Insert a chord as a Roman numeral, or 'x' to quit:\n")
        if(chord == "x"):
            keepGoing = False
        # Uppercase Roman numeral indicates a major chord, consisting of root, third, and fifth
        elif(chord.isupper()):
            tonic = root
            third = 4
            fifth = 7
            if(chord == "II"):
                tonic = root + 2
            elif(chord == "III"):
                tonic = root + 4
            elif(chord == "IV"):
                tonic = root + 5
            elif(chord == "V"):
                tonic = root + 7
            elif(chord == "VI"):
                tonic = root + 9
            elif(chord == "VII"):
                tonic = root + 11
            else:
                tonic = root
            
            chordToAdd = (tonic, tonic + third, tonic + fifth)
            chords.append(chordToAdd)
        # Case: minor chords
        else:
            tonic = root
            third = 3
            fifth = 7

            if(chord == "ii"):
                tonic = root + 2
            elif(chord == "iii"):
                tonic = root + 4
            elif(chord == "iv"):
                tonic = root + 5
            elif(chord == "v"):
                tonic = root + 7
            elif(chord == "vi"):
                tonic = root + 9
            elif(chord == "vii"):
                tonic = root + 11
            else:
                tonic = root

            chordToAdd = (tonic, tonic + third, tonic + fifth)
            chords.append(chordToAdd)

    return chords


def create_midi_from_chord_list(chords, filename, division):
    mid = MidiFile()
    track0 = MidiTrack()
    mid.tracks.append(track0)
    track0.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
    track0.append(MetaMessage('set_tempo', tempo = 833333, time=0))
    track0.append(MetaMessage('end_of_track', time=0))

    track1 = MidiTrack()
    mid.tracks.append(track1)
    track1.append(MetaMessage('track_name', name='Smooth Synth', time=0))
    track1.append(Message('program_change', channel=0, program=80, time=0))
    if division.lower() == "w":
        for chord in chords:
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=768))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))
    elif division.lower() == "h":
        for chord in chords:
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=384))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=384))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))
    elif division.lower() == "q":
        for chord in chords:
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=192))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=192))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=192))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[0], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_on', channel=0, note=chord[2], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[0], velocity = 50, time=192))
            track1.append(Message('note_off', channel=0, note=chord[1], velocity = 50, time=0))
            track1.append(Message('note_off', channel=0, note=chord[2], velocity = 50, time=0))

    track1.append(MetaMessage('end_of_track', time=0))

    mid.save("midi/" + filename + ".mid")
    
    print("Generated file successfully.")
    return mid


convert_midi_to_txt("midi/output.mid")