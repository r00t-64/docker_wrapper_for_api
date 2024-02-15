import os

def set_vars(project_name, port):
    env_content = f"PROJECT_NAME={project_name}\nPORT={port}"
    with open('.env', 'w') as file:
        file.write(env_content)
    print(".env file created/updated successfully!")
    print("""
        Now clone your project to virtualize here!
        $  git clone ...
    """)


if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    port = input("Enter the port number: ")

    set_vars(project_name, port)
