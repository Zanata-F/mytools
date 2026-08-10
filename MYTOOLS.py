PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def pi_real(n):
    try:
        n = int(n)
        if n<=0 or n>=100:
            print("Digite um número entre 0 e 100.")
            return(0)
        return("3,"+PI_INT[0:n])
    except ValueError:
        print("Digite um número inteiro.")
        return(0)
def e_real(n):
    try:
        n = int(n)
        if n<=0 or n>=100:
            print("Digit eum número entre 0 e 100.")
            return(0)
        return("2,"+E_INT[0:n])
    except ValueError:
        print("Digite um número inteiro.")
        return(0)