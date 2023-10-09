"""
echo "# ASSIGNMENT-01" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/WhO-D-ShAziD/ASSIGNMENT-01.git
git push -u origin main

"""

# Taking the radius value from the user:
print("/////////// Area of Circle Calculation /////////////////\n")

print("\n")

r = float(input("Please enter the value of radius: \n"))



# Declearing the value of Pi:
pi = 3.1416

# Area Calcualtion:
area = pi * r * r

print("The area of the circle is: \n", area)
