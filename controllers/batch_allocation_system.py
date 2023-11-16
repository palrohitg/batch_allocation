from student import Student
from admin import Admin
from batch import Batch

class BatchAllocationSystem:
    def __init__(self):
        self.students = []
        self.admins = []
        self.batches = []

    def register_student(self, name, gender):
        student = Student(name, gender, "Student")
        self.students.append(student)
        return student

    def register_admin(self, name, gender):
        admin = Admin(name, gender, "Admin")
        self.admins.append(admin)
        return admin

    def create_batch(self, admin, capacity, stream, timing):
        if admin in self.admins:
            batch = Batch(capacity, stream, timing)
            self.batches.append(batch)
            return batch
        else:
            return None

    def enroll_student(self, student, stream):
        if student in self.students:
            if student.stream_enrolled is None:
                student.stream_enrolled = stream
                return True
            else:
                return False

    def allocate_batch(self, admin, student, criteria):
        if admin in self.admins and student in self.students:
            if criteria == "Gender Based" and student.gender == "Female":
                sorted_batches = sorted(self.batches, key=lambda x: (x.timing, x.capacity), reverse=True)
                for batch in sorted_batches:
                    if batch.stream == student.stream_enrolled and len(batch.students) < batch.capacity:
                        batch.students.append(student)
                        return batch
                return None
            elif criteria == "Higher capacity":
                sorted_batches = sorted(self.batches, key=lambda x: x.capacity, reverse=True)
                for batch in sorted_batches:
                    if batch.stream == student.stream_enrolled and len(batch.students) < batch.capacity:
                        batch.students.append(student)
                        return batch
                return None
        else:
            return None

    def display_student_with_batch(self):
        for batch in self.batches:
            print(batch.stream)
            print(batch.timing)
            for student in batch.students:
                print(student.name)


# Sample usage
system = BatchAllocationSystem()

student1 = system.register_student("Akhilesh", "Male")
student2 = system.register_student("Komal", "Female")
student3 = system.register_student("Rajnish", "Male")
student4 = system.register_student("Mayuri", "Female")

admin1 = system.register_admin("Kamesh", "Male")
admin2 = system.register_admin("M", "Male")

batch1 = system.create_batch(admin1, 3, "IIT", "Morning")
batch2 = system.create_batch(admin1, 2, "NEET", "Evening")
batch3 = system.create_batch(admin1, 3, "IIT", "Evening")

system.enroll_student(student1, "IIT")
system.enroll_student(student2, "IIT")
system.enroll_student(student3, "NEET")
system.enroll_student(student4, "IIT")

system.allocate_batch(admin2, student2, "Gender Based")
system.allocate_batch(admin2, student4, "Higher capacity")
system.allocate_batch(admin1, student1, "Higher capacity")
system.allocate_batch(admin1, student3, "Higher capacity")
system.display_student_with_batch()