class lexer:
    def __init__(self, inp):
        self.inp = inp
    def Tokens(self):
        tokens = []
        while len(self.inp) >= 3:
            txt = ''
            if self.inp[:3] == 'out':
                    tokens.append("OUT")
                    self.inp = self.inp[4:]
            if self.inp[:2] == 'in':
                    tokens.append("IN")
                    self.inp = self.inp[3:]
            if self.inp[0] in '{':
                    tokens.append("REP_START")
                    self.inp = self.inp[1:]
            if self.inp[0] in '}':
                    tokens.append("REP_END")
                    self.inp = self.inp[1:]
            if self.inp[0] in '[':
                    tokens.append("DO_START")
                    self.inp = self.inp[1:]
            if self.inp[0] in ']':
                    tokens.append("DO_END")
                    self.inp = self.inp[1:]
            if self.inp[:1] == ':':
                    tokens.append("SET")
                    self.inp = self.inp[1:]
            if self.inp[:1] == ',':
                    tokens.append("NEXT")
                    self.inp = self.inp[1:]
            if self.inp[0] in '"\'`':
                s = self.inp[0]
                while not self.inp[0] in '\'"`':
                    txt += self.inp[0]
                    self.inp = self.inp[1:]
                if s == '"' and self.inp[0] == '"':
                    tokens.append(f"EXP..:{txt}")
                if s == "'" and self.inp[0] == '"':
                    tokens.append(f"EXP_.:{txt}")
                if s == '"' and self.inp[0] == "'":
                    tokens.append(f"EXP._:{txt}")
                if s == "'" and self.inp[0] == "'":
                    tokens.append(f"EXP__:{txt}")
                if s == '`' and self.inp[0] == '"':
                    tokens.append(f"EXP-.:{txt}")
                if s == "`" and self.inp[0] == "'":
                    tokens.append(f"EXP-_:{txt}")
                if s == '`' and self.inp[0] == "`":
                    tokens.append(f"EXP--:{txt}")
                if s == '"' and self.inp[0] == '`':
                    tokens.append(f"EXP.-:{txt}")
                if s == "'" and self.inp[0] == "`":
                    tokens.append(f"EXP_-:{txt}")
