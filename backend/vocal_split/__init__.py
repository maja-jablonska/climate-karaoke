from spleeter.separator import Separator
from spleeter.audio.adapter import get_default_audio_adapter


separator: Separator = Separator('spleeter:2stems')
audio_loader = get_default_audio_adapter()
sample_rate: int = 44100


def split_vocals(filepath: str):
    separator.separate_to_file(filepath, filepath.replace('.mp3', '-split.mp3'))
