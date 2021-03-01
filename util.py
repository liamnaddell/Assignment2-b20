def strip_nu(s: str) -> str:
    newstr = ""
    for c in s:
        if not c in ['0','1','2','3','4','5','6','7','8','9']:
            newstr+=c
    return newstr


