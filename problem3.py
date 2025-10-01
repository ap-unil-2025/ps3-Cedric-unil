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
    if not numbers:
        return {
            "count": 0,
            "sum": 0,
            "average": 0,
            "min": None,
            "max": None,
            "even_count": 0
        }
    # Total count of elements
    count = len(numbers)
    # Sum all numbers
    total_sum = sum(numbers)
    # Average of the list
    average = total_sum / count
    # Minimum value
    minimum = min(numbers)
    # Maximum value
    maximum = max(numbers)
    # Count even numbers and odd
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # Return the results as a dictionary
    return {
        "count": count,
        "sum": total_sum,
        "average": average,
        "min": minimum,
        "max": maximum,
        "even count": even_count,
        "odd count": odd_count
        }



def display_analysis(analysis):
    print("\nAnalysis Results:")
    print("-" * 20)
    if not analysis:
        print(analysis)
    else:
        print(analysis)


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