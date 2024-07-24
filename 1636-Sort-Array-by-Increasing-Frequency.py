class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Initialize a list of empty lists to store numbers by their frequency
        frequency_buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        # Sort numbers in descending order to adhere to the unique condition:
        ## "If multiple values have the same frequency, sort them in 
        ## decreasing order."
        nums.sort(reverse=True)

        previous_number = nums[0]
        count = 1

        # Count frequencies and populate frequency_buckets
        for num in range(1, len(nums)):
            if nums[num] == previous_number:
                count += 1
            else:
                frequency_buckets[count].append(previous_number)
                previous_number = nums[num]
                count = 1

        # Don't forget to add the last counted number to frequency_buckets
        frequency_buckets[count].append(previous_number)

        # Build the result list based on frequency_buckets
        for frequency, numbers in enumerate(frequency_buckets):
            if numbers:
                for number in numbers:
                    result.extend([number] * frequency)

        return result