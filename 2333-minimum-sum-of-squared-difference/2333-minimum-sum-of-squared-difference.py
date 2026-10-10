# Allows subtracting to the largest value of the sorted array in O(1), even
# with repeated values. Does not allow values initially equal to zero.
# Note: values inside the prefix are not updated except for the first one,
#       which serves as representative to the rest.
class PrefixArray:
    def __init__(self, array: List[int]):
        assert array
        assert array[-1] != 0
        self._array = array
        self._prefixLimit = self._findRightMostOccurrenceOfStartValue(0)

    def allZeros(self) -> bool:
        ret = (self._array[0] == 0)
        # if the first element (largest one) is 0 and we consider only non-negative values,
        # then the prefix must span the whole array.
        assert not ret or self._isAllPrefix()
        return ret 

    # How many unit operation in values so that the largest value reaches the second
    # larges value.
    def countModificationsToExpandPrefix(self) -> int:
        if self._isAllPrefix():
            return self._array[0] * (self._prefixLimit + 1)
        return (self._array[0] - self._array[self._prefixLimit + 1]) * (self._prefixLimit + 1) 

    def evaluateSquaredDifferenceInPartialExpansion(self, k: int) -> int:
        # The prefix cannot be expanded as a whole. Let's break up into the number
        # of modifications we can do in the whole prefix and the number of operations
        # we only can do in part of the prefix.
        modificationsOnWholePrefix = k // (self._prefixLimit + 1)
        nDiffsWithExtraModification = k % (self._prefixLimit + 1)
        nDiffsWithSimpleModification = (self._prefixLimit + 1) - nDiffsWithExtraModification
        # So there will be nDiffsWithSimpleModification diffs with value
        # array[0]-modificationsOnWholePrefix...
        sPrefix = nDiffsWithSimpleModification*(self._array[0]-modificationsOnWholePrefix)**2
        # ...and nDiffsWithExtraModification diffs with value
        # array[0]-modificationsOnWholePrefix-1
        sPrefix += nDiffsWithExtraModification*(self._array[0]-modificationsOnWholePrefix-1)**2
        
        sSuffix = 0
        for i in range(self._prefixLimit+1, len(self._array)):
            sSuffix += self._array[i] ** 2
        
        return sPrefix + sSuffix

    def expandPrefixToSecondLargest(self):
        if self._isAllPrefix():
            self._array[0] = 0
            return

        secondLargest = self._array[self._prefixLimit+1]
        self._array[0] = secondLargest
        self._prefixLimit = self._findRightMostOccurrenceOfStartValue(self._prefixLimit+1)

    def _isAllPrefix(self) -> bool:
        return self._prefixLimit == len(self._array)-1

    # Requires self._array[startIndex:] to be sorted, that is, it must not belong to
    # the prefix.
    def _findRightMostOccurrenceOfStartValue(self, startIndex: int) -> int:
        value = self._array[startIndex]
        endIndex = len(self._array)-1
        while startIndex < endIndex:
            mid = (startIndex + endIndex + 1) // 2
            if (self._array[mid] == value):
                startIndex = mid
            else:
                endIndex = mid-1
        return startIndex

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = [abs(nums1[i] - nums2[i]) for i in range(len(nums1)) if nums1[i] != nums2[i]]
        diffs.sort(reverse=True)
        k = k1+k2

        if not diffs:
            return 0
        
        prefixDiffs = PrefixArray(diffs)
        while not prefixDiffs.allZeros():
            # How many unit operation in values so that the largest value reaches the second
            # largest value.
            k0 = prefixDiffs.countModificationsToExpandPrefix()
            if k0 > k:
                return prefixDiffs.evaluateSquaredDifferenceInPartialExpansion(k)
            k -= k0
            prefixDiffs.expandPrefixToSecondLargest()

        return 0