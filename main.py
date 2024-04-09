# Using try without except (ignoring exceptions) in Python

my_list = []

# ✅ Ignore any exception
try:
    print(my_list[100])
except:
    # 👇️ this runs
    pass