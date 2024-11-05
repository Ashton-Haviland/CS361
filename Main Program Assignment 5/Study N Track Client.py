# Main Program for Ashton Haviland's CS361 Assignment, client side,
# Handles basic menu interaction and allows user to access functionality that
# will be added later through microservices.  Uses ZeroMQ for communication pipeline
# Will convert to threading once adding microservices

import zmq 
import os

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def clear_screen():
    # code to clear terminal for different OS
    os.system('cls' if os.name == 'nt' else 'clear')

def check_for_subfolders(path):
    """Checks if a directory contains subfolders."""

    for entry in os.scandir(path):
        if entry.is_dir():
            return True

    return False


def main_application():
    while True:
        clear_screen()
        print("Welcome to Study’n Track note taking app!")
        print("Your one stop shop to Notes, tracking media, and study timers.")
        print()
        print('To view notes, type "Notes".')
        print('To view media, type "Media".')
        print('To access the pomodoro timer, type "Timer".')
        print('To exit, type "Exit" at any time.')
        print()

        choice = input("User Input: ")

        if choice == "Notes":
            subject_notes()
        elif choice == "Media":
            media()
        elif choice == "Timer":
            timer()
        elif choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def subject_notes():
    while True:
        clear_screen()
        print("Notes")
        print("Here you can create folders to store notes, and access notes for review.")
        print('To create a subject, type "Subject Create".')
        print("To access a subject, type the name of the subject")
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()
        print("Subjects:")

        # Need to implement on server side to send back all current subject names.
        # Sets a parent folder directory for subject storage, sends as a request to server,
        # receives list of subject names
        parent_folder = r"G:\VS Code\CS 361\Main Program Assignment 5\Subjects"
        socket.send_string(parent_folder)
        subjects = socket.recv_string().split("\n")
        for subfolder in subjects:
            print(subfolder)

        if not check_for_subfolders(parent_folder):
            print("No current subjects, please add a subject first.")

        choice = input("User Input: ")

        if choice == "Subject Create":
            subject_create()

        elif choice in subjects:
            notes(choice)

        elif choice == "Back":
            main_application()

        elif choice == "Exit":
            clear_screen()
            print("Exiting")
            break

    pass


def notes(choice):
    while True:
        clear_screen()
        subject = choice
        socket.send_string(choice)
        note_names = socket.recv_string().splitlines()

        print("These are the current notes for", choice)
        print('To create a new note type "New Note".')
        print("To create edit/review/delete a note, type the note name.")
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()
        print("Notes:")
        for file in note_names:
            print(file)

        note_choice = input("User Input: ")

        if note_choice == "New Note":
            new_note(choice)

        if note_choice in note_names:
            socket.send_string(note_choice)
            note_info = socket.recv_string().splitlines()
            clear_screen()
            print(note_choice)
            print()
            print("Editing, and the like is not yet implemented.")
            print('To go back, type "Back".')
            print('To exit, type "Exit".')
            print()
            print(note_info)
            print()
            user_input = input("User Input: ")

            if user_input == "Back":
                subject_notes()

            elif choice == "Exit":
                clear_screen()
                print("Exiting")
                break

        elif note_choice == "Back":
            notes(subject)

        elif choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def subject_create():
    while True:
        clear_screen()
        print("Create New subject")
        print()
        print("This is where you will create a new subject.")
        print('To create new subject, type "New"')
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()

        subject_choice = input("User Input: ")

        if subject_choice == "New":
            # Insert Logic For creating new note with name and description with prompts, send to
            # server to pass off to microservice to create note within folder.
            print('Not yet Implemented"Insert Microservice call".')

        elif subject_choice == "Back":
            subject_notes()

        elif subject_choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def new_note(choice):
    while True:
        print("Create New note for", choice)
        print("This is where you will create a new note.")
        print('To create new note, type "New"')
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()

        note_choice = input("User Input: ")

        if note_choice == "New":
            # Insert Logic For creating new note with name and description with prompts, send to
            # server to pass off to microservice to create note within folder.
            print("Not yet Implemented\"Insert Microservice call\"")

        elif note_choice == "Back":
            notes(choice)

        elif note_choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def media():
    while True:
        clear_screen()
        print("Media")
        print("Here you can create folders to store different types of media, access self made notes,")
        print("see a wikipedia summary, and rate it personally.")
        print('To create a media type, type "Media Type Create".')
        print("To access a media type, type the name of the media type.")
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()
        print("Media Types:")

        # Need to implement on server side to send back all current subject names.
        # Sets a parent folder directory for subject storage, sends as a request to server,
        # receives list of subject names
        parent_folder_media = r"G:\VS Code\CS 361\Main Program Assignment 5\Media"
        socket.send_string(parent_folder_media)
        media_types = socket.recv_string().split("\n")
        for subfolder in media_types:
            print(subfolder)

        if not media_types:
            print("No current Media Types, please add a Media Type first.")

        choice = input("User Input: ")

        if choice == "Media Type Create":
            media_subject_create()

        elif choice in media_types:
            media_type(choice)

        elif choice == "Back":
            main_application()

        elif choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def media_type(choice):
    while True:
        clear_screen()
        socket.send_string(choice)
        medias = socket.recv_string().splitlines()

        print("These are the current media for", choice)
        print('To create a new", choice," note type "New ', choice, ' Note".')
        print("To create edit/review/delete a media note, or view the wikipedia blurb, type the note name.")
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()
        print(choice, "Notes:")
        for file in medias:
            print(file)

        note_choice = input("User Input: ")

        if note_choice == ("New ", choice, " Note"):
            new_media_note(choice)

        if note_choice in medias:
            socket.send_string(note_choice)
            note_info = socket.recv_string().splitlines()
            clear_screen()
            print(note_choice, "Notes")
            print()
            print('To go back, type "Back".')
            print('To exit, type "Exit".')
            print()
            print(note_info)
            user_input = input("User Input: ")

            if user_input == "Back":
                media_type(choice)

            elif choice == "Exit":
                clear_screen()
                print("Exiting")
                break

        elif choice == "Back":
            media()

        elif choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def media_subject_create():
    while True:
        clear_screen()
        print("Create New Media Type")
        print()
        print("This is where you will create a new Media Type.")
        print('To create new media type, type "New"')
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()

        subject_choice = input("User Input: ")

        if subject_choice == "New":
            # Insert Logic For creating new note with name and description with prompts, send to
            # server to pass off to microservice to create note within folder.
            print("Not yet Implemented\"Insert Microservice call\"")

        elif subject_choice == "Back":
            media()

        elif subject_choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def new_media_note(choice):
    while True:
        print("Create New media note for", choice)
        print()
        print("This is where you will create a new media note.")
        print('To create new media note, type "New"')
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()

        note_choice = input("User Input: ")

        if note_choice == "New":
            # Insert Logic For creating new note with name and description with prompts, send to
            # server to pass off to microservice to create note within folder.
            print('Not yet Implemented "Insert Microservice call".')

        elif note_choice == "Back":
            media_type(choice)

        elif note_choice == "Exit":
            clear_screen()
            print("Exiting")
            break


def timer():
    while True:
        print("Welcome to the adjustable timer(pomodoro based) for Study N' Track!")
        print()
        print("This is currently not implemented, however when it is you will be prompted if you wish to")
        print("change any of the intervals, and what kind of alarm you would like. Potentially also a way")
        print("to track sessions total or on what days.")
        print()
        print('To go back, type "Back".')
        print('To exit, type "Exit".')
        print()

        choice = input("User Input: ")

        if choice == "Back":
            main_application()

        elif choice == "Exit":
            clear_screen()
            print("Exiting")
            break


if __name__ == "__main__":
    main_application()
