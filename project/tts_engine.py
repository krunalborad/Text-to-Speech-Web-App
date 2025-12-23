from TTS.api import TTS

# Load TTS model (first run will download model)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def generate_voice(text, output_path="output/audio.wav"):
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path