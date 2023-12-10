import requests
import subprocess

def jfrogUpload():
  # Define the URL, filepath, and authentication credentials
  url=''
  file_path='/var/lib/jenkins/workspace/projectname/target/'
  username='admin'
  password='admin@1234'
  # Send the PUT request with authentication and file upload
  with open(file_path, 'rb') as file:
     response=requests.put(url, auth=(username, password), data=file)
  # Check the response status code
  if response.status_code==201:
      print("\n PUT request was successful!")
  else:
        print(f'Put request failed with status code {response.status_code}')
        print('Response content:')
        print(response.text)
def mvnBuild():
  # Define the maven command
  maven_command='mvn clean install -DskipTests'
  # Run the maven command as a subprocess
  try:
    subprocess.run(maven_command, check=True,text=True,shell=True)
    print('\n maven build completed successfully')
  except subprocess.CalledProcessError as e:
     print(f'Error: Maven build failed with exit {e.returncode}')
def main():
  #mvnBuild()
  jfrogUpload()
if __name__=='__main__':
  main()
  
  
