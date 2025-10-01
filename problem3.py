"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    numbers = []
    while True:
        user_input= input("Give me a list of numbers, type done to finish: ")
        if user_input == "done":
            print("Final list: ",numbers)
            break
        try :
            numbertofloat = float(user_input)
            numbers.append(numbertofloat)
        except ValueError:
            print("Not a number or done, please give a number or type done")

    return numbers



def analyze_numbers(numbers):
    analysis = {}
    # Total count of elements
    analysis["count"] = len(numbers)
    # Sum all numbers
    analysis["sum"] = sum(numbers)
    # Average of the list
    analysis["average"] = analysis["sum"] / analysis["count"]
    # Minimum value
    analysis["minimum"] = min(numbers)
    # Maximum value
    analysis["maximum"] = max(numbers)
    # Count even numbers and odd
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    analysis["even_count"], analysis["odd_count"] = even_count, odd_count
    # Return the results as a dictionary
    return analysis



def display_analysis(analysis):
    print("\nAnalysis Results:")
    print("-" * 20)
    if not analysis:
        return    
    for key in analysis.keys():
        print(f"{key} is {analysis[key]}")

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    pass


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()