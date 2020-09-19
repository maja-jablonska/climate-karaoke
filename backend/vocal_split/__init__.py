from spleeter.separator import Separator
from spleeter.audio.adapter import get_default_audio_adapter


separator: Separator = Separator('spleeter:2stems')
audio_loader = get_default_audio_adapter()
sample_rate: int = 44100


def split_vocals(filepath: str):
    separated_filename: str = filepath.replace('.mp3', '.split')
    separator.separate_to_file(filepath, separated_filename)
    subdir: str = separated_filename.split('/')[-1].replace('.split', '')
    return f'{separated_filename}/{subdir}', f'accompaniment.wav'
