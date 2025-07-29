# text_stats.py

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    return len(text)

def line_count(text):
    return text.count('\n') + 1

def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return {
                'lines': line_count(content),
                'words': word_count(content),
                'characters': char_count(content)
            }
    except FileNotFoundError:
        print("File not found.")
        return None

# Example usage
if __name__ == '__main__':
    file_path = 'sample.txt'
    stats = analyze_text(file_path)
    if stats:
        print(f"Lines: {stats['lines']}")
        print(f"Words: {stats['words']}")
        print(f"Characters: {stats['characters']}")
