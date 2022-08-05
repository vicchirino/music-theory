# Music Theory

Coding a little bit of music theory.

## Note Class

### Creation

```
  class Note:
    base_frequency = BASE_FREQUENCY # A4
    name: str
    octave: int
```

- Create a note without octave (default octave is 4)

`A = Note('A')`

- Create a note with octave

`C = Note('C', 5)`

- Create a sharp note

`F_sharp4 = Note('F#', 4)`

### Methods

- Create an audio file from a note.

`C.generate_audio_file()`

https://user-images.githubusercontent.com/3228237/182922818-25d6e414-b456-4b81-87c9-3ec74ff04da6.mov

- Plot the frequency spectrum of a note.

```
  G4 = Note('G')
  G4.plot_wave_note()
```

<img width="400" alt="image" src="https://github.com/vicchirino/music-theory/blob/main/plots/notes/G4.png?raw=true">

### Classes method

- Plot a list of notes.

`Note.plot_list_of_note_waves([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)`

<img width="400" alt="image" src="https://github.com/vicchirino/music-theory/blob/main/plots/notes/C4_E4_G4_B4.png?raw=true">

- Plot frequency of a chord.

`Note.plot_chord_wave([C4, E4, G4, B], duration=1)`

<img width="400" alt="image" src="https://github.com/vicchirino/music-theory/blob/main/plots/chords/C4-E4-G4-B4.png?raw=true">

- Create an audio file from a chord.

`Note.generate_audio_file_for_chord([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)`

https://user-images.githubusercontent.com/3228237/182923288-4801d934-e096-4d67-8c45-ef2d953bef6f.mov

- Create an audio file from a progression.

```
Note.generate_audio_file_for_progression(
  [
    Note("G"), Note("G"), Note("A"), Note("G"), Note("C", 5), Note("B"), Note("G"),
    Note("G"),Note("A"), Note("G"), Note("D", 5), Note("C", 5), Note("G"),
    Note("G"), Note("E", 5), Note("C", 5), Note("B"), Note("A"), Note("F", 5),
    Note("F", 5), Note("E", 5), Note("C", 5), Note("D", 5), Note("C", 5),
  ]
)
```
