# Medway 1943

CS50 final project (due July 2027) by Andy.

## Tools

- `tools/crop_sprites.py` splits a sprite sheet into one transparent PNG per sprite.
  Usage: `python tools/crop_sprites.py sheet.png out_dir` (needs `pip install pillow`).

## Asset credits

- **1943 artwork:** the sheets in Andy's uploaded `Medway images.zip` credit Capcom, *1943: The Battle of Midway* (1987). The original download URL, sheet compiler/ripper and licence were not specified in the supplied archive and still need recording; no CC0/public-domain licence is claimed.
- **Prepared asset pack:** `Medway-1943-transparent-sprites.zip`, delivered separately from this repository. Its `sprites/` folder contains 919 transparent PNG cutouts. Its `backgrounds/` folder contains 97 scenery/tile files, retaining drawn water, sky and terrain. Native pixels were preserved, and the identical Super Ace input sheets were processed once. The archive includes source fingerprints, crop coordinates, previews and an AI-use record.
- Add sources, authors and licences for any additional sprites, sounds and fonts as they are introduced.

## AI use (CS50 academic honesty)

- **Claude (Anthropic):** wrote `tools/crop_sprites.py` and this README template.
- **ChatGPT (OpenAI / Rock):** explained general Scratch concepts (loops, concurrent scripts, conditionals and waits) and suggested starting with a small prototype and expanding it incrementally. Reviewed the repository and CS50's published AI-use rules. On 31 October 2026, wrote and ran a separate asset-preparation process to crop the user-supplied 1943 sprite sheets, remove their lime-green and pink packing backgrounds, preserve native foreground pixels, inspect the crops, and prepare an archive with 919 transparent sprite PNGs, 97 scenery/tile files, previews and crop records. Also updated this disclosure and the asset-credit notes. No game-specific Scratch scripts or game logic were supplied in this work. The preparation code is credited in its own header and included as a preparation record in the delivered archive.

The game's core code and design are my own work.

### Rules for AI help

[CS50x's final-project instructions](https://cs50.harvard.edu/x/2026/project/)
explicitly permit external AI helpers for the final project, provided the essence
of the work remains the student's own. Cite any AI use in code comments as the
course requires, and keep the contributions recorded above accurate as work
continues. The final-project exception does not apply to the Week 0 Scratch
assignment or other problem sets; use the
[CS50 Duck](https://cs50.ai/) for assignment-specific AI help.
