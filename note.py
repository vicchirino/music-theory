import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
SAMPLE_RATE = 44100
COLORS_FOR_PLOT = [
  "#343090", "#5f59f7", "#6592fd", "#44c2fd", "#8c61ff", "#12492f", "#0a2f35", "#f56038", "#f7a325", "#ffca7a", "#58b368", "#dad873"
]

class Note:
  base_frequency = 440 # A4
  name: str
  octave: int

  def __init__(self, name: str, octave: int = 4):
    self.name = name
    self.octave = octave

  def get_wave(self, duration):
    """
    Function takes the note and "time_duration" for a wave
    as the input and returns a "numpy array" of values at all points
    in time
    """

    amplitude = 4096
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
    plt.show()

  def generate_wave_file(self):
    """
    Function that generates a wave file from the note frequency wave.
    """
    wave = self.get_wave(duration=1)
    wavfile.write(f"wave_files/{self.get_complete_name()}.wav", rate=SAMPLE_RATE, data=wave.astype(np.int16))

def plot_list_of_note_waves(notes, duration=0.5):
    """
    Function takes a list of notes and plots the wave of each note on the graph.
    """
    legends = []

    for note in notes:
        note_wave = note.get_wave(duration)
        x = np.linspace(0, duration, 100)
        plt.plot(x, note_wave[0:int(SAMPLE_RATE/440)], color=COLORS_FOR_PLOT[NOTES.index(note.name)])
        legends.append(note.name)

    plt.title(str("Notes frequency"))
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(legends)
    plt.grid()
    plt.show()

plot_list_of_note_waves([Note("C"), Note("E"), Note("G"), Note("B")], duration=1)

A = Note('A')
A_sharp = Note('A#', 4)


A_sharp.get_frequency()

A.generate_wave_file()

