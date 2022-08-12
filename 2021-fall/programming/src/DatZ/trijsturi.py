# Eduards Liepiņš-Melnis, e21128
# A26. Doti trīs pozitīvi skaitļi. Noteikt, vai eksistē trijstūris ar tādiem malu garumiem un vai tas ir šaurleņķa.
# Programma izveidota: 2021/09/26

print('Hello!!!')
while True:  # piešķiram kodam atkārtošanas iespēju "while True".
    print("Input a, b, c : ")

    inputLine = input()
    numbers = inputLine.split(' ')
    #print('Input 1 ir {}'.format(aa))
    #break
    a = float(numbers[0])  # Trijstūris arī var eksistēt, ja malu garums ir decimālskaitlis.
    b = float(numbers[1])
    c = float(numbers[2])
    if a <= 0 or b <= 0 or c <= 0: print(
        "ERROR - Input positive integers!")  # Pārbauda vai malu garumi nav ievadīti 0 vai <0.
    if a < b + c and b < a + c and c < a + b:
        print("Triangle exists.")  # Pārbaudam trijstūra eksistenci lietojot šīs formulas.
    else:
        print("Triangle does not exist.")  # ja neizpildās iepriekšējais nosacījums izvada šo paziņojumu.
    if a * a + b * b > c * c:
        print("Triangle is acute.")  # Pārbaudam vai trijstūris ir šaurleņķa.
    else:
        print("Triangle is not acute.")
    if input("Do You want to repeat (Y/N) ? ") == 'n':  # Piedāvājam lietotājam atkārtot šo darbību.
        break  # apturam ciklu un atgriežamies uz sākumu.
