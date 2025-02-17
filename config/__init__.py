from __future__ import absolute_import

import os
import sys
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# This allows easy placement of apps within the interior
# apps directory.

sys.path.append(str(BASE_DIR / "apps"))
env = environ.Env()

# Fetching
env_dir = os.path.join(BASE_DIR, "envs", ".env")
if os.path.exists(env_dir):
    environ.Env.read_env(env_dir)
