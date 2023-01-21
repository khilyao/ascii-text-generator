from data import styles

user_word = input('Enter your name: ')

fixed_word = " ".join(user_word)

print(styles.style_1(fixed_word))
print(styles.style_2(fixed_word))
print(styles.style_3(fixed_word))
print(styles.style_4(fixed_word))
print(styles.style_5(fixed_word))
