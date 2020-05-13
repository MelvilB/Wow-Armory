
WowArmory = { }

function WowArmory:SoftTry()
    message("Hello World!");
end

function WowArmory:HardTry()
  local equipment = {};
  local equipment_icon = {};
  local invBags = {};
  local invBags_icon = {};
  local guildName = "";
  for i=1,19 do
    print(GetInventoryItemID("player",i));
    local ok = GetInventoryItemID("player",i);
    if(ok == nil) then
      print("Emplacement vide");
      print(i);
      table.insert(equipment, -1);
      table.insert(equipment_icon, -1);
    else
      print(ok);
      table.insert(equipment, ok);
      table.insert(equipment_icon, GetItemIcon(ok));
    end
  end
  print("affichage de la table");
  for i=1,19 do
      print(equipment_icon[i]);
  end
  print("======================== PASSAGE AUX SACS ============================")
  table.insert(invBags, "backpack");
  table.insert(invBags_icon, "backpack");
  a = 2;
  for j=0,4 do
      taille = GetContainerNumSlots(j);
      if (j ~= 0 and j ~= 4) then
          sacID = GetInventoryItemID("player", 20+j-1);
          table.insert(invBags, sacID);
          table.insert(invBags_icon, GetItemIcon(sacID));
      end
      table.insert(invBags, {});
      table.insert(invBags_icon, {});
      print(taille);
      if (taille ~= 0) then
          print("début de la boucle")
          for k=1,taille do
              itemID = GetContainerItemID(j,k);
              if (itemID == nil) then
                  print("Emplacement vide")
              else
                  print(itemID)
                  table.insert(invBags[j+a], itemID)
                  table.insert(invBags_icon[j+a], GetItemIcon(itemID))
              end
          end
          a = a+1;
      end
  end
  guildName = GetGuildInfo("player");
  if (guildName ~= nil) then
      guildName = GetGuildInfo("player");
  else
      guildName = "";
  end
  print("oui")
  print(guildName)

  local player = {
	  name = UnitName("player"),
	  level = UnitLevel("player"),
	  className, classFilename, classID = UnitClass("player"),
	  englishFaction, localizedFaction = UnitFactionGroup("player"),
	  maxHealth = UnitHealthMax("player"),
	  raceName, raceFile, raceID = UnitRace("player"),
	  gender = UnitSex("player"),
	  currently_equipped = equipment,
      strength = UnitStat("player", 1),
      agility = UnitStat("player", 2),
      stamina = UnitStat("player", 3),
      intellect = UnitStat("player", 4),
      spirit = UnitStat("player", 5),
	  baseArmor , effectiveArmor, armor, posBuffArmor, negBuffArmor = UnitArmor("player"), -- armor takes in account kits and enchantments, effectiveArmor takes in account buffs
	  critChance = GetCritChance("player"),
	  blockChance = GetBlockChance("player"),
	  dodgeChance = GetDodgeChance("player"),
	  parryChance = GetParryChance("player"),
      basePower = UnitAttackPower("player"),
      lowDmg = UnitDamage("player"),
	  haste = UnitAttackSpeed("player"),
	  maxpower = UnitPowerMax("player"), --powerTypes are Mana/Rage/Energy...
      currently_equipped_icon = equipment_icon,
      bags = invBags,
      bags_icon = invBags_icon,
      guild = guildName,
	  realmName = GetRealmName(),
  }
  savedplayer=player;
  print("addon done");
end

local frame, events = CreateFrame("Frame"), {};
function events:PLAYER_ENTERING_WORLD()
    WowArmory:HardTry();
end
function events:PLAYER_EQUIPMENT_CHANGED()
    WowArmory:HardTry();
end

frame:SetScript("OnEvent", function(self, event)
    events[event](self); -- call one of the functions above
    end);
for k, v in pairs(events) do
    frame:RegisterEvent(k); -- Register all events for which handlers have been defined
end

--[[
INVSLOT_AMMO = 0
INVSLOT_HEAD = 1
INVSLOT_NECK = 2
INVSLOT_SHOULDER = 3
INVSLOT_BODY = 4 (shirt)
INVSLOT_CHEST = 5
INVSLOT_WAIST = 6
INVSLOT_LEGS = 7
INVSLOT_FEET = 8
INVSLOT_WRIST = 9
INVSLOT_HAND = 10
INVSLOT_FINGER1 = 11
INVSLOT_FINGER2 = 12
INVSLOT_TRINKET1 = 13
INVSLOT_TRINKET2 = 14
INVSLOT_BACK = 15
INVSLOT_MAINHAND = 16
INVSLOT_OFFHAND = 17
INVSLOT_RANGED = 18
INVSLOT_TABARD = 19
CONTAINER_BAG_OFFSET+1 = 20 (first bag, the rightmost one)
CONTAINER_BAG_OFFSET+2 = 21 (second bag)
CONTAINER_BAG_OFFSET+3 = 22 (third bag)
CONTAINER_BAG_OFFSET+4 = 23 (fourth bag, the leftmost one)
]]--
