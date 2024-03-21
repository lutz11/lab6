#Berenice Guzman decoder

def decode(password):
    decoded = ''
    for i in range(8):
        x = int(password[i])
        x = x - 3
        x %= 10
        x = str(x)
        decoded = decoded + x
    return decoded


