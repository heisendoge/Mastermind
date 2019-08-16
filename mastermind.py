

def compare (a,b):
    if len(a)==len(b):
        l = len(a)
        result = ""
        remains_a, remains_b = "",""
        for i in range(l):
            if a[i]==b[i]:
                result += "1"
            else:
                remains_a += a[i]
                remains_b += b[i]
        for char in remains_a:
            for i in range(len(remains_b)):
                if char==remains_b[i]:
                    result+="0"
                    remains_b = remains_b[:i]+remains_b[i+1:]
                    break
        for char in remains_b:
            result+="_"
        return result
    return ""

code = input("What's the solution?\n")
guess = input("What's the guess?\n")

print(compare(code,guess))
##print(compare("aaab","aabb"))
