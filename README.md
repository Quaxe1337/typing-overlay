# 🧑‍💻 Typing Character Overlay — Standalone Windows EXE

Follow these steps exactly and you'll have a double-clickable
`TypingOverlay.exe` with **zero software to install on your PC**.

---

## What you need

- A free GitHub account → https://github.com/signup
- A browser — that's it.

---

## Step 1 — Create a new GitHub repository

1. Log in to https://github.com
2. Click the **+** icon (top-right) → **New repository**
3. Name it: `typing-overlay`
4. Leave it **Public** (required for free Actions minutes)
5. Click **Create repository**

---

## Step 2 — Upload the files

You need to upload these files in the right folder structure:

```
typing-overlay/
├── overlay.py
├── overlay.spec
└── .github/
    └── workflows/
        └── build.yml
```

### Upload overlay.py and overlay.spec

1. On your new repo page, click **"uploading an existing file"** (or "Add file" → "Upload files")
2. Drag and drop `overlay.py` and `overlay.spec`
3. Scroll down, click **Commit changes**

### Upload build.yml (needs to go in a subfolder)

GitHub doesn't let you create folders via drag-and-drop, so do this:

1. Click **Add file** → **Create new file**
2. In the filename box type exactly:
   ```
   .github/workflows/build.yml
   ```
   (typing the `/` characters will automatically create the folders)
3. Open the `build.yml` file you downloaded, copy all its contents
4. Paste into the editor on GitHub
5. Click **Commit changes**

---

## Step 3 — Watch it build

1. Click the **Actions** tab at the top of your repo
2. You should see a workflow run called **"Build Windows EXE"** already running
3. Click on it to watch the live build log
4. It takes about **2–3 minutes**
5. When it shows a green ✅ checkmark — it's done!

> If you don't see it running automatically, click **"Build Windows EXE"**
> on the left → click **"Run workflow"** → **"Run workflow"** (green button)

---

## Step 4 — Download your EXE

1. Click on the completed workflow run (green ✅)
2. Scroll down to the **Artifacts** section at the bottom
3. Click **TypingOverlay-Windows** to download a zip file
4. Unzip it — inside is `TypingOverlay.exe`
5. **Double-click it** — no installation needed!

---

## Using the overlay

| Action | How |
|---|---|
| Move it | Left-click and drag the character |
| Resize / Quit | Right-click the character |

The character reacts to every key you type:

| Key | Reaction |
|---|---|
| Any letter/number | 🧑‍💻 ↔ ⌨️ typing animation |
| Spacebar | 🕺 dance |
| Enter | 🙌 celebration |
| Backspace | 😬 cringe |
| Escape | 😱 shock |

---

## Troubleshooting

**Windows Defender warns about the EXE**
This is normal for unsigned apps built by individuals.
Click **"More info"** → **"Run anyway"** to proceed.

**The overlay doesn't react to keys**
Right-click → try running the EXE as Administrator.

**Actions tab shows a red ✗**
Click the failed run → click the failed step to see the error log,
then feel free to share it here for help.
