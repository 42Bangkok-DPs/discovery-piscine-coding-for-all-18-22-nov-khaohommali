def parse_board(board_string):
    """แปลงกระดานจากข้อความหลายบรรทัดเป็น 2D list"""
    # Remove extra spaces and handle proper trimming for each row
    board = [row.strip().split() for row in board_string.strip().split("\n")]
    return board

def print_board(board):
    """แสดงกระดานในรูปแบบที่อ่านง่าย"""
    for row in board:
        print(" ".join(row))

def is_under_attack(board, row, col):
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # แนวตรง
        (-1, -1), (-1, 1), (1, -1), (1, 1) # แนวทแยง
    ]

    # ตรวจสอบการโจมตีจากเรือ (rook) และควีน (queen) แนวตรง
    for dx, dy in directions[:4]:
        x, y = row + dx, col + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] != ".":
                if board[x][y] in ("r", "q"):  # ตัวเรือหรือควีน (ฝ่ายตรงข้าม)
                    return True
                break
            x += dx
            y += dy

    # ตรวจสอบการโจมตีจากบิชอป (bishop) และควีน (queen) แนวทแยง
    for dx, dy in directions[4:]:
        x, y = row + dx, col + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] != ".":
                if board[x][y] in ("b", "q"):  # ตัวบิชอปหรือควีน (ฝ่ายตรงข้าม)
                    return True
                break
            x += dx
            y += dy

    # ตรวจสอบการโจมตีจากม้า (knight)
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    for dx, dy in knight_moves:
        x, y = row + dx, col + dy
        if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == "n":  # ม้า
            return True

    # ตรวจสอบการโจมตีจากเบี้ย (pawn)
    pawn_moves = [(-1, -1), (-1, 1)]  # ทิศทางเบี้ย (เฉพาะฝ่ายล่าง)
    for dx, dy in pawn_moves:
        x, y = row + dx, col + dy
        if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == "p":  # เบี้ย
            return True

    return False

def find_king(board):
    """หาตำแหน่งกษัตริย์ (K)"""
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "K":  # กษัตริย์ของคุณ
                return row, col
    return -1, -1  # กรณีหาไม่เจอ

def checkmate(board):
    """ตรวจสอบว่ากษัตริย์ถูกโจมตีทุกทางหรือไม่ (Checkmate)"""
    
    # ตรวจสอบว่ากระดานเป็นขนาด 8x8
    if len(board) != 8 or any(len(row) != 8 for row in board):
        return "Invalid board size."  # Simply return a message, no detailed error

    king_row, king_col = find_king(board)
    
    if king_row == -1 or king_col == -1:
        return "King not found on the board."
    
    # ตรวจสอบทุกตำแหน่งรอบ ๆ กษัตริย์
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row, new_col = king_row + i, king_col + j
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # ต้องอยู่ในกระดาน
                if not is_under_attack(board, new_row, new_col):
                    return "The king is not in checkmate."  # มีช่องที่ปลอดภัยอยู่
    return "Checkmate! The king has no safe moves."

def main():
    # กระดานตัวอย่างจากภาพหลายๆ ตาราง
    board_strings = [
        """
r . . . . . . r
p p p . . . . p
. . . . . . . .
. . . k . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
""",
        """
r . . . . . . r
p p p p . . . p
. . . . . . . .
. . . . k . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
""",
        """
. . . . . . . .
. . . p . . . .
. . . . k . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
""",
        """
r . . . . . . r
. . p . p . . .
. . . . . . . .
. . . k . . . .
. . . . . . . .
P . . . . P P P
R N B Q K B N R
""",
        """
. . . . . . . .
. . p p p . . .
. . . . k . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
"""
    ]
    
    # Loop through all the boards and check for checkmate
    for index, board_string in enumerate(board_strings):
        print(f"\n--- Board {index + 1} ---")
        board = parse_board(board_string)  # แปลงกระดาน
        print_board(board)

        # ตรวจสอบสถานะ Checkmate
        result = checkmate(board)
        print(result)

if __name__ == "__main__":
    main()
