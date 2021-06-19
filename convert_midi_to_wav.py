import sys
from midi2audio import FluidSynth

args = sys.argv
# 引数argsの2番目(indexは1)に第一引数が格納されている
name = args[1]
soundfontName = args[2]
fs = FluidSynth(sound_font = '/mount/soundfonts/' + soundfontName)
fs.midi_to_audio('/mount/midi/' + name + '.mid', '/mount/wav/' + name + '.wav')