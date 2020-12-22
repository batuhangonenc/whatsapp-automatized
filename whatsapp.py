import pywhatkit

receivers = []

print("\n\n\nfor stop the loop 'q'.\n\n\n")

while 1:

	num = input("enter a phone number (ex --> +90 xxx xxx xx xx) :")

	generalstr = ""
	for i in receivers:
		generalstr += i

	if num == "q":
		break
		
	elif generalstr.count(num) == 0:
		
		hour = int(input("enter a hour :"))
		
		minute = int(input("enter minute:"))
		
		message = input("enter your message :")

		content = f"{num}$@${message}$@${hour}$@${minute}"

		receivers.append(content)

	else:
		print("this phone num is already in list.\n\n")
		continue




for num in receivers:
	try:
		data = num.split("$@$")
		pywhatkit.sendwhatmsg(data[0],data[1],data[2],data[3])
		print(f"\nmessage sent : {num}")
	except:
		print("***\nsomething went wrong.")

	