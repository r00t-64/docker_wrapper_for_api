import re, os

def set_vars(project_name, port):
    # Read Dockerfile content
    with open('Dockerfile', 'r') as file:
        dockerfile_content = file.read()

   # Use regular expression to find and replace the value after ARG PROJECT_NAME=
    pattern = r'ARG PROJECT_NAME=(.*)\n'
    dockerfile_content = re.sub(pattern, f'ARG PROJECT_NAME={project_name}\n', dockerfile_content)

    pattern = r'ARG PORT=(.*)\n'
    dockerfile_content = re.sub(pattern, f'ARG PORT={port}\n', dockerfile_content)

    # Write back to Dockerfile
    with open('Dockerfile', 'w') as file:
        file.write(dockerfile_content)
    
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
