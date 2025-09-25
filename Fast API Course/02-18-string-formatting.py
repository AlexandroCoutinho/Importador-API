first_name = "Eric"

print("Hi " + first_name)

print(f"Hi {first_name}")

sentence = "Hi {}"
print(sentence.format(first_name))

last_name = "Roby"
sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you're learning.")