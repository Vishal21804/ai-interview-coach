
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
print("Skills: ",",".join(candidate["skills"]))
print("Total Skills: ",len(candidate["skills"]))

while True:
    print("\n=====Skill Management=====")
    print("1.Add Skill")
    print("2.View Skills")
    print("3.Search Skill")
    print("4.Remove Skills")
    print("5.Exit")
    
    choice = input("Enter your Choice: ").strip()

    if choice == "1":
        new_skill = input("Enter New Skill: ")

        if not new_skill:
            print("Skill cannot be empty")
            continue

        if new_skill.lower() in [item.lower() for item in skills]:
            print("Skill already exist")
            continue

        skills.append(new_skill)
        print("Skill Added Successfully")

    elif choice == "2":
        if not skills:
            print("No Skills Found")
        else:
            print("My Skills: ")
            for skill in skills:
                print("-",skill)

    elif choice == "5":
        print("Exiting program....")
        break





