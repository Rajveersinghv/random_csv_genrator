## random_csv_generator

**random_csv_generator** is a Python script that generates random CSV samples for different categories: Organizations, People, and Customers. This tool is perfect for developers, data scientists, and anyone who needs synthetic data for testing, development, or educational purposes.

### Features
- **Organizations CSV Samples**: Generates random data for organizations, including fields like Organization Id, Name, Website, Country, Description, Founded, Industry, and Number of Employees.
- **People CSV Samples**: Generates random data for individuals, including fields like User Id, First Name, Last Name, Sex, Email, Phone, Date of Birth, and Job Title.
- **Customers CSV Samples**: Generates random data for customers, including fields like Customer Id, First Name, Last Name, Company, City, Country, Phone 1, Phone 2, Email, Subscription Date, and Website.
- **Chunk Handling**: Efficiently handles large data generation by saving data in chunks and combining them into a single CSV file.
- **Progress Tracking**: Saves progress and allows resuming from where it left off in case of interruptions.
- **Automatic Folder Creation**: Automatically creates a "sample" folder to save the generated CSV files.
- **Auto Resume**: Automatically resumes data generation from the last saved progress in case of interruptions.
- **Chunk Deletion**: Deletes chunk files after combining them into the final CSV file.

### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/random_csv_generator.git
   ```
2. Install the required libraries:
   ```bash
   pip install pandas faker tqdm
   ```
3. Run the script and follow the prompts to generate the desired CSV samples:
   ```bash
   python random_csv_generator.py
   ```

### License
This project is licensed under the MIT License
