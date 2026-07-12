# Discord Banner Sticker Splitter

A minimalist desktop utility that splits any image into six 320x320 PNG tiles optimized for Discord bio banners.

Unlike manual image cropping tools, this utility automatically resizes, center-crops, and slices your image into exactly 6 parts, exporting them with optimized names (`1.png` to `6.png`) to ensure the shortest possible character length in your Discord bio.

[![Discord Banner Sticker Splitter Demo](https://github.com/user-attachments/assets/1f818b4b-b4a1-4b7c-a514-83cd8c9a29e1)](https://youtu.be/_gRKmXKPrsU)

---

## Features

* **Real-time 3x2 Grid Preview:** Instantly previews how your banner will be divided into the 6 sticker slots.
* **Smart Auto-Resizing:** Automatically scales and center-crops images of any dimension to fit the optimal 960x640 size.
* **Optimized Naming Scheme:** Saves files directly as `1.png` through `6.png` to keep the custom emoji references in your bio under the 190-character limit.
* **Clean Premium UI:** A gorgeous, distraction-free dark-theme interface built with CustomTkinter.
* **Native Drag & Drop:** Easily drop images directly into the application window.

---

## Prerequisites

1. **Python 3.x** installed on your system.
2. **PIP** (Python package installer).

---

## Installation

### 1. Clone or Download the Files

Clone the repository or download the source files to a folder on your computer.

### 2. Install Dependencies

Install the required Python libraries using the command line:

* **Windows (PowerShell / Command Prompt):**
  ```powershell
  pip install -r requirements.txt
  ```

---

## Configuration & Usage

1. Launch the application:
   ```bash
   python main.py
   ```
2. Drag and drop any image file onto the dashed drop panel, or click the panel to browse your computer.
3. The app will instantly crop the image to 960x640 and split it into 6 previews in a 3x2 grid.
4. Click on **Export Stickers** at the bottom, select a folder, and your stickers will be saved.
5. The export folder will automatically open when completed.

---

## Discord Bio Layout Guide

> [!WARNING]
> Free Discord servers only offer 5 sticker slots. To upload all 6 banner stickers, your server needs to be boosted to Tier 1 (15 slots), or you must upload them to different servers.

1. Upload the exported files `1.png` through `6.png` as custom stickers to a server where you have manage sticker permissions.
2. Go to your **Discord User Settings** > **Profiles** > **About Me (Bio)**.
3. Copy/paste the sticker emojis in the correct layout (3 per line, without spaces):
   ```text
   :1::2::3:
   :4::5::6:
   ```
4. Click save, and your profile bio will display the custom banner.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
