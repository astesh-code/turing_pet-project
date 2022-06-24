### Turing machine executor class ###
from src.command import command


class machine(list):

    def __init__(self, instruction: list, input_val: str) -> None:
        # default values, they are the same for every machine
        self._pos = 0
        self.state = 'q1'
        self.com = None
        self._moves = {
            'R': 1, 'L': -1, 'N': 0
        }
        # start list of values on "tape", string
        self.extend(list(input_val))
        # commands list
        self.commands = tuple(command(line) for line in instruction)
        self._check()

    def _check(self) -> None:
        '''Check for broken instructions (doesn't cover all cases). Throw exceptions, if something wrong'''
        text = None
        if any([com.t['move'] not in self._moves.keys() for com in self.commands]):
            text = 'Instruction has unexpected moves'
        if 'q1' not in [com.f['state'] for com in self.commands]:
            text = 'Instruction has not start state'
        if 'q0' not in [com.t['state'] for com in self.commands]:
            text = 'Instruction has not exit state'
        if any([com.f['state'] == 'q0' for com in self.commands]):
            text = 'Instruction has going from exit state command'
        outs = set(com.t['state']
                   for com in self.commands if com.t['state'] not in ['q0', 'q1'])
        ins = set(com.f['state']
                  for com in self.commands if com.f['state'] != 'q1')
        if (outs != ins):
            text = 'Instruction has inextricable state'
        if (text):
            raise AttributeError(text)

    def __str__(self) -> None:
        lu = '  '*self._pos+'↓'+'  '*(len(self)-self._pos-1)
        ld = ' '.join(self)
        ru = 'NO COMMAND' if self.com == None else self.com
        rd = self.state
        return f'{lu}  |  command: {ru}\n{ld}  |  state: {rd}\n'

    def step(self, com: command) -> None:
        '''
        Make a one step of Machine
        com : command to execute on this step
        '''
        if com:
            self[self._pos] = com.t['sym']
            self.state = com.t['state']
            self._pos += self._moves.get(com.t['move'])

            # "tape" enlongation
            if (self._pos < 0):
                self.insert(0, '#')
                self._pos += 1
            elif self._pos > len(self)-1:
                self.append('#')

    def _cur_command(self) -> None:
        '''Find next suitable command from instruction. If there are no suitable command, set value as None'''
        for com in self.commands:
            if self.state == com.f['state'] and self[self._pos] == com.f['sym']:
                self.com = com
                break
        else:
            self.com = None

    def start(self, trace: bool = False) -> None:
        '''
        Start executing
        trace : is in charge of step-by-step output
        '''
        while self.state != 'q0':
            if trace:
                print(self)
            self._cur_command()
            if not self.com:
                break
            self.step(self.com)
        if trace:
            print(self)
