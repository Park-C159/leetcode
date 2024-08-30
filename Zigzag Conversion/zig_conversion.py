def convert(s: str, numRows: int) -> str:
    if numRows >= len(s) or numRows == 1:
        return s

    rows = [''] * numRows
    cur_row = 0
    going_down = False
    for c in s:
        rows[cur_row] += c
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down
        cur_row += 1 if going_down else -1
    return ''.join(rows)