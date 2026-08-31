def main():
    totalSales = int(0)
    NUM_FLAVORS = int (5+1)
    numFlavor = int(0)
    flavorSales = [int(0)] * NUM_FLAVORS
    flavorNames = [str("")] * NUM_FLAVORS
    flavorNames = ["None","Orange","Strawberry","Chocolate","Mango","Vanilla"]
    START_OF_DAY = int(0)
    END_OF_DAY = int(-1)
    flavor = int(START_OF_DAY)
    MAX_FLAVORS = int(NUM_FLAVORS)
    numSnowconeMsg = str("")

    print("Welcome to our snowcone shop!")
    while flavor != END_OF_DAY:
        #Display Flavor List
        print("\nHere are our Snowcone Flavors")
        numFlavor = int(0)
        while numFlavor < NUM_FLAVORS:
            print(f"{numFlavor} -- {flavorNames[numFlavor]}")
            numFlavor +=1 
        print()
        
        flavor = int(input("Enter the number of the flavor would you like to purchase? "))
        if flavor > 0 and flavor <= MAX_FLAVORS:
            numSnowconeMsg = "How many " + flavorNames[flavor] +"  snowcones do you want?"
            numSnowcones = int(input(numSnowconeMsg))
        
                   
    
            flavorSales[flavor] += numSnowcones
            totalSales += numSnowcones
            print()
            print(f"Thank you for purchasing {numSnowcones} snowcones today!\n\n")
            print("Welcome to our snowcone shop!")
        elif flavor > MAX_FLAVORS:
            print(f"Flavor number {flavor} not found.  Please try again")
        if flavor == 0:
            print(f"Thank you for coming by our snowcone shop today!")
            print("\n\n")
            print("Welcome to our snowcone shop!")

    print ("\n\nEND-OF-DAY Flavor Sales Report")
    print ("\n   FLAVOR       SALES\n")
    for flavor in range (NUM_FLAVORS):
        print (f"   1: {flavorNames[flavor]}    {flavorSales[flavor]}")
    print ("")
    print (f"TOTAL SALES: {totalSales}")
        
main()        




