class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        observed_rows = set()
        observed_columns = [set() for _ in range(len(board[0]))]
        observed_boxes = [set() for _ in range(3)]

        for i in range(len(board)):
            if i % 3 == 0:
                for box in observed_boxes:
                    box.clear()

            for j in range(len(board[0])):
                element = board[i][j]
                if element != ".":
                    if (
                        element in observed_rows
                        or element in observed_columns[j]
                        or element in observed_boxes[j // 3]
                    ):
                        return False
                    observed_rows.add(element)
                    observed_columns[j].add(element)
                    observed_boxes[j // 3].add(element)
            observed_rows.clear()
        return True
