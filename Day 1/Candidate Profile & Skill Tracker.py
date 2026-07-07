name = input("Enter name of the Candidate: ")
target_role = input("Enter the target role: ")

skills = []

for i in range(3):
    skill = input("Enter role: ")
    skills.append(skill)

candidate = {
    "name":name,
    "target_role" : target_role,
    "skills" : skills 
}

print("Name : ",candidate["name"])
print("Target Role: ",candidate["target_role"])
print("skills: ",",".join(candidate["skills"]))
print("Total Skills: ",len(candidate["skills"]))

