# Load and process the keywords file
import yaml

# Load the intent keywords file
file_path = 'intent_keywords.yml'

with open(file_path, 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

# Extract keywords and remove duplicates
keywords_set = set()

for intent in data['nlu']:
    for example in intent['examples'].split("\n"):
        words = example.strip().split()
        keywords_set.update(words)

# Convert set to sorted list
deduplicated_keywords = sorted(list(keywords_set))

# Format keywords into the desired format
formatted_keywords = ["esp_keywords = ["]
formatted_keywords += [f'    "{keyword}",' for keyword in deduplicated_keywords]
formatted_keywords.append("]")

# Join the formatted keywords into a single string
formatted_keywords_str = "\n".join(formatted_keywords)

# Print the formatted keywords string
print(formatted_keywords_str)
