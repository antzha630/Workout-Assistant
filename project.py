class Node():
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            other = Node(data)
            other.next = self.head
            other.prev = temp
            temp.next = other
            self.head.prev = other

    def get_nth(self, number):
        i = 0
        pearl = self.head
        while i < number:
            self.head = self.head.next
            i += 1
        done = self.head
        self.head = pearl
        return done


class liftPal():
    def __init__(self):
        self.maxes = {}
        self.schedule = LinkedList()
        self.goals = {}

    def display_menu(self):
        print("\n--- LiftPal Menu ---")
        print("1. Create Workout Schedule")
        print("2. View Today's Muscle Group")
        print("3. Log a New Max Lift")
        print("4. List Max Lifts")
        print("5. Set a Goal")
        print("6. Check Progress Towards Goals")
        print("7. What should I focus on?")
        print("8. Exit")

    def menu(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            if choice == '1':
                self.make_schedule()
            elif choice == '2':
                self.find_muscle_group()
            elif choice == '3':
                self.log_max()
            elif choice == '4':
                self.list_lifts()
            elif choice == '5':
                self.set_goal()
            elif choice == '6':
                self.check_progress()
            elif choice == '7':
                self.find_fault()
            elif choice == '8':
                print("Exiting!")
                break
            else:
                print("Invalid choice. Please try again.")

    def make_schedule(self):
        print("Welcome to LiftPal! Here we will make your schedule of workouts.")
        i = 0
        temp = {"Chest": 1, "Arms": 2, "Legs": 3, "Back": 4, "Rest": 5}
        done = []
        while i < 5:
            print("Select a muscle group:")
            if "Chest" in temp:
                print(f"-Chest")
            if "Arms" in temp:
                print(f"-Arms")
            if "Legs" in temp:
                print(f"-Legs")
            if "Back" in temp:
                print(f"-Back")
            if "Rest" in temp:
                print(f"-Rest")
            if done is None:
                print("Your schedule is empty, please select your first workout")
            else:
                print("What is your next muscle group?")
            real = False
            while real == False:
                hold = str(input())
                if hold == "Chest":
                    done.append("Chest")
                    temp.pop("Chest")
                    print(f'You have chosen {hold}')
                    real = True
                elif hold == "Back":
                    done.append("Back")
                    temp.pop("Back")
                    print(f'You have chosen {hold}')
                    real = True
                elif hold == "Arms":
                    done.append("Arms")
                    temp.pop("Arms")
                    print(f'You have chosen {hold}')
                    real = True
                elif hold == "Legs":
                    done.append("Legs")
                    temp.pop("Legs")
                    print(f'You have chosen {hold} 🙁')
                    real = True
                elif hold == "Rest":
                    done.append("Rest")
                    temp.pop("Rest")
                    print(f'You have chosen {hold}')
                    real = True
                else:
                    print("You seem to have not inputted one of the options. Please check your spelling and try again.")
            x = 0
            yelp = ""
            while x < len(done):
                yelp += done[x]
                if x != (len(done) - 1):
                    yelp += ", "
                x += 1
            if i != 4:
                print(f"Your schedule currently is {yelp}")
            i += 1
        y = 0
        pub = ""
        while y < len(done):
            pub += done[y]
            if y != (len(done) - 1):
                pub += ", "
            self.schedule.insert(done[y])
            y += 1
        print(f"Your final schedule is {pub}")

    def find_muscle_group(self):
        broken = False
        while broken == False:
            print("Do you want to know what you're hitting today? (Y or N)")
            hold = str(input())
            if hold == "Y":
                print(f"You are hitting {self.schedule.head.data}")
                broken = True
            elif hold == "N":
                broken = True
                broken2 = False
                while broken2 == False:
                    print(f"How many days in the future do you want to know your exercise plan?")
                    wait = input()
                    if wait <= 0:
                        print("Please input at least 1")
                    elif wait.isnumeric():
                        wait = int(wait)
                        temp = self.schedule.head
                        broken2 = True
                        t = 0
                        while t < wait:
                            temp = temp.next
                            t += 1
                        if wait == 1:
                            if temp.data != "Rest":
                                print(f"In 1 day you will be hitting {temp.data}")
                            else:
                                print(f"In 1 day you will be resting")
                        else:
                            if temp.data != "Rest":
                                print(f"In {wait} days you will be hitting {temp.data}")
                            else:
                                print(f"In {wait} days you will be resting")
                    else:
                        print("Please input a number")
            else:
                print("Please try again and enter either Y or N")

    def log_max(self):
        print("Please name the exercise you want to log data for:")
        hold = str(input())
        broken = False
        print("How much weight did you use?")
        lbs = input()
        while broken == False:
            if lbs.isnumeric():
                broken = True
            else:
                print("Please input a number")
                print("How much weight did you use?")
                lbs = input()
        lbs = int(lbs)
        if hold in self.maxes:
            if self.maxes[hold] > lbs:
                # Inform the user that the new weight doesn't exceed the current max
                print(
                    f"Your current personal record is {self.maxes[hold]}lbs, meaning that your {lbs}lbs lift will not change your max")
            elif self.maxes[hold] < lbs:
                # Update the max if the new weight is higher and congratulate the user
                print(
                    f"Congratulations you have increased your max! You have increased your max weight on {hold} from {self.maxes[hold]}lbs to {lbs}lbs")
                self.maxes[hold] = lbs
        else:
            self.maxes[hold] = lbs
            print(f"For your first time doing this exercise, you did {lbs}lbs")
        # Check if the exercise has a goal set
        if hold in self.goals:  
            # If the new weight meets or exceeds the goal
            if lbs >= self.goals[hold]:  
                print(f"Great job! You've reached your goal for {hold}: {self.goals[hold]}lbs.")  # Congratulate the user
                del self.goals[hold]  # Remove the goal from the goals dictionary

    def set_goal(self):
        print("Please name the exercise you want to set a goal for:")
        hold = str(input())
        print("What is your target weight?")
        lbs = input()
        while not lbs.isnumeric():
            print("Please input a valid number")
            lbs = input()
        lbs = int(lbs)
        self.goals[hold] = lbs
        print(f"Goal set for {hold}: {lbs}lbs.")

    def list_lifts(self):
        combo = []
        for val in self.maxes:
            combo.append((self.maxes[val], val))
        i = 1
        while i < len(combo):
            spot = combo[i]
            j = i - 1
            while j >= 0 and spot[0] < combo[j][0]:
                combo[j + 1] = combo[j]
                j -= 1
            combo[j + 1] = spot
            i += 1
        print("You max lifts for your exercises in ascending order are as follows:")
        x = 0
        while x < len(combo):
            print(f"{combo[x][1]}- {combo[x][0]}lbs")
            x += 1

    def check_progress(self):
        if not self.goals:
            print("You haven't set any goals")
            return
        print("Progress towards your goals:")
        # Iterate through each exercise and its target weight in the goals dictionary
        for exercise, target in self.goals.items():
            # Check if the exercise has a recorded max in the maxes dictionary
            if exercise in self.maxes:

                current_max = self.maxes[exercise]
                difference = target - current_max
                # If the current max is less than the target, show how much more is needed to reach the goal
                if difference > 0:
                    print(f"For {exercise}, you need {difference} more lbs to reach your goal of {target}lbs")
                else:
                    print(
                        f"You have already exceeded your goal for {exercise} with {current_max} lbs (original goal: {target} lbs).")
            else:
                print(f"For {exercise}, there is no exercise max recorded yet. The listed goal is {target}lbs.")

    def find_fault(self):
        if not self.goals:
            print("You haven't set any goals")
            return
        base = []
        # Iterate through each exercise and its target weight in the goals dictionary
        for exercise, target in self.goals.items():
            # Check if the exercise has a recorded max in the maxes dictionary
            if exercise in self.maxes:
                current_max = self.maxes[exercise]
                difference = target - current_max
                temp = (difference, exercise)
                base.append(temp)
        i = 1
        while i < len(base):
            spot = base[i]
            j = i - 1
            while j >= 0 and spot[0] > base[j][0]:
                base[j + 1] = base[j]
                j -= 1
            base[j + 1] = spot
            i += 1
        if len(base) == 1:
            print(f"You only have one goal exercise being {base[0][1]} and you are {base[0][0]}lbs away from your goal")
            return
        print(f"Here are a list of your lifts sorted from furthest from your goal to closest:")
        i = 0
        while i < len(base):
            print(f"{base[i][1]} - {base[i][0]}lbs away from goal")
            i += 1
        print(f"We believe you should focus the most on {base[0][1]}")






class main():
    client1 = liftPal()
    client1.menu()


if __name__ == "main":
    main()