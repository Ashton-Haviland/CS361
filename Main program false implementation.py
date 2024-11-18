import zmq
import time

# Set up ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send request to microservice
request = "Albert Einstein"
socket.send_string(request)
time.sleep(1)

# Receive response from microservice
response = socket.recv_string()
print(f"Received response: {response}")

if response == "not found":
    print("Page of that title not found"
          "Please try again with a different title")
    exit()

if response == "what type?":
    # Send second request to microservice
    request = "summary"
    socket.send_string(request)

    # Receive final response from microservice
    response = socket.recv_string()
    print(f"Brief Summary of Albert Einstein: {response}")

# EVERYTHING AGAIN TO SHOW IMAGES
# Send request to microservice
time.sleep(1)
request = "Albert Einstein"
socket.send_string(request)
time.sleep(1)

# Receive response from microservice
response = socket.recv_string()
print(f"Received response: {response}")

if response == "not found":
    print("Page of that title not found"
          "Please try again with a different title")
    exit()

if response == "what type?":
    # Send second request to microservice
    request = "photo"
    socket.send_string(request)

    # Receive final response from microservice
    response = socket.recv_string()
    print(f"Image URL from wikipedia:: {response}")
    exit()
