from core.engine import Engine
from stages.menu import menu
from stages.play import play

e = Engine('Strategy')
e.register('Menu', menu)
e.register('Play', play)
e.switch_to('Menu')
e.run()