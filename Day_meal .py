Day = input("enter th day")
meal=input("enetr the meal")
if Day == "monday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("rajma chawla")
    else:
        print("Roti sabji")
elif Day == "tuesday":
    if meal=="breakfast":
        print("poori sabji")
    elif meal=="lunch":
        print("thupka")
    else:
        print("chikin chawla")
else:
    print("aur kisi bhi din ham daal roti sabji khayege")
