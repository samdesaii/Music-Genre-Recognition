#extracting audio
import os
import librosa
import config
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def main():
    samp_rate = config.CreateDataset.SAMPLING_RATE
    frame_size = config.CreateDataset.FRAME_SIZE
    hop_size = config.CreateDataset.HOP_SIZE
    dataset_dir = config.CreateDataset.DATASET_DIRECTORY
    # GET_SUBFOLDERS
    sub_folders = get_subdirectories(dataset_dir)

    for sub_folder in sub_folders:
        print(".......Working in ", sub_folder)
        audio_files = get_audio_file(dataset_dir, sub_folder)
        for audio_file in audio_files:
            path = get_audio_path(dataset_dir, sub_folder, audio_file)
            get_spectrogram(path, frame_size, hop_size, audio_file)


def get_audio_path(dataset_dir, sub_folders, audio_file):
    return [dataset_dir + "/" + sub_folders + "/" + audio_file]


def get_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]


def get_audio_file(dataset_dir, sub_folder):
    return librosa.util.find_files(dataset_dir + "/" + sub_folder)


def get_spectrogram(path, FRAME_SIZE, HOP_SIZE, audio_file):
    scale, sr = librosa.load(path)
    S = np.abs(librosa.stft(scale, n_fft=FRAME_SIZE, hop_length=HOP_SIZE))
    M = librosa.power_to_db(S)

    fig = plt.figure(figsize=(16, 10))
    librosa.display.specshow(M, sr=sr, hop_length=HOP_SIZE, x_axis="time", y_axis="log")
    plt.colorbar()
    fig.savefig(audio_file+".png")
    plt.close(fig)
