from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        number_of_tries = 0
        students_queue = deque(students)
        sandwiches = deque(sandwiches)
        while sandwiches:
            if len(students_queue) == number_of_tries:
                break
                
            if students_queue[0] == sandwiches[0]:
                students_queue.popleft()
                sandwiches.popleft()
                number_of_tries = 0
            else:
                students_queue.append(students_queue.popleft())
                number_of_tries += 1

        return len(students_queue)

