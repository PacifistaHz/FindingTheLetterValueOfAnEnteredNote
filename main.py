from array import array

note=input("Enter a note: ")
note=float(note)

noteList={
    84:["AA", 4.0, "Passed"],
    77:["AB", 3.7, "Passed"],
    71:["BA", 3.3, "Passed"],
    66:["BB", 3.0, "Passed"],
    61:["BC", 2.7, "Passed"],
    56:["CB", 2.3, "Passed"],
    50:["CC", 2.0, "Passed"],
    46:["CD", 1.7, "Passed on the average"],
    40:["DC", 1.3, "Passed on the average"],
    33:["DD", 1.0, "Passed on the average"],
    0:["FF", 0.0, "Failed"]
}

for i in noteList:
    if note>=i:
        array=noteList[i]
        print("Letter Value: "+array[0])
        print("4 note system: "+str(array[1]))
        print("Situation: "+array[2])
        break