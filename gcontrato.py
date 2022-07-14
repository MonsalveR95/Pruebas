from datetime import datetime

def replaceText(text):
    filters = [["[COMPANY_NAME]", "nombre de la compañia"],
    ["[EMPLOYEE_NAME]", "nombre del empleado"],
    ["[CITY]", "ciudad"],
    ["[COUNTRY]", "pais"],
    ["[PRICE]", "sueldo a convenir"]]
    for filter in filters: 
        print("¿Cual es el " + filter[1] + "?")
        txtInput = input()
        text = text.replace(filter[0], txtInput)
    
    
    return  text.replace("[CURRENT_DAY]", datetime.today().strftime("%Y / %m / %d"))
    

contractFile = open("contract.txt", "r")
result = ""
for row in contractFile:
    result += row
result = replaceText(result)


with open("contract-prossed.txt", "w") as textFile:
    textFile.write(result)


#[CURRENT_DAY]

#[EMPLOYEE_NAME]
#[CITY]
#[COUNTRY]
#[PRICE]
   



