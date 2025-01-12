import os
import pandas as pd
from faker import Faker
from tqdm import tqdm
import pickle

fake = Faker()

def generate_customers_csv(num_records, chunk_size, file_path, progress_file):
    data = []
    start_index = 0

    # Check if progress file exists
    if os.path.exists(progress_file):
        with open(progress_file, 'rb') as f:
            start_index = pickle.load(f)

    for i in tqdm(range(start_index, num_records), desc="Generating Customers CSV"):
        data.append([
            i,  # Index
            fake.uuid4(),  # Customer Id
            fake.first_name(),  # First Name
            fake.last_name(),  # Last Name
            fake.company(),  # Company
            fake.city(),  # City
            fake.country(),  # Country
            fake.phone_number(),  # Phone 1
            fake.phone_number(),  # Phone 2
            fake.email(),  # Email
            fake.date_this_decade(),  # Subscription Date
            fake.url()  # Website
        ])

        # Save chunk to CSV
        if (i + 1) % chunk_size == 0 or i + 1 == num_records:
            df = pd.DataFrame(data, columns=[
                "Index", "Customer Id", "First Name", "Last Name", "Company", "City", "Country",
                "Phone 1", "Phone 2", "Email", "Subscription Date", "Website"
            ])
            chunk_file_path = f"{file_path}_part_{i // chunk_size + 1}.csv"
            df.to_csv(chunk_file_path, index=False)
            data = []

            # Save progress
            with open(progress_file, 'wb') as f:
                pickle.dump(i + 1, f)

def generate_people_csv(num_records, chunk_size, file_path, progress_file):
    data = []
    start_index = 0

    # Check if progress file exists
    if os.path.exists(progress_file):
        with open(progress_file, 'rb') as f:
            start_index = pickle.load(f)

    for i in tqdm(range(start_index, num_records), desc="Generating People CSV"):
        data.append([
            i,  # Index
            fake.uuid4(),  # User Id
            fake.first_name(),  # First Name
            fake.last_name(),  # Last Name
            fake.random_element(elements=("M", "F")),  # Sex
            fake.email(),  # Email
            fake.phone_number(),  # Phone
            fake.date_of_birth(),  # Date of birth
            fake.job()  # Job Title
        ])

        # Save chunk to CSV
        if (i + 1) % chunk_size == 0 or i + 1 == num_records:
            df = pd.DataFrame(data, columns=[
                "Index", "User Id", "First Name", "Last Name", "Sex", "Email", "Phone", "Date of birth", "Job Title"
            ])
            chunk_file_path = f"{file_path}_part_{i // chunk_size + 1}.csv"
            df.to_csv(chunk_file_path, index=False)
            data = []

            # Save progress
            with open(progress_file, 'wb') as f:
                pickle.dump(i + 1, f)

def generate_organizations_csv(num_records, chunk_size, file_path, progress_file):
    data = []
    start_index = 0

    # Check if progress file exists
    if os.path.exists(progress_file):
        with open(progress_file, 'rb') as f:
            start_index = pickle.load(f)

    for i in tqdm(range(start_index, num_records), desc="Generating Organizations CSV"):
        data.append([
            i,  # Index
            fake.uuid4(),  # Organization Id
            fake.company(),  # Name
            fake.url(),  # Website
            fake.country(),  # Country
            fake.catch_phrase(),  # Description
            fake.year(),  # Founded
            fake.bs(),  # Industry
            fake.random_int(min=1, max=10000)  # Number of employees
        ])

        # Save chunk to CSV
        if (i + 1) % chunk_size == 0 or i + 1 == num_records:
            df = pd.DataFrame(data, columns=[
                "Index", "Organization Id", "Name", "Website", "Country", "Description", "Founded", "Industry", "Number of employees"
            ])
            chunk_file_path = f"{file_path}_part_{i // chunk_size + 1}.csv"
            df.to_csv(chunk_file_path, index=False)
            data = []

            # Save progress
            with open(progress_file, 'wb') as f:
                pickle.dump(i + 1, f)

def combine_chunks(file_path, num_chunks):
    combined_df = pd.concat([pd.read_csv(f"{file_path}_part_{i + 1}.csv") for i in range(num_chunks)])
    combined_df.to_csv(f"{file_path}.csv", index=False)

    # Delete chunk files
    for i in range(num_chunks):
        os.remove(f"{file_path}_part_{i + 1}.csv")

def main():
    print("Select the type of random data you want to generate:")
    print("1: Organizations CSV Samples")
    print("2: People CSV Samples")
    print("3: Customers CSV Sample")
    choice = input("Enter your choice (1/2/3): ")

    num_records = int(input("Enter the number of records you want to generate: "))
    chunk_size = 10000  # Adjust the chunk size as needed

    # Create "sample" folder if it doesn't exist
    if not os.path.exists("sample"):
        os.makedirs("sample")

    if choice == "1":
        file_path = "sample/organizations"
        progress_file = "sample/organizations_progress.pkl"
        generate_organizations_csv(num_records, chunk_size, file_path, progress_file)
        combine_chunks(file_path, (num_records + chunk_size - 1) // chunk_size)
    elif choice == "2":
        file_path = "sample/people"
        progress_file = "sample/people_progress.pkl"
        generate_people_csv(num_records, chunk_size, file_path, progress_file)
        combine_chunks(file_path, (num_records + chunk_size - 1) // chunk_size)
    elif choice == "3":
        file_path = "sample/customers"
        progress_file = "sample/customers_progress.pkl"
        generate_customers_csv(num_records, chunk_size, file_path, progress_file)
        combine_chunks(file_path, (num_records + chunk_size - 1) // chunk_size)
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

if __name__ == "__main__":
    main()
