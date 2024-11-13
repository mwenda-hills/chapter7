import os


def run(**args):
    print("[*] In environment module.")  # Updated print statement for Python 3
    return str(os.environ)

if __name__ == "__main__":
    result = run()
    print(result)
