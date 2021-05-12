# This is a simple melody making agent, defined by the interface in the readme.
from mido import MidiFile, Message


# Adds a melody to a text file representing MIDI music
def create_melody(chords, mid, output):
    i = 0
    chord = 0
    track = mid.tracks[1]
    while i in range(len(track)) and chord < len(chords):
        msg = track[i]

        if msg.time == 768:
            track.insert(i, Message("note_on", channel=0, note=chords[chord][1] + 12, velocity=50, time=0))
            track.insert(i+1, Message("note_off", channel=0, note=chords[chord][1] + 12, velocity=50, time=384))
            track.insert(i+2, Message("note_on", channel=0, note=chords[chord][2] + 12, velocity=50, time=0))
            track.insert(i+3, Message("note_off", channel=0, note=chords[chord][2] + 12, velocity=50, time=384))
            track.insert(i+4, Message("note_off", channel=0, note=msg.note, velocity=50, time=0))
            track.remove(msg)
            chord = chord + 1
            i = i + 5
        i = i + 1

    for msg in track:
        print(msg)

    mid.save("midi/" + output + ".mid")

