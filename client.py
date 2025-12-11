import socket
import json

HOST = "127.0.0.1"
PORT = 5200

def collect_input():
    name = input("Enter full name: ")
    address = input("Enter address: ")
    qualifications = input("Enter educational qualifications: ")

    print("\nCourses:")
    print("1. MSc in Cyber Security")
    print("2. MSc Information Systems & Computing")
    print("3. MSc Data Analytics")

    course_choice = input("Pick course (1/2/3): ")

    if course_choice == "1":
        course = "MSc in Cyber Security"
    elif course_choice == "2":
        course = "MSc Information Systems & Computing"
    else:
        course = "MSc Data Analytics"

    start_year = input("Enter start year (YYYY): ")
    start_month = input("Enter start month: ")

    return {
        "name": name,
        "address": address,
        "qualifications": qualifications,
        "course": course,
        "start_year": start_year,
        "start_month": start_month
    }


def send_to_server(data):
    try:
        json_data = json.dumps(data)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        client_socket.send(json_data.encode())

        response = client_socket.recv(4096).decode()
        print("\n--- Server Response ---")
        print(response)

        client_socket.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    form_data = collect_input()
    send_to_server(form_data)
