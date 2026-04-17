import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.current_index = 0

        self.is_playing = False
        self.start_time = 0
        self.pause_time = 0

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))
        return sorted(files)

    def play(self):
        if not self.playlist:
            return

        track = self.playlist[self.current_index]
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()

        self.is_playing = True
        self.start_time = pygame.time.get_ticks()

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_track_info(self):
        if not self.playlist:
            return "No tracks", 0, 0

        name = os.path.basename(self.playlist[self.current_index])
        return name, self.current_index + 1, len(self.playlist)

    def get_position(self):
        if not self.is_playing:
            return 0

        return (pygame.time.get_ticks() - self.start_time) // 1000