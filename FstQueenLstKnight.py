from Queen import queen
from Knight import knight
from Board import board
import pandas as pd
import numpy as np

chess = board(8, 8)
board_size = (8, 8)

data = [['X'] * 8] * 8
df = pd.DataFrame(data)

place_piece = 'Q'
safe_place = chess.copy()
not_safe_place = []
next_place = 1

for pos in safe_place:

    if next_place in range(1,5):

        safe = True
        veri = []

        if df.iloc[pos[0], pos[1]] == 'X':
            atk_pos = queen(pos[0], pos[1], board_size)

            for danger in atk_pos:
                veri.append(df.iloc[danger[0], danger[1]])

            for piece in veri:
                if piece == 'X':
                    safe = True
                elif piece == 'D':
                    safe = True
                else:
                    safe = False
                    break

            if safe == True:
                df.iloc[pos[0], pos[1]] = 'Q'

                for danger in atk_pos:
                    df.iloc[danger[0], danger[1]] = 'D'

                next_place = next_place + 1

    if next_place in range(4, 9):

        safe = True
        veri = []

        if df.iloc[pos[0], pos[1]] == 'X':
            atk_pos = knight(pos[0], pos[1])

            for danger in atk_pos:
                veri.append(df.iloc[danger[0], danger[1]])

            for piece in veri:
                if piece == 'X':
                    safe = True
                elif piece == 'D':
                    safe = True
                else:
                    safe = False
                    break

            if safe == True:
                df.iloc[pos[0], pos[1]] = 'K'

                for danger in atk_pos:
                    df.iloc[danger[0], danger[1]] = 'D'

                next_place = next_place + 1

print(df)