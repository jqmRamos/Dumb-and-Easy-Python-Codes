
if __name__ == "__main__":
    square = -9
    if square < 1 and square > 0:
        print("enter here")
        low = square
        high = 0.999
    else:
        low = 0
        high = square
    guess = (high + low)/2.0
    epsilon = 0.001
    tries = 0
    while(abs(square - guess**3) >= epsilon):
        
        #print(f"{low}º guess: {high}")
        if abs(guess**3) > abs(square):
            high = guess
        else: 
            low = guess
        guess = (high + low)/2.0
        tries = tries + 1
    print(f"{guess} is close to the root of {square} \n{guess**3}")
    print(f"\n{square - guess**3}")