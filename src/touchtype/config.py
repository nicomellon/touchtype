import json

from . layouts import KeyboardLayout, Qwerty


class Config:

    _filename = "config.json"

    @classmethod
    def _load_config(cls):
        try:
            with open(cls._filename) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @classmethod
    def _save_config(cls, config: dict):
        with open(cls._filename, 'w') as f:
            json.dump(config, f, indent=4)

    layout = property()

    @layout.getter
    def layout(self) -> KeyboardLayout:
        config = self._load_config()
        match config.get("layout"):
            case Qwerty.name:
                return Qwerty()
            case _:
                return Qwerty()

    @layout.setter
    def layout(self, layout: KeyboardLayout) -> None:
        config = self._load_config()
        config.update({"layout": layout.name})
        self._save_config(config)
