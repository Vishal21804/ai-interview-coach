
while True:
    name = input("Enter name of the Candidate: ").strip()
    if name:
        break
    print("Invalid name")

while True:
    target_role = input("Enter the target role: ").strip()
    if target_role:
        break
    print("Invalid target role")

skills = []

while True:
    skill = input("Add Skill (type 'done' to stop): ").strip()
    if skill.lower()=="done":
        break

    if not skill:
        print("Skill Cannot be empty")
        continue

    if skill.lower() in [item.lower() for item in skills]:
        print("Skill already exist")
        continue

    skills.append(skill)
    print("Skill Added Successfully")
    

candidate = {
    "name":name,
    "target_role" : target_role,
    "skills" : skills 
}

print("Name : ",candidate["name"])
print("Target Role: ",candidate["target_role"])
print("skills: ",",".join(candidate["skills"]))
print("Total Skills: ",len(candidate["skills"]))

