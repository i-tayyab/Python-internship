import json

def read_client_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    data = {}
    features = []
    reading_features = False

    for line in lines:
        line = line.strip()
        if line.startswith("Project:"):
            data["Project"] = line.split(":", 1)[1].strip()
        elif line.startswith("Features:"):
            reading_features = True
        elif reading_features and line.startswith("-"):
            features.append(line.lstrip("- ").strip())
        elif line.startswith("Timeline:"):
            data["Timeline"] = line.split(":", 1)[1].strip()
        elif line.startswith("Priority:"):
            data["Priority"] = line.split(":", 1)[1].strip()

    data["Features"] = features
    return data

def write_summary(data, txt_output, json_output):
    # Text Output
    with open(txt_output, 'w') as f:
        f.write("📘 Project Summary Report\n")
        f.write("-------------------------\n")
        f.write(f"Project: {data['Project']}\n")
        f.write(f"Timeline: {data['Timeline']}\n")
        f.write(f"Priority: {data['Priority']}\n")
        f.write("Features to Implement:\n")
        for feature in data["Features"]:
            f.write(f" - {feature}\n")

    # JSON Output
    feature_status = {feature: "Pending" for feature in data["Features"]}
    with open(json_output, 'w') as f:
        json.dump({
            "Project": data["Project"],
            "Timeline": data["Timeline"],
            "Priority": data["Priority"],
            "Features": feature_status
        }, f, indent=2)

if __name__ == "__main__":
    input_file = "client_requirements.txt"
    summary_file = "project_summary.txt"
    json_file = "project_summary.json"

    client_data = read_client_requirements(input_file)
    write_summary(client_data, summary_file, json_file)
