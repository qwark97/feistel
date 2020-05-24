def read_key_file(path_to_key_file):
    try:
        with open(path_to_key_file, 'rb') as f:
            key = f.read()
    except FileNotFoundError:
        raise FileNotFoundError('Provide valid path to the key file')

    return key
