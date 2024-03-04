def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = 'C:\\Users\\InterCom\\OneDrive - Office 365\\Pulpit\\Dokument.txt'
line_gen = read_large_file(file_path)
for i, line in enumerate(line_gen):
    print(f"Linia {i + 1}: {line}")
