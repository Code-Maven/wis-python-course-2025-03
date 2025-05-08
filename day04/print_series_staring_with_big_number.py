
def print_series(series):
    started = False;
    for val in series:
        if val == "start":
            started = True
            print("start new series")

        if not started:
            continue

        if val != "start":
            print(val)


print_series(["start", "2", "3", "start", "1", "7"])
print()
print_series(["1", "4", "start", "2", "3", "start", "1", "7"])
