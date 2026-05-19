

def parse():
    # Definer variabler
    error = 0
    warning = 0
    info = 0
    
    # Les fil og split per newline
    file = "log"
    with open (file) as log:
        data = (log.read().split("\n"))
    # Sjekk feilkoder.
    for line in data:
        if ("ERROR" in line):
            error += 1 
        elif ("WARNING" in line):
            warning += 1 
        elif ("INFO" in line):
            info += 1 
    return error,warning,info


if __name__ == "__main__":
    error, warning, info = parse()
print(f"{{'ERROR': {error}, 'WARNING': {warning}, 'INFO': {info}}}")
