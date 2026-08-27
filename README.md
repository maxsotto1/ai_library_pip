# ai_library

`ai_library` is a Python package that exposes model training, inference, metrics recording, cron scheduling, and package-based configuration management.

## Package Overview

### Available Top-Level APIs

- `ai_library.validate_config(config_path=None)`
  - Loads and validates the package default `ai_library/config.yaml` if no path is provided.
  - Returns the parsed configuration dictionary.

- `ai_library.update_config(config_path=None, updates=...)`
  - Updates the package config file by default.
  - Supports a dictionary, a `[key, value]` pair, or a list of `[key, value]` pairs.

- `ai_library.show_config(config_path=None)`
  - Prints the current configuration to stdout.

- `ai_library.train()`
  - Loads configuration from the package config.
  - Reads data, builds the selected pipeline, and trains the model.

- `ai_library.infer()`
  - Loads package configuration.
  - Loads a saved model and performs inference.
  - returns predictions, first_predicted, last_predicted, data_frequency, conformal_q 
  - conformal_q is the safety margin in order to be 1-alpha accurate for the predicted time window

- `ai_library.record`
  - Use `ai_library.record.main()` or run the module directly to start metric collection.

- `ai_library.add_to_cron()` / `ai_library.remove_from_cron()`
  - Manage cron scheduling for recurring training runs.
  - Adds or removes a cron job that runs `python3 -m ai_library.codebase.setup.train`.

## How to Use

### Install
```bash
pip install ai-library-swch==0.1.1 
```
a safe python version is 3.12.3

### Configuration
```python
from ai_library import validate_config, update_config, show_config

update_config(None, updates=["parquet_train_size", 100000])
show_config()
validate_config()
```

### Metric Recorder Function
Make sure that `.env` is reachable in the folder where this is executed, and that the specified port is reachable.
Sample `.env` configuration:
```python
MON_CLIENT_STOMP_HOST=127.0.0.1
MON_CLIENT_STOMP_PORT=61622
```
Execution command:
```bash
nohup python3 -c "from ai_library import record; record.main()" > record.log 2>&1 &
```

### Train and Infer
```python
from ai_library import train, infer
```

# Manually use train (no cron)
```python
train()
```

### Cron Scheduling
```python
import ai_library.codebase.setup.cron_manager as cron_manager

cron_manager.add_to_cron()
cron_manager.remove_from_cron()
```

# Inference
```python
predictions, first_predicted, last_predicted, data_frequency, conformal_q = infer()
```
