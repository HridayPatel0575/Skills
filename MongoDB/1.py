import pymongo


def main():

    print(client)
    db = client['Hriday']
    collection = db['Names']
    i=0
    while i==0:
        print("Select option:")
        print("1.Add One")
        print("2.Add Many")
        print("3.Find")
        print("4.Exit")
        a = int(input())
        if a == 1:
            nm = input("Enter name:")
            ag = int(input("Enter Age:"))
            dictionary = {'name':nm,'age': ag}
            collection.insert_one(dictionary)
            print(dictionary)
        if a == 2:
            nm1 =[]
            ag1 =[]
            for i in range(0,4):
                nm1.append(input(f"Enter name No.{i+1}: ")) 
                ag1.append(input(f"Enter name No.{i+1}: "))
            addThese = [{'name':nm1[0],'age':ag1[0]},{'name':nm1[1],'age':ag1[1]},{'name':nm1[2],'age':ag1[2]},{'name':nm1[3],'age':ag1[3]}] 
            collection.insert_many(addThese)
        if a ==3:
            f = input("Enter Name: ")
            allD = collection.find({'name':f},{'name':1,'_id':0,})
            for it in allD:
                print(it)
        if a == 4:
            i = 1
        else:
            print("Enter Proper Option")

    
    





if __name__ =="__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    main()