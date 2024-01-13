#Task 1
# implementing Lists and Slicing
# List 'mixed_data' with 8 elements consisting of integers, floats and strings
mixed_data = [1,'python',3.14,5,'CSI',2.7,10,2.512525]

# ': n' prints all elements upto n-1 position
print("First three elements are :",mixed_data[:3])

# 'a : b' prints all elements from a to b-1 position
print("Elements from 2nd to 5th position :",mixed_data[1:5])

# '-n :' prints all elements from len - n positio
print("Last two elements :",mixed_data[-2:])


#Task 2
# implementing Functions
def calculate_discount(original_price,discount_percentage):
    return original_price - (original_price * discount_percentage / 100)

print(f"\nPrice after 10% discount is :",calculate_discount(100,10))


#Task 3
# implementing Control Statements
x = float(input("\nEnter original Price :"))
y = float(input("Enter Discount :"))

print(f"\nPrice after {y}% discount is :",calculate_discount(x,y))

if calculate_discount(x,y)<50 :
    print("Low-cost item.")
elif 50<calculate_discount(x,y)<100 :
    print("Moderate-cost item.")
else:
    print("High-cost item.")

for i in mixed_data:
    # type(i).__name__ can be used to show only the name of the data type
    print("\nelement :",i,"\ndata type :",type(i).__name__)


# Task 4
# implementing File Handling
file_1 = open("product_descriptions.txt","r")
file_2 = open("formatted_descriptions.txt","w")

for line in file_1:
    file_2.write(line.title())

file_1.close()
file_2.close()


# Task 5
# implementing Dictionaries
customer_info = {'name':'Azim','age':19,'purchase_history':['Laptop','Mobile','Mouse']}

print("\nName :",customer_info['name'],"\nSecond Purchase :",customer_info['purchase_history'][1])


# Task 6
# implementing classes
class Book:
    title = "Harry Potter"
    author = "J.K Rowling"
    genre = "Fantasy"

#creating object named 'new_book' using class 'Book'
new_book = Book()
Book.title = "Voldemort"

print("\nTitle :",Book.title,"\nAuthor :",Book.author,"\nGenre :",Book.genre)