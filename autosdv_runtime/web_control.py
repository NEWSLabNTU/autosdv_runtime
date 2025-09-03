#!/usr/bin/env python3
"""
AutoSDV Web Control Interface
Provides REST API endpoints for controlling AutoSDV system via web interface
"""

import argparse
import sys
from pathlib import Path

# Import the existing web control implementation and adapt it
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / 'scripts/vehicle'))

try:
    from autosdv_web_control import AutoSDVWebControl
except ImportError:
    # Fallback: create a minimal implementation
    class AutoSDVWebControl:
        def run(self, host='0.0.0.0', port=8081, debug=False):
            print(f"AutoSDV Web Control would run on {host}:{port}")
            print("Note: Full implementation requires Flask and other dependencies")


def main():
    """Main entry point for autosdv-web-control command"""
    parser = argparse.ArgumentParser(description='AutoSDV Web Control Interface')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=8081, help='Port to listen on (default: 8081)')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    try:
        control_server = AutoSDVWebControl()
        control_server.run(host=args.host, port=args.port, debug=args.debug)
    except KeyboardInterrupt:
        print("\nWeb control server stopped")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()