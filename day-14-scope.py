class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        maxElement=max(self.__elements)
        minElement=min(self.__elements)
        self.maximumDifference=abs(maxElement - minElement)
# End of Difference class
