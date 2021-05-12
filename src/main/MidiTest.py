# Requires mido, run "pip install mido" on your terminal.

from mido import Message, MetaMessage, MidiFile, MidiTrack
import os

def main():
    mid = MidiFile('midi/Untitled_2044026_1.mid')
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)
    print("Select chord progression:")
    print("1. I V vi IV")
    print("2. i bVII VI V")
    choice = int(input())

    if choice==1:
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
        track1.append(Message('note_on', channel=0, note=60, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=64, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=67, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=67, velocity = 50, time=768))
        track1.append(Message('note_off', channel=0, note=64, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=60, velocity = 50, time=0))

        track1.append(Message('note_on', channel=0, note=67, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=62, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=59, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=67, velocity = 50, time=768))
        track1.append(Message('note_off', channel=0, note=62, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=59, velocity = 50, time=0))


        track1.append(Message('note_on', channel=0, note=57, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=60, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=64, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=57, velocity = 50, time=768))
        track1.append(Message('note_off', channel=0, note=60, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=64, velocity = 50, time=0))


        track1.append(Message('note_on', channel=0, note=60, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=65, velocity = 50, time=0))
        track1.append(Message('note_on', channel=0, note=57, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=60, velocity = 50, time=768))
        track1.append(Message('note_off', channel=0, note=65, velocity = 50, time=0))
        track1.append(Message('note_off', channel=0, note=57, velocity = 50, time=0))

        track1.append(MetaMessage('end_of_track', time=0))

        mid.save('midi/new_song.mid')

    else:
        print("Not finished yet.")


if __name__ == '__main__':
    main()