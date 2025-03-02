import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Customize notification interval'
    )
    parser.add_argument('--seconds', type=int, default=5, help='Notify every given seconds')
    args = parser.parse_args()

    subprocess.run(['python', 'bin/orchestrator.py', str(args.seconds)])

if __name__ == "__main__":
    main()