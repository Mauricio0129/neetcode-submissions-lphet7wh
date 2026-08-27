class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rejections = 0

        while students and rejections < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rejections = 0
            else:
                rejections += 1
                student = students.pop(0)
                students.append(student)

        return len(students)






                

        