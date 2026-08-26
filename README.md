# ai_library

`ai_library` is a Python package that exposes model training, inference, metrics recording, cron scheduling, and package-based configuration management.

## Package overview


### Available top-level APIs

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

- `ai_library.record`
  - Use `ai_library.record.main()` or run the module directly to start metric collection.

- `ai_library.add_to_cron()` / `ai_library.remove_from_cron()`
  - Manage cron scheduling for recurring training runs.
  - Adds or removes a cron job that runs `python3 -m ai_library.codebase.setup.train`.
