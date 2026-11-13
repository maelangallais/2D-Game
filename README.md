# 🕹️ 2D-Game

A top-down 2D pixel-art action game for the **NumWorks** calculator (MicroPython), featuring custom sprite rendering, enemy combat, projectiles, collectibles, and a full multi-language menu system.

---

## ⚠️ Project Notes & Limitations

- **Split Architecture**: Due to strict flash/RAM storage limits on the NumWorks calculator, the main game had to be split into two separate scripts (`game_part1_menus.py` and `game_part2_gameplay.py`).
- **Complexity & Potential Bugs**: This is a fairly ambitious and complex project for a graphing calculator. While playable, it may contain undiscovered bugs, edge-case glitches, or performance bottlenecks.
- **Minimal Storyline**: Despite having a complete video-game menu structure (Save points, Settings, Credits), the narrative/story is **very short and minimal** — enemies appear for combat without much lore or plot explaining why you are fighting them.
- **Performance Tip (`game_part2_gameplay.py`)**: On physical calculator hardware, replacing `draw` with `ls` around line 128 (or adjusting lines 118–119) trades visual bullet continuity for a much smoother framerate.

---

## 📂 Repository Structure

```
2D-Game/
├── game_part1_menus.py      # Full bilingual (FR/EN) game menus, settings & save UI
├── game_part2_gameplay.py   # Core 2D gameplay, sprites, projectiles, enemies & combat
├── history/
│   └── game_v1_monolithic.py # Early all-in-one v1 prototype before the memory split
└── experiments/
    └── chunk_system.py       # Experimental 2D chunk loader for smoother open-world rendering
```

---

### Script Timeline
- **`game_part1_menus.py`** *(Created July 23, 2023)* : Complete menu engine (New Game, Load Save, Bilingual Settings, Credits, Quit).
- **`game_part2_gameplay.py`** *(Created July 23, 2023)* : Main gameplay loop, pixel-encoded sprites, enemy spawning, shooting mechanics, and collectibles.
- **`history/game_v1_monolithic.py`** *(Created July 23, 2023)* : Initial single-file version combining menus and early gameplay before hitting calculator memory limits.
- **`experiments/chunk_system.py`** *(Created September 09, 2025)* : Experimental chunk-based rendering system that only loads and refreshes the region around the player.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `time`, `random`).
