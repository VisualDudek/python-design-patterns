import json
from typing import Any


type Data = list[dict[str, Any]]


class DataPipeline:

    def run(self) -> None:
        # Hardcoded loader
        data = self._load_data_from_csv()

        # Hardcoded transformation
        cleaned = [row for row in data if row["age"] is not None]

        # Hardcoded export
        self._export_to_json(cleaned)

    def _load_data_from_csv(self) -> Data:
        # simulate reading form CSV
        return [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]
    
    def _export_to_json(self, data: Data) -> None:
        with open("output.json", "w") as f:
            json.dump(data, f, indent=2)


def main() -> None:
    pipeline = DataPipeline()
    pipeline.run()
    print("Pipeline completed. Output written to output.json")


if __name__ == '__main__':
    main()