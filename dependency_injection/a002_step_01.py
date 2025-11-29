import json
from typing import Any


type Data = list[dict[str, Any]]


class DataPipeline:

    def run(self) -> None:
        # Hardcoded loader
        data = load_data_from_csv()

        # Hardcoded transformation
        cleaned = clean_data(data) 

        # Hardcoded export
        export_to_json(cleaned)


def load_data_from_csv() -> Data:
    # simulate reading form CSV
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]


def export_to_json(self, data: Data) -> None:
    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)


def clean_data(data: Data) -> Data:
        return [row for row in data if row["age"] is not None]


def main() -> None:
    pipeline = DataPipeline()
    pipeline.run()
    print("Pipeline completed. Output written to output.json")


if __name__ == '__main__':
    main()