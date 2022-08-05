from note import Note

# Generate some random notes
A = Note('A')
A_sharp = Note('A#', 4)
B = Note('B', 4)
C = Note('C', 5)
C_sharp = Note('C#', 5)

C4 = Note('C', 4)
D4 = Note('D', 4)
E4 = Note('E', 4)
G4 = Note('G', 4)
F_sharp4 = Note('F#', 4)

# Generate audio files for some notes
A.generate_audio_file(duration=1)
A_sharp.generate_audio_file(duration=1)
B.generate_audio_file()
C.generate_audio_file()
C_sharp.generate_audio_file(duration=2)
C4.generate_audio_file()
F_sharp4.generate_audio_file()
G4.generate_audio_file()

# Plot some frequencies of notes separately
A.plot_wave_note()
A_sharp.plot_wave_note()
G4.plot_wave_note()

# Plot some frequencies of notes all togheter
Note.plot_list_of_note_waves([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)

# Plot a chord wave
Note.plot_chord_wave([C4, E4, G4, B], duration=1)

# Generate audio files for a chord
Note.generate_audio_file_for_chord([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)
Note.generate_audio_file_for_chord([D4, F_sharp4, A], duration=1)

# Generate audio files from a progression
# Happy birthday song.
Note.generate_audio_file_for_progression(
  [
    Note("G"), Note("G"), Note("A"), Note("G"), Note("C", 5), Note("B"), Note("G"),
    Note("G"),Note("A"), Note("G"), Note("D", 5), Note("C", 5), Note("G"),
    Note("G"), Note("E", 5), Note("C", 5), Note("B"), Note("A"), Note("F", 5),
    Note("F", 5), Note("E", 5), Note("C", 5), Note("D", 5), Note("C", 5),
  ]
)