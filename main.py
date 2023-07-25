import requests
import pandas as pd

url = "https://trackingpackage.p.rapidapi.com/TrackingPackage"

headers = {
	"Authorization": "Basic Ym9sZGNoYXQ6TGZYfm0zY2d1QzkuKz9SLw==",
	"X-RapidAPI-Key": "fea76a78e2msh6ceeb99b809a476p150fb7jsn56411c2365be",
	"X-RapidAPI-Host": "trackingpackage.p.rapidapi.com"
}

def track_numbers(tracking_numbers):
  for tracking_number in tracking_numbers:
    querystring = {"trackingNumber":tracking_number}

    try:
      response = requests.get(url, headers=headers, params=querystring).json()
    except:
      print("Error with connection to api")
    
    print("----------------------------------------------")
    print("\nTracking Number: " + tracking_number, end='\n')
    print("Status: ", response.get('Status', 'None'), end='\n')
    print("Service Type: ", response.get('ServiceType', 'None'), end='\n')
    print("Delivered Date/Time:", response.get("DeliveredDateTimeInDateTimeFormat", "None"), end='\n')
    print("----------------------------------------------")

def track_file(file):
  df = pd.read_excel(file)
  tracking_numbers = []
  for cell_value in df['Tracking']:
    if pd.notna(cell_value):
      tracking_numbers.append(cell_value)
  track_numbers(tracking_numbers)
       
  
while True:
    
	choices = input("""Enter your choice:\n
1 - Track pages by entering tracking numbers\n
2 - Track pages pages by uploading an Excel file\n
Input: """)

	if choices == "1":
		tracking_numbers = input("Enter your tracking numbers: ")
		tracking_numbers = tracking_numbers.split(",")
		track_numbers(tracking_numbers)
	elif choices == "2":
		file = input("Enter the file path: ")
		track_file(file)
	else:
		print("Invalid input\n")