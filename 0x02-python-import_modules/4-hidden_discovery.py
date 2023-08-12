#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for run in dir(hidden_4):
        if not run.startswith("__"):
            print(run)
