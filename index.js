/**
 * Calculates the factorial of a given number.
 * @param {number} n - The number to calculate factorial for.
 * @returns {number} The factorial of n.
 */
function factorial(n) {
    // Check for invalid inputs
    if (n < 0) return NaN;
    if (!Number.isInteger(n)) return NaN;

    // Base case
    if (n === 0 || n === 1) {
        return 1;
    }

    // Iterative approach to avoid stack overflow for large numbers
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }

    return result;
}

// Example usage
console.log(factorial(5)); // 120
console.log(factorial(0)); // 1
console.log(factorial(10)); // 3628800