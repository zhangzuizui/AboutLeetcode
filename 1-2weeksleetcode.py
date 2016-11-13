# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:23:10 2016

@author: zxn
"""
#27
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = 0
        LEN = len(nums)
        i = 0
        while i < LEN:
            if nums[i] != val:
                result += 1
                i += 1
            else:
                nums.pop(i)
                LEN -= 1
        return result

#414
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = []
        for x in nums:
            if x not in L:
                if len(L) == 0:
                    L.append(x)
                else:
                    flag = 0
                    for y in range(len(L)):
                        if x > L[y]:
                            L.insert(y, x)
                            flag = 1
                            break
                    if flag == 0:
                        L.append(x)
                            
                if len(L) == 4:
                    L.pop(3)
                
        if len(L) <= 2:
            return L[0]
        else:
            return L[2]

#118
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        base = [1]
        L = [base]
        for i in range(numRows):
            if i == 0:
                continue
            else:
                flag1 = -1
                flag2 = 0
                newL = []
                while flag1 < len(L[i-1]):
                    if flag1 == -1:
                        newL.append(L[i-1][flag2])
                        flag1 += 1
                        flag2 += 1
                    elif flag1 == len(L[i-1])-1:
                        newL.append(L[i-1][flag1])
                        flag1 += 1
                        flag2 += 1
                    else:
                        newL.append(L[i-1][flag1] + L[i-1][flag2])
                        flag1 += 1
                        flag2 += 1
                L.append(newL)
        return L
#119
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        base = [1]
        for i in range(rowIndex+1):
            if i == 0:
                continue
            else:
                flag1 = -1
                flag2 = 0
                L = []
                while flag1 < len(base):
                    if flag1 == -1:
                        L.append(base[flag2])
                        flag1 += 1
                        flag2 += 1
                    elif flag1 == len(base)-1:
                        L.append(base[flag1])
                        flag1 += 1
                        flag2 += 2
                    else:
                        L.append(base[flag1] + base[flag2])
                        flag1 += 1
                        flag2 += 1
                base = L
        return base
#64
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column = len(grid[0])  
        row = len(grid)
        minsumpre = []
        for i in range(len(grid[0])):
            if i == 0:
                minsumpre.append(grid[0][0])
            else:
                minsumpre.append(minsumpre[i-1]+grid[0][i])
        
        minsumnext = minsumpre[:]
        for i in range(len(grid)):
            if i == 0:
                continue
            
            else:
                minsumpre = minsumnext[:]
                temp = []
                for j in range(len(minsumpre)):
                    if j == 0:
                        temp.append(minsumpre[j]+grid[i][j])
                    else:
                        if minsumpre[j]+grid[i][j] > temp[j-1]+grid[i][j]:
                            temp.append(temp[j-1]+grid[i][j])
                        else:
                            temp.append(minsumpre[j]+grid[i][j])
                minsumnext = temp[:]
        return minsumnext[column-1]

#1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Dict = {}
        Dict2 = {}
        for i in range(len(nums)):
            if nums[i] not in Dict:
                Dict[nums[i]] = i
            else:
                Dict2[nums[i]] = i
        
        
        for key in Dict:
            if (target - key == key) & (key in Dict2):
                return [Dict[key], Dict2[key]]
            elif (target - key in Dict) & (target - key != key):
                return [Dict[key], Dict[target - key]]
#15
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i!=0 and nums[i-1] == nums[i]: 
                continue
            target, Dict, begin = 0-nums[i], {}, i+1
            while begin < len(nums):
                if nums[begin] in Dict:
                    result.append([nums[i], target-nums[begin], nums[begin]])
                    if begin < len(nums)-1 and nums[begin] == nums[begin+1]:
                        begin += 1
                Dict[target-nums[begin]] = nums[begin]
                begin += 1
        return result
#16
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[2] 
        nums.sort()
        for i in range(len(nums)):
            if i!=0 and nums[i-1] == nums[i]: 
                continue
            low = i+1
            high = len(nums)-1
            while low < high:
                if abs(result - target) > abs(nums[i] + nums[low] + nums[high] - target):
                    result = nums[i] + nums[low] + nums[high]
                if nums[i] + nums[low] + nums[high] > target:
                    high -= 1
                elif nums[i] + nums[low] + nums[high] < target:
                    low += 1
                else:
                    return target
                        
                
        return result

#26
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)