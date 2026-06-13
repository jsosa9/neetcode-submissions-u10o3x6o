class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        sorted from least to greatest 
        and we basicaly have to go through each row and items in each one 
        to see if we find the target

        so we need to go through each sub array insdie the array 

        and we should check the last element in the sub array 

        if its == or greater then the target then we preform binary searhc 
        otherwise we continue to the next row 
        """
        # for x, y in matrix:
        for row in matrix:
            if row[-1] == target:
                return True 
            if row[-1] > target:
                # for val in row:
                l, r = 0, len(row) - 1
                while l <= r: 
                    mid = (l + r) // 2
                    print(row[mid])
                    if row[mid] > target:
                        r = mid - 1
                        print(row[r])
                    elif row[mid] < target:
                        l = mid + 1
                        print(row[l])
                    else:
                        return True
        return False