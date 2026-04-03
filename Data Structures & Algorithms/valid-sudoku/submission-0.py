class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_of_row_sets = [set() for _ in range(9)]
        list_of_col_sets = [set() for _ in range(9)]
        list_of_sub_box_sets = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    # Row check
                    if board[i][j] in list_of_row_sets[i]:
                        print("Triggered row")
                        return False
                    else:
                        list_of_row_sets[i].add(board[i][j])
                        print(list_of_row_sets[i])
                    # Col Check
                    if board[i][j] in list_of_col_sets[j]:
                        print("Triggered col")
                        return False
                    else:
                        list_of_col_sets[j].add(board[i][j])
                    # Sub boxes check
                    sub_box_idx = (i // 3) * 3 + (j // 3)
                    print(sub_box_idx)
                    if board[i][j] in list_of_sub_box_sets[sub_box_idx]:
                        print("Triggered sub box")
                        return False
                    else:
                        list_of_sub_box_sets[sub_box_idx].add(board[i][j]) 
        
        return True

                    

            
        