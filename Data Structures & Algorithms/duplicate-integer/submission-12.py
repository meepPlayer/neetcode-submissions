class Solution:
    # returns true if duplicate exists
    def hasDuplicate(self, nums: List[int]) -> bool:
        # tracks whether duplicate is detected
        visited = set()

        # iterates through all elements
        for item in nums:
            # checks if number has been visited before
            if item in visited:
                return True

            # updates visited hashset
            visited.add(item)

        # returns false if no duplicate found
        return False