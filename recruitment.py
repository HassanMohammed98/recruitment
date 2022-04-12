def get_skills():
    # Add at least 3 random skills for the user to select from
        return ["Python", "javascript", "CSS3", "Bootstrap"]


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    # ...
    print("\nSkills:")
    for skill in skills:
        print("{}. {}".format(skills.index(skill)+1,skill))
    # for count, skill in enumerate(skills, start=1):
    #     print("{}. {}".format(count, skill))
    print()

def get_user_skills(skills):
	
    # Show the available skills and have user pick from them
    # Write your code here
    # ...
    show_skills(skills)
    i = 0
    chosen_skills = []
    while (i < 2):
        try:
            if (i == 0):
                skill = int(input("Choose a skill from above by entering its number: "))
            elif (i == 1):
                skill = int(input("Choose another skill from above by entering its number: "))
        except:
            print("input is invalid. try again.")
        else:
            if (skill in range(1,(len(skills)+1))):
                if(skills[skill-1] not in chosen_skills):
                    chosen_skills.append(skills[skill-1])
                    i+=1
                else:
                    print("skill is repeated. try again.")
            else:
                print("input is out of bounds. try again.")
    return chosen_skills


def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    # ...
    i = 0
    cv = {'name' : input("What's your name? "),'age':0,'experience':0}
    while (i < 2):
        try:
            if (i == 0):
                age = int(input("How old are you? "))
            elif (i == 1):
                experience = int(input("How many years of experience do you have? "))
        except:
            print("input is invalid. try again.")
        else:
            if (i == 0 and age > -1):
                cv['age'] = age
                i+=1
            elif (i == 1 and experience > -1):
                cv['experience'] = experience
                i+=1
            else:
                print("input is out of bounds. try again.")
    cv['skills'] = get_user_skills(skills)
    return cv


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    # ...
    if (desired_skill in cv['skills'] and cv['age'] > 24 and cv['age'] < 41 and cv['experience'] > 3):
        return True
    else:
        return False

def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    # ...
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    cv = get_user_cv(skills)
    if (check_acceptance(cv, skills[2])):
        print("You have been accepted, {}.".format(cv['name']))
    else:
        print("You have been rejected, {}.".format(cv['name']))



if __name__ == "__main__":
    main()
