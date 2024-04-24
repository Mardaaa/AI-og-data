import requests

def load_dataset(url):
    response = requests.get(url)
    if response.status_code == 200:
        # If the request is successful, read the content
        content = response.text
        # Process the content here
        # For example, you can split lines and extract data
        lines = content.split('\n')
        # Process each line as needed
        for line in lines:
            # Example: print the first 5 lines
            print(line)
            if len(line) == 0:
                break
    else:
        # If the request fails, print an error message
        print("Failed to fetch data from:", url)

# URL of the dataset
url = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_complete.txt"

# Call the function to load the dataset
load_dataset(url)
