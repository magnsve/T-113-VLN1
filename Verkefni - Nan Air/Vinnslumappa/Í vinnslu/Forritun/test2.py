import io
import sys
import textwrap

class Filler(io.TextIOBase):
    def __init__(self, file, width=70):
        self.file = file
        self.textwrapper = textwrap.TextWrapper(width=width)
        self.buf = ''
    def write(self, buf):
        self.buf += buf
        lines = self.buf.split('\n')
        self.buf = lines.pop()
        for line in lines:
            self.file.write(self.textwrapper.fill(line) + '\n')
    def close(self):
        if self.buf:
            self.file.write(self.textwrapper.fill(buf))
        self.buf = ''
        self.file.close()

sys.stdout = Filler(sys.stdout, 32)

print('Spam spam spam spammity ' * 10)
print('Spam', 'Eggs')
sys.stdout.textwrapper.width = 80
print('Spam ' + 'spam ' * 50, 'and eggs', sep='... ')
print('Spam', end=' ')
print('Eggs', end=' ')
print('Cheese')