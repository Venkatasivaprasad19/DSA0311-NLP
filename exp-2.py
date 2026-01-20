def fsa_ends_with_ab(s):
    if s.endswith("ab"):
        return "accepted"
    else:
        return "rejected"
string = input("enter a string:")
print("result",fsa_ends_with_ab(string))