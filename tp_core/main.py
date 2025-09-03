#!/usr/bin/env python3
import argparse
import sys
from datetime import datetime

APP_NAME = "Telepresence Core"
APP_VERSION = "0.2.0"

def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="telepresence-core",
        description="Minimal telepresence core stub."
    )
    # Basics
    p.add_argument("--version", action="store_true", help="Print version and exit")
    p.add_argument("--dry-run", action="store_true", help="Run without engaging real hardware")
    p.add_argument("--log-level", default="info",
                   choices=["debug", "info", "warn", "error"],
                   help="Logging level")

    # NEW options
    p.add_argument("--video", default="webrtc",
                   choices=["webrtc", "rtsp"],
                   help="Video transport protocol")
    p.add_argument("--control-port", type=int, default=9000,
                   help="Port for control messages")
    p.add_argument("--robot-name", default="NOA",
                   help="Robot name for identification")

    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    if args.version:
        print(f"{APP_NAME} v{APP_VERSION}")
        return 0

    # Startup banner
    now = datetime.now().isoformat(timespec="seconds")
    print(f"[{now}] {APP_NAME} starting…")
    print(f"  log-level={args.log_level}")
    print(f"  dry-run={args.dry_run}")
    print(f"  video={args.video}")
    print(f"  control-port={args.control_port}")
    print(f"  robot-name={args.robot_name}")

    # TODO: wire video transport + control transport implementations here
    print("OK: init complete (stub).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
