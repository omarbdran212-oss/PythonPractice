import json
import os

def load_file(filepath: str) -> list:
  if not os.path.exists(filepath):
    return []

  try:
    with open(filepath, "r", encoding="utf-8") as file:
      return json.load(file)
  except (json.JSONDecodeError, FileNotFoundError):
    return []

def save_to_file(items, filepath):
    with open(filepath, "w") as file:
        json.dump(items, file, indent=4)



def remove_from_file(filepath: str, content_to_delete: str) -> bool:
    contents = load_file(filepath)
    
    if content_to_delete in contents:
        contents.remove(content_to_delete)
        save_to_file(contents, filepath)
        return True
    else:
        return False

def main():
    my_items = load_file("grocery_list.json")
    while True:
        item = input("please add your item: ")
        if item == "q":
            break
        my_items.append(item)
    for t in my_items:
        print(t)
    save_to_file(my_items, "grocery_list.json")

    


if __name__ == "__main__":
    main()




