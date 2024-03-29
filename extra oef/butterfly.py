def createButterfly():
    aantal_jongeren=20
    speeltijd=30
    opdrachtenlijst = []
    with open("opdrachten.txt","r") as opdrachtenfile:
        opdrachten = {}
        for i in range(1,len(opdrachtenlijst)+1):
            key="O"+str(i)
            value = opdrachtenlijst[i-1].strip()
            opdrachten[key]=value

    xlist=[]
    for i in range(aantal_jongeren):
        xlist.append("")
    frame=[]
    for j in range(speeltijd):
        frame.append(xlist)
    print(len(frame))

createButterfly()

