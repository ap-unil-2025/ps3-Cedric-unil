"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    numbers = []
    print("Enter numbers one by one, or type 'done' to finish.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "done":
            print("Final list:", numbers)
            break
        try:
            # Convert input to float to handle integers and decimals
            numbertofloat = float(user_input)
            numbers.append(numbertofloat)
        except ValueError:
            print("Invalid input. Please enter a number or type 'done'.")

    return numbers


def analyze_numbers(numbers):
    analysis = {}

    # --- FIX FOR ZeroDivisionError ---
    # If the list is empty, return early to prevent division by zero.
    if not numbers:
        # Return a dictionary indicating a count of 0
        return {"count": 0} 
    # ---------------------------------
    
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
        # Check if the number is an 'even' or 'odd' integer.
        # This check works for floating point numbers like 4.0 (even) vs 4.5 (odd).
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    analysis["even_count"], analysis["odd_count"] = even_count, odd_count
    
    # Return the results as a dictionary
    return analysis


def display_analysis(analysis):
    print("\nAnalysis Results:")
    print("-" * 30)
    
    # Check if analysis is empty or count is zero (from the early exit in analyze_numbers)
    if not analysis or analysis.get("count", 0) == 0:
        print("No numbers were entered for analysis.")
        return 
        
    print(f"Count:      {analysis['count']}")
    print(f"Sum:        {analysis['sum']:.2f}")
    # Display statistics with two decimal places for readability
    print(f"Average:    {analysis['average']:.2f}") 
    print(f"Minimum:    {analysis['minimum']:.2f}")
    print(f"Maximum:    {analysis['maximum']:.2f}")
    print(f"Even Count: {analysis['even_count']}")
    print(f"Odd Count:  {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("=" * 20)
    print("Number Analyzer")
    print("=" * 20)

    # Get numbers from user
    numbers = get_numbers_from_user()

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()