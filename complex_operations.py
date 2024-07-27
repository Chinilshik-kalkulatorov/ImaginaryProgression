import numpy as np

def input_complex():
    real = float(input("Enter the real part: "))
    imag = float(input("Enter the imaginary part: "))
    return complex(real, imag)

def add_complex(c1, c2):
    return c1 + c2

def subtract_complex(c1, c2):
    return c1 - c2

def multiply_complex(c1, c2):
    return c1 * c2

def divide_complex(c1, c2):
    return c1 / c2

def magnitude_complex(c):
    return abs(c)

def conjugate_complex(c):
    return np.conj(c)

def main():
    print("Enter the first complex number:")
    c1 = input_complex()
    print("Enter the second complex number:")
    c2 = input_complex()

    print("\nComplex number 1:", c1)
    print("Complex number 2:", c2)

    print("\nAddition (c1 + c2):", add_complex(c1, c2))
    print("Subtraction (c1 - c2):", subtract_complex(c1, c2))
    print("Multiplication (c1 * c2):", multiply_complex(c1, c2))
    print("Division (c1 / c2):", divide_complex(c1, c2))
    print("Magnitude of c1 (|c1|):", magnitude_complex(c1))
    print("Magnitude of c2 (|c2|):", magnitude_complex(c2))
    print("Conjugate of c1:", conjugate_complex(c1))
    print("Conjugate of c2:", conjugate_complex(c2))

if __name__ == "__main__":
    main()
