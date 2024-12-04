"""
This module contains the logic for animating a DNA double-helix using ASCII art.
The animation alternates between two rows of the DNA,
with random bases (A, T, C, G) used in the animation.
Note:
    The animation runs in an infinite loop until
    manually interrupted (e.g., by pressing Ctrl+C).
"""

import random
import time

# Rows for DNA animation. Each string represents a row of the helix.
ROWS = [
    "         ##",
    "        #{}-{}#",
    "       #{}---{}#",
    "      #{}-----{}#",
    "     #{}------{}#",
    "    #{}------{}#",
    "    #{}-----{}#",
    "     #{}---{}#",
    "     #{}-{}#",
    "      ##",
    "     #{}-{}#",
    "     #{}---{}#",
    "    #{}-----{}#",
    "    #{}------{}#",
    "     #{}------{}#",
    "      #{}-----{}#",
    "       #{}---{}#",
    "        #{}-{}#"
]


def animate_dna(pause: float):
    """
    Animates the DNA by replacing placeholders in the ROWS.

    Args:
        pause (float): Time to pause between frames in seconds.
    """
    while True:
        # Generate random DNA bases for the animation
        row_1 = random.choice(['A', 'T'])
        row_2 = random.choice(['C', 'G'])

        # Create the animated rows
        animation_rows = []
        for row in ROWS:
            # Insert the random DNA bases into the row template
            animation_rows.append(row.format(row_1, row_2))

        # Clear the screen and print the new frame
        print("\033[H\033[J", end="")  # Clear the screen (ANSI escape codes)
        print("\n".join(animation_rows))

        # Pause before the next frame
        time.sleep(pause)
