## Music Theory

Coding a little bit of music theory.

## Note

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

-- audio c5 aca --

- Plot the frequency spectrum of a note.

```
  G4 = Note('G')
  G4.plot_wave_note()
```

-- Plot aca de G4 --

### Classes method

- Plot a list of notes.

`Note.plot_list_of_note_waves([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)`

-- plot de cuatro notas aca--

- Plot frequency of a chord.

`Note.plot_chord_wave([C4, E4, G4, B], duration=1)`

-- plot de acorde aca

- Create an audio file from a chord.

`Note.generate_audio_file_for_chord([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)`

-- audio file aca --
