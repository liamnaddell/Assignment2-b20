def strip_nu(s: str) -> str:
    newstr = ""
    if s.islower() and s.isalpha():
        return s.upper()
    elif s.isupper() and s.isalpha():
        return s.lower()
    else:
        for c in s:
            if not c in ['0','1','2','3','4','5','6','7','8','9']:
                newstr+=c
        return newstr


