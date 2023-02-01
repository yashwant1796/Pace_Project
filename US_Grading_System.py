def reporting(subject1):

    option1 = input("( best worst average end summary ): ")
    if option1 == 'best':
        print(f"Your best score in {subject} is {max(grades[subject])}")
        reporting(subject)
    elif option1 == 'worst':
        print(f"Your worst score in {subject} is {min(grades[subject])}")
        reporting(subject)
    elif option1 == 'average':
        print(f"Your average score in {subject} is {((sum(grades[subject]))/len((grades[subject]))):0.2f}")
        reporting(subject)
    elif option1 == 'summary':
        print(f"Your grades in {subject} are {grades[subject]}")
        reporting(subject)
    elif option1== 'end':
        print("\nreporting or maintenance\n 1=reporting \n 2=maintenance \n 0=exit\n")
        print()
        selection = int(input("which function: "))
        if selection == 1:
            reporting(subject)
        elif selection == 2:
            print("Currently the grades are: ", *grades[subject])
            maintenance(subject)
        elif selection == 0:
            None

def maintenance(subject2):

    print("1) change a grade\n2) add a grade\n3) delete  grade\n4) end")
    option2=int(input("What would you like to do: "))
    if option2 == 1:
        change=int(input("which grade should be change: "))
        index_value = grades[subject].index(change)
        new_value=input("What is the New grade: ")
        grades[subject][index_value]=new_value
        print(grades[subject])
        maintenance(subject)
    elif option2 == 2:
        add_value=int(input("What is the new grade: "))
        grades[subject].append(add_value)
        print(f"OK, {subject} now has the following grades: \n{grades[subject]}")
        maintenance(subject)
    elif option2 == 3:
        delete_value=int(input("Which grade should be deleted: "))
        grades[subject].remove(delete_value)
        maintenance(subject)
    elif option2==4:
        print("*"*20)
        print("\nreporting or maintenance\n 1=reporting \n 2=maintenance \n 0=exit\n")
        print()
        selection = int(input("which function: "))
        if selection == 1:
            reporting(subject)
        elif selection == 2:
            print("Currently the grades are: ", *grades[subject])
            maintenance(subject)
        elif selection == 0:
            None

if __name__ == '__main__':
    grades={'english':[90,95,81],'math':[100,95,92,98],'history':[76,98]}
    print("Your grade manager contain grades for:\n >english\n >math\n >history\n")
    subject = input("What Class you would like to work with or end to finish ( english math or history): ")
    print("*"*80)
    print("\nreporting or maintenance\n 1=reporting \n 2=maintenance \n 0=exit\n")
    print()
    selection = int(input("which function: "))
    if selection == 1:
        reporting(subject)
    elif selection == 2:
        print("Currently the grades are: ", *grades[subject])
        maintenance(subject)
    elif selection== 0:
        None

    if subject == 'english':
      print("\nreporting or maintenance\n 1=reporting \n 2=maintenance \n 0=exit\n")
      print()
      selection=int(input("which function: "))
      if selection == 1:
          reporting(subject)
      elif selection == 2:
          print("Currently the grades are: ", *grades[subject])
          maintenance(subject)
    elif subject == 'math':
       print("\nreporting or maintenance\n 1=reporting \n 2=maintenance \n 0=exit\n")
       print()
       selection=input("which function: ")
       if selection == 1:
           reporting(subject)
       elif selection == 2:
           print("Currently the grades are: ", *grades[subject])
           maintenance(subject)
    elif subject == 'history':
       print("\nreporting or maintenance\n 1=reporting \n 2=maintenance \n 0=exit\n")
       print()
       selection=input("which function: ")
       if selection == 1:
           reporting(subject)
       elif selection == 2:
           print("Currently the grades are: ", *grades[subject])
           maintenance(subject)
    elif subject == 'end':
       print("Bye Bye")
    else:
        print("error")
