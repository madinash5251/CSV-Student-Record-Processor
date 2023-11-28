import pandas as pd

def load_csv(file_path):
    try:
        # Read CSV file using pandas read_csv function
        df = pd.read_csv(file_path)

        # Convert grade columns to numeric values using to_numeric method
        grade_columns = ['Math', 'English', 'History']
        for col in grade_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Check for non-convertible values and replace them with zeros
        df[grade_columns] = df[grade_columns].fillna(0).astype(int)

        # Calculate average scores by taking mean of grade columns
        df['Average'] = df[grade_columns].mean(axis=1)

        # Sort students by their average scores in descending order
        sorted_data = df.sort_values(by='Average', ascending=False)

        # Save sorted data to a text file using save_to_txt function
        save_to_txt(sorted_data)

        return sorted_data, None  # Return sorted data and no error
    except Exception as e:
        return None, f"Error loading CSV file: {e}"  # Return None and error message if an exception occurs

def save_to_txt(dataframe):
    try:
        # Write sorted student names and their average scores to a text file
        with open('sorted_students.txt', 'w') as file:
            file.write("Sorted Students (Name, Average):\n")
            for index, row in dataframe.iterrows():
                file.write(f"{row['Name']}, {row['Average']:.2f}\n")
    except Exception as e:
        print(f"Error saving to text file: {e}")  # Print error message if saving to text file fails
