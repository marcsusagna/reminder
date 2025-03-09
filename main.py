import subprocess
import argparse

import config as conf

def main():
    parser = argparse.ArgumentParser(
        description='Customize notification interval'
    )
    parser.add_argument('--seconds', type=int, default=conf.DEFAULT_INTERVAL, help='Notify every given seconds')
    args = parser.parse_args()

    subprocess.run(['python3', 'bin/run_reminders.py', str(args.seconds)])

if __name__ == "__main__":
    main()