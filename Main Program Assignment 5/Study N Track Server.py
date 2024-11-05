# Server side program for Ashton Haviland CS361 assignment.
# This side will handle calling to the different microservices after receiving response from primary program.

import zmq
import os


def append_subfolder(base_path, subfolder):
    """Appends a subfolder to a given file path."""

    return os.path.join(base_path, subfolder)

# Example usage:
# base_path = "/home/user/documents"
# subfolder = "projects"
# new_path = append_subfolder(base_path, subfolder)


def main():
    context = zmq.Context()

    # Create a REP (reply) socket
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        # Wait for a request from the client
        message = socket.recv_string()

        parent_folder = r"G:\VS Code\CS 361\Main Program Assignment 5\Subjects"
        subfolder = os.path.join(parent_folder, message)

        subfolders = [
            f for f in os.listdir(parent_folder) 
            if os.path.isdir(os.path.join(parent_folder, f))
            ]
        
        files = [
            f for f in os.listdir(subfolder) 
            if os.path.isfile(os.path.join(subfolder, f))
            ]

        # Handle the menu option
        if message == parent_folder:
            # Request for when user enters notes, to see subjects
            socket.send_string("\n".join(subfolders))

        elif message in subfolders:
            while True:
                socket.send_string("\n".join(files))
                message = socket.recv_string()

                if message in files:
                    response = "this is where you would see note information, once microservice is set up!"
                    socket.send_string(response)

        # THIS SECTION IS TO HANDLE THE MEDIA ASSIGNMENTS
        parent_folder_media = r"G:\VS Code\CS 361\Main Program Assignment 5\Media"
        subfolder = os.path.join(parent_folder, message)

        subfolders = [
            f for f in os.listdir(parent_folder_media) 
            if os.path.isdir(os.path.join(parent_folder_media, f))
            ]
        
        files = [
            f for f in os.listdir(subfolder) 
            if os.path.isfile(os.path.join(subfolder, f))
            ]

        # Handle the menu option
        if message == parent_folder_media:
            # Request for when user enters notes, to see Media types
            socket.send_string("\n".join(subfolders))

        elif message == parent_folder_media:
            socket.send_string("\n".join(subfolders))

        elif message in subfolders:
            while True:
                socket.send_string("\n".join(files))
                message_1 = socket.recv_string()

                if message_1 in files:
                    response = "This is where you would see media note information, once microservice is set up!"
                    socket.send_string(response)

        if message in files:
            text = "Implement communication w/ microservice to access/review/update/delete notes/view wikipedia blurbs."
            socket.send_string(text)

        # THIS IS SECTION TO BE IMPLEMENTED FOR TIMER FUNCTIONALITY.


if __name__ == "__main__":
    main()
