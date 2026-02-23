# Playlist Chaos

Your AI assistant tried to build a smart playlist generator. The app runs, but some of the behavior is unpredictable. Your task is to explore the app, investigate the code, and use an AI assistant to debug and improve it.

This activity is your first chance to practice AI-assisted debugging on a codebase that is slightly messy, slightly mysterious, and intentionally imperfect.

You do not need to understand everything at once. Approach the app as a curious investigator, work with an AI assistant to explain what you find, and make targeted improvements.

---

## How the Code Is Organized

### `app.py`
The Streamlit user interface. It handles:
- Showing and updating the mood profile
- Adding songs
- Displaying playlists
- Lucky Pick
- Stats and history

### `playlist_logic.py`
The logic behind the app, including:
- Normalizing and classifying songs
- Building playlists
- Merging playlist data
- Searching
- Computing statistics
- Lucky Pick mechanics

You will need to look at both files to understand how the app behaves.

---

## How to Run the App

### 1. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
or
python3 -m venv venv
```

Activate it:

- **macOS/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate`

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py

Streamlit is a Python library that lets you turn regular Python scripts into interactive web apps — without needing HTML, CSS, or JavaScript.
```

A browser window should open automatically. If it does not, open the URL shown in the terminal (usually `http://localhost:8501`).

### 4. Stop the App

Press `Ctrl + C` in the terminal.

---



## What You Will Do

### 1. Explore the App

Run the app and try things out:
- Add several songs with different titles, artists, genres, and energy levels
- Change the mood profile
- Use the search box
- Try the Lucky Pick
- Inspect the playlist tabs and stats
- Look at the history

As you explore, write down at least **five things** that feel confusing, inconsistent, or strange. These might be bugs, quirks, or unexpected design decisions.

### 2. Ask AI for Help Understanding the Code

Pick one issue from your list. Use an AI coding assistant to:
- Explain the relevant code sections
- Walk through what the code is supposed to do
- Suggest reasons the behavior might not match expectations

**Example prompt:**
> "Here is the function that classifies songs. The app is mislabeling some songs. Help me understand what the function is doing and where the logic might need adjustment."

Before making changes, summarize in your own words what you think is happening.

### 3. Fix at Least Four Issues

Make improvements based on your investigation. For each fix:
- Identify the source of the issue
- Decide whether to accept or adjust the AI assistant's suggestions
- Update the code
- Add a short comment describing the fix

Your fixes may involve logic, calculations, search behavior, playlist grouping, Lucky Pick behavior, or anything else you discover.

### 4. Test Your Changes

After each fix, interact with the app again:
- Add new songs
- Change the profile
- Try search and stats
- Check whether playlists behave more consistently

Confirm that the behavior matches your expectations.

### 5. Stretch Goals (Optional)

If you finish early or want an extra challenge:
- Improve search behavior
- Add a "Recently Added" view
- Add sorting controls
- Improve how Mixed songs are handled
- Add new features to the history view
- Introduce better error handling for empty playlists
- Add a new playlist category of your own design

---

## Tips for Success

- You do not need to solve everything. Focus on exploring and learning.
- When confused, ask an AI assistant to explain the code or summarize behavior.
- Test the app often. Small experiments reveal useful clues.
- Treat surprising behavior as something worth investigating.
- Stay curious. The unpredictability is intentional and part of the experience.

When you finish, Playlist Chaos will feel more predictable — and you will have taken your first steps into AI-assisted debugging.