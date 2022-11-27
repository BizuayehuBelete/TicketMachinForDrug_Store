from timer import Timer
from drug_store import drug_store
c=0
ph=0
p=0
while True:
  list = (346189640, 346396088)
  count=0
  max_count=3

  while max_count>count:
     id = int(input("please enter your id:"))
     if id in list:
       # order = input(
       #
       #   "Enter Your Option:\npress 'c' for cosmetics\nPress 'ph' for pharmaceuticals\npress 'p' for perfumery: ")

      while True:
       order = drug_store()

       if order == "c":
           # global c
           c += 1
           print("Your Ticket Number is",f"c _ {c}")
           print("Please wait and someone will assist you shortly.")
       if order == "ph":
           # global ph
           ph += 1
           print("Your Ticket Number is",f"ph _ {ph}")
           print("Please wait and someone will assist you shortly.")
       if order == "p":
           # global p
           p += 1
           print("Your Ticket Number is",f"p _ {p}")
           print("Please wait and someone will assist you shortly.")
       permission = input("Do you want to continue y\n ? ")
       if permission == "y":
        continue
       else:
           exit(0)
       # while order!="":
         # print("Your Ticket Number is")
         # drug_store()
         # print(input2)
         # permission=input("Do you want to continue? ")
         # if permission=="y":
         #     drug_store()
             # print(input2)
            # order = input(
            # "Enter Your Option:\npress 'c' for cosmetics\nPress 'ph' for pharmaceuticals\n press 'p' for perfumery: ")
         # else:
         #    print()

     count+=1

  else:
      Timer()
