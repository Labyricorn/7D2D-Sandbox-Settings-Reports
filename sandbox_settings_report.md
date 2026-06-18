# 7 Days to Die - 3.0 'Sandbox Siege' Sandbox Settings

The `SandboxCode` is a serialized base-26 (A-Z) string (e.g., `AAAJABJACJADJARFBNC`) that represents the state of all sandbox settings. The first character is a format version header (currently `'A'`). The remainder of the string consists of 3-character blocks. In each block, the first two characters encode the 0-based option index (Enum ID) in base-26 (where AA=0, AB=1, etc.), and the third character encodes the selected value's index (0-based) from that option's allowed values array (mapped from `'A'` to `'Z'`).

This document details all **150** sandbox options available in the new Sandbox Siege update, grouped in their exact interface hierarchy and order. Use this reference to reconstruct the sandbox options menu in server management tools.

## Category: Player (General)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Ranged Damage | `RangedDamage` | **AA (0)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Melee Damage | `MeleeDamage` | **AB (1)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Block Damage | `BlockDamage` | **AC (2)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Terrain Damage | `TerrainDamage` | **AD (3)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Headshot Multiplier | `HeadshotMultiplier` | **AE (4)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Incoming Damage | `IncomingDamage` | **AR (17)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Walk Speed | `WalkSpeed` | **AG (6)** | Float | 1 | [ 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2, 3 ] | A: 0.25, B: 0.5, C: 0.6, D: 0.7, E: 0.8, F: 0.9, G: 1, H: 1.1, I: 1.2, J: 1.3, K: 1.4, L: 1.5, M: 2, N: 3 | Yes | - |
| Run Speed | `RunSpeed` | **AH (7)** | Float | 1 | [ 0, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.6, E: 0.7, F: 0.8, G: 0.9, H: 1, I: 1.1, J: 1.2, K: 1.3, L: 1.4, M: 1.5, N: 2, O: 3 | - | - |
| Crouch Speed | `CrouchSpeed` | **AF (5)** | Float | 1 | [ 0, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.6, E: 0.7, F: 0.8, G: 0.9, H: 1, I: 1.1, J: 1.2, K: 1.3, L: 1.4, M: 1.5, N: 2, O: 3 | - | - |
| Jump Height | `JumpStrength` | **AI (8)** | Float | 1 | [ 0, 0.5, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.5, C: 1, D: 1.25, E: 1.5, F: 2, G: 3 | - | - |
| Stamina Regen | `StaminaRegen` | **AK (10)** | Float | 1 | [ 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0.25, B: 0.5, C: 0.75, D: 1, E: 1.25, F: 1.5, G: 2, H: 3 | - | - |
| Stamina Usage | `StaminaUsage` | **AJ (9)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 1.75, I: 2 | - | Disables: [StaminaRegen] when value is 0 |
| XP Multiplier | `XPMultiplier` | **AS (18)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 3, 5 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 1.75, I: 2, J: 3, K: 5 | Yes | - |
| Show XP | `ShowXP` | **AT (19)** | Int | 0 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | - | - |
| Level Health/Stam Bonus | `PlayerLevelBonusApplied` | **AL (11)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Skill Gain Rate | `SkillGainRate` | **EM (116)** | Int | 1 | [ 1, 2, 3, 4, 5 ] | A: 1, B: 2, C: 3, D: 4, E: 5 | - | Disables: [SkillPointsPerLevel] when value is 0 |
| Skill Gain Amount | `SkillPointsPerLevel` | **EN (117)** | Int | 1 | [ 0, 1, 2, 3, 4, 5, 6, 7 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7 | - | - |
| Death Penalty | `DeathPenalty` | **BA (26)** | Int | 1 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | Yes | - |
| Lose Items Death Type | `LoseItemsOnDeathType` | **AW (22)** | Int | 0 | [ 0, 1, 2, 3, 4, 5 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5 | - | - |
| Lose Items Death Count | `LoseItemsOnDeathCount` | **AX (23)** | Int | 1 | [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] | A: 1, B: 2, C: 3, D: 4, E: 5, F: 6, G: 7, H: 8, I: 9, J: 10 | - | - |
| Degrade Items On Death | `DegradeItemsOnDeath` | **AY (24)** | Int | 0 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | - | - |
| Degrade Amount On Death | `DegradeAmountOnDeath` | **AZ (25)** | Float | 0.1 | [ 0, 0.05, 0.1, 0.15, 0.2, 0.25 ] | A: 0, B: 0.05, C: 0.1, D: 0.15, E: 0.2, F: 0.25 | - | - |
| Drop On Death | `DropOnDeath` | **BB (27)** | Int | 1 | [ 0, 1, 2, 3, 4 ] | A: 0, B: 1, C: 2, D: 3, E: 4 | - | - |
| Drop On Quit | `DropOnQuit` | **BC (28)** | Int | 0 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | - | - |
| Infection Rate | `InfectionRate` | **BD (29)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | Yes | - |
| Allow Newbie Coat | `NewbieCoat` | **AP (15)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Encumbrance Modifier | `EncumbranceModifier` | **AU (20)** | Float | 1 | [ 10, 1.35, 1, 0.7, 0.35, 0 ] | A: 10, B: 1.35, C: 1, D: 0.7, E: 0.35, F: 0 | - | - |
| Jar Refund | `JarRefund` | **AM (12)** | Float | 0.6 | [ 0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1 ] | A: 0, B: 0.05, C: 0.1, D: 0.2, E: 0.3, F: 0.4, G: 0.5, H: 0.6, I: 0.7, J: 0.8, K: 0.9, L: 1 | - | - |

## Category: Entities (Entities)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Enemy Spawn | `EnemySpawnMode` | **BE (30)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Max Enemy Type | `MaxEnemyTier` | **BR (43)** | Int | 5 | [ 0, 1, 2, 3, 4, 5 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5 | - | - |
| Biome Enemy Density | `BiomeEnemyDensity` | **BU (46)** | Int | 0 | [ 0, 1, 2, 3, 4, 5 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5 | - | - |
| Biome Enemy Respawn | `BiomeZombieRespawn` | **BS (44)** | Int | 0 | [ 0, 1, 2, 3, 4, 5 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5 | - | - |
| Biome Animal Respawn | `BiomeAnimalRespawn` | **BT (45)** | Int | 0 | [ 0, 1, 2, 3, 4, 5 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5 | - | - |
| Entity Damage | `EntityDamage` | **BF (31)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | Yes | - |
| Entity Incoming Damage | `EntityIncomingDamage` | **BQ (42)** | Float | 1 | [ 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0.25, B: 0.35, C: 0.5, D: 0.65, E: 0.75, F: 0.85, G: 1, H: 1.25, I: 1.5, J: 2, K: 2.5, L: 3 | - | - |
| Entity Block Damage | `BlockDamageAI` | **BG (32)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Blood Moon Block Damage | `BlockDamageAIBM` | **BH (33)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Headshot Mode | `HeadshotMode` | **AQ (16)** | Int | 0 | [ 0, 1, 2 ] | A: 0, B: 1, C: 2 | - | - |
| Entity Health Bars | `ShowHealthBars` | **AN (13)** | Bool | False | [ False, True ] | A: False, B: True | - | - |
| Show Entity Damage | `ShowEnemyDamage` | **AO (14)** | Bool | False | [ False, True ] | A: False, B: True | - | - |
| Zombie Day Speed | `ZombieMove` | **BI (34)** | Int | 0 | [ 0, 1, 2, 3, 4 ] | A: 0, B: 1, C: 2, D: 3, E: 4 | Yes | - |
| Zombie Night Speed | `ZombieMoveNight` | **BJ (35)** | Int | 3 | [ 0, 1, 2, 3, 4 ] | A: 0, B: 1, C: 2, D: 3, E: 4 | - | - |
| Zombie Feral Speed | `ZombieFeralMove` | **BK (36)** | Int | 3 | [ 0, 1, 2, 3, 4 ] | A: 0, B: 1, C: 2, D: 3, E: 4 | - | - |
| Zombie Blood Moon Speed | `ZombieBMMove` | **BL (37)** | Int | 3 | [ 0, 1, 2, 3, 4 ] | A: 0, B: 1, C: 2, D: 3, E: 4 | - | - |
| Zombie Feral Sense | `ZombieFeralSense` | **BM (38)** | Int | 0 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | Yes | - |
| Zombie AI Smell Mode | `AISmellMode` | **BN (39)** | Int | 3 | [ 0, 1, 2, 3, 4, 5 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5 | - | - |
| Zombie Rage Chance | `ZombieRageChance` | **BP (41)** | Float | 0.15 | [ 0, 0.15, 0.3, 0.35, 0.4, 0.5, 0.6, 0.75, 0.9, 1 ] | A: 0, B: 0.15, C: 0.3, D: 0.35, E: 0.4, F: 0.5, G: 0.6, H: 0.75, I: 0.9, J: 1 | - | - |
| Allow Zombie Digging | `AllowZombieDigging` | **BO (40)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Zombies Eat Animals | `ZombiesEatAnimals` | **BV (47)** | Bool | True | [ False, True ] | A: False, B: True | - | - |

## Category: World (World)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Global GameStage | `GlobalGSModifier` | **CI (60)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| Biome GameStage | `BiomeGSModifier` | **CJ (61)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| Biome Progression | `BiomeProgression` | **CD (55)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Temperature Survival | `TemperatureSurvival` | **CE (56)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Max Tech Type | `MaxTechType` | **CW (74)** | Int | 4 | [ 0, 1, 2, 3, 4 ] | A: 0, B: 1, C: 2, D: 3, E: 4 | - | - |
| Workstations in the Wild | `WorkstationsInTheWild` | **CV (73)** | Float | 0 | [ 0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1 ] | A: 0, B: 0.05, C: 0.1, D: 0.2, E: 0.3, F: 0.4, G: 0.5, H: 0.6, I: 0.7, J: 0.8, K: 0.9, L: 1 | - | - |
| Blood Moon Frequency | `BloodMoonFrequency` | **BW (48)** | Int | 7 | [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 30 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 8, J: 9, K: 10, L: 14, M: 20, N: 30 | Yes | Disables: [BloodMoonRange, BloodMoonEnemyCount, BloodMoonWarning] when value is 0 |
| Blood Moon Range | `BloodMoonRange` | **BX (49)** | Int | 0 | [ 0, 1, 2, 3, 4, 7, 10, 14, 20 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 7, G: 10, H: 14, I: 20 | - | - |
| Blood Moon Count | `BloodMoonEnemyCount` | **BZ (51)** | Int | 8 | [ 4, 6, 8, 10, 12, 16, 24, 32, 64 ] | A: 4, B: 6, C: 8, D: 10, E: 12, F: 16, G: 24, H: 32, I: 64 | - | - |
| Blood Moon Warning | `BloodMoonWarning` | **BY (50)** | Int | 1 | [ 0, 1, 2 ] | A: 0, B: 1, C: 2 | - | - |
| Air Drops | `AirDropFrequency` | **CA (52)** | Int | 3 | [ 0, 1, 2, 3, 4, 5, 6 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6 | - | Disables: [AirDropRandomTime, AirDropMarker] when value is 0 |
| Air Drop Random Time | `AirDropRandomTime` | **CC (54)** | Int | 0 | [ 0, 1, 2, 3, 4, 5, 6 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6 | - | - |
| Storm Frequency | `StormFreq` | **CF (57)** | Float | 1 | [ 0, 0.5, 1, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.5, C: 1, D: 1.5, E: 2, F: 3, G: 4, H: 5 | Yes | Disables: [StormWarning] when value is 0 |
| Storm Warning | `StormWarning` | **CG (58)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Heatmap Sensitivity | `HeatMapSensitivity` | **CH (59)** | Float | 1 | [ 0, 0.25, 0.5, 1, 1.5, 2 ] | A: 0, B: 0.25, C: 0.5, D: 1, E: 1.5, F: 2 | - | - |
| 24 Day Cycle | `DayNightLength` | **CO (66)** | Int | 60 | [ 10, 20, 30, 40, 50, 60, 90, 120 ] | A: 10, B: 20, C: 30, D: 40, E: 50, F: 60, G: 90, H: 120 | - | - |
| Day Light Length | `DayLightLength` | **CP (67)** | Int | 18 | [ 0, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24 ] | A: 0, B: 4, C: 6, D: 8, E: 10, F: 12, G: 14, H: 16, I: 18, J: 20, K: 24 | - | - |
| Mark Air Drops | `AirDropMarker` | **CB (53)** | Bool | True | [ False, True ] | A: False, B: True | Yes | - |
| Allow Map | `AllowMap` | **CQ (68)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Allow Compass | `AllowCompass` | **CR (69)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Allow Screen Markers | `AllowScreenMarkers` | **CS (70)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Show Location Info | `ShowLocationInfo` | **CT (71)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Show Day/Time | `ShowDayTime` | **CU (72)** | Bool | True | [ False, True ] | A: False, B: True | - | - |

## Category: Resources (Resources)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Loot Max Tier | `LootMaxTier` | **CZ (77)** | Int | 6 | [ 1, 2, 3, 4, 5, 6 ] | A: 1, B: 2, C: 3, D: 4, E: 5, F: 6 | - | - |
| Global LootStage | `GlobalLSModifier` | **CK (62)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| Biome LootStage | `BiomeLSModifier` | **CL (63)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| POI Tier LootStage | `POITierLSModifier` | **CM (64)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| Loot Respawn Days | `LootRespawnDays` | **CX (75)** | Int | 7 | [ -1, 5, 7, 10, 15, 20, 30, 40, 50 ] | A: -1, B: 5, C: 7, D: 10, E: 15, F: 20, G: 30, H: 40, I: 50 | Yes | - |
| Loot Time | `LootTimer` | **CY (76)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | - | - |
| Loot Bag Chance | `LootBagChance` | **DM (90)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Global Loot Abundance | `GlobalLootCount` | **DA (78)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | Yes | Disables: [FoodLootCount, DrinkLootCount, MedicalLootCount, AmmoLootCount, ResourceLootCount, ArmorLootCount, MeleeLootCount, RangedLootCount, DukesLootCount, CraftingMagazinesLootCount, TreasureMapChance] when value is 0 |
| Food Abundance | `FoodLootCount` | **DB (79)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Drink Abundance | `DrinkLootCount` | **DC (80)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Medical Abundance | `MedicalLootCount` | **DD (81)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Ammo Abundance | `AmmoLootCount` | **DE (82)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Resource Abundance | `ResourceLootCount` | **DF (83)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Armor Abundance | `ArmorLootCount` | **DG (84)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Melee Abundance | `MeleeLootCount` | **DH (85)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Ranged Abundance | `RangedLootCount` | **DI (86)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Dukes Abundance | `DukesLootCount` | **DJ (87)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Magazines Abundance | `CraftingMagazinesLootCount` | **DK (88)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Treasure Map Chance | `TreasureMapChance` | **DL (89)** | Float | 1 | [ 0, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.6, E: 0.7, F: 0.8, G: 0.9, H: 1, I: 1.1, J: 1.2, K: 1.3, L: 1.4, M: 1.5, N: 2, O: 3 | - | - |
| Mining Output | `MiningOutput` | **DX (101)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | Yes | - |
| Crop Output | `CropOutput` | **DN (91)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Seed Drop Output | `SeedDropOutput` | **DO (92)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Harvesting Output | `HarvestingOutput` | **DY (102)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 3, 4, 5 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 3, M: 4, N: 5 | - | - |
| Crop Growth | `CropGrowthSpeed` | **DP (93)** | Float | 1 | [ 1000, 0, 0.2, 0.5, 0.75, 1, 1.5, 2, 3 ] | A: 1000, B: 0, C: 0.2, D: 0.5, E: 0.75, F: 1, G: 1.5, H: 2, I: 3 | - | - |

## Category: Crafting (Crafting)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Crafting Progression | `CraftingProgression` | **DS (96)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Crafting Max Tier | `CraftingMaxTier` | **DW (100)** | Int | 6 | [ 1, 2, 3, 4, 5, 6 ] | A: 1, B: 2, C: 3, D: 4, E: 5, F: 6 | - | - |
| Magazine Points | `PointsPerMagazine` | **EL (115)** | Int | 1 | [ 0, 1, 2, 3, 4, 5, 6, 7 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7 | - | - |
| Backpack Crafting | `BackpackCrafting` | **DQ (94)** | Int | 1 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | - | - |
| Workstation Crafting | `WorkstationCrafting` | **DR (95)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Smelter Type | `SmeltingType` | **EA (104)** | Bool | False | [ False, True ] | A: False, B: True | - | - |
| Crafting Time | `CraftingTime` | **DT (97)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | - | - |
| Crafting Input | `CraftingInput` | **DU (98)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | - | - |
| Crafting Output | `CraftingOutput` | **DV (99)** | Float | 1 | [ 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0.25, B: 0.5, C: 0.75, D: 1, E: 1.25, F: 1.5, G: 2, H: 3 | - | - |
| Scrapping Output | `ScrappingOutput` | **DZ (103)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | - | - |
| Dew Collector Time | `DewCollectorTime` | **EB (105)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | Yes | - |
| Dew Collector Output | `DewCollectorOutput` | **EC (106)** | Float | 1 | [ 1, 2, 3, 4, 5 ] | A: 1, B: 2, C: 3, D: 4, E: 5 | - | - |
| Dew Collector Input | `DewCollectorInput` | **ED (107)** | Float | 1 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | - | - |
| Apiary Time | `ApiaryTime` | **EE (108)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 2, I: 3 | - | - |
| Apiary Output | `ApiaryOutput` | **EF (109)** | Float | 1 | [ 1, 2, 3, 4, 5 ] | A: 1, B: 2, C: 3, D: 4, E: 5 | - | - |
| Apiary Input | `ApiaryInput` | **EG (110)** | Float | 1 | [ 0, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2, 3 ] | A: 0, B: 0.2, C: 0.4, D: 0.6, E: 0.8, F: 1, G: 1.5, H: 2, I: 3 | - | - |
| Item Degradation | `ItemDegradation` | **AV (21)** | Float | 1 | [ 0, 0.25, 0.5, 1, 1.5, 2 ] | A: 0, B: 0.25, C: 0.5, D: 1, E: 1.5, F: 2 | Yes | - |
| Item Repair Types | `RepairTypes` | **EJ (113)** | Int | 3 | [ 0, 1, 2, 3 ] | A: 0, B: 1, C: 2, D: 3 | - | - |
| Max Degrade Amount | `MaxDegradationAmount` | **EK (114)** | Float | 0 | [ 0, 0.05, 0.1, 0.15, 0.2, 0.25 ] | A: 0, B: 0.05, C: 0.1, D: 0.15, E: 0.2, F: 0.25 | - | - |

## Category: Traders (Traders)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Trading Enabled | `TradersEnabled` | **EY (128)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Vending Machines Enabled | `VendingEnabled` | **EZ (129)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Trader Hours | `TraderHours` | **EX (127)** | Int | 0 | [ 0, 1, 2, 3, 4, 5, 6 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6 | - | - |
| Trader Protection | `TraderProtection` | **FC (132)** | Int | 0 | [ 0, 1, 2 ] | A: 0, B: 1, C: 2 | - | - |
| Trading Dialog | `TraderDialog` | **EW (126)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Global TraderStage | `GlobalTSModifier` | **CN (65)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | Yes | - |
| Trader Max Tier | `TraderMaxTier` | **FG (136)** | Int | 6 | [ 1, 2, 3, 4, 5, 6 ] | A: 1, B: 2, C: 3, D: 4, E: 5, F: 6 | - | - |
| Trader Item Abundance | `TraderItemAbundance` | **FE (134)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| Vending Item Abundance | `VendingItemAbundance` | **FI (138)** | Float | 1 | [ 0.25, 0.5, 1, 1.5, 2 ] | A: 0.25, B: 0.5, C: 1, D: 1.5, E: 2 | - | - |
| Trader Reset Interval | `TraderResetInterval` | **FD (133)** | Int | -1 | [ -1, 1, 2, 3, 4, 5, 6, 7, 14 ] | A: -1, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 14 | - | - |
| Vending Reset Interval | `VendingResetInterval` | **FH (137)** | Int | -1 | [ -1, 1, 2, 3, 4, 5, 6, 7, 14 ] | A: -1, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 14 | - | - |
| Traders Sell Price | `TraderSellPrices` | **FA (130)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 3, 4 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 1.75, I: 2, J: 3, K: 4 | - | - |
| Traders Buy Price | `TraderBuyPrices` | **FB (131)** | Float | 1 | [ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 3, 4 ] | A: 0, B: 0.25, C: 0.5, D: 0.75, E: 1, F: 1.25, G: 1.5, H: 1.75, I: 2, J: 3, K: 4 | - | - |
| Trader Buy Limit | `TraderBuyLimit` | **FF (135)** | Int | 3 | [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 8, J: 9, K: 10 | - | - |

## Category: Tasks (Tasks)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Challenges Enabled | `ChallengesEnabled` | **FJ (139)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Quests Enabled | `QuestsEnabled` | **EO (118)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Intro Challenges Enabled | `IntroChallengesEnabled` | **FK (140)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Intro Quest Enabled | `IntroQuestEnabled` | **EP (119)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Trader to Trader Quests | `TraderToTraderQuestsEnabled` | **EQ (120)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Buried Quests Enabled | `BuriedQuestsEnabled` | **EU (124)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| POI Quests Enabled | `POIQuestsEnabled` | **EV (125)** | Bool | True | [ False, True ] | A: False, B: True | - | - |
| Quests per Tier | `QuestsPerTier` | **ES (122)** | Int | 10 | [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 8, J: 9, K: 10, L: 11, M: 12, N: 13, O: 14, P: 15 | - | - |
| Quests per Day | `QuestProgressionDailyLimit` | **ET (123)** | Int | 4 | [ -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] | A: -1, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 8, J: 9, K: 10 | - | - |
| Starter Skill Points | `StarterSkillPoints` | **ER (121)** | Int | 4 | [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] | A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7, I: 8, J: 9, K: 10 | - | - |

## Category: Misc (Misc)

| Option Name | XML Property / Enum Name | Enum ID | Type | Default | Values / Range | Value Code Map | UI Section Start | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Vehicle Fuel Usage | `VehicleFuelUsage` | **FL (141)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Vehicle Entity Damage | `VehicleEntityDamage` | **FM (142)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Vehicle Block Damage | `VehicleBlockDamage` | **FN (143)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Vehicle Self Damage | `VehicleSelfDamage` | **FO (144)** | Float | 1 | [ 0, 0.25, 0.35, 0.5, 0.65, 0.75, 0.85, 1, 1.25, 1.5, 2, 2.5, 3 ] | A: 0, B: 0.25, C: 0.35, D: 0.5, E: 0.65, F: 0.75, G: 0.85, H: 1, I: 1.25, J: 1.5, K: 2, L: 2.5, M: 3 | - | - |
| Electrical Output | `ElectricalOutput` | **FP (145)** | Float | 1 | [ 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 3 ] | A: 0.25, B: 0.5, C: 0.75, D: 1, E: 1.25, F: 1.5, G: 2, H: 3 | Yes | - |
| Celebrate Kills | `SillyCelebrate` | **FQ (146)** | Int | 0 | [ 0, 1, 2 ] | A: 0, B: 1, C: 2 | Yes | - |
| Big Heads | `SillyBigHeads` | **FR (147)** | Bool | False | [ False, True ] | A: False, B: True | - | - |
| Tiny Zombies | `SillyTinyZombies` | **FS (148)** | Bool | False | [ False, True ] | A: False, B: True | - | - |
| Gravity | `SillyLowGravity` | **FU (150)** | Float | 1 | [ 0.5, 0.6, 0.7, 0.8, 0.9, 1 ] | A: 0.5, B: 0.6, C: 0.7, D: 0.8, E: 0.9, F: 1 | - | - |
| Silly Sounds | `SillySounds` | **FT (149)** | Bool | False | [ False, True ] | A: False, B: True | - | - |
| Black and White | `SillyBlackandWhite` | **FV (151)** | Bool | False | [ False, True ] | A: False, B: True | - | - |

