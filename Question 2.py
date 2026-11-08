# ------------------------------------------------------------
# 1. Course Entity Class
# ------------------------------------------------------------

class Course:
    def __init__(self, course_code, course_name,
                 credit_hours, level, description):

        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.level = level
        self.description = description

    def display(self):

        print("\n===== COURSE DETAILS =====")
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credit Hours:", self.credit_hours)
        print("Course Level:", self.level)
        print("Description:", self.description)


# ------------------------------------------------------------
# 2. Generic Directed Graph Class
# ------------------------------------------------------------

class Graph:
    def __init__(self):
        # Dictionary stores vertices and outgoing edges
        self.adjacency_list = {}

    # Add a new vertex
    def addVertex(self, vertex):

        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True

        return False

    # Add a directed edge from source to destination
    def addEdge(self, source, destination):

        if source not in self.adjacency_list:
            print("Source vertex does not exist.")
            return False

        if destination not in self.adjacency_list:
            print("Destination vertex does not exist.")
            return False

        if source == destination:
            print("A course cannot be its own prerequisite.")
            return False

        if destination in self.adjacency_list[source]:
            print("This prerequisite already exists.")
            return False

        self.adjacency_list[source].append(destination)
        return True

    # List all incoming adjacent vertices
    def listIncomingAdjacentVertex(self, vertex):

        incoming_vertices = []

        if vertex not in self.adjacency_list:
            return incoming_vertices

        for source in self.adjacency_list:

            if vertex in self.adjacency_list[source]:
                incoming_vertices.append(source)

        return incoming_vertices

    # List all outgoing adjacent vertices
    def listOutgoingAdjacentVertex(self, vertex):

        if vertex not in self.adjacency_list:
            return []

        return self.adjacency_list[vertex]

    # Remove a directed edge
    def removeEdge(self, source, destination):

        if source not in self.adjacency_list:
            return False

        if destination not in self.adjacency_list[source]:
            return False

        self.adjacency_list[source].remove(destination)
        return True


# ------------------------------------------------------------
# 3. Course Data
# ------------------------------------------------------------

def create_courses():

    courses = {

        "CS101": Course(
            "CS101",
            "Introduction to Programming",
            3,
            "Core",
            "Introduces fundamental programming concepts."
        ),

        "CS201": Course(
            "CS201",
            "Data Structures",
            3,
            "Core",
            "Introduces arrays, linked lists, stacks and queues."
        ),

        "CS301": Course(
            "CS301",
            "Algorithms",
            4,
            "Core",
            "Covers searching, sorting and algorithm analysis."
        ),

        "CS302": Course(
            "CS302",
            "Database Systems",
            3,
            "Core",
            "Introduces database design and SQL."
        ),

        "CS401": Course(
            "CS401",
            "Software Engineering",
            3,
            "Elective",
            "Covers software development principles."
        ),

        "CS402": Course(
            "CS402",
            "Artificial Intelligence",
            3,
            "Elective",
            "Introduces artificial intelligence concepts."
        )
    }

    return courses


# ------------------------------------------------------------
# 4. Display All Courses
# ------------------------------------------------------------

def display_all_courses(courses):

    print("\n===== AVAILABLE COURSES =====")

    for course_code in courses:
        course = courses[course_code]

        print(course.course_code, "-", course.course_name)


# ------------------------------------------------------------
# 5. View Course Details
# ------------------------------------------------------------

def view_course_details(courses):

    course_code = input("Enter Course Code: ").strip().upper()

    if course_code in courses:
        courses[course_code].display()
    else:
        print("Course not found.")


# ------------------------------------------------------------
# 6. View Prerequisite Courses
# ------------------------------------------------------------

def view_prerequisites(graph, courses):

    course_code = input("Enter Course Code: ").strip().upper()

    if course_code not in courses:
        print("Course not found.")
        return

    prerequisites = graph.listIncomingAdjacentVertex(course_code)

    print("\nPrerequisites for", course_code,
          "-", courses[course_code].course_name)

    if len(prerequisites) == 0:
        print("No prerequisite courses.")
    else:
        for code in prerequisites:
            print("-", code, "(", courses[code].course_name, ")")


# ------------------------------------------------------------
# 7. View Courses Unlocked
# ------------------------------------------------------------

def view_unlocked_courses(graph, courses):

    course_code = input("Enter Course Code: ").strip().upper()

    if course_code not in courses:
        print("Course not found.")
        return

    unlocked = graph.listOutgoingAdjacentVertex(course_code)

    print("\nCourses unlocked by", course_code,
          "-", courses[course_code].course_name)

    if len(unlocked) == 0:
        print("This course does not unlock any courses.")
    else:
        for code in unlocked:
            print("-", code, "(", courses[code].course_name, ")")


# ------------------------------------------------------------
# 8. Add Course (Advanced Feature)
# ------------------------------------------------------------

def add_course(graph, courses):

    course_code = input("Enter New Course Code: ").strip().upper()

    if course_code == "":
        print("Course code cannot be empty.")
        return

    if course_code in courses:
        print("Course already exists.")
        return

    course_name = input("Enter Course Name: ").strip()

    try:
        credit_hours = int(input("Enter Credit Hours: "))

        if credit_hours <= 0:
            print("Credit hours must be positive.")
            return

    except ValueError:
        print("Invalid credit hours.")
        return

    level = input("Enter Level (Core/Elective): ").strip().capitalize()

    if level not in ["Core", "Elective"]:
        print("Invalid course level.")
        return

    description = input("Enter Course Description: ").strip()

    course = Course(
        course_code,
        course_name,
        credit_hours,
        level,
        description
    )

    courses[course_code] = course
    graph.addVertex(course_code)

    print("New course added successfully.")


# ------------------------------------------------------------
# 9. Add Prerequisite (Advanced Feature)
# ------------------------------------------------------------

def add_prerequisite(graph, courses):

    print("\nEnter the course that requires a prerequisite.")

    destination = input("Course Code: ").strip().upper()

    source = input("Prerequisite Course Code: ").strip().upper()

    if source not in courses or destination not in courses:
        print("One or both courses do not exist.")
        return

    if graph.addEdge(source, destination):
        print("Prerequisite added successfully.")


# ------------------------------------------------------------
# 10. Remove Prerequisite (Advanced Feature)
# ------------------------------------------------------------

def remove_prerequisite(graph, courses):

    print("\nEnter the course whose prerequisite you want to remove.")

    destination = input("Course Code: ").strip().upper()

    source = input("Prerequisite Course Code to remove: ").strip().upper()

    if source not in courses or destination not in courses:
        print("One or both courses do not exist.")
        return

    if graph.removeEdge(source, destination):
        print("Prerequisite removed successfully.")
    else:
        print("Prerequisite relationship not found.")


# ------------------------------------------------------------
# 11. Main Program
# ------------------------------------------------------------

def main():

    courses = create_courses()

    graph = Graph()

    # Add all courses as graph vertices
    for course_code in courses:
        graph.addVertex(course_code)

    # Create prerequisite relationships
    # Source -> Destination
    graph.addEdge("CS101", "CS201")
    graph.addEdge("CS201", "CS301")
    graph.addEdge("CS101", "CS301")
    graph.addEdge("CS101", "CS302")
    graph.addEdge("CS201", "CS401")
    graph.addEdge("CS301", "CS402")

    while True:

        print("\n===== UNIVERSITY COURSE PREREQUISITE SYSTEM =====")
        print("1. View All Courses")
        print("2. View Course Details")
        print("3. View Prerequisites of a Course")
        print("4. View Courses Unlocked by a Course")
        print("5. Add New Course")
        print("6. Add Prerequisite")
        print("7. Remove Prerequisite")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_all_courses(courses)

        elif choice == "2":
            view_course_details(courses)

        elif choice == "3":
            view_prerequisites(graph, courses)

        elif choice == "4":
            view_unlocked_courses(graph, courses)

        elif choice == "5":
            add_course(graph, courses)

        elif choice == "6":
            add_prerequisite(graph, courses)

        elif choice == "7":
            remove_prerequisite(graph, courses)

        elif choice == "8":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
