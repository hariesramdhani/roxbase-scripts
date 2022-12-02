import difflib
import os

MAIN_DIR = "D://side_project//"
REGION = "sea"

OLD_DATE = "20220512"
OLD_DIR = f"{MAIN_DIR}{REGION}_{OLD_DATE}//TextAsset"

NEW_DATE = "20220609"
NEW_DIR = f"{MAIN_DIR}{REGION}_{NEW_DATE}//TextAsset"

# Check the difference using difflib
TARGET_FILES = [
  "en_langs.bytes",
  "cn_langs.bytes",
  "data_drop_Drop.bytes",
  "data_equip_EquipmentFormula.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_Equip.bytes",
  "data_equip_Refine.bytes",
  "data_equip_ItemSplit.bytes",
  "data_equip_ItemCombine.bytes",
  "data_item_Item.bytes",
  "data_item_CardCoordinates.bytes",
  "data_monster_Monster.bytes",
]

for TARGET_FILE in TARGET_FILES:
  with open(f"{NEW_DIR}/{TARGET_FILE}", "r", encoding="utf8") as filename:
    new_en_langs = filename.readlines()

  with open(f"{OLD_DIR}/{TARGET_FILE}", "r", encoding="utf8") as filename:
    old_en_langs = filename.readlines()

  d = difflib.Differ()
  diffs = [x for x in d.compare(old_en_langs, new_en_langs) if x[0] in ('+', '-')]

  MAIN_DIFF_DIR = "../../update_changes"
  CHANGE_NEW_DIR = f"{MAIN_DIFF_DIR}/{NEW_DATE}"

  # print(not os.path.isdir(CHANGE_DIR))
  if not os.path.isdir(CHANGE_NEW_DIR):
    os.mkdir(CHANGE_NEW_DIR)

  with open(f"{CHANGE_NEW_DIR}/{TARGET_FILE}", "w", encoding="utf8") as filename:
    filename.writelines(diffs)