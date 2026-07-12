# Discord Banner Emoji Splitter

A minimalist desktop utility that splits any image into six 320x320 PNG tiles optimized for Discord bio banners.

Unlike manual image cropping tools, this utility automatically resizes, center-crops, and slices your image into exactly 6 parts, exporting them with optimized names (`1.png` to `6.png`) to ensure the shortest possible character length in your Discord bio.

[![Discord Banner Emoji Splitter Demo](https://github.com/user-attachments/assets/8ac7d125-66cd-4238-a357-d07a306ca032)](https://youtu.be/Lc59zoeqCGc)

---

## Features

* **Real-time 3x2 Grid Preview:** Instantly previews how your banner will be divided into the 6 emoji slots.
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
4. Click on **Export Emojis** at the bottom, select a folder, and your emojis will be saved.
5. The export folder will automatically open when completed.

---

## Discord Bio Layout Guide

> [!NOTE]
> Standard Discord servers (without any boosts) allow up to 50 custom emojis for free. Since this banner only requires 6 emoji slots, you do not need to boost your server!

1. Upload the exported files `1.png` through `6.png` as custom emojis to a server where you have **Manage Emojis** permissions (Server Settings > Emoji > Upload Emoji).
2. Go to your **Discord User Settings** > **Profiles** > **About Me (Bio)**.
3. Add the custom emojis from your server selector in the correct grid layout (3 per line, without spaces):
   ```text
   :1::2::3:
   :4::5::6:
   ```
   *(Pro-tip: Hold Shift + Enter to create a line break).*

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

