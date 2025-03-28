from pathlib import Path
import json
path = Path("mystudy\codes\like_number.json")
if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number is {number+1}")
else:
    number = input("请输入你最喜欢的数:")
    number = int(number)
    content = json.dumps(number)
    path.write_text(content)