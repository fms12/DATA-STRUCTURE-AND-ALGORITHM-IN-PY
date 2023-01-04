def replace(s: str, old: str, new: str) -> str:
    if not s:
        return ''

    if s.startswith(old):
        s = new + s[len(old):]

    return s[0] + replace(s[1:], old, new)

for i in range(int(input())):
    print(replace(input(), 'pi', '3.14'))
