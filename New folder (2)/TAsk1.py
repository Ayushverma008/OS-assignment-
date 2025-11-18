import os

def create_children(N):
    print(f"Parent PID: {os.getpid()} is creating {N} child processes...\n")

    for i in range(N):
        pid = os.fork()

        if pid == 0:
            # This is the child process
            print(f"Child {i+1}:")
            print(f"    PID: {os.getpid()}")
            print(f"    Parent PID: {os.getppid()}")
            print(f"    Message: Hello, I am child process {i+1}!\n")
            os._exit(0)        # Child exits to prevent creating more children

    # Parent process waits for all children
    for _ in range(N):
        finished = os.wait()
        print(f"Parent: Child with PID {finished[0]} has finished.")

if __name__ == "__main__":
    N = int(input("Enter number of child processes to create: "))
    create_children(N)
