# Воспроизведение мультимедиа
# создайте два класса:
# Класс 1
# AudioFileMixin — требует наличие поля
# audio_tracks (список треков).
# Метод play_audio() выводит:
# Воспроизведение аудио для <НазваниеКласса>:
# <название трека>
# <название трека>
# Класс 2
# VideoFileMixin — требует наличие поля
# video_files (список видео).
# Метод play_video() выводит:
# Воспроизведение видео для <НазваниеКласса>:
# <название видео>
# <название видео>
# Если нужное поле отсутствует — выбрасывайте AttributeError.

# Создайте два класса:
# ● MediaPlayer — поддерживает только аудио. Принимает список треков.
# ● Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
# Проверьте работу классов, вызвав методы воспроизведения

class AudioFileMixin:
    def play_audio(self) -> str:
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("У объекта отсутствует поле audio_tracks")

        lines = [f"Воспроизведение аудио для {self.__class__.__name__}:"]

        for track in self.audio_tracks:
            lines.append(track)

        return "\n".join(lines)


class VideoFileMixin:
    def play_video(self) -> str:
        if not hasattr(self, "video_files"):
            raise AttributeError("У объекта отсутствует поле video_files")

        lines = [f"Воспроизведение видео для {self.__class__.__name__}:"]

        for video in self.video_files:
            lines.append(video)

        return "\n".join(lines)


class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks: list[str]) -> None:
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks: list[str], video_files: list[str]) -> None:
        self.audio_tracks = audio_tracks
        self.video_files = video_files


player = MediaPlayer(["track1.mp3", "track2.mp3"])
laptop = Laptop(["track1.mp3", "track2.mp3"], ["movie.mp4", "trailer.mov"])

print(player.play_audio())
print(laptop.play_video())
print(laptop.play_audio())
