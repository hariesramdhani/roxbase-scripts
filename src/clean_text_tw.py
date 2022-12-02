import os

MAIN_DIR = "D://side_project//"
REGION = "tw"
NEW_DATE = "20220808"
NEW_DIR = f"{MAIN_DIR}{REGION}_{NEW_DATE}//TextAsset"

TARGET_FILES = [
  "data_dropV2_DropV2.bytes",
  "data_dropV2_DropCollection.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_Equip.bytes",
  "data_equip_Refine.bytes",
  "data_equip_ItemSplit.bytes",
  "data_equip_ItemCombine.bytes",
  "data_item_Item.bytes",
  "data_item_CardCoordinates.bytes",
  "data_monster_Monster.bytes",
  "data_area_Area.bytes",
  "data_AccumulativeMonth_AccumulativeMonth.bytes",
  "data_AttrPoint.bytes",
  "data_AutoPoint.bytes",
  "data_baselevel.bytes",
  "data_BaseLevelGrowth.bytes",
  "data_equip_Appraisal.bytes",
  "data_equip_AppraisalLib.bytes",
  "data_equip_EquipmentDecomposition.bytes",
  "data_equip_EquipmentRepair.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_EquipmentType.bytes",
  "data_equip_ItemCombine.bytes",
  "data_equip_ItemSplit.bytes",
  "data_equip_PropID.bytes",
  "data_equip_Refine.bytes",
  "data_equip_SlotStrengthen.bytes",
  "data_EquipmentSmelting_EquipmentSmelting.bytes",
  "data_GiftBoxV2.bytes",
  "data_Gifts_Gifts.bytes",
  "data_InstanceGroup_InstanceGroup.bytes",
  "data_item_CardCoordinatesAttr.bytes",
  "data_ItemType.bytes",
  "data_job_Job.bytes",
  "data_joblevel.bytes",
  "data_JobReward.bytes",
  "data_lifeSkill_AreaDrop.bytes",
  "data_lifeSkill_LifeLevel.bytes",
  "data_lifeSkill_LifeProduce.bytes",
  "data_lifeSkill_MineInfo.bytes",
  "data_lifeSkill_PlantInfo.bytes",
  "data_Mount.bytes",
  "data_mvpboss_MVP.bytes",
  "data_npc_NPC.bytes",
  "data_npc_NPCIntimacy.bytes",
  "data_Pendant.bytes",
  "data_pet_Pet.bytes",
  "data_pet_PetEvolution.bytes",
  "data_pet_PetCatchingRate.bytes",
  "data_pet_PetIntimacy.bytes",
  "data_pet_PetIntimacyItem.bytes",
  "data_pet_PetPotentiality.bytes",
  "data_pet_PetPotentialityRedistribute.bytes",
  "data_pet_PetSkill.bytes",
  "data_pet_PetSkillGroup.bytes",
  "data_pet_PetSkillTraining.bytes",
  "data_Prop.bytes",
  "data_PropCalculation.bytes",
  "data_skill_CommonSkill.bytes",
  "data_skill_Skill.bytes",
  "data_skill_SkillRes.bytes",
  "data_SkillFactor.bytes",
  "data_Trade_Trade.bytes",
  "data_scene_Scene.bytes",
  "data_pet_PetBaseAttr.bytes",
  "data_pet_PetDecoration.bytes",
  "data_pet_PetDecorationSet.bytes",
  "data_pet_PetInitEndowment.bytes",
]

for TARGET_FILE in TARGET_FILES:
  with open(f"{NEW_DIR}//{TARGET_FILE}", "r", encoding="utf8") as filename:
    data = []
    lines = filename.readlines()

    for i in range(len(lines)):
      data.append(lines[i])

  MAIN_DIFF_DIR = "../../update_changes"
  CHANGE_NEW_DIR = f"{MAIN_DIFF_DIR}/{REGION}/{NEW_DATE}/cleaned"

  if not os.path.isdir(CHANGE_NEW_DIR):
    os.mkdir(CHANGE_NEW_DIR)

  with open(f"{CHANGE_NEW_DIR}/{TARGET_FILE}", "w", encoding="utf8") as filename:
    filename.writelines(data[2:-1])