import json
from typing import Any, Callable, Protocol


type Data = list[dict[str, Any]]


class DataPipeline:

    def __init__(
            self, 
            loader: DataLoader,
            transformer: Transformer, 
            exporter: Exporter,
        ) -> None:
        self.loader = loader
        self.transformer = transformer
        self.exporter = exporter


    def run(self) -> None:
        data = self.loader.load()
        transformed = self.transformer.transform(data)
        self.exporter.export(transformed)


class DataLoader(Protocol):
    def load(self) -> Data: ...


class Transformer(Protocol):
    def transform(self, data: Data) -> Data: ...


class Exporter(Protocol):
    def export(self, data: Data) -> None: ...


class InMemoryLoader:
    def load(self) -> Data:
        return [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]


class JSONExporter:
    def __init__(self, filename: str="output.json") -> None:
        self.filename = filename

    def export(self, data: Data) -> None:
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)


class CleanMissingFields:
    def transform(self, data: Data) -> Data:
            return [row for row in data if row["age"] is not None]


# --- CONTAINER ---
class Container:
    def __init__(self) -> None:
        self._providers: dict[str, tuple[Callable[[], Any]], bool] = {}
        self._singletons: dict[str, Any] = {}

    def register(self, name: str, provider: Callable[[], Any], singleton: bool=False) -> None:
        self._providers[name] = (provider, singleton)


    def resolve(self, name: str) -> Any:
        if name in self._providers:
            return self._get_instance(name)
        
        if name not in self._singletons:
            raise ValueError(f"Dependency '{name}' not registered.")
        
        provider, singleton = self._providers[name]
        isinstance = provider()

        if singleton:
            self._singletons[name] = isinstance

        return isinstance


def main() -> None:
    container = Container()
    container.register("loader", lambda: InMemoryLoader(), singleton=True)
    container.register("transformer", lambda: CleanMissingFields())
    container.register("exporter", lambda: JSONExporter(filename="output.json"))

    container.register(
        "pipeline",
        lambda: DataPipeline(
            loader=container.resolve("loader"),
            transformer=container.resolve("transformer"),
            exporter=container.resolve("exporter"),
        ),
    )   

    pipeline = container.resolve("pipeline")
    pipeline.run()

    print("Pipeline completed. Output written to output.json")


if __name__ == '__main__':
    main()