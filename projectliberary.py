print ("\n\tproject Liberary by Tushar...")
class Liberary:
      def __init__(self,list,user):
         self.booklist = list
         self.user = user
         self.ecodict = {}
      def displaybooks(self): #to diplay books
          print (f"\nWe have these books present in our liberary: {self.user}\n")
          for book in self.booklist:
              print (book)

      def lendbook(self,user,book): #to lend books
          if book not in self.ecodict.keys():
             self.ecodict.update({book:user})
             print ("\n DATABASE has been UPDATED seXy, You can take your BOOK now:)")
          else:
             print (f"\nBook is already being used by {self.ecodict[book]}")

      def addbook(self,book): #to add books
          self.booklist.append(book)
          print ("\nBook has been added to the book list")

      def returnbook(self,book): #to return books
          self.ecodict.pop(book)
          print ("\nBook returned successfully and kept in booklist.")
if __name__=='__main__':
   tush = Liberary(['LIFE OF INTROVERT','HOW TO BE SAD WITHOUT ANY REASON','OVERTHINKING','PYTHON'],"Sapph_Moonlight's")
   while(True):
        print (f"\nWelcomen to the {tush.user} liberary.Enter your  choice to continue: ")
        print ("1. Display book")
        print ("2. Lend a book")
        print ("3. Add a book")
        print ("4. Return a book")
        choice = int(input("Enter your choice: "))

        if choice==1:
           tush.displaybooks()

        elif choice==2:
             book = input("Enter the name of the book you wanna lend: ")
             user = input("Enter your SeXy Name: ")
             tush.lendbook(user,book)

        elif choice==3:
             book = input("Enter the name of the book you wanna add: ")
             tush.addbook(book)

        elif choice==4:
             book = input("Enter the name of the book you wanna return: ")
             tush.returnbook(book)

        else:
            print ("\nNot a proper option cutieee. Try again...")
            print("Press q to quit and c to continue")
            user_choice2 = ""
            while(user_choice2!="c" and user_choice2!="q"):
                  user_choice2 = input()
                  if user_choice2 == "q":
                     exit()

                  elif user_choice2 == "c":
                       continue
#Add something new according to your preferences....
