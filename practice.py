print(''''
      Hello there,
      My name is Fizaan Ali Shafiq Mughal.
      I am learning Python programing.
      I am 17 years old.
      This is pretty fun to do.
      I hope to learn more and more.
      I am studying BS IT at Government College Gujranwala.
      Thank you for reading this.
      Bye Bye!
      ''')

string = "This is great!"
string_ = ""
count = 0
for i in string:
      if i == " ":
            count+=1
      else:
            string_ += i
print(count); print(string_)


print("{}".format("one", "two", "three"))