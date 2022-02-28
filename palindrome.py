class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]


def run():
    solution = Solution()
    if(solution.isPalindrome(str(input("is this a Palindrome? ")))):
        print("Yes, this is a Palidrome")
    else:
        print("No, this is NOT a Palindrome")


if __name__ == "__main__":
    run()