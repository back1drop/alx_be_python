task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ").lower()
time=input("Is it time-bound? (yes/no): ").lower()
if task !="":
    match priority:
           case 'high':
                if time=='yes': 
                       print(f"Reminder: {task} is a high priority task that requires immediate attention today! ")
                elif time =='no':

                    print(f"Reminder: {task} is a high priority task that is not time bound so deal with it soon! ")
                else:

                    print("enter the time details")
           case 'medium':
                if time=='yes':
                    print(f"Reminder: {task} is a medium priority task that requires immediate attention soon before the deadline! ")
                elif time =='no':

                    print(f"Reminder: {task} is a low medium task. Consider completing it when you have free time ")
                else: 
                    print("enter the time details") 
           case 'low':
                if time=='yes':
                    print(f"Note: {task} is a low priority task. Consider completing it when you have free time soon ")
                elif time =='no':
                    print(f"Note: {task} is a low priority task. Consider completing it when you have free time. ")
                else:
                    print("enter the time details")
           case _:
                print("enter the priority details")
else:
     print("please enter a task")
     

          
          