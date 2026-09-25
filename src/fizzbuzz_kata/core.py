def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz representation of a positive integer n."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("fizzbuzz expects a strictly positive integer")

    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)
