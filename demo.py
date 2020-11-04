class search_sort:
    list_1=[]                           # Data member of This class
    n1=0
    def list_input(self):
        self.list_1=[]
        self.n1=int(input("Enter the number of elements in the lists:"))
        print("Enter the Values:")
        for i in range(self.n1):
            elements=int(input())
            self.list_1.append(elements)

    pos=-1
    def __binary(self,list_1,n):                   # Main Logic of Binary search 
        l=0
        u=len(list_1)-1        
        while l<=u:
            mid=(l+u)//2
            if list_1[mid]==n:
                self.pos=mid
                return True
            else:
                if list_1[mid]<n:
                    l=mid+1
                else:
                    u=mid-1

    def __linear(self,list_1,n):                    # Main Logic of Linear search 
        for i in range(len(list_1)):
            if list_1[i]==n:
                self.pos =i
                return True
        return False

    def __bubble(self,list_1,n1):                    # Main Logic of Bubble sort 
        for i in range(len(list_1)-1,0,-1):
            for j in range(i):
                if list_1[j]>list_1[j+1]:
                    temp=list_1[j]
                    list_1[j]=list_1[j+1]
                    list_1[j+1]=temp
                    print(list_1)

    def __selection(self,list_1,n1):                   # Main Logic of Selection sort 
        for i in range(len(list_1)-1):
            minpos=i
            for j in range(i,len(list_1)):
                if list_1[j]<list_1[minpos]:
                    minpos=j
               
            temp=list_1[i]
            list_1[i]=list_1[minpos]
            list_1[minpos]=temp
            print(list_1)

    def __partition(self,list_1,start,end):                        # Main Logic of Quick sort(Both partition and quicksort function)
        pivot=list_1[end]
        partitionindex=start
        for i in range(start,end):
            if list_1[i]<=pivot:
                list_1[i],list_1[partitionindex]=list_1[partitionindex],list_1[i]  # swap using tuple assignment i.e a,b=b,a
                partitionindex=partitionindex+1
        list_1[partitionindex],list_1[end]=list_1[end],list_1[partitionindex]
        return partitionindex
    def __quicksort(self,list_1,start,end):
        if(start<end):
            partitionindex=self.__partition(list_1,start,end)                       
            self.__quicksort(list_1,start,partitionindex-1)
            self.__quicksort(list_1,partitionindex+1,end)
            print("sorting process:",list_1,)
    
    def __mergesort(self,list_1,n1):                                # Main Logic Of Merge Sort
        if len(list_1)>1:
            mid=len(list_1)//2
            left_list_1=list_1[:mid]
            right_list_1=list_1[mid:]
            self.__mergesort(left_list_1,n1)
            self.__mergesort(right_list_1,n1)
            i=0
            j=0
            k=0
            while i<len(left_list_1) and j<len(right_list_1):
                if left_list_1[i]<right_list_1[j]:
                    list_1[k]=left_list_1[i]
                    i+=1
                    k+=1
                else:
                    list_1[k]=right_list_1[j]
                    j+=1
                    k+=1
            while i<len(left_list_1):
                list_1[k]=left_list_1[i]
                i+=1
                k+=1
            while j<len(right_list_1):
                list_1[k]=right_list_1[j]
                j+=1
                k+=1
            print("Sorting Process",list_1)

    def __insertionsort(self,list_1,n1):                #Main Logic Of Insertion Sort
        for i in range(1,n1):
            value=list_1[i]
            hole=i-1
            while(hole>=0 and list_1[hole]>value):
                list_1[hole+1]=list_1[hole]
                hole=hole-1
            list_1[hole+1]=value
            print("Sorting Process",list_1)
    
    def is_found(self,list_1,n,searchtype="linear"):        # This function is used to access the private member function from main
        if(searchtype=="binary"):
            if self.__binary(list_1,n):
                print("\nBy using Binary Search, Element found at position:",(a.pos+1),"\n")
            else:
                print("\nElement Not Found\n")
               
        else:
            if self.__linear(list_1,n):
                print("\nBy using linear Search, Element found at position:",(a.pos+1),"\n")
            else:
                print("\nElement Not Found\n")

    def is_found1(self,list_1,n1,searchtype=""):    # This function is used to access the private member function from main
        if(searchtype=="bubble"):
            print("Before sorting:",list_1)
            self.__bubble(list_1,n1)
            print("After using Bubble Sort:",list_1)

        elif(searchtype=="selection"):
            print("Before sorting:",list_1)
            self.__selection(list_1,n1)
            print("After using Selection Sort:",list_1)

        elif(searchtype=="quick"):
            print("Before sorting",list_1)
            print(sep="\n")
            self.__quicksort(list_1,0,n1-1)
            print("\nAfter using Quick sort",list_1)
            print(sep="\n")

        elif(searchtype=="merge"):
            print("Before Sorting",list_1)
            print(sep="\n")
            self.__mergesort(list_1,n1)
            print("\nAfter using Merge Sort",list_1)
            print(sep="\n")
        else:
            print("Before Sorting",list_1)
            print(sep="\n")
            self.__insertionsort(list_1,n1)
            print("\nAfter using Insertion Sort",list_1)
            print(sep="\n")

    def binary_main_input(self):
        print("\nYou Choose Binary Search:\n")       # Binary input and print list
        self.list_input()
        print("Given list:",end="")
        print(self.list_1,"\n")

    def binary_main_checklist(self):                   # Checked if list is sorted or not
        flag = 0
        if(self.list_1 == sorted(self.list_1)): 
            flag = 1
        if (flag==1) : 
            print ("List is sorted, Now Press 3 for Searching") 
        else : 
            print ("List is not sorted, First Press 2 to Sort The List")
        time.sleep(2)
        
    def binary_main_sort(self):                                         # If list is not sorted then for sorting the list
        self.is_found1(self.list_1,self.n1,"quick")
        n=int(input("Enter a value from given list to search:"))
        binary_search_start_time=time.time()
        self.is_found(self.list_1,n,"binary")
        binary_search_end_time=time.time()
        print("Time taken by binary search:",binary_search_end_time - binary_search_start_time)
        input("\npress Enter to continue...")
        
    def binary_main_search(self):                                          # Searching Element in the list
        print("\nGiven list:",end="")
        print(self.list_1,"\n")
        n=int(input("Enter a value from given list to search:"))
        binary_search_start_time=time.time()
        self.is_found(self.list_1,n,"binary")
        binary_search_end_time=time.time()
        print("Time taken by binary search:",binary_search_end_time - binary_search_start_time)
        input("\npress Enter to continue...")

    def linear_main(self):                              # For Linear Search
        print("\nYou Choose Linear Search:\n")
        self.list_input()
        print("Given list:",end="")
        print(self.list_1,"\n")
        n=int(input("Enter a value from given list to search:"))
        linear_search_start_time=time.time()
        self.is_found(self.list_1,n,"linear")
        linear_search_end_time=time.time()
        print("Time taken by linear search:",linear_search_end_time - linear_search_start_time)
        input("\npress Enter to continue...")

    def bubble_main(self):                          # For Bubble Sort
        print("\nYou Choose Bubble Sort:\n")
        self.list_input()
        bubble_sort_start_time=time.time()
        self.is_found1(self.list_1,self.n1,"bubble")
        bubble_sort_end_time=time.time()
        print("\nTime taken by Bubble Sort:",bubble_sort_end_time - bubble_sort_start_time)
        input("\npress Enter to continue...")

    def selection_main(self):                       # For Selection Sort
        print("\nYou Choose Selection Sort:\n")
        self.list_input()
        selection_sort_start_time=time.time()
        self.is_found1(self.list_1,self.n1,"selection")
        selection_sort_end_time=time.time()
        print("\nTime taken by Selection Sort:",selection_sort_end_time - selection_sort_start_time)
        input("\npress Enter to continue...")

    def quick_main(self):                           # For Quick Sort
        print("\nYou Choose Quick Sort:\n")
        self.list_input()
        quick_sort_start_time=time.time()
        self.is_found1(self.list_1,self.n1,"quick")
        quick_sort_end_time=time.time()
        print("\nTime taken by Quick Sort:",quick_sort_end_time - quick_sort_start_time)
        input("\npress Enter to continue...")

    def merge_main(self):                           # For Merge Sort
        print("\nYou Choose Merge Sort:\n")
        self.list_input()
        merge_sort_start_time=time.time()
        self.is_found1(self.list_1,self.n1,"merge")
        merge_sort_end_time=time.time()
        print("Time taken by Merge Sort:",merge_sort_end_time - merge_sort_start_time)
        input("\npress Enter to continue...")

    def insertion_main(self):                       # For Insertion Sort
        print("\nYou Choose Insertion Sort:\n")
        self.list_input()
        insertion_sort_start_time=time.time()
        self.is_found1(self.list_1,self.n1,"insertion")
        insertion_sort_end_time=time.time()
        print("Time taken by Insertion Sort:",insertion_sort_end_time - insertion_sort_start_time)
        input("\npress Enter to continue...")

def clear():
        if name == 'nt':                # It is a Global Function & it used to clear the screen
            _ = system('cls') 
            
if __name__ == "__main__":                  # Main Function
    import time
    from os import system, name
    a=search_sort()                         # Object Creation
    while(1):                                               # Starting of Menu-driven Features
        print("---------------------------------")
        print("\n*****Main Menu*****\n")
        print("Press 1 For Searching\n")
        print("Press 2 For Sorting\n")
        print("Press 3 for Exit The Program\n")
        print("---------------------------------")
        Choice=int(input("Enter your choice:"))
        clear()
        if Choice==1:
            while(1):
                print("---------------------------------")
                print("\n*****Sub Menu For Searching*****\n")
                print("Press 1 For Binary Search\n")
                print("Press 2 For Linear Search\n")
                print("Press 3 For main menu\n")
                print("---------------------------------")
                ch=int(input("Enter Another Choice:"))
                if ch==1:
                    a.binary_main_input()
                    a.binary_main_checklist()
                    while(1):
                        print("---------------------------------")
                        print("\n*****Sub Menu For Binary Search******\n")
                        print("press 1 for New List\n")
                        print("Press 2 For Sorting the given array\n")
                        print("Press 3 For Search the element\n")
                        print("Press 4 to see the List\n")
                        print("Press 5 For Previous Menu\n ")
                        print("---------------------------------")
                        choose=int(input("Enter your Choice:"))
                        if choose==1:
                           a.list_input()
                           a.binary_main_checklist()

                        elif choose==2:
                            a.binary_main_sort()   

                        elif choose==3:
                            a.binary_main_search()

                        elif choose==4:
                            print("\nGiven list:",end="")
                            print(a.list_1,"\n")
                            input("\npress Enter to continue...")
                            
                            
                        elif choose==5:
                            clear()
                            break

                        else:
                            print("\nWrong Entry,Type Between 1-3")
                            input("\npress Enter to continue...")

                elif ch==2:
                    a.linear_main()
                    
                elif ch==3:
                    clear()
                    break
                else:
                    print("\nWrong Entry,Type Between 1-3")
                    input("\npress Enter to continue...")

        elif Choice==2:
            while(1):
                print("---------------------------------")
                print("\n*****Sub Menu For Sorting*****\n")
                print("Press 1 For Bubble Sort\n")
                print("Press 2 For Selection Sort\n")
                print("Press 3 For Quick Sort\n")
                print("Press 4 For Merge Sort\n")
                print("press 5 For Insertion Sort\n")
                print("Press 6 For main menu\n")
                print("---------------------------------") 
                ch=int(input("Enter Another Choice:"))
                if ch==1:
                    a.bubble_main()  

                elif ch==2:
                    a.selection_main() 

                elif ch==3:
                    a.quick_main()
                    
                elif ch==4:
                    a.merge_main()
                
                elif ch==5:
                    a.insertion_main()
                    
                elif ch==6:
                    clear()
                    break
                else:
                    print("\nWrong Entry,Type Between 1-4")
                    input("\npress Enter to continue...")

        elif Choice==3:
            print("\nExiting The Program.......\n")
            time.sleep(2)
            print("Done Successfully!!\n")
            exit()   
        else:
            print("\nWrong Entry,Type Between 1-3")
            input("\npress Enter to continue...")

        # Ending The Program

      
            

            
        
        
    



