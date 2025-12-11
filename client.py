import socket
import json

HOST = "127.0.0.1"
PORT = 5200

COURSES = {
    "1": "MSc in Cyber Security",
    "2": "MSc Information Systems & Computing",
    "3": "MSc Data Analytics"
}

def collect_input():
    name = input("Enter full name: ").strip()
    address = input("Enter address: ").strip()
    qualifications = input("Enter educational qualifications: ").strip()

    print("\nCourses:")
    for key, course in COURSES.items():
        print(f"  {key}. {course}")

    course_choice = input("Pick course (1/2/3): ").strip()
    course = COURSES.get(course_choice, COURSES["3"])

    start_year = input("Enter start year (YYYY): ").strip()
    start_month = input("Enter start month: ").strip()

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
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Is it running?")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    form_data = collect_input()
    send_to_server(form_data)
