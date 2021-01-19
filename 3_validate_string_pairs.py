def isOpenCharacter(character):
    return character in ['[', '{', '(']

def closeCharacter(character):
    closeCharacters = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return closeCharacters.get(character)

def validateString(text):
    stack = []
    for s in text:
        if isOpenCharacter(s):
            stack.append(s)
        else:
            if closeCharacter(stack[len(stack) - 1]) == s:
                stack.pop()
            else:
                return "Invalid"
    return "Valid" if len(stack) == 0 else "Invalid"
    
string_1 = "({})"
string_2 = "({()()}[()])"
string_3 = "{[}()]"

print(validateString(string_1))
print(validateString(string_2))
print(validateString(string_3))
