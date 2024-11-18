Communication Contract(between Microservice A and main program.)
# How to REQUEST data from microservice. Microservice will continuously listen on the port, and when it receives initial request it is currently set to immediately 
#     check if there is a similar page with that name using wikipedia.suggest. It then expects after sending a "what type?" call to receive either "photo" or "summary", to which it 
#	will once again respond, this time with text, either the first 10 sentences of summary of page, or the first image's url on the wikipedia page.

# How to Receive Data from program: Microservice will send data through socket after specific input's are received, and data received will always be of text type.
	EXAMPLE CALL: 
request = "some user input/page fill from buttons"                    # MAIN PROGRAM TO MICROSERVICE
socket.send_string(request)	# sends initial request for wikipedia search		
response = socket.recv_string()       # either receive call to ask for type, or that page not found.
if response == "not found" 
display some form of invalid search attempt message	# if page not found, display error message and try again
if response == "what type"	# if what type asked, send the type request to receive response
socket.send_string(photo or summary from user input/button selection)	# send type to receive response "photo" or "summary"
	response = socket.recv_string()		# receive output information
	print(response)		# print response(do with what you will)









UML SEQUENCE DIAGRAM
![image](https://github.com/user-attachments/assets/04b278d1-efec-4957-b415-d60f0b762af5)

