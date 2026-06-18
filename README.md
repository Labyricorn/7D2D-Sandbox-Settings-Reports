# 7 Days to Die - 3.0 'Sandbox Siege' Specifications

This repository contains reverse-engineered technical specifications and configuration details for the **Sandbox Options** introduced in the 3.0 "Sandbox Siege" update of *7 Days to Die*. 

These resources are compiled with the intent to aid developers building server management applications, web-based control panels, and automated game configuration utilities for dedicated servers.

---

## Web-based Configurator Tool

An interactive companion tool is available online at:
👉 **[7 Days to Die Sandbox Options Configurator](https://labyricorn.github.io/7D2D-Sandbox-Settings-Reports)**

### Key Features & Usage

*   **Interactive UI:** Configure all 150+ sandbox options directly inside a responsive, themed web interface mimicking the game's menu style.
*   **Real-time SandboxCode Generation:** As you tweak options, the corresponding compact `SandboxCode` is generated dynamically and shown in the sidebar.
*   **Paste & Import:** You can click **Paste Code** to input any existing `SandboxCode` and instantly load its settings into the visual configurator.
*   **Server Config XML:** Generate the exact `<property name="SandboxCode" value="..." />` line ready to be copied and pasted directly into your server's `serverconfig.xml` file.
*   **Copy Web Link:** Click **Copy Web Link** in the footer to copy a shareable link of your active configuration directly to your clipboard.

### URL Code Sharing (`/?code=`)

The configurator supports loading settings directly from the URL query string using the `?code=` parameter. 

For example, loading the URL:
```url
https://labyricorn.github.io/7D2D-Sandbox-Settings-Reports/?code=AAAKABKACKADKARDBNB
```
will automatically open the configurator and import the settings defined by that sandbox code (in this case, the **Scavenger** difficulty preset). 

As you configure settings, the web browser's URL is dynamically updated with the active code. You can copy the browser URL or click the **Copy Web Link** button to easily share your custom setups with players or server admins.

---

## Repository Contents

*   **[Sandbox Settings Report (sandbox_settings_report.md)](sandbox_settings_report.md)**: A complete reference table documenting all **150 sandbox options** grouped by their interface categories (Player, Entities, World, Resources, Progression, and Claim). It exposes:
    *   XML property / Enum names
    *   Assigned Enum IDs (0 to 149)
    *   Allowed values, ranges, and default values
    *   Value-to-Character mapping for `SandboxCode` serialization
    *   Option dependency relationships (e.g. options disabled when a parent option is `0` or `False`)
*   **[Sandbox Presets Report (sandbox-presets-report.md)](sandbox-presets-report.md)**: Details the **17 built-in game presets** (6 standard Difficulty presets and 11 themed Official developer presets). It maps:
    *   Preset categories and difficulty ratings (from 1/9 to 9/9)
    *   The exact preset `SandboxCode` strings (e.g., `AAAKABKACKADKARDBNB` for Scavenger)
    *   Localized string keys and UI icon resource paths
    *   Preset-specific behaviors (such as options that are forced to always be visible in the user interface)

---

## Technical Overview: The Sandbox Code

In *7 Days to Die* (3.0), the entire state of the sandbox menu is serialized into a compact, human-readable string called the `SandboxCode` (e.g., `AAAJABJACJADJARFBNC`). This encoding allows complex server configurations to be shared as a single code block.

### Encoding Mechanics
1.  **Format Version Header**: The first character is a version identifier (currently `'A'`).
2.  **Option Blocks**: The remainder of the string consists of 3-character blocks (e.g., `AAJ`, `ARF`):
    *   **Characters 1 & 2 (Enum ID)**: A 2-character base-26 representation (using letters `A-Z` where `AA` = 0, `AB` = 1, `BA` = 26, `BB` = 27, etc.) representing the option's index in the global sandbox options array.
    *   **Character 3 (Value Index)**: A single-character index mapped to the chosen value's position in that option's allowed values array (where `'A'` = index 0, `'B'` = index 1, `'C'` = index 2, etc.).
3.  **Omission of Defaults**: To keep the serialization string compact, any options set to their engine-level default values are completely omitted from the code. For example, the **Nomad** preset (which leaves all options at default) produces an empty code (`""` or just the header `"A"`).

---

## Extraction Methodology

The data contained in these reports was extracted directly from the game's compiled asset files:
*   The raw preset structures and parameters are loaded by `SandboxOptionManager::LoadInternalPresets` from the compiled `TextAsset` located at `Data/Sandbox/sandbox_presets`.
*   This asset was retrieved by parsing the `UnityFS` version 8 file structure of `7DaysToDie_Data/data.unity3d`. Individual 128KB blocks (specifically Blocks 310–320) were decompressed using raw LZ4 block decompression starting from an aligned physical offset of `7520`.

*Disclaimer: This is a purely academic project of technical exploration and reverse engineering. All properties, asset names, and game titles are trademarks of The Fun Pimps.*
