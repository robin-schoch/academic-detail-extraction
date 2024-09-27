from parser import parse_input
import json

def split_data_set():
    input = parse_input('./academic_details.json')

    df_formatted = [
        {
            "messages": [
                {"role": "user", "content": item.input},
                {"role": "assistant", "content": str(item.output)},
            ]
        }
        for item in input[0:30]
    ]

    with open("data.jsonl", "w") as f:
        for line in df_formatted:
            json.dump(line, f)
            f.write("\n")



if __name__ == "__main__":
    split_data_set()
