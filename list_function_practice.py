cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"]
print (cart[-1:-4:-1])


tags = ["banana", "Vipia", "apple", "cherry", "vipin"]
tags.sort()
print (tags)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (numbers[::4])


notifications = ["Like", "Comment"]
notifications.insert(0,"New Followers")
print (notifications)


log_data = ["Vipin", 25, "Jaipur", 302020, True, ["Test", 43, [23242, [234234]]]]
print (log_data[-1][-1 ][-1][-1])


ledger = [100, -50, 200]
new_batch = [500, -20, 30]
ledger.extend(new_batch)
print (ledger)