import os
import json
from dotenv import load_dotenv
from graph import create_workflow

def main():
    # Load environment variables
    try:
        load_dotenv()
        print("Environment variables loaded successfully.")
    except Exception as e:
        print(f"Failed to load environment variables: {str(e)}")
        return  # Exit if environment loading fails

    # Initialize the workflow
    try:
        chain = create_workflow()
        print("Workflow initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize the workflow: {str(e)}")
        return  # Exit if workflow initialization fails

    # Specify the resume file to process
    file_path = r"C:\Projects\project\resume.pdf"

    # Ensure the file exists before processing
    if not os.path.isfile(file_path):
        print(f"Resume file does not exist: {file_path}")
        return  # Exit if the file does not exist

    try:
        # Process the resume
        result = chain.invoke(file_path)
        print("Resume processed successfully.")
    except Exception as e:
        print(f"Processing failed: {str(e)}")
        return  # Exit if processing fails

    # Specify output JSON file path
    output_file_path = r"C:\Projects\project\output.json"

    try:
        # Write result to JSON file
        with open(output_file_path, 'w') as json_file:
            json.dump(result, json_file, indent=4)  # Use indent for pretty printing
        print(f"Output written to: {output_file_path}")
    except IOError as e:
        print(f"Failed to write to JSON file: {str(e)}")
    except TypeError as e:
        print(f"Failed to serialize result to JSON: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred while writing to JSON: {str(e)}")

if __name__ == "__main__":
    main()