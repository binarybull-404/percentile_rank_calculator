numofstudents=int(input("Enter number of students: "))
numofsubjects=int(input("Enter number of subjects: "))
totalmarkspersubject=float(input("Enter total marks per subject: "))
dict_percentage={}

for i in range(numofstudents):
    sub=[]
    print("For student ",i+1)

    score={}
    for j in range(numofsubjects):
        mark=float(input("Enter marks of subject "+str(j+1)+": "))
        sub.append(mark)
        
        while sub[j]>totalmarkspersubject or sub[j]<0:
            print("Invalid marks entered. Please re-enter the marks.")
            sub.pop(j)
            mark=float(input("Enter marks of subject "+str(j+1)+": "))
            sub.append(mark)

        
        
        score['Subject '+str(j+1)]=sub[j]


    
    dict_percentage.update({'Student '+str(i+1):(sum(sub)*100)/(totalmarkspersubject*numofsubjects)})


    print(score)

    
    for k in range(len(sub)):
        if sub[k]*100/totalmarkspersubject<33:
            print("You have failed in subject",(k+1),"with marks",sub[k],"due to less than 33% marks.")
            
    

    if (sum(sub)*100)/(totalmarkspersubject*numofsubjects)<=40:
            print("You have failed due to overall percentage less than or equal to 40%")
    
    print('Student',i+1,'overall percentage is:',(sum(sub)*100)/(totalmarkspersubject*numofsubjects),'%')

    
    print("Overall percentage of all students respectively:",dict_percentage)

sorted_percentage=dict(sorted(dict_percentage.items(), key=lambda x:x[1], reverse=True))
print("Overall percentage of all students in descending order:",sorted_percentage)

for key, value in sorted_percentage.items():
    if value==max(sorted_percentage.values()):
        print(key,"has secured the highest percentage of",value,"%")    

percentile = {}
rank = 0

for student in sorted_percentage:
    percentile[student] = ((numofstudents - rank) / numofstudents) * 100
    rank += 1

print("Percentile of all students respectively:", percentile)
        