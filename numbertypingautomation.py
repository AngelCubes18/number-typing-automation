import pyautogui
import time
import random
import os

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def biased_sleep_time(min_time, max_time):
    sleep_ranges = [(min_time, (min_time + max_time) / 2), ((min_time + max_time) / 2, max_time)]
    weights = [1, 3] 

    selected_range = random.choices(sleep_ranges, weights)[0]
    return random.uniform(*selected_range)

def get_filtered_numbers(start, end, digit_constraints):
    filtered_numbers = []
    for number in range(start, end + 1):
        num_str = str(number).zfill(len(str(end))) 
        valid = all(num_str[pos - 1] == str(value) for pos, value in digit_constraints.items())
        if valid:
            filtered_numbers.append(number)
    return filtered_numbers

def main():
    while True:
        clear_screen()  
        
        print("                                                                                                     ")
        print(" ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗     ████████╗██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ ")
        print(" ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔════╝ ")
        print(" ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝       ██║    ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ███╗ ")
        print(" ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗       ██║     ╚██╔╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║ ")
        print(" ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║       ██║      ██║   ██║     ██║██║ ╚████║╚██████╔╝ ")
        print(" ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝       ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
                                                                                                          
        print("  █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗ ")               
        print(" ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║ ")
        print(" ███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║ ")                  
        print(" ██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║ ")                  
        print(" ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║ ")
        print(" ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝  by za Cubes")
        print()
        start = int(input("Enter the starting number you want the bot to write from: "))
        clear_screen() 

        end = int(input("Enter the ending number you want the bot to write to end from: "))
        clear_screen() 

        min_sleep = float(input("Enter the minimum random sleep time between numbers (in seconds) This first number will have the weight by 1: "))
        clear_screen() 

        max_sleep = float(input("Enter the maximum random sleep time between numbers (in seconds) This second number will have the weight by 3: "))
        clear_screen()

        # Get digit constraints
        print("Enter the fixed digit position/s and value/s (e.g., '2 4' 2 for second digit and 4 as the value). Type 'done' when finished.")
        digit_constraints = {}
        while True:
            constraint = input("Digit position and value of it: ").strip().lower()
            if constraint == "done":
                break
            try:
                pos, value = map(int, constraint.split())
                digit_constraints[pos] = value
            except ValueError:
                print("Invalid input. Please provide position and value separated by a space.")
            
            clear_screen()

        print(f"Digit constraints applied: {digit_constraints}")

        numbers = get_filtered_numbers(start, end, digit_constraints)

        if not numbers:
            print("No valid numbers found with the given constraints. Please try again.")
            input("Press Enter to continue...")  
            continue 

        print("Focus on the target window. Writing starts in 5 seconds...")
        time.sleep(5)

        for num in numbers:
            pyautogui.typewrite(str(num))
            pyautogui.press('enter')

            sleep_time = biased_sleep_time(min_sleep, max_sleep)
            print(f"Typed {num}, waiting for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
        
        break

if __name__ == "__main__":
    main()
