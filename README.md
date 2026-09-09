# MavsPy

This repo installs the Python interface to the [MSU Autonomous Vehicle Simulator](https://www.mavsim.org/). It builds Python wheels for Linux and Windows that allow you to install MAVS with "pip".

MAVS is a software library for simulating autonomous ground vehicles in off-road terrain. MAVS simulates the sensors, vehicle, and environment. It uses physics-based models to simulate camera, lidar, and radar interacting with environmental features such as rain, dust, and fog.

Once installed, examples of scripts running different autonomous simulations can be found on the [MAVS-Examples GitHub](https://github.com/CGoodin/MAVS-Examples).

---

## Installation

Pre-built wheels for Linux and Windows are attached to each [GitHub Release](https://github.com/CGoodin/mavspy/releases). The wheel bundles all native MAVS libraries (`libmavs.so` / `mavs.dll`) and their dependencies - no separate MAVS build or install is required.

**Requirement:** Python 3.8 or later.

---

### Linux

#### 1. Download the wheel

From the [Releases page](https://github.com/CGoodin/mavspy/releases), download the file ending in `linux_x86_64.whl`. To get the most recent wheel on linux run:

```
curl -L -O https://github.com/CGoodin/mavspy/releases/download/v1.0.31/mavspy-1.0.31-py3-none-linux_x86_64.whl
```

#### 2. Install the wheel

```bash
pip install mavspy-1.0.7-py3-none-linux_x86_64.whl
```

You can also run ina a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install mavspy-1.0.7-py3-none-linux_x86_64.whl
```

#### 3. Verify the installation

```bash
python -c "import mavspy; print('mavspy imported successfully')"
```

---

### Windows

#### 1. Download the wheel

From the [Releases page](https://github.com/CGoodin/mavspy/releases), download the file ending in `win_amd64.whl`, for example:

```
curl -L -O https://github.com/CGoodin/mavspy/releases/download/v1.0.31/mavspy-1.0.31-py3-none-win_amd64.whl
```

#### 2. Install the wheel

Open a Command Prompt or PowerShell and run:

```powershell
pip install mavspy-1.0.7-py3-none-win_amd64.whl
```

Or use a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install mavspy-1.0.7-py3-none-win_amd64.whl
```

#### 4. Verify the installation

```powershell
python -c "import mavspy; print('mavspy imported successfully')"
```

---

## Quick Start

After installation, a basic simulation can be run with:

```python
import mavspy

# See the MAVS-Examples repository for full working scripts:
# https://github.com/CGoodin/MAVS-Examples
```

Full working example scripts covering sensors, vehicles, and environments are available at the [MAVS-Examples GitHub](https://github.com/CGoodin/MAVS-Examples).

---

## Troubleshooting

### Linux: Missing system dependencies

The wheel bundles most native libraries, but a few lightweight system packages are required that are not bundled (X11 display and JPEG support):

**Debian / Ubuntu:**
```bash
sudo apt-get install -y libx11-6 libjpeg62
```

**RHEL / CentOS / Fedora:**
```bash
sudo dnf install -y libX11 libjpeg-turbo
```

> **Headless / server environments:** If you are running on a machine with no display (e.g. a CI runner or SSH session), set the `DISPLAY` environment variable or use an offscreen renderer. MavsPy can generate sensor data and output files without a visible window in most use cases, but some visualisation features require a display.

### Linux: `ImportError: libmavs.so: cannot open shared object file`

The wheel sets an RPATH of `$ORIGIN/lib` so that Python can find the bundled libraries relative to the installed package. If this error appears:

1. Confirm the wheel installed correctly: `pip show mavspy`
2. Check that the `lib/` directory exists inside the installed package:
   ```bash
   python -c "import mavspy, os; print(os.path.dirname(mavspy.__file__))"
   # Then ls that directory/lib/
   ```
3. If you installed system-wide without a virtual environment, try reinstalling inside a fresh virtual environment.

### Linux: `GLIBC_2.x not found`

The wheels are built against glibc 2.28 (manylinux_2_28). Any Linux distribution shipped since approximately 2019 meets this requirement. If you are on an older system, you will need to build from source - see the [MAVS repository](https://github.com/Mississippi-State-University-OTM/MAVS).

### Windows: `The specified module could not be found` or `DLL load failed`

The bundled `mavs.dll` requires the **Microsoft Visual C++ Redistributable for Visual Studio 2019 or later (x64)**. Most Windows machines already have this. If you see an error like `The specified module could not be found` when importing mavspy, install the redistributable from Microsoft:

https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist

Download and run the **x64** installer (`vc_redist.x64.exe`).

1. Install the [Visual C++ Redistributable (x64)](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) as described above.
2. Ensure you downloaded the `win_amd64.whl` wheel and are running a 64-bit Python interpreter:
   ```powershell
   python -c "import struct; print(struct.calcsize('P') * 8, 'bit')"
   ```
   This should print `64 bit`.

### Wrong wheel for your platform

Make sure you download the wheel matching your OS:

| File suffix | Platform |
|---|---|
| `linux_x86_64.whl` | Linux, 64-bit x86 |
| `win_amd64.whl` | Windows, 64-bit x86 |

---

## Citing MAVS

If you use MAVS for your research, please cite the following:

 - Hudson, C., Goodin, C., Miller, Z., Wheeler, W., & Carruth, D. (2020, August). Mississippi state university autonomous vehicle simulation library. In *Proceedings of the Ground Vehicle Systems Engineering and Technology Symposium* (pp. 11 - 13).
 - Goodin, C., Carruth, D. W., Dabbiru, L., Hudson, C. H., Cagle, L. D., Scherrer, N., ... & Jayakumar, P. (2022, June). Simulation-based testing of autonomous ground vehicles. In *Autonomous Systems: Sensors, Processing and Security for Ground, Air, Sea and Space Vehicles and Infrastructure 2022* (Vol. 12115, pp. 167 - 174). SPIE.

---

## Other Documentation

 - MAVS software documentation: https://mavs-documentation.readthedocs.io/en/latest/
 - MAVS API reference: https://cgoodin.gitlab.io/msu-autonomous-vehicle-simulator/