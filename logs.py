#słowniki
from collections import defaultdict
user_total_time = defaultdict(int)
user_last_login = []
#otwieramy dane
with open("../szkolenie/logs.txt") as f:
    for line in f:
        user, action, t = line.strip().split(";")
        t = int(t)

        if action == "LOGIN":
            user_last_login[user] = t
        elif action == "LOGOUT":
            user_total_time[user] += t - user_last_login[user]

for item in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(f"")
