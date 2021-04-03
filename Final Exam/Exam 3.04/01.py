# 01


line = input()
cmd = input()


def check_idx(idx):
    if 0 <=  idx < len(line):
        return False
    return True


def s_replace(r_arr):
    old, new = r_arr[0], r_arr[1]
    res = line.replace(old, new)
    return res


def s_cut(c_arr):
    start_idx, end_idx = int(c_arr[0]), int(c_arr[1])
    if check_idx(start_idx) or check_idx(end_idx):
        print("Invalid indices!")
        return line
    first = line[:start_idx]
    second = line[end_idx + 1:]
    print(first + second)
    return first + second


def s_make(m_arr):
    s_case = m_arr[0]
    if s_case == "Upper":
        return line.upper()
    elif s_case == "Lower":
        return line.lower()
    return line


def s_check(ch_arr):
    text = ch_arr[0]
    if text in line:
        print(f"Message contains {text}")
    else:
        print(f"Message doesn't contain {text}")
    return line


def s_sum(s_arr):
    start_index = int(s_arr[0])
    end_index = int(s_arr[1])
    if check_idx(start_index) or check_idx(end_index):
        print("Invalid indices!")
        return line
    sm = sum([ord(_) for _ in line[start_index:end_index + 1]])
    print(sm)
    return line


while cmd != "Finish":
    cmd = cmd.split()
    if cmd[0] == "Replace":
        line = s_replace(cmd[1:])
        print(line)
    elif cmd[0] == "Cut":
        line = s_cut(cmd[1:])
    elif cmd[0] == "Make":
        line = s_make(cmd[1:])
        print(line)
    elif cmd[0] == "Check":
        line = s_check(cmd[1:])
    elif cmd[0] == "Sum":
        line = s_sum(cmd[1:])
    cmd = input()

