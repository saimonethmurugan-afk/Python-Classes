#Roman Numerals to Normal Numbers Calculator

def romantoint(romaninput):
    #Assigning the roman letters to their numbers
    roman = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    resultinteger =0

    for i in range(0,len(romaninput) - 1):
        if roman[romaninput[i]] < roman[romaninput[i + 1]]:
            resultinteger -= roman[romaninput[i]]
    else:
        resultinteger+=roman[romaninput[i]]
    return resultinteger + roman[romaninput[i-1]]

#Taking the roman numeral input from the user
roman = input("Please enter the number you wish to be converted to the Standard Numbers(make sure it is Roman e.g. VI,MI): ")

print("Integer equivalent: ",romantoint(roman))