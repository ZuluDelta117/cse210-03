class TerminalService:
    # Obviously we want to set this class up to display to the terminal - Jordan
    def read_text(self, prompt):
        return input(prompt)
    
    def read_word(self, prompt):
        return str(input(prompt))

    def write_word(self, word):
        print(word)
