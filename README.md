# Medway 1943

Andy's 1943-inspired game project. The first Scratch version is intended for
CS50 Week 0; a later expansion is intended for the final project.

**Current stage: Week 0 Scratch assignment**, confirmed by Andy on 31 October 2026.
The final-project AI exception does not apply to this initial submission.

## Tools

- `tools/crop_sprites.py` splits a sprite sheet into one transparent PNG per sprite.
  Usage: `python tools/crop_sprites.py sheet.png out_dir` (needs `pip install pillow`).

## Asset credits

- **1943 artwork:** the sheets in Andy's uploaded `Medway images.zip` credit Capcom, *1943: The Battle of Midway* (1987). The original download URL, sheet compiler/ripper and licence were not specified in the supplied archive and still need recording; no CC0/public-domain licence is claimed.
- **Prepared asset pack:** `Medway-1943-transparent-sprites.zip`, delivered separately from this repository. Its `sprites/` folder contains 919 transparent PNG cutouts. Its `backgrounds/` folder contains 97 scenery/tile files, retaining drawn water, sky and terrain. Native pixels were preserved, and the identical Super Ace input sheets were processed once. The archive includes source fingerprints, crop coordinates, previews and an AI-use record.
- **`assets/sprites/planes/`:** "Top Down Planes Sprite Pack" by Unlucky Studio, CC0 (credit not required, given anyway). 24 planes cropped to transparent PNGs by Claude using `tools/crop_sprites.py`.
- Add sources, authors and licences for any additional sprites, sounds and fonts as they are introduced.

## AI use (CS50 academic honesty)

- **Claude (Anthropic):** wrote `tools/crop_sprites.py` and this README template.
- **ChatGPT (OpenAI / Rock):** explained general Scratch concepts (loops, concurrent scripts, conditionals and waits) and suggested starting with a small prototype and expanding it incrementally. Reviewed the repository and CS50's published AI-use rules. On 31 October 2026, wrote and ran a separate asset-preparation process to crop the user-supplied 1943 sprite sheets, remove their lime-green and pink packing backgrounds, preserve native foreground pixels, inspect the crops, and prepare an archive with 919 transparent sprite PNGs, 97 scenery/tile files, previews and crop records. Also updated this disclosure and the asset-credit notes. No game-specific Scratch scripts or game logic were supplied in this work. The preparation code is credited in its own header and included as a preparation record in the delivered archive.

The game's core code and design are my own work.

### Rules for AI help

**Week 0 is the current assessment.** Follow
[CS50x's academic honesty policy](https://cs50.harvard.edu/x/2026/honesty/)
and the [Week 0 assignment](https://cs50.harvard.edu/x/2026/psets/0/).

For the current Week 0 work, ChatGPT and Claude must not suggest or complete
assessment answers or code. Our working boundary is therefore to leave
game-specific Scratch block sequences, implementation plans/pseudocode, code
generation and debugging fixes to Andy and the
[CS50 Duck](https://cs50.ai/). Do not create or edit the assessed game logic
on Andy's behalf. Calling the repository a future final project does not change
the rules for the Week 0 submission.

Repository administration, source/credit records and explanations of general
course material must remain separate from supplying the assessed solution.
The AI-use and asset-credit sections above record assistance already provided;
they are disclosures, not a claim of course approval. The published policy
does not expressly resolve this particular AI-assisted image-cropping workflow.
If its use in the Week 0 submission is uncertain, obtain written clarification
from the course heads as the policy directs.

For the later final project only,
[CS50x's final-project instructions](https://cs50.harvard.edu/x/2026/project/)
permit external AI helpers, provided the essence of the work remains the
student's own. Cite AI use in code comments and keep the contribution record
accurate. Recheck the applicable course rules when that phase begins.
