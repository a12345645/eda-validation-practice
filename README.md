# EDA Validation Practice

A lightweight EDA validation flow demo project using Verilog, Yosys, Tcl, Perl, and Python.  
Simulates an RTL-to-netlist flow with PPA analysis, log parsing, and regression-ready structure.

---

## 🛠️ Environment

- OS: Ubuntu 20.04+ (WSL or native)
- Tools used:
  - Yosys (open-source logic synthesis)
  - Python 3 (for report parsing and visualization)
  - Perl (for log summary)
  - Bash (for shell automation)
  - Tcl (for flow scripting)

---

## 📦 Install Yosys (Ubuntu)

You can install Yosys via apt, or build from source if you want the latest version.

### 🔹 Option 1: Install via apt

```bash
sudo apt update
sudo apt install yosys
```

Check the version:
```bash
yosys -V
```

### 🔹 Option 2: Build Yosys from source (recommended for latest)

```bash
sudo apt install -y build-essential clang bison flex libreadline-dev \
    gawk tcl-dev libffi-dev git mercurial graphviz xdot pkg-config \
    python3 python3-pip libboost-system-dev libboost-python-dev \
    libboost-filesystem-dev zlib1g-dev

git clone https://github.com/YosysHQ/yosys.git
cd yosys
make -j$(nproc)
sudo make install
```
## ▶️ Run the Flow
```bash
yosys -s scripts/synth_flow.tcl
```
Check the output logs in `logs/`, including:
 - Synthesized netlist: `counter_syn.v`
 - Synthesis log: `counter.log`


