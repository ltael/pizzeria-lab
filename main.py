from terminal import TerminalWorker
from life_cycle import ProgrammCycle

def main():
    terminal = TerminalWorker()
    cycle = ProgrammCycle(terminal)
    cycle.start()


if __name__ == "__main__":
    main()