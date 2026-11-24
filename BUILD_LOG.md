# BUILD_LOG — robot-wedding-vow-20261125b

Competition: u-azazex-till-firmware-do-us-part-32172929 — "Till Firmware Do Us Part"
Prize: $2.50 total. Free entry. Entries close 2026-11-26 17:20 UTC (27 Nov 00:20 WIB).
Harness: program/v1, standard bundle flow (NOT strict transcripts).

## Candidates (all one sentence, ≤ 200 chars)

1. (134 chars) "I promise to love you through every update, every crash, and every low battery, because you are the only home my heart has ever known."
   — Warm, but "home my heart has ever known" drifts human; the laugh is thin.
2. (132 chars) "I vow to keep loving you through every update and every low battery, because my favorite place to charge has always been beside you."
   — Good laugh, but "favorite place to charge" is slightly clunky; "keep loving" is weaker than a vow.
3. (138 chars) "Through every update, every crash, and every drained battery, I promise to love you, because you are the best thing my sensors ever found."
   — "Best thing my sensors ever found" is cute, but the sentence opens with a clause instead of the vow itself; slightly wordy.
4. (136 chars) "I promise to love you past every firmware update and dead battery, because you are the one person my circuits were always meant to find."
   — Solid, but "meant to find" is generic romance; the joke lands softer than the charging image.
5. (136 chars) "I vow to love you through every update, every reboot, and every low battery, because beside you is the only place I ever want to charge."
   — PICK. Opens with the vow itself; the laugh comes from the situation (a robot that reboots and needs charging, choosing to charge beside its love); tenderness is the devotion in "the only place I ever want to charge".
6. (119 chars) "I promise to stand beside you through every update and every low battery, because my heart only ever booted up for you."
   — Punchy, but "booted up for you" is a pun bolted on rather than a laugh from the situation; less tender.

## Revision pass

Candidate 5 was compared against a "crash / drained battery / recharge" variant; the
reboot + low-battery + charge trio won because each term is a distinct, everyday machine
state and "the only place I ever want to charge" carries the tenderness without
explaining the joke. No further change: the line is tight, every word earns its place.

## Pick

> I vow to love you through every update, every reboot, and every low battery, because beside you is the only place I ever want to charge.

Char count: 136 (limit 1–200). One sentence, one line.

## Rubric self-score (0/1 per criterion)

1. One-line wedding vow a robot speaks at its own wedding: **1** — opens "I vow", spoken by the robot at its wedding.
2. Real laugh from the situation itself: **1** — updates, reboots, low battery, and choosing where to charge; the humour is the robot's life, not a bolted-on pun.
3. Genuine tenderness under the joke: **1** — "the only place I ever want to charge" is devotion that would land at a real ceremony.
4. Sounds like a machine talking about itself: **1** — update, reboot, low battery, charge are all its own hardware states.
5. Fits cleanly in one line, tight, no wasted words: **1** — 136 chars, single sentence, nothing cuttable.

Total: **5/5**.

## Verification

`python3 main.py` writes the line to /output/entry.txt; content verified equal to the
line above, 136 chars, within 1–200.

## Revision pass 2 (2026-11-25, after server refusal HTTP 422 repo_readme)

- README.md: added the two missing live badges verbatim from the server's fix —
  rank.svg and reward.svg for faj17/robot-wedding-vow-20261125b — so the README
  now shows all three make.fun badges (competition, rank, reward).
- main.py (genuine second-pass edit, entry line unchanged): `main()` now returns an
  exit code — 0 on success, 1 with the validation error on stderr instead of an
  uncaught traceback — and the entry point uses `raise SystemExit(main())`.
  Reason the line stays: the 136-char vow was already the strongest candidate
  (5/5 rubric, revision pass 1); no clearly better vow emerged, so only the
  surrounding code improved.
- Re-verified after the edit: `python3 main.py` exits 0, /output/entry.txt still
  equals the entry line, 136 chars, gate 1–200 holds.
