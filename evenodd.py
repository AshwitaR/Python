print('.'*20,'Hello there! This is Python program workout by Ashwita Rajesh:)','.'*20)
H=(input('How do you do?:'))
if H=='fine':
    print('perfect!')
elif H=="Fine":
    print('Perfect :)')
else:
    print('Oh okay then lets start:')
print('*Lets know if your number is odd or even!*')
x = int(input("Now Enter your number : "))
if x%2 == 0 :
    print('Well,',x," is an even number!")
else :
    print('Well,',x,"is an odd number!")
print("*Now Lets know if your number is positive or negative!*")
y = float(input('Enter another number:'))
if y>0:
    print('Its a positive number:)')
elif y==0:
    print('Zero! Its a positive number')
else:
    print('Its a negative number:)')
print("Thank you")
print('.'*20,'Program by AR','.'*20)
