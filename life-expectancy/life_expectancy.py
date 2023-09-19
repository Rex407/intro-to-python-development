i = 0
lowest = 100
lowestyear = ""
lowestcountry = ""
with open("c:/Users/REX-MAN/Documents/intro to python development/life-expectancy/life-expectancy.csv") as lifefile:
    for line in lifefile:
        i = i+1
        cleanline = line.strip()
        words = cleanline.split(",")
        if i > 1:
           
            print(f"{i}: {cleanline}")
            print(f"{i}: {words[0]} - {words[2]} - {words[3]}") 
            print()
            if lowest > float(words[3]):
                lowest = float(words[3])
                lowestyear = words[0]
                print(f"{lowest} - {lowestyear} - {lowestcountry}")
                print()
                    

        #lifefile = input("What is the year and country that has the lowest life expectancy in the dataset?: ")
        #lifefile.lowestyear(words)
        #lifefile = (f"What is the year and country that has the highest life expectancy in the dataset?")
    


            

           
        



