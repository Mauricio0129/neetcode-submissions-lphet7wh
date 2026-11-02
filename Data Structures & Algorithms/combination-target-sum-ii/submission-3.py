class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = [0 for _ in range(0 , 51)]

        for num in candidates:
            count[num] += 1
        
        working_list = []
        
        for index, val in enumerate(count):
            for _ in range(val):
                working_list.append(index)

        return self.helper(0, [], [], working_list, target)

    def helper(self, starting_index, current_collection, res, options, target):
        # 1. O(1) base cases checking the remaining target directly
        if target == 0:
            res.append(current_collection.copy())
            return
        elif target < 0:
            return 
        
        for i in range(starting_index, len(options)):
            # 2. Your NO-then-YES duplicate trap
            if i > starting_index and options[i] == options[i - 1]:
                continue
                
            # 3. EARLY STOPPING: If this number overshoots, the rest will too
            if options[i] > target:
                break
                
            # 4. Standard backtracking, subtracting from the target on the way down
            current_collection.append(options[i])
            self.helper(i + 1, current_collection, res, options, target - options[i])
            current_collection.pop()  
            
        return res