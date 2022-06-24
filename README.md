# Overview
Emulator completely repeats [Turing machine](https://en.wikipedia.org/wiki/Turing_machine) behaviour. 
#
# Features
 - Work tracing - step by step execution with machine's state output.
 - Commands correctness cheching (in dev)
 - Simple C commands converter (in dev)
 #
# Requirements
 - Python 3.6 and above;
 #

# Expected syntax:
```in_state``` ```in_value``` > ```out_state``` ```out_value``` ```move```
Command wiil be executed only if current state is **in_state** and value on tape is **in_value**. After execution state and value turn into **out_state** and **out_value** and pointer will be moved according to **move** parameter
- **in_state** and **out_state** belong to finit set of states. **q1** start machine state, **q0** - finish machine state (execution will be stopped if machine is in this state). Preferably, all states should starts with **q**, but it isn't a rule.
- **in_value** and **out_value**- a sumbol at tape from machine alphabet. **#** symbol is symbol of None (tape is filled with it by default)
- **move** belongs to {L, N ,R} - left, neutral and right - direction, tape pointer will be moved AFTER exectuion.
# Usage examples
With tracing (simple invertor code):
```
$ python3 main.py
Input start values on tape: 1
Input commands by enter: 
q1 1 > q0 0 N
q1 0 > q0 1 N
q1 # > q0 # N

↓  |  command: NO COMMAND
1  |  state: q1

↓  |  command: q1 1 > q0 0 N
0  |  state: q0

↓  |  command: q1 1 > q0 0 N
0  |  state: q0
```

*To Do: GUI, converter, syntax configuration*
