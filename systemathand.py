import subprocess

# Start a new terminal shell and run the 'ls' command, then display a message
subprocess.run(["gnome-terminal", "--", "bash", "-c", "sudo passwd root; echo 'This is powered by my tech knowledge. Make sure you do not do anything fishy here.'; sudo -i; su; exec bash"])

# Print additional messages in the main Python program
print("This is powered by my tech knowledge. Make sure you do not do anything fishy here.")
print("This is powered by my tech knowledge. Make sure you do not do anything fishy here.")
print("This is powered by my tech knowledge. Make sure you do not do anything fishy here.")
