def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_profile(Name="Mehala", Age=19, Course="B.Sc Computer Science", Year="2nd Year")
