години = int(input("Введіть кількість годин: "))
if 0 <= години < 6:
    повідомлення = "Good Night"
elif 6 <= години < 13:
    повідомлення = "Good Morning"
elif 13 <= години < 17:
    повідомлення = "Good Day"
else:
    повідомлення = "Good Evening"
print(повідомлення)

