# 7 Days to Die - 3.0 'Sandbox Siege' Sandbox Presets

This document exposes the built-in **Sandbox Presets** extracted directly from the game's installation files (Unity Web Archive `7DaysToDie_Data/data.unity3d`). These presets configure the 150+ sandbox options automatically based on difficulty level or themed official playstyles.

For server administrators hosting dedicated servers, these presets can be applied directly using their corresponding `SandboxCode` values.

---

## Presets Reference Table

| Preset Name | Category | Difficulty | Sandbox Code | Default | Always Show Fields / Notes | Localized Key | Icon Resource |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- | :--- |
| **Scavenger** | Difficulty | 2/9 | `AAAKABKACKADKARDBNB` | - | - | `goDifficulty1` | `Data/Sandbox/icons/diff_scavenger` |
| **Adventurer** | Difficulty | 3/9 | `AAAJABJACJADJARFBNC` | Yes | - | `goDifficulty2` | `Data/Sandbox/icons/diff_adventurer` |
| **Nomad** | Difficulty | 4/9 | *Custom / Empty* | - | RangedDamage,MeleeDamage,BlockDamage,TerrainDamage,IncomingDamage,AISmellMode | `goDifficulty3` | `Data/Sandbox/icons/diff_nomad` |
| **Warrior** | Difficulty | 5/9 | `AAAGABGACGADGARJBND` | - | AISmellMode | `goDifficulty4` | `Data/Sandbox/icons/diff_warrior` |
| **True Survivalist** | Difficulty | 6/9 | `AAAEABEACEADEARKBNE` | - | AISmellMode | `goDifficulty5` | `Data/Sandbox/icons/diff_survivalist` |
| **Insane** | Difficulty | 7/9 | `AAADABDACDADDARLBNF` | - | AISmellMode | `goDifficulty6` | `Data/Sandbox/icons/diff_insane` |
| **Almost Creative** | Official | 1/9 | `ABEABTBBWADFN` | - | - | `xuiSandboxOfficialAlmostCreative` | `Data/Sandbox/icons/official_almostcreative` |
| **Chibi Mode** | Official | 3/9 | `AAAJABJACJADJAEIARFAGIAHJAFJAIEAKEAJDASGENDBAAAYBAZBBBABDCAUBAMJBUEBSEBTEAQBBIBBKEBLEBMBBNCCVHBZDCACCLDCMDCXBCYCDMJDAIDXIDNIDOIDYIDPGDTGEBGEEGAVCEXFCNDETFFLGFMJFOGFQCFRBFSBFUB` | - | - | `xuiSandboxOfficialAlmostChibiMode` | `Data/Sandbox/icons/official_chibimode` |
| **Dumpster Diver** | Official | 4/9 | `AAUABUCCVLCABCXBDMKDALDFJDKDDXADNADOADYBEABDVGDZFEXFFKA` | - | - | `xuiSandboxOfficialDumpsterDiver` | `Data/Sandbox/icons/official_dumpsterdiver` |
| **Legacy Survival** | Official | 4/9 | `AAHIAJDBACAPAAUAAMLBREBUEBSCBNCBPABOABVACDACVGCGACBACXBDDGDJIDNJDOJDSAELAEABEBGCNDFEDFIDFAFEOAFKAEPAEQA` | - | - | `xuiSandboxOfficialLegacySurvival` | `Data/Sandbox/icons/official_legacysurvival` |
| **Disaster Film** | Official | 5/9 | `AAXBAYDAZFBDFBVACFHDAKDDJDKFAVFEKFFOJ` | - | - | `xuiSandboxOfficialDisasterFilm` | `Data/Sandbox/icons/official_disasterfilm` |
| **Caveman Life** | Official | 6/9 | `AAADABJBTFCDACWBCAACQACRADNADOADWAEZAEWAFGAFKAFPA` | - | - | `xuiSandboxOfficialCavemanLife` | `Data/Sandbox/icons/official_cavemanlife` |
| **Dying World** | Official | 6/9 | `AAMABTBCAACXADMADOAEBAEJAFEAFIAFDIFHIFJAEOAEPA` | - | - | `xuiSandboxOfficialDyingWorld` | `Data/Sandbox/icons/official_dyingworld` |
| **Undead Matinee** | Official | 6/9 | `AAAFABIACGADGAEIARJAGHAHEAFIAKEAJCBACAWBAXBAYDAZDBDGAPAAMFBUEBSEBFKBQEAQCBJABKABLBBMBBNCBPJCIDCJDCVEBZFCAGCFECYDDBDDCDDDDDEBDGDDHJDIBDKFAVEEKDFDFFHF` | - | - | `xuiSandboxOfficialUndeadMatinee` | `Data/Sandbox/icons/official_undeadmatinee` |
| **Seven days Later** | Official | 7/9 | `AAAGABGACGADGARJBACAWFAXBAYDAPABUEBSEBICBJCBKCBLCBMCBPFBZFBYC` | - | - | `xuiSandboxOfficialSevendaysLater` | `Data/Sandbox/icons/official_sevendayslater` |
| **Madmoles Mayhem** | Official | 8/9 | `AAAGABGACGAPAAMIAWBAXCAZEBACBFIBGIBHIBIBBKEBLEBNFBUEBSECIDCJDBZFCVDDCDDDDDEDDFDDGDDJFEXF` | - | - | `xuiSandboxOfficialMadmolesMayhem` | `Data/Sandbox/icons/official_madmolesmayhem` |
| **Bite Club** | Official | 9/9 | `AAAGABGACGADGARJAHJBADBDGBIBBMCBNEBPFBZFCFDCXADADEYA` | - | - | `xuiSandboxOfficialBiteClub` | `Data/Sandbox/icons/official_biteclub` |

---

## Preset Categories & Descriptions

### 1. Difficulty Presets
These are the standard game difficulties that scale enemy strength, player damage, and game progression parameters.
*   **Scavenger** (Difficulty 2): A relaxed entry-level sandbox configuration for players focusing on building and crafting.
*   **Adventurer** (Difficulty 3): The default experience with moderate combat challenges.
*   **Nomad** (Difficulty 4): Balanced settings. This preset is characterized by having an empty `SandboxCode` as it uses the base defaults of the game engine while forcing certain options (like damage multipliers) to always be visible in the UI.
*   **Warrior** (Difficulty 5): A tougher survival setup with increased entity threat levels.
*   **True Survivalist** (Difficulty 6): Highly demanding settings for veterans, requiring careful planning and resource management.
*   **Insane** (Difficulty 7): Extremely punishing combat mechanics and minimal player advantages.

### 2. Official (Themed) Presets
These presets represent unique developer-curated scenarios, custom modes, and experimental playstyles.
*   **Almost Creative** (Difficulty 1): Near-sandbox mode with maximum player damage and minimal threats, similar to creative mode but maintaining survival mechanics.
*   **Chibi Mode** (Difficulty 3): Modifies various scaling values for a playful experience.
*   **Dumpster Diver** (Difficulty 4): Focuses on maximum loot and scavenger mechanics.
*   **Legacy Survival** (Difficulty 4): Re-creates classic settings from earlier Alpha versions of the game.
*   **Disaster Film** (Difficulty 5): Themed to simulate a movie-like apocalypse.
*   **Caveman Life** (Difficulty 6): Restricts high-tech items, forcing primitive survival techniques.
*   **Dying World** (Difficulty 6): Punishing environmental conditions and resource scarcity.
*   **Undead Matinee** (Difficulty 6): Increases zombie presence and movie-apocalypse rules.
*   **Seven days Later** (Difficulty 7): Fast-paced progression and combat scaling culminating in massive Blood Moons.
*   **Madmole's Mayhem** (Difficulty 8): The personal favorite challenge preset of lead developer Madmole.
*   **Bite Club** (Difficulty 9): The absolute highest official difficulty setup with maximum feral presence and minimal player margins.

---

## Sandbox Code Serialization Note
As detailed in the main [Sandbox Settings Report](file:///C:/Users/cgcha/.gemini/antigravity/brain/a1c37c6c-8637-4b28-8389-177ee8c0d5f8/sandbox_settings_report.md), the `SandboxCode` string (e.g., `AAAKABKACKADKARDBNB`) is a base-26 (A-Z) representation of non-default options. 

*   **Format Header**: Every code starts with a version header character (currently `'A'`).
*   **3-Character Blocks**: The rest of the code consists of 3-character blocks (e.g. `AAK`).
    *   **Characters 1 & 2** (e.g. `AA`): The Enum ID of the option encoded in base-26 (where `AA` is 0, `AB` is 1, `BA` is 26, etc.).
    *   **Character 3** (e.g. `K`): The index of the selected value from that option's allowed value array (mapped from `'A'` to `'Z'`).
*   **Defaults Omission**: Settings that remain at their default values are omitted from the code to compress string length. This is why the **Nomad** preset code is empty (as it represents all settings at defaults).
