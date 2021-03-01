def strip_nu(s: str) -> str:
    newstr = ""
    if s.islower():
        s.lower()
        return s
    elif s.isupper():
        s.upper()
        return s
    for c in s:
        if not c in ['0','1','2','3','4','5','6','7','8','9']:
            newstr+=c
    return newstr


