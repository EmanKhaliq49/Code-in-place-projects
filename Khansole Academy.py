import random

def main():
    print("Khansole Academy")
 #generates any two random numbers       
    num_1 = random.randint(10, 99)
    num_2 = random.randint(10, 99)
    answer = num_1 + num_2
    print(f"What is {num_1} + {num_2}?")
    guess = int(input("Your answer: "))
    
#check if the guess is correct or not
    if guess == answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", answer)
    
    
if __name__ == '__main__':
    main()
