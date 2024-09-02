def is_palindrome(s):
    return s == s[::-1]

def count_fake_palindromes(s):
    substrings = set()
    
    # Generate all substrings and add to the set
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    
    fake_palindromes_count = 0
    
    # Check each substring if it's a fake palindrome
    for substring in substrings:
        if not is_palindrome(substring):
            fake_palindromes_count += 1
    
    return fake_palindromes_count

# Example usage
A = "ababa"
print("Number of fake palindromes:", count_fake_palindromes(A))
