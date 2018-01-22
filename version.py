from subprocess import check_output


def get_version():
    # Get the version using "git describe".
    return check_output('git describe --tags --match [0-9]* --dirty'.split()).decode().strip().replace('-dirty', '.dev')

if __name__ == '__main__':
    print(get_version())
