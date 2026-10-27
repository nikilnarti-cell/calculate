import sys 
def sim_interest(principal, rate, time):
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p=int(sys.argv[1])
    r=float(sys.argv[2])
    t=int(sys.argv[3])
    print("simple interest is:", sim_interest(p, r, t))
