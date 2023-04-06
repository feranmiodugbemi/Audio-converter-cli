import sys
import os
from pydub import AudioSegment
import argparse

def help_message():
    message = """usage: cli.py [-h] -convert audio_file format [-name new_name] [-dir directory]

Convert an audio file to a different format.

positional arguments:
  audio_file          The path to the audio file you want to convert.
  format              The audio format you want to convert to.

optional arguments:
  -h, --help          show this help message and exit
  -name new_name      The new name for the converted audio file.
  -dir directory      The directory where you want the converted audio file to be saved."""

    return message

def error_message(command):
    message = """Unknown option: {}
usage: my_converter.py [-h] -convert audio_file format [-name new_name] [-dir directory]
Try `my_converter.py -h' for more information.""".format(command)

    return message


if len(sys.argv) < 2:
    print(error_message(""))
    sys.exit(1)
    
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_message())
    sys.exit(0)

if sys.argv[1] != "-convert":
    print(error_message(sys.argv[1]))
    sys.exit(1)

audio = sys.argv[2]
format = sys.argv[3]

if len(sys.argv) == 5:
    name, audiotype = os.path.splitext(audio)
    name = name.split("/")[-1] # to remove the path and get only the filename
    new_name = sys.argv[4]
    new_name = new_name + '.' + format
    audio = AudioSegment.from_file(audio, format=audiotype[1:])
    audio.export(new_name, format=format)
    
elif len(sys.argv) == 6:
    name, audiotype = os.path.splitext(audio)
    name = name.split("/")[-1] # to remove the path and get only the filename
    new_name = sys.argv[4]
    new_directory = sys.argv[5]
    audio = AudioSegment.from_file(audio, format=audiotype[1:])
    name = new_name if new_name.endswith(format) else new_name + '.' + format
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    output_file = os.path.join(new_directory, name)
    audio.export(output_file, format=format)
    
else:
    name, audiotype = os.path.splitext(audio)
    name = name.split("/")[-1] # to remove the path and get only the filename
    audio = AudioSegment.from_file(audio, format=audiotype[1:])
    name = name + '.' + format
    audio.export(name, format=format)
