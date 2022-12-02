import os

MAIN_DIR = "D://side_project//"
REGION = "sea"
NEW_DATE = "20220609"
NEW_DIR = f"{MAIN_DIR}{REGION}_{NEW_DATE}//TextAsset"
LANGUAGE = "en_langs"

# En Langs
with open(f"{NEW_DIR}//{LANGUAGE}.bytes", "r", encoding="utf8") as filename:
  en_langs = []
  lines = filename.readlines()

  for line in lines:
    en_langs.append(line.strip())

  en_langs = en_langs[2:-1]

MAIN_DIFF_DIR = "../../update_changes"
CHANGE_NEW_DIR = f"{MAIN_DIFF_DIR}/{NEW_DATE}/cleaned"

if not os.path.isdir(CHANGE_NEW_DIR):
  os.mkdir(CHANGE_NEW_DIR)

with open(f"{CHANGE_NEW_DIR}/{LANGUAGE}.bytes", "w", encoding="utf8") as filename:
  filename.writelines("\n".join(en_langs))