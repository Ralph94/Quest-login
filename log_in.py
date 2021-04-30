
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from time import sleep
import sys
import sound

image = Image.open("lab.PNG")
image2 = Image.open("load.JPG")
image3 = Image.open("load2.PNG")
image4 = Image.open("spec.JPG")
image.show()
print("")



class Quest:
	def __init__(self, name_login,
	login_password):
		self.name_login = name_login
		self.login_password = login_password
		
		
	def medical(self):
		User_ID = input("Employee I.D: ")
		if User_ID == "Rafael.X.Perez":
			password = input("Password: ")
			if password == "Test123":
				print("login accepted")
				sound.play_effect('login-accepted.mp3')
			else:
				print("Incorrect Try again")
				sys.exit()
		
		
	def loading(self):
		sleep(3)
		image2.show()
		print('Before Proceeding Fill Out Information: ')
		print("")
		numofthings=int(input("How many stops did you have today? "))
		print("")
		numoftasks=int(input("How many specimens did you pick up "))
		checklist1=[]
		end=' '
		while end.lower()!='end':
			item=input("Please enter the Accounts you picked up today: ")
			checklist1.append(item)
			print(checklist1)
			end=item
			
			
	def loading2(self):
		print("Okay Processing...")
		sound.play_effect("data-stream.mp3")
		sleep(5)
		image3.show()
			
	
		
		
		
		
	def info(self):
		sleep(3)
		print("")
		print('SPECIMEN PICK UPS FOR TODAY!')
		image4.show()
		print("")
		info_d = ("{} {} {} {}".format(*["•Valencia ", "•QLS ", "•WestHills", "•Pap"]))
		print(info_d[0:9])
		print(info_d[10:15])
		print(info_d[16:27])
		print(info_d[28:33])
	
		
		
		
		
		


quest = Quest('Rafael.X.Perez', '324255')

quest.medical()

quest.loading()

quest.loading2()

quest.info()



#PieChart
sleep(5)
x = np.array([35, 25, 25, 15])

mylables2 = [
	
"QLS 35%", 
"Valenica 25%", 
"WestHills 25%", 
"Pap 15%"

]

plt.pie(x, labels = mylables2)
plt.show()





