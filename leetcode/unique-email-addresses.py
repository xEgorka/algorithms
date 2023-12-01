# https://leetcode.com/problems/unique-email-addresses

# Clean data


from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        u_emails = set()
        for e in emails:
            domain = e[e.find('@') :]
            e = e[: e.find('@')]
            if e.find('+') > 0:
                e = e[: e.find('+')]
            e = e.replace('.', '')
            u_emails.add(e + domain)
        return len(u_emails)


def main() -> int:
    # emails = [
    # "test.email+alex@leetcode.com",
    # "test.e.mail+bob.cathy@leetcode.com",
    # "testemail+david@lee.tcode.com",
    # ]
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    x = Solution().numUniqueEmails(emails)
    print(x)
    return 0


if __name__ == '__main__':
    main()
