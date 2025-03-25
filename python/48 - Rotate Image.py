def rotate(matrix: list[list[int]]) -> None:
    l, r = 0, len(matrix)-1
    while l < r:
        for i in range(r-l): # ensure we won't realocate the already moved elements
            topLeftValue = matrix[l][l+i]
            matrix[l][l+i] = matrix[r-i][l]
            matrix[r-i][l] = matrix[r][r-i]
            matrix[r][r-i] = matrix[l+i][r]
            matrix[l+i][r] = topLeftValue

            # Easier to code first, then adjusted to a better version to improve memory use
            # valueA = matrix[l][l+i] # always get first LINE   element (each for interaction)
            # valueB = matrix[l+i][r] # always get last  COLUMN element (each for interaction)
            # valueC = matrix[r][r-i] # always get last  LINE   element(each for interaction)
            # valueD = matrix[r-i][l] # always get first COLUMN element (each for interaction)

            # matrix[l+i][r] = valueD
            # matrix[l+i][r] = valueA
            # matrix[r][r-i] = valueB
            # matrix[r-i][l] = valueC

            # 0,0 -> 0,1 -> 0,2 -> next interaction -> 1,1
            # 0,3 -> 1,3 -> 2,3 ->  (inner matrix)  -> 1,2
            # 3,3 -> 3,2 -> 3,1 ->                  -> 2,2
            # 3,0 -> 2,0 -> 1,0 ->                  -> 2,1

        r-=1 # moving analysis to the next inner matrix
        l+=1

    return matrix



# it's also possible to pre-calculate the number of matrix interactions instead of using the classic 2 pointers approach:
# def rotate(matrix: list[list[int]]) -> None:
#     interactions = len(matrix[0]) // 2
#     for j in range(interactions):
#         y = len(matrix[0]) -1 -j
#         for i in range(j, y):
#             aux = len(matrix[0]) - i -1
#             topLeftValue = matrix[j][i]
#             matrix[j][i] = matrix[aux][j]
#             matrix[aux][j] = matrix[y][aux]
#             matrix[y][aux] = matrix[i][y]
#             matrix[i][y] = topLeftValue

#             # Easier to code first, then adjusted to a better version to improve memory use
#             # valueA = matrix[j][i]
#             # valueB = matrix[i][y]
#             # valueC = matrix[y][aux]
#             # valueD = matrix[aux][j]
            
#             # matrix[j][i] = valueD
#             # matrix[i][y] = valueA
#             # matrix[y][aux] = valueB
#             # matrix[aux][j] = valueC

#     return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))                            # expected output: [[7,4,1],[8,5,2],[9,6,3]]
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))     # expected output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
