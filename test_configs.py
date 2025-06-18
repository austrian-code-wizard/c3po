import json
import sys

configs = ['configs/config_sft_fast.json', 'configs/config_dpo_fast.json', 'configs/config_lcdpo_fast.json']

for config in configs:
    try:
        with open(config, 'r') as f:
            data = json.load(f)
        print(f"✓ {config}: Valid JSON")
    except Exception as e:
        print(f"✗ {config}: Invalid - {e}")
        sys.exit(1)

print("All configuration files are valid!")
