# Q:
i'm finally in the container and upgraded pip; i received a warning about using root to execute commands...should i create a user? if so, how do i added a password to root?
# A:
Great to hear that you were able to access the container! It is indeed a good practice to use a non-root user for running applications and managing dependencies to improve security. Here’s how to create a new user and manage the root password in your container.

### 1. **Creating a New User in the Container**

#### Step 1: Create a new user

1. In the container terminal, run the following command to create a new user. Replace `newusername` with the desired username.

   ```bash
   adduser newusername
   ```

   - You will be prompted to set a password for the new user, along with other optional information (which you can skip by pressing Enter).

#### Step 2: Grant sudo privileges (optional but recommended)

If you want the new user to have the ability to execute commands as root (which is often necessary for managing software), do the following:

1. Ensure `sudo` is installed. If it’s not installed, you may need to install it using package manager:

   ```bash
   apt-get update && apt-get install sudo
   ```

   (Use `yum` if using a Red Hat-based distribution.)

2. Add the new user to the `sudo` group:

   ```bash
   usermod -aG sudo newusername
   ```

### 2. **Setting a Password for the Root User**

If you want to set or change the password for the root user, you can do it with the following command:

1. Run the following command to set a new password for root:

   ```bash
   passwd
   ```

2. You will be prompted to enter a new password for the root user. Make sure to remember this password since it allows full access to the container.

### 3. **Using the New User**

After you've created the new user, you can switch to that user within the container:

1. Switch to the new user by running:

   ```bash
   su - newusername
   ```

2. You can now run commands as that user. Use `sudo` to execute commands that require root privileges. For example:

   ```bash
   sudo apt-get update
   ```

### 4. **Best Practices**

- **Avoid Using Root:** It’s generally safer to operate as a non-root user and only use root privileges when necessary via `sudo`.
- **Unique User:** Create unique users for different purposes to help with access control and auditing activities.

### Summary of Commands

| Step                     | Command                                     | Description                                    |
|--------------------------|---------------------------------------------|------------------------------------------------|
| Create a new user        | `adduser newusername`                     | Create a new user and set a password           |
| Install sudo (if needed) | `apt-get install sudo`                    | Install sudo to allow privilege escalation      |
| Add user to sudo group   | `usermod -aG sudo newusername`             | Give new user sudo access                       |
| Change root password      | `passwd`                                  | Set or change the password for root             |
| Switch user               | `su - newusername`                        | Switch to the new user                          |

Let me know if you have any questions or need further assistance!