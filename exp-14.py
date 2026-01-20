def check_agreement(subject, verb):
    if subject == "he" and verb.endswith("s"):
        return "accepted"
    else:
        return "rejected"
subject ="he"
verb ="runs"
print(check_agreement(subject, verb))