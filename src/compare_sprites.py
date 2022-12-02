import os
import shutil

MAIN_DIR = "D://side_project//"
REGION = "sea"

OLD_DATE = "20220127"
OLD_DIR = f"{MAIN_DIR}{REGION}_{OLD_DATE}"

NEW_DATE = "20220311"
NEW_DIR = f"{MAIN_DIR}{REGION}_{NEW_DATE}"

old_sprites = set(os.listdir(f"{OLD_DIR}//Sprite"))
new_sprites = set(os.listdir(f"{NEW_DIR}//Sprite"))

new_differences = list(new_sprites - old_sprites)

# print(list(new_sprites)[0])
# print(list(old_sprites)[0])
# print(len(old_sprites))
# print(len(new_sprites))
# print(differences[:10])
# print(len(differences))

MAIN_DIFF_DIR = "../../update_changes"
CHANGE_NEW_DIR = f"{MAIN_DIFF_DIR}/{NEW_DATE}/added"

# print(not os.path.isdir(CHANGE_DIR))
if not os.path.isdir(CHANGE_NEW_DIR):
  os.mkdir(CHANGE_NEW_DIR)

for new_difference in new_differences:
  shutil.copy2(f"{NEW_DIR}//Sprite//{new_difference}", f"{CHANGE_NEW_DIR}")

old_differences = list(old_sprites - new_sprites)

MAIN_DIFF_DIR = "../../update_changes"
CHANGE_OLD_DIR = f"{MAIN_DIFF_DIR}/{NEW_DATE}/removed"

# print(not os.path.isdir(CHANGE_DIR))
if not os.path.isdir(CHANGE_OLD_DIR):
  os.mkdir(CHANGE_OLD_DIR)

for old_difference in old_differences:
  shutil.copy2(f"{OLD_DIR}//Sprite//{old_difference}", f"{CHANGE_OLD_DIR}")