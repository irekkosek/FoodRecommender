from pathlib import Path
import json_parsing
cwd = Path.cwd()
print(cwd)

mod_path = Path(__file__).parent
print(mod_path)
mod_path = Path(json_parsing.__file__).parent.resolve()
print(mod_path)