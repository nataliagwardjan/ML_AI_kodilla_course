def is_palindrome(text: str):
    """
    Function checking if text is a palindrome.
    Return True if text is palindrome
    and False if text is not palindrome
    """
    checking_text = ''.join(char for char in text if char.isalnum())
    return checking_text.lower() == checking_text[::-1].lower()

result = is_palindrome("kajak")
print(f"Is word 'kajak' a palindrome? {result}")
result = is_palindrome("text")
print(f"Is word 'text' a palindrome? {result}")
result = is_palindrome("Kobyla ma maly bok")
print(f"Is sentence 'Kobyla ma maly bok' a palindrome? {result}")
result = is_palindrome("A to idiota")
print(f"Is sentence 'A to idiota' a palindrome? {result}")
result = is_palindrome("Zwykle zdanie")
print(f"Is sentence 'Zwykle zdanie' a palindrome? {result}")