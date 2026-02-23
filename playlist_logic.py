from collections import Counter
from typing import Dict, List, Optional, Tuple

Song = Dict[str, object]
PlaylistMap = Dict[str, List[Song]]

# Constants for mood classification
HYPE_KEYWORDS = ["rock", "punk", "party"]
CHILL_KEYWORDS = ["lofi", "ambient", "sleep"]

DEFAULT_PROFILE = {
    "name": "Default",
    "hype_min_energy": 7,
    "chill_max_energy": 3,
    "favorite_genre": "rock",
    "include_mixed": True,
}


def normalize_string(value: str, lowercase: bool = False) -> str:
    """Normalize a string by stripping whitespace and optionally lowercasing."""
    if not isinstance(value, str):
        return ""
    normalized = value.strip()
    if lowercase:
        normalized = normalized.lower()
    return normalized


def normalize_title(title: str) -> str:
    """Normalize a song title for comparisons."""
    return normalize_string(title)


def normalize_artist(artist: str) -> str:
    """Normalize an artist name for comparisons."""
    return normalize_string(artist, lowercase=True)


def normalize_genre(genre: str) -> str:
    """Normalize a genre name for comparisons."""
    return normalize_string(genre, lowercase=True)


def normalize_song(raw: Song) -> Song:
    """Return a normalized song dict with expected keys."""
    title = normalize_title(str(raw.get("title", "")))
    artist = normalize_artist(str(raw.get("artist", "")))
    genre = normalize_genre(str(raw.get("genre", "")))
    energy = raw.get("energy", 0)

    if isinstance(energy, str):
        try:
            energy = int(energy)
        except ValueError:
            energy = 0

    tags = raw.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]

    return {
        "title": title,
        "artist": artist,
        "genre": genre,
        "energy": energy,
        "tags": tags,
    }


def is_hype(song: Song, profile: Dict[str, object]) -> bool:
    """Check if a song qualifies as Hype based on profile."""
    energy = song.get("energy", 0)
    genre = song.get("genre", "")
    favorite_genre = profile.get("favorite_genre", "")
    hype_min_energy = profile.get("hype_min_energy", 7)
    is_hype_keyword = any(k in genre for k in HYPE_KEYWORDS)
    return genre == favorite_genre or energy >= hype_min_energy or is_hype_keyword


def is_chill(song: Song, profile: Dict[str, object]) -> bool:
    """Check if a song qualifies as Chill based on profile."""
    energy = song.get("energy", 0)
    genre = song.get("genre", "")
    chill_max_energy = profile.get("chill_max_energy", 3)
    is_chill_keyword = any(k in genre for k in CHILL_KEYWORDS)
    return energy <= chill_max_energy or is_chill_keyword


def classify_song(song: Song, profile: Dict[str, object]) -> str:
    """Return a mood label given a song and user profile."""
    if is_hype(song, profile):
        return "Hype"
    elif is_chill(song, profile):
        return "Chill"
    return "Mixed"


def build_playlists(songs: List[Song], profile: Dict[str, object]) -> PlaylistMap:
    """Group songs into playlists based on mood and profile."""
    playlists: PlaylistMap = {
        "Hype": [],
        "Chill": [],
        "Mixed": [],
    }

    for song in songs:
        normalized = normalize_song(song)
        mood = classify_song(normalized, profile)
        normalized["mood"] = mood
        playlists[mood].append(normalized)

    return playlists


def merge_playlists(a: PlaylistMap, b: PlaylistMap) -> PlaylistMap:
    """Merge two playlist maps into a new map."""
    merged = {}
    for key in set(a.keys()) | set(b.keys()):
        merged[key] = a.get(key, []) + b.get(key, [])
    return merged


def compute_playlist_stats(playlists: PlaylistMap) -> Dict[str, object]:
    """Compute statistics across all playlists."""
    all_songs = [song for playlist in playlists.values() for song in playlist]

    hype = playlists.get("Hype", [])
    chill = playlists.get("Chill", [])
    mixed = playlists.get("Mixed", [])

    total = len(all_songs)
    hype_ratio = len(hype) / total if total > 0 else 0.0

    avg_energy = 0.0
    if all_songs:
        total_energy = sum(song.get("energy", 0) for song in all_songs)
        avg_energy = total_energy / len(all_songs)

    top_artist, top_count = most_common_artist(all_songs)

    return {
        "total_songs": len(all_songs),
        "hype_count": len(hype),
        "chill_count": len(chill),
        "mixed_count": len(mixed),
        "hype_ratio": hype_ratio,
        "avg_energy": avg_energy,
        "top_artist": top_artist,
        "top_artist_count": top_count,
    }


def most_common_artist(songs: List[Song]) -> Tuple[str, int]:
    """Return the most common artist and count."""
    artists = [str(song.get("artist", "")).strip() for song in songs if song.get("artist")]
    if not artists:
        return "", 0
    artist, count = Counter(artists).most_common(1)[0]
    return artist, count


def search_songs(
    songs: List[Song],
    query: str,
    field: str = "artist",
) -> List[Song]:
    """Return songs matching the query on a given field."""
    if not query:
        return songs

    query_lower = query.lower().strip()
    filtered: List[Song] = []

    for song in songs:
        value = str(song.get(field, "")).lower()
        if value and query_lower in value:
            filtered.append(song)

    return filtered


def lucky_pick(
    playlists: PlaylistMap,
    mode: str = "any",
) -> Optional[Song]:
    """Pick a song from the playlists according to mode."""
    if mode == "hype":
        songs = playlists.get("Hype", [])
    elif mode == "chill":
        songs = playlists.get("Chill", [])
    elif mode == "mixed":
        songs = playlists.get("Mixed", [])
    else:
        # "any" mode: combine all playlists
        songs = [song for playlist in playlists.values() for song in playlist]

    return random_choice_or_none(songs)


def random_choice_or_none(songs: List[Song]) -> Optional[Song]:
    """Return a random song or None."""
    if not songs:
        return None
    import random
    return random.choice(songs)


def history_summary(history: List[Song]) -> Dict[str, int]:
    """Return a summary of moods seen in the history."""
    moods = [song.get("mood", "Mixed") for song in history]
    counts = Counter(mood if mood in ["Hype", "Chill", "Mixed"] else "Mixed" for mood in moods)
    return {
        "Hype": counts.get("Hype", 0),
        "Chill": counts.get("Chill", 0),
        "Mixed": counts.get("Mixed", 0),
    }
