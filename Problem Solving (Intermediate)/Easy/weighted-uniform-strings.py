def c2i(char):
    return ord(char) - ord('a') + 1


def weightedUniformStrings(s, queries):
    # Write your code here
    w = set()
    for i in range(len(s)):
        runner = c2i(s[i]) if i == 0 or s[i] != s[i-1] else runner + c2i(s[i])
        w.add(runner)

    return ['Yes' if query in w else 'No' for query in queries]

print(weightedUniformStrings('ccxxc', [4]))