# 🕹️ 2D-Game

An ambitious, multi-week **top-down 2D pixel-art action & shooter engine** built in MicroPython for the **NumWorks** graphing calculator.

Designed around a custom sprite decoder, camera-scrolling world, multi-tier enemy AI, hit-stun & regeneration mechanics, a shrink/grow traversal system, achievements, live statistics, and a password-based checkpoint system — all heavily compressed to fit within the NumWorks' strict RAM and flash limits.

---

## 📂 Repository Structure

```
2D-Game/
├── game_part2_gameplay.py      # Showcase: Core 2D engine, AI, combat, sprites & mechanics
├── game_part1_menus.py         # Full bilingual (FR/EN) menus, difficulty, stats, achievements & saves
├── ai_difficulty_balancing.csv # Full spreadsheet of AI & combat balancing across all 5 difficulties
├── history/
│   └── game_v1_monolithic.py   # Early all-in-one v1 prototype before the memory split
└── experiments/
    └── chunk_system.py         # Experimental 2D open-world chunk loader
```

---

## 🌟 Core Gameplay & Engine Features (`game_part2_gameplay.py`)

### 1. Multi-Tier Enemy AI & Combat Mechanics
- **5 Difficulty Modes** (`Peaceful`, `Easy`, `Intermediate`, `Hard`, `Hardcore`) dynamically scaling enemy HP, damage, firing rate, count, hit-stun, regeneration, and movement intelligence.
- **Adaptive Aiming (`c_a`)**:
  - *Peaceful / Easy*: Cardinal directions (`0°`, `90°`, `180°`, `270°`) with increasing player tracking.
  - *Intermediate*: Full cardinal tracking toward the player.
  - *Hard / Hardcore*: Full **360° trigonometric targeting** (`atan2`) aiming directly at the player's center.
- **Positioning & Aggro (`c_pos`)**:
  - Enemies wander within arena bounds, keep optimal combat distance (`hrng=100`, `vrng=80`) in higher difficulties, and alert nearby allies within a `200px` radius when attacked.
  - *Hardcore* was designed with **bullet-dodging AI** and adaptive speed (partially commented out in the standalone script due to calculator RAM constraints).
- **Hit-Stun & Regeneration**: Both player and enemies experience brief stun lockouts on hit (`st` / `ste`) and periodic HP regeneration (`c_v`) every 5 seconds.

### 2. Size-Shifting Traversal Mechanic (`change_t`)
- The player can **shrink** from normal scale (`2×`) down to mini scale (`1×`, halving movement step from `20px` to `10px`).
- Shrinking automatically triggers when approaching narrow paths (`chemin`), allowing access to secret/cave areas that are otherwise impassable at full size, or can be toggled manually.

### 3. Custom Pixel-Art & Rotated Projectiles
- **Encoded Sprite Engine**: Characters (`toad`, `minion`), obstacles (`rocher`), impact sparks (`touche`), directional aim arrows (`fleche`), and projectiles are stored as compact string-encoded pixel matrices, decoded at startup and immediately freed (`del`) from RAM.
- **Dynamic Projectile Rasterizer (`draw_b`)**: Supports arbitrary-angle projectile rotation using `cos`/`sin` matrix transforms for `Hard` and `Hardcore` 360° enemy shots.

### 4. Password-Based Checkpoint System, Achievements & Stats (Part 1 ↔ Part 2 Bridge)
Because NumWorks MicroPython cannot write persistent save files to flash during execution, this game implements a clever workaround:
- **Checkpoint Passwords (`cp` / `cb`)**: Reaching a checkpoint zone (such as the Cave) generates a unique **6-character checkpoint password** on screen. Entering that password in **Part 1 (`Load a save point`)** restores your position and lets you resume directly from that zone.
- **Achievements (`success` / `sb`)**: Real-time achievement popups (e.g., *"Kill an enemy"*, *"Get smaller"*) tracked persistently across runs in Part 1.
- **Live Statistics (`stats`)**: Tracks shots fired, hits landed (accuracy %), HP regenerated, damage taken, and enemies defeated — viewable in Part 1's Statistics menu.

*(Note: In standalone `game_part2_gameplay.py`, the Part 1 bridge hooks for `stats`, `success`, and `cp` are commented out so the gameplay script can run independently.)*

### 5. Aggressive Memory & Code-Size Optimization
To squeeze a full 2D engine onto calculator hardware:
- Originally **319 lines (10.6 KB)** → compressed down to **211 lines (9.04 KB)** → expanded with difficulty tiers, stats, achievements, and checkpoints to **399 lines (~14 KB)**.
- Uses single-line `lambda` helpers, inline list comprehensions, short identifiers, immediate `del` of temporary sprite strings, and splits the **22.9 KB menu system** (`game_part1_menus.py`) from the **14.5 KB gameplay engine** (`game_part2_gameplay.py`).

---

## 📊 AI & Difficulty Balancing Matrix

Full dataset available in [`ai_difficulty_balancing.csv`](ai_difficulty_balancing.csv):

| Difficulty | Player Cooldown | Player Dmg | Enemy Cooldown | Enemy Dmg | Enemy HP | Enemies | Player Regen | Player Stun | Enemy Stun | Enemy Regen | Vertical / Horizontal AI |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Peaceful** | None | `35–45` | `5.0s` | `5–15` | `40–70` | `1` | `10–15` | None | `1.0–2.0s` | None | Random (tiny) / Disabled |
| **Easy** | `0.5s` | `25–35` | `3.0s` | `10–20` | `60–100` | `1` | `5–10` | `0.1–0.4s` | `0.5–1.5s` | None | Random (small) / Random (tiny) |
| **Intermediate** | `1.0s` | `15–25` | `2.0s` | `15–25` | `80–120` | `1` | `3–7` | `0.3–0.7s` | `0.5–1.0s` | None | Random (medium) / Random (small) |
| **Hard** | `1.5s` | `10–20` | `1.5s` | `25–35` | `100–150` | `2` | `1–4` | `0.5–1.0s` | `0.3–0.7s` | `1–4` | Keeps distance in range / Random (medium) |
| **Hardcore** | `2.5s` | `5–15` | `0.5s` | `35–45` | `130–170` | `3` | `0–1` | `0.5–2.0s` | `0.1–0.3s` | `3–7` | Bullet-dodging, range-keeping, adaptive speed |

---

## ⌨️ Controls (`game_part2_gameplay.py`)

- **Directional Arrows (`0`–`3`)** : Move player (and orient aim direction when unlocked).
- **OK / EXE** *(Key `4` on NumWorks / `52` on PC emulator)* : Fire projectile.
- **Shift** *(Key `12`)* : Toggle **Aim Lock** (`mf`) — lets you strafe/move without changing your shooting direction.
- **Clear** *(Key `17`)* : Manually toggle **Shrink / Grow** size.
- **Backspace** *(Key `16`)* : Open Options menu *(requires Part 1 merged)*.

---

## ⚙️ Performance Tuning (Physical Hardware)

If you experience low framerates on a physical NumWorks calculator, you can trade projectile visual fidelity for speed directly in `game_part2_gameplay.py`:
- **Line `140`** (`ls(x+ax,y+ay,t,d,color)` inside `draw()`): Switching the projectile renderer to call `ls` directly (bypassing the 4-corner border pass in `draw`) significantly boosts FPS, at the cost of small gaps in rotated bullets.
- **Lines `132–133`** (`for a in range(t): for b in range(t):` inside `ls()`): Adding `-1` to `t` (`range(t-1)`) reduces the number of `fill_rect` calls per projectile pixel for an even faster framerate, making bullets slightly thinner/more perforated.

---

## ⚠️ Project Notes & Limitations

- **Split Architecture**: Part 1 (`game_part1_menus.py`, *Created July 23, 2023*) and Part 2 (`game_part2_gameplay.py`, *Created July 23, 2023*) were separated due to NumWorks storage constraints; `history/game_v1_monolithic.py` (*Created July 23, 2023*) preserves the original combined prototype.
- **Minimal Storyline**: Despite the full RPG/action menu suite (save system, settings, achievements, stats, credits), the narrative is **very short and minimal** — enemies spawn for combat without an underlying story explaining why you are fighting them.
- **Potential Bugs**: Due to the complexity of the engine and aggressive code compression, some edge-case bugs or visual glitches may still exist.
- **Experiments**: `experiments/chunk_system.py` (*Created September 09, 2025*) is an experimental chunk-based rendering engine built to load only the area around the player for smoother 2D open-world exploration.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `math`, `time`, `random`).
- Runs on physical NumWorks calculators (N0110 / N0120) and web/PC emulators (adjust `KEY[0]` between `4` for calculator and `52` for PC).
