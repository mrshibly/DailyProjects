# 🌟 InsightOS 🌟

InsightOS is a comprehensive tool designed to display detailed information about your operating system, including basic OS details, CPU, memory, disk, and network usage.

## ✨ Features
- 📋 **Basic OS Information**: System details, OS version, and uptime.
- 🔧 **CPU Information**: Core count, frequency, and usage statistics.
- 🧠 **Memory Information**: Total, available, and used memory, along with swap details.
- 💾 **Disk Information**: Disk partitions and usage statistics.
- 🌐 **Network Information**: Network I/O statistics including bytes and packets sent/received.

## 📦 Installation
1. Download the `InsightOS` project folder.

2. Install the required dependencies using `pip`:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the script with the desired options to display system information:

- Display all information:
  ```sh
  python insightos.py --all
  ```

- Display specific information:
  ```sh
  python insightos.py --cpu --memory
  ```

## ⚙️ Options
- `--basic`: Display basic OS information
- `--cpu`: Display CPU information
- `--memory`: Display memory information
- `--disk`: Display disk information
- `--network`: Display network information
- `--all`: Display all information

## 🖼️ Example
```sh
$ python insightos.py --all
```

## 📜 License
This project is licensed under the MIT License.

---

🔧 **InsightOS**: Your all-in-one system information tool!

### Instructions to Use:
1. **Download the Project**: Manually download the `InsightOS` folder to your local machine.
2. **Install Dependencies**: Open a terminal or command prompt, navigate to the `InsightOS` folder, and run `pip install -r requirements.txt` to install the necessary dependencies.
3. **Run the Script**: Use the command `python insightos.py` followed by the appropriate options to get the desired system information.
