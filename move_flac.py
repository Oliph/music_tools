import os
import shutil

AUDIO_EXTENSION = ['3gp', 'aac', 'act', 'aiff', 'alac', 'amr',
                                'atrac', 'au', 'awb', 'dct', 'dss', 'dvf',
                                'flac', 'gsm', 'm4a', 'm4p', 'mmf', 'mp3',
                                'mpc', 'msv', 'ogg', 'opus', 'ra', 'rm',
                                'raw', 'tta', 'vox', 'wav', 'wavpack',
                                'wma']


def create_directory(dirname, light_dir):
    album = dirname.split('/')[-1]
    artist = dirname.split('/')[-2]
    directory = '{}{}/{}/'.format(light_dir, artist, album)
    if os.path.exists(directory):
        return None
    if not os.path.exists(directory):
        os.makedirs(directory)
        return directory


def process(input_dir, flac_copy, none_flac_copy):
    """ """
    for dirname, subdir, files_ in os.walk(input_dir):
        # Directory level, checking if there is no subdir anymore
        if not subdir:
            flac = False
            for file_ in files_:
                if file_.lower().endswith('flac'):
                    print(file_)
                    flac = True
                    try:
                        shutil.copy2(file_, flac_copy)
                    except Exception as e:
                        print(e)
                        raise
                        create_directory(dirname, flac_copy)
                        shutil.copy2(file_, flac_copy)
            if flac is False:
                for file_ in files_:
                    if file_.lower().endswith(tuple(AUDIO_EXTENSION)):
                        try:
                            shutil.copy2(file_, none_flac_copy)
                        except Exception as e:
                            print(e)
                            raise
                            create_directory(dirname, none_flac_copy)
                            shutil.copy2(file_, none_flac_copy)

def open_directory(inputname):
    """
    """


def main():
    process('/home/olivier/nfs_music/Music/Albums', '/home/olivier/nfs_music/Music/test_flac', '/home/olivier/nfs_music/Music/test_none_flac')
