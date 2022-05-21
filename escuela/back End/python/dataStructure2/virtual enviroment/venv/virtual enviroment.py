# Virtual Enviroment

# Creating an Virtual enviroment in terminal
# cd my_projectt-directory
# python3 -m venv file_name (usually venv)

# using the virtual enviroment
# source venv/bin/activate   (venv is file name)

# you dint have acces to globally instaled pip3

# i installed (pip3 install faker)

# from faker import Faker

from mondrian_art import generate
plt = generate()
plt.show()


# fake = Faker()
# for x in range(10):
#     print(fake.name())


# to leave virtual enviroment
# deactivate
