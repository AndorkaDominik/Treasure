# Treasure Island Game

This is a simple text-based adventure game where the player makes choices to find the treasure.

## How to Play

1. Run the game script.
2. Follow the prompts and make your choices by typing the indicated letters.

## Game Flow

- **Initial Choice:** Choose between two paths, left (L) or right (R).
  - **Left Path:** Leads to a lake.
    - **Lake Choice:** Choose to swim (S) or wait for a boat (W).
      - **Wait for Boat:** Leads to a house with three doors.
        - **Door Choice:** Choose between blue (B), red (R), or yellow (Y) doors.
          - **Blue Door:** Eaten by cannibals. Game over.
          - **Red Door:** Found treasure guarded by dragons. Game over.
          - **Yellow Door:** Starved to death. Game over.
      - **Swim:** Stung by a poisonous jellyfish. Game over.
  - **Right Path:** Fall into a hole. Game over.
