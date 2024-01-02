INFO = 0
WARNING = 1
ERROR = 2


def logs(says_type, says, who_said = "pygl"):
    if says_type == INFO:
        print("\033[34m", who_said, ":[INFO]", says, "\033[0m")
    if says_type == WARNING:
        print("\033[33m", who_said, ":[WARNING]", says, "\033[0m")
    if says_type == ERROR:
        print("\033[31m", who_said, ":[ERROR]", says, "\033[0m")