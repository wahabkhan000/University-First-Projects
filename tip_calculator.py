# This is a US based tip calculator
def float1(m):
    m = float(m.replace("$", ""))
    return m
def float2(n):
    n= float(n.replace("%",""))
    return n
def main():
    m = str(input("How much was the meal? "))
    o=float1(m)
    n = str(input("What percent would you like to tip? "))
    p=float2(n)
    tip=o*(p/100)
    # print("Leave $",tip)
    print(f"Leave $ {tip:.2f}")
main()
