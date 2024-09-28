# сложное условие (логическое "И")
# 6 <= hour < 12 - good morning
# 12 <= hour < 17 good day
# 17 <= hour < 22 good evening
# good night

hour = 12  # 0... 23

# 1 variant
if hour >= 6 and hour < 12:
    print('good morning')
elif hour >= 12 and hour < 17:
    print('good morning')
elif hour >= 17 and hour < 22:
    print('good evening')
else:
    print('good night')

# 2 variant

if 6 <= hour < 12 :
    print('good morning')
elif 12 <= hour < 17:
    print('good morning')
elif 17 <= hour < 22:
    print('good evening')
else:
    print('good night')