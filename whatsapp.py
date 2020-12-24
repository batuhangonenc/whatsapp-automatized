import pywhatkit,re
from datetime import datetime as dt

receivers = []


print("\n\n\nfor stop the loop 'q'.\n\n\n")

while 1:
	
	pattern=r"^\+[0-9]* [0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9] [0-9][0-9]$"

	num = input("enter a phone number (ex -> +90 xxx xxx xx xx) :")

	match = re.match(pattern,num)

	if not(match) and not(num == "q"):
		print("\nunvalid input type.")
		continue


	elif num == "q":
		break

	generalstr = ""

	for i in receivers:
		generalstr += i


	if generalstr.count(num) == 0:

		message = input(f"enter your message to {num} :")

		while 1:
			pat2 = r"^[0-9]{1,2}"
			
			hour = input("enter a hour :")

			match = re.match(pat2,hour)

			if not(match):
				print("\nunvalid input type.")
				continue



			minute = input("enter a minute :")
			match = re.match(pat2,minute)

			if not(match):
				print("\nunvalid input type")
				continue

			break

		

		content = f"{num}$@${message}$@${hour}$@${minute}"

		receivers.append(content)

	else:
		print("--\nthis phone num is already in list.\n")


for messages in receivers:
	data = messages.split("$@$")

	try:

		pywhatkit.sendwhatmsg(data[0],data[1],int(data[2]),int(data[3]))
		print(f"---\nmessage sent successfully : {data[0]}")


	except:
		print(f"--\nsomething went wrong : {data[0]}.")

