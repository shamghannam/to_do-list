tasks=[]

def add_task(task):
    tasks.append(task)
    print(f"Task '{tasks}'")

def show_tasks():
        print("your to do list:")
        for index, task in enumerate(tasks,1):
           print(f"{index}.{task}")
     
def delete_tasks(index):
     if 1<=index <=len(tasks):
          deleted_task=tasks.pop(index-1)
          print("the delete had done", deleted_task)   
        
     else:
        print("the num you enter did not exist")

while True:
     print("choose a procedure")
     print("1-Add tasks")
     print("2-Show tasks")
     print("3-Delete tasks")
     print("4-Exit")
    
     choice=input("enter a number of procedure from num(1,2,3,4)")
    
     if choice=="1":
          new_task=input("Enter new task")
          add_task(new_task)

     elif choice=="2":
          show_tasks()

     elif choice=="3":
          number_to_delete=int(input("Enter the task number to be deleted:"))
          delete_tasks(number_to_delete)

     elif choice=="4":
          print("exit done")
          break
     
     else:
          print("wrong choice")

          
     
    
   
          

          




            
      