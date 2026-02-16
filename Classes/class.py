class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"{self.name} deposited ${amount}. New balance: ${self.balance}")
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("your account has insufficient bank balance , you have only:$",self.balance)
    def show_balance(self):
        print("your current balance is:$",self.balance)
    def transfer(self,amount,to_amount):
        if amount > self.balance:
            print(f"{self.name} your account has insufficient bank balance {self.balance}")
        else:
            self.balance -= amount
            to_amount.balance += amount
            print(f"transferred {amount} from {self.name} to {to_amount.name}")


account1 = BankAccount("Yashika", 1000)
account2 = BankAccount("kamalesh", 500)

account1.deposit(500)

account2.withdraw(200)

account1.show_balance()
account2.show_balance()

account1.transfer(2000,account2)



# 2
class LibraryBook:
    def __init__(self,title,author,available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow_book(self,borrow):
        if borrow >= self.available_copies:
            print(f"only we have {self.available_copies} books but you asked {borrow} books")
        else:
            self.available_copies -= borrow
            print(f"total {self.available_copies}")
    def return_book(self,increase):
        self.available_copies += increase 
        print(f"total {self.available_copies}") 
    def show_status(self):
        print(f"Title {self.title} Author {self.author} and Available copies are {self.available_copies}") 

book1= LibraryBook("Singam","Yashika",3)
book2 = LibraryBook("Jungle Book","Aniruth",4)

book1.show_status()
book1.borrow_book(1)
book1.return_book(1)
book1.borrow_book(4)

class MovieTicket:
    def __init__(self):
        self.final = []
    def add_movie(self,title,price,total_avl):
        now ={"title":title,"price":price,"total_avl":total_avl}
        self.final.append(now)
        print(self.final)
    def book_ticket(self,title,book):
        pass


    def cancel_ticket(self,title,price,total_avl,book):
        t = total_avl + book
        print(t)
    def show(self):
        print(self.final)
movie1=MovieTicket()
movie1.add_movie("Jananayagan",200,500)
movie1.book_ticket("Jananayagan",book=2)        


class MovieTickets:
    # constructor
    def __init__(self):
        self.movies = []

    # methods
    def add_movie(self, title, price, seat):
        # current movie
        current_movie = {"title": title, "price": price, "seats": seat}
        # appending the movie to existing movies list
        self.movies.append(current_movie)
        print(f"Admin has added the movie - {title}")

    def book_ticket(self, curr_show, friends_count):
        # count - {seat} = revised_count
        for el in self.movies:
            # finding title of movie
            if el["title"] == curr_show:
                # seat - decrease
                if friends_count > el["seats"]:
                    return "Invalid Ticket count"
                else:
                    el["seats"] -= friends_count
                    print(f"{curr_show} - tickets {friends_count} sold out ")

    def cancel_ticket(self, title, count):
        pass

    def check_availability(self, title):
        result = 0
        for el in self.movies:
            if title == el["title"]:
                result = el["seats"]
        print(f"{title} - current seat is {result}")

    # extra method
    def print_movies(self):
        print(self.movies)


# bsr mall
mall_bsr = MovieTickets()
mall_bsr.add_movie(title="Interstellar", price=200, seat=100)
mall_bsr.add_movie(title="Tenet", price=250, seat=150)

# print entire movies
mall_bsr.print_movies()

# check availability
mall_bsr.check_availability("Tenet")

# ticket booking
mall_bsr.book_ticket(curr_show="Interstellar", friends_count=20)
mall_bsr.print_movies()
mall_bsr.book_ticket(curr_show="Interstellar", friends_count=30)
mall_bsr.check_availability(title="Interstellar")


class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self,id:int,task:str):
        cur_task={}
        cur_task["id"] = id
        cur_task["task"] =task
        cur_task["status"]= "pending"
        self.tasks.append(cur_task)
        print("task added successfully")
    def view_task(self):
        print(self.tasks)
    def delete_task(self,id):
        for el in self.tasks:
            if el["id"] == id:
                self.tasks.remove(el)
        print("deleted successfully")
    def status(self,id):
        for el in self.tasks:
            if el["id"] == id:
                el["status"]= "completed"
    def filter_completed(self,status):
        for el in self.tasks:
            if el["status"] == "completed":
                print(el)
    def clear_all(self):
        for el in self.tasks:
            self.tasks.remove(el)
        print("truncate")
task1=TodoList()
task1.add_task(1,"buy vegetables")
task1.add_task(2,"Read 30mins")
task1.view_task()
# task1.delete_task(1)
task1.view_task()
task1.status(1)
task1.view_task()
task1.filter_completed("completed")
task1.clear_all()
task1.view_task()


class Orders:
    def __init__(self):
        self.cart=[]
        # final=0
    def add_item(self,id,pro_name,quantity,price):
        cur_cart={"id":id,"product_name":pro_name,"quantity":quantity,"price":price}
        self.cart.append(cur_cart)
        print("success")
    def remove(self,id):
        for el in self.cart:
            if el["id"]==id:
                self.cart.remove(el)
        print("remove")
    def view(self):
        print(self.cart)
    def total(self,id):
        for el in self.cart:
            if el["id"]==id:
                final=el["quantity"]*el["price"]
        print(final)
ord1=Orders()
ord1.add_item(1,"potato",2,50)
ord1.add_item(2,"tomato",4,50)
# ord1.remove(1)
ord1.view()
ord1.total(1)
ord1.total(2)


class AppointmentList:
    def __init__(self):
        self.appointments = []

class AppointmentBooking(AppointmentList):
    def __init__(self):
        super().__init__()
    def book_appointment(self,id: int, patient: str, doctor: str, time: str):
        curr_appointment={"id":id,"patient":patient,"doctor":doctor,"time":time}
        self.appointments.append(curr_appointment)
    def cancel_appointment(self,id):
        for el in self.appointments:
            if el["id"]==id:
                self.appointments.remove(el)
        print("canceled")
    def reschedule_appointment(self,id, new_time):
        for el in self.appointments:
            if el["id"]==id:
                el["time"]=new_time
        print("rescheduled")
    def view_all_appointments(self):
        print(self.appointments)

app1=AppointmentBooking()
app1.book_appointment(1,"yashika","John","3:00pm")
app1.book_appointment(2,"Vijay","ajith","3:30pm")
app1.view_all_appointments()
# app1.cancel_appointment(2)
# app1.view_all_appointments()
app1.reschedule_appointment(1,"5:00pm")
app1.view_all_appointments()













    



        
        







