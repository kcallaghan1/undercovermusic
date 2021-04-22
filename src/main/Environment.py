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