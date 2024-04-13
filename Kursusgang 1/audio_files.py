import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play
import os





def record_audio(seconds, output_name):
    chunk = 1024 # Specify chunk size
    sample_format = pyaudio.paInt16 # 16 bits pr sample
    channels = 1
    fs = 44100 # Record 44100 samples pr sec
    seconds = seconds # Record 3 seconds
    filename = os.path.join(os.path.dirname(__file__), output_name)

    p = pyaudio.PyAudio()
    print("Recording")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = [] # List to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs/chunk*seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print(frames) 
    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    p.terminate()

    print("Finished recording")

    # Save recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


    
def load_audio(audio_file_name):
    file = os.path.join(os.path.dirname(__file__), audio_file_name)
    sound = AudioSegment.from_wav(file)
    print("Playing audio")
    play(sound)
    print("Finised playing audio")
    

def main():
    # record_audio(3, 'output_test2.wav')
    # load_audio('output_test2.wav')
    pass

if __name__ == '__main__':
    main()