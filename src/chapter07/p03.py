"""
**Jukebox**:

Design a musical jukebox using object-oriented principles.
"""

# Objects:
# * Jukebox
# * CD
# * Song

# Actions:
# * Play Song
# * Play CD
# * Insert CD
# * Shuffle
# * Remove CD
import random
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Song:
    title: str
    duration: int


@dataclass
class CD:
    title: str
    songs: List[Song]


@dataclass
class JukeBok:
    max_cd_count: int
    cds: Dict[str, CD] = field(default_factory=dict)
    current_cd: CD = field(default=None)

    def insert_cd(self, cd: CD):
        if not self.is_full:
            self.cds[cd.title] = cd

    def remove_cd(self, title: str):
        if self.cds.get(title):
            self.cds.pop(title)

    def play_song(self, title: str):
        if self.current_cd:
            print(f"playing {title}")

    def shuffle(self):
        all_songs = [
            (cd.title, song.title) for cd in self.cds.values() for song in cd.songs
        ]
        song = random.choice(all_songs)
        return self.play_cd(song[0], song[1])

    def play_cd(self, title: str, song_title: str = None):
        if not self.current_cd:
            self.current_cd = self.cds[title]
        if not song_title:
            song_title = next(song.title for song in self.current_cd.songs)
        self.play_song(song_title)

    @property
    def is_full(self):
        return len(self.cds) >= self.max_cd_count
