
class Telephonebook:
	def __init__(self,name,telno):
		self.name=name
		self.telno=telno
		
def insertion_lp():
	hashtable=[None for i in range(10)]
	num_records=int(input("Enter the number of records:"))
	for i in range(num_records):
		n=input("Enter the name of the person:")
		tel=int(input("enter the telephone number:"))
		hashvalue=tel%10
		if(hashtable[hashvalue] is None):
		
			hashtable[hashvalue]=Telephonebook(n,tel)
		
		else:
		
			for j in range(num_records):
				newHvalue=(hashvalue+j)%10
				if(hashtable[newHvalue] is None):
				 
					hashtable[newHvalue]=Telephonebook(n,tel)
					break
				
	return hashtable
	
def insertion_qp():
	hashtable=[None for i in range(10)]
	num_records=int(input("Enter the number of records:"))
	for i in range(num_records):
		n=input("Enter the name of the person:")
		tel=int(input("enter the telephone number:"))
		hashvalue=tel%10
		if(hashtable[hashvalue] is None):
		
			hashtable[hashvalue]=Telephonebook(n,tel)
		
		else:
		
			for j in range(1,num_records):
				newHvalue=(hashvalue+j**2)%10
				if(hashtable[newHvalue] is None):
				 
					hashtable[newHvalue]=Telephonebook(n,tel)
					break
				
	return hashtable
	
def double_hash():
	hashtable=[None for i in range(10)]
	num_records=int(input("Enter the number of records:"))
	for i in range(num_records):
		n=input("Enter the name of the person:")
		tel=int(input("enter the telephone number:"))
		hashvalue=tel%10
		if(hashtable[hashvalue] is None):
		
			hashtable[hashvalue]=Telephonebook(n,tel)
		
		else:
		
			for j in range(1,num_records):
				newHvalue=(hashvalue+j*(7-(tel%7)))%10
				if(hashtable[newHvalue] is None):
				 
					hashtable[newHvalue]=Telephonebook(n,tel)
					break
				
	return hashtable
	
def search_name(hash1):
	name=input("Enter the name to be searched:")
	for obj in hash1:
		if(obj is not None and obj.name==name):
			print("name found at index:",hash1.index(obj))
			return 0
	print("name not present!")	
			

def display(hash1):
	for obj in hash1:
		if(obj is not None):
			print(hash1.index(obj),obj.name,obj.telno)
		
def main():
	while(True):
		print("Choose the type of hashing!")
		print("\n1.Linear Probing,search name")
		print("\n2.Quadratic Probing")
		print("\n3.Double Hashing")
		print("\n4.Exit")
		ch=int(input())
		hash1=[None for i in range(10)]
		if(ch==1):
			
			hash1=insertion_lp()
			display(hash1)
			search_name(hash1)
		elif(ch==2):
			
			hash1=insertion_qp()
			display(hash1)
		elif(ch==3):
			
			hash1=double_hash()
			display(hash1)
		elif(ch==4):
			print("\nProgram terminated!")
			break
		else:
			print("Invalid choice!!!enter correct choice")
	
main()
tele.py
Displaying tele.py.
