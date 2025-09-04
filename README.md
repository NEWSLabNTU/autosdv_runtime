# AutoSDV Runtime

AutoSDV Runtime provides a unified command-line interface and systemd service management for the AutoSDV autonomous vehicle platform.

## Overview

The `autosdv_runtime` package simplifies the deployment and management of AutoSDV systems by providing:
- A single `autosdv` command for all system operations
- Systemd service integration for automatic startup and process management
- Web-based system monitoring interface
- Simplified logging and status reporting

## Installation

After building the AutoSDV workspace with colcon, the `autosdv` command will be available in your system PATH.

```bash
# Build the workspace
colcon build --symlink-install

# Source the workspace
source install/setup.bash

# Install the systemd service
autosdv install
```

## Usage

### Command Overview

The `autosdv` command provides the following operations:

| Command | Description |
|---------|-------------|
| `autosdv install` | Install systemd user service for automatic startup |
| `autosdv start` | Start the AutoSDV system |
| `autosdv stop` | Stop the AutoSDV system |
| `autosdv restart` | Restart the AutoSDV system |
| `autosdv status` | Show current system status and recent logs |
| `autosdv monitor` | Open the web-based system monitor in browser |
| `autosdv uninstall` | Remove the systemd service |

### Basic Workflow

1. **Install the service** (one-time setup):
   ```bash
   autosdv install
   ```
   This creates a systemd user service that can manage the AutoSDV launch process.

2. **Start the system**:
   ```bash
   autosdv start
   ```
   This launches the complete AutoSDV stack including sensors, localization, planning, and control.

3. **Monitor the system**:
   ```bash
   # Check status and logs
   autosdv status
   
   # Open web monitor (http://localhost:8080)
   autosdv monitor
   ```

4. **Stop the system**:
   ```bash
   autosdv stop
   ```

### Systemd Service Features

Once installed, the AutoSDV service provides:
- **Automatic startup** at user login (when enabled)
- **Process supervision** with automatic restart on failure
- **Unified logging** through systemd journal
- **Resource management** and proper shutdown handling

### Enable Boot Startup

To have AutoSDV start automatically at system boot (not just user login):

```bash
# Enable user lingering (allows services to run without login)
sudo loginctl enable-linger $USER

# The service will now start at boot
```

### View Logs

The systemd integration provides centralized logging:

```bash
# View recent logs
journalctl --user -u autosdv -n 50

# Follow logs in real-time
journalctl --user -u autosdv -f

# View logs from specific time
journalctl --user -u autosdv --since "10 minutes ago"
```

## Architecture

The runtime package consists of:

- **autosdv CLI**: Main command-line interface (`/usr/bin/autosdv`)
- **Launch Script**: Generated bash script that sources ROS and launches the system
- **Systemd Service**: User service file for process management
- **Python Module**: Core implementation of CLI commands and service management

## Service Management

The systemd service (`autosdv.service`) is installed to `~/.config/systemd/user/` and provides:
- Proper environment setup (ROS sourcing, workspace paths)
- Working directory configuration
- Restart policies and failure handling
- Integration with systemd journal for logging

## Web Monitor

When the system is running, a web-based monitor is available at:
- **URL**: http://localhost:8080/
- **Features**: Real-time system status, sensor data visualization, performance metrics

Access the monitor using:
```bash
autosdv monitor  # Opens in default browser
```

## Troubleshooting

### Service Won't Start
```bash
# Check service status
autosdv status

# View detailed logs
journalctl --user -u autosdv -n 100

# Check if workspace is built
ls -la ~/AutoSDV/install/
```

### Service Not Found
```bash
# Reinstall the service
autosdv install

# Reload systemd daemon
systemctl --user daemon-reload
```

### Permission Issues
```bash
# Ensure launch script is executable
chmod +x ~/AutoSDV/install/autosdv_runtime/share/autosdv_runtime/scripts/autosdv-launch.sh

# Check service file permissions
ls -la ~/.config/systemd/user/autosdv.service
```

## Requirements

- ROS 2 Humble
- Ubuntu 22.04 or compatible
- Python 3.10+
- systemd (for service management)
- Built AutoSDV workspace

## License

Part of the AutoSDV project. See main repository for license information.