import sys 
principal =float(sys.argv[1])
rate =float(sys.argv[2])
time =float(sys.argv[3])

interest = (principal * rate * time) / 100
print("Simple Interest is:", interest)
