import requests
import csv

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def write_data_to_csv(data, csv_filename):
    if not data:
        raise ValueError("No data to write to CSV.")
    
    header = data[0].keys()
    
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

def main():
    print("Welcome to APItoCSV!")
    api_url = input("Enter the API URL: ")
    csv_filename = input("Enter the desired CSV file name: ")
    
    try:
        data = fetch_data_from_api(api_url)
        write_data_to_csv(data, csv_filename)
        print(f"Data successfully written to {csv_filename}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred while fetching data from the API: {req_err}")
    except ValueError as val_err:
        print(f"An error occurred while writing to CSV: {val_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
