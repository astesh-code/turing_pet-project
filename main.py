from sys import stdin
from trace import Trace
from src.machine import machine


if __name__ == '__main__':
    start_values = input("Input start values on tape: ")
    commands = [input("Input commands by enter: \n")]
    while len(commands[-1])>5:
        commands.append(input())
    commands.pop()
    M = machine(commands, start_values)
    M.start(True)
    print(M)