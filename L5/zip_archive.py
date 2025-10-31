import zipfile

def check_password(zip_path, password):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for info in zip_ref.infolist():
                if info.flag_bits & 0x1:
                    try:
                        with zip_ref.open(info, pwd=password.encode()) as f:
                            f.read(1)
                        zip_ref.extractall(path="dezarhivat", pwd=password.encode())
                        return True
                    except RuntimeError:
                        return False
            return True 
    except zipfile.BadZipFile:
        print("Invalid ZIP file.")
        return False

password = "1234567890123456789012345678901234567890123456789012345678901234"
with zipfile.ZipFile("arhiva.zip", 'r') as zip_ref:
    if check_password("arhiva.zip", password):
        print()
        print(password)
    else:
        print('.', end='', flush=True)
print()