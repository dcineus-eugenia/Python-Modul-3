# # Exercice 1

# String_variable = ("Hello world ! My name is Damien.")
# Upper_case = String_variable.upper()
# print(Upper_case)

# Lower_case = String_variable.lower()
# print(Lower_case)

# Capitalize_str = String_variable.title()
# print(Capitalize_str)

# remplace_world = String_variable.replace("Damien", "Martin")
# print(remplace_world)

# Str_variable2 = ("Hello" "world" "!" "How" "are" "you" "?")
# Join_str = (String_variable + Str_variable2)
# print(Join_str)

# Join_str = "-".join(Str_variable2)
# print(Join_str)

# split_str = String_variable.split()
# print(split_str)

# print("Exercice 2")

# Name = "Damien"
# Age = 23
# Height = 1.78

# txt_format = "My name is {}, I am {} y/o and my height is {}".format(Name,Age,Height)
# print(txt_format)

# txt_fstring = f"My name is {Name}, I am {Age} y/o and my height is {Height}"
# print(txt_fstring)

# txt_operator = "My name is %s, I am %d y/o and my height is %f"%(Name,Age,Height)
# print(txt_operator)

# formatted_height = "{:.2f}".format(Height)
# print(formatted_height)

# print("\nTable like out put")
# print(("{:>10} {:>10} {:>10}").format(Name,Age,Height))
# print("-" * 30)
# print(("{:>10} {:>10} {:10.2f}").format(Name,Age,Height))

# print("Exercice 3")

num_list = [1,2,3,5,10,9,8,7,6]
for number in num_list:
    print(number)
print("  ")

for i, value in enumerate(num_list) :
    print(i, value)
    print(f"(i) :(value)")
