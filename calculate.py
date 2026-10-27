import sys 
def sim_interest(principal, rate, time):
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p=int(input("Enter principal amount: "))
    r=float(input("Enter rate of interest: "))
    t=int(input("Enter time in years: "))
    
    print("simple interest is:", sim_interest(p, r, t))
