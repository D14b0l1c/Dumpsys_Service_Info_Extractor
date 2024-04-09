import os
import re

def extract_service_info(dumpsys_file):
    """Extract information for each service"""
    service_info = {}
    current_service = None
    try:
        with open(dumpsys_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            current_text = []  # Initialize current text list
            for line in lines:
                line = line.strip()
                if line.startswith('DUMP OF SERVICE'):
                    if current_service is not None:
                        # Store current text for previous service
                        service_info[current_service] = current_text
                    current_service = line[len('DUMP OF SERVICE'):].strip()
                    current_service = current_service.lstrip()  # Strip leading space
                    current_service = re.sub(r'[^\w\s]', '_', current_service)  # Replace invalid characters with underscores
                    if current_service not in service_info:
                        service_info[current_service] = []  # Initialize empty list for current service
                    current_text = []  # Reset current text list for new service
                else:
                    # Append line to current text list
                    current_text.append(line)
            # Store text for the last service
            if current_service is not None:
                service_info[current_service] = current_text
        return service_info
    except FileNotFoundError:
        print(f"File '{dumpsys_file}' not found.")
        return {}

def write_service_info(service_info, output_folder):
    """Write service info to separate files in the specified output folder"""
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
    for service, info in service_info.items():
        filename = f'{service}.txt'
        # Replace invalid characters in the service name with underscores
        filename = re.sub(r'[^\w\s.]', '_', filename)
        with open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as file:
            for line in info:
                file.write(line + '\n')

def main():
    # Dumpsys file path
    dumpsys_file = 'YOUR FILE.txt'

    # Extract information for each service
    service_info = extract_service_info(dumpsys_file)

    # Write service info to separate files in an output folder named after the dumpsys file
    output_folder = os.path.splitext(dumpsys_file)[0]
    write_service_info(service_info, output_folder)

if __name__ == "__main__":
    main()