import os
import subprocess

def insecure_function():
    # Hardcoded secret (B105:hardcoded_password_string)
    password = "supersecretpassword1"

    # Unsafe use of subprocess (B602:subprocess_popen_with_shell_equals_true)
    command = "ls -l"
    subprocess.Popen(command, shell=True)

    # Insecure use of eval (B307:eval)
    user_input = input("Enter some code to execute: ")
    eval(user_input)

    # Weak cryptographic key (B303:md5)
    import hashlib
    m = hashlib.md5()
    m.update(b"Hello, world!")
    print(m.hexdigest())

if __name__ == "__main__":
    insecure_function()
