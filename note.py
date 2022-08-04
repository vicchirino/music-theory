import enum
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from utils import NOTES, SAMPLE_RATE, COLORS_FOR_PLOT, AMPLITUDE, BASE_FREQUENCY

class Note:
  base_frequency = BASE_FREQUENCY # A4
  name: str
  octave: int

  def __init__(self, name: str, octave: int = 4):
    self.name = name
    self.octave = octave

  def get_wave(self, duration, amplitude: int = 4096) -> np.ndarray:
    """
    Function takes the note and "time_duration" for a wave
    as the input and returns a "numpy array" of values at all points
    in time
    """
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    
    wave = amplitude * np.sin(2 * np.pi * self.get_frequency() * t)

    return wave

  def get_complete_name(self) -> str:
    return str(self.name) + str(self.octave)
  
  def get_frequency(self) -> float:
    """
    Function that returns the frequency.
    """
    keyNumber = NOTES.index(self.name);
    
    if (keyNumber < 3) :
        keyNumber = keyNumber + 12 + ((self.octave - 1) * 12) + 1; 
    else:
        keyNumber = keyNumber + ((self.octave - 1) * 12) + 1; 

    frequency = self.base_frequency * 2** ((keyNumber- 49) / 12)
    print("Frequency of " + self.name + " is " + str(frequency))
    return frequency

  def plot_wave_note(self, duration: float = 0.5):
    """
    Function takes plot the note frequency on a graph.
    """
    note_wave = self.get_wave(duration)

    plt.plot(note_wave[0:int(SAMPLE_RATE/self.base_frequency)], color=COLORS_FOR_PLOT[NOTES.index(self.name)])
    plt.title(str("Note " +  self.get_complete_name() + " wave"))
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(["Note " + self.name])
    plt.grid()
    plt.savefig(f"/Users/victorchirino/Projects/music-theory/plots/notes/{self.get_complete_name()}.png")
    plt.show()

  def generate_audio_file(self, duration: float = 0.5):
    """
    Function that generates a wave file from the note frequency wave.
    """
    wave = self.get_wave(duration)
    wavfile.write(f"wav_files/notes/{self.get_complete_name()}.wav", rate=SAMPLE_RATE, data=wave.astype(np.int16))

  @classmethod
  def plot_list_of_note_waves(cls, notes, duration):
    """
    Function takes a list of notes and plots the wave of each note on the graph.
    """
    legends = []
    plot_name = ""
    for idx, note in enumerate(notes):
        note_wave = note.get_wave(duration)
        x = np.linspace(0, duration, 100)
        plt.plot(x, note_wave[0:int(SAMPLE_RATE/Note.base_frequency)], color=COLORS_FOR_PLOT[NOTES.index(note.name)])
        legends.append(note.name)
        if idx == 0:
          plot_name = note.get_complete_name()
        else:
          plot_name = plot_name + "_" + note.get_complete_name()

    plt.title(str(f"Frequency of {plot_name}"))
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(legends)
    plt.grid()
    plt.savefig(f"/Users/victorchirino/Projects/music-theory/plots/notes/{plot_name}.png")
    plt.show()

  def __get_chord_wave(chord, duration) -> np.ndarray:
    """
    Function takes a list of notes and superpose the wave of each note on a final wave.
    """
    superposed_wave = []
    print(f"Superposed wave initial state: {superposed_wave}")
    for idx, note in enumerate(chord):
      adjusted_wave = note.get_wave(duration, AMPLITUDE)*(AMPLITUDE/len(chord))
      if idx == 0:
        superposed_wave = adjusted_wave
      else:
        superposed_wave = np.sum([superposed_wave, adjusted_wave], axis=0)
    
    return superposed_wave

  @classmethod
  def plot_chord_wave(cls, chord, duration):
    """
    Function takes a list of notes and plots the wave of each note on the graph.
    """
    chord_wave = Note.__get_chord_wave(chord, duration)
    legends = ""
    for idx, note in enumerate(chord):
        if idx == 0:
          legends = note.get_complete_name()
        else:
          legends = legends + "-" + note.get_complete_name()

    plt.plot(chord_wave[0:int(SAMPLE_RATE/Note.base_frequency)], color="red")
    plt.title(str(f"Chord {legends} frequency"))
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend([legends])
    plt.grid()
    plt.savefig(f"/Users/victorchirino/Projects/music-theory/plots/chords/{legends}.png")
    plt.show()

  @classmethod
  def generate_audio_file_for_chord(cls, chord, duration):
    """
    Function that generates a wav file from the chord frequency wave.
    """
    file_name = []
    for idx, note in enumerate(chord):
        if idx == 0:
          file_name = note.name
        else:
          file_name = file_name + "-" + note.name

    chord_wave = Note.__get_chord_wave(chord, duration)

    wavfile.write(f"wav_files/chords/{file_name}.wav", SAMPLE_RATE, chord_wave)
    print("Audio file generated")

