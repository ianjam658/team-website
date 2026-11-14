# Team Website Assignment — Work Log

## Repository

- **GitHub repository:** [ianjam658/team-website](https://github.com/ianjam658/team-website)
- **Default branch:** `main`
- **Website source folder:** `team-website/`

## What the repository contains

The website is organized into HTML pages, CSS styling, and JavaScript behavior:

```text
team-website/
├── index.html
├── projects.html
├── contact.html
├── css/
│   └── styles.css
└── js/
    └── script.js
```

The repository also includes `create_zip.py`, which creates a ZIP of the project, and this work-log document.

## What we did

1. Created the `team-website` GitHub repository.
2. Added the website files to the repository: the home, projects, and contact pages, stylesheet, and JavaScript file.
3. Added a Python helper to package the repository files into a ZIP archive.
4. Added this document describing the project and the terminal commands for working with it.

## Working with the repository from a terminal

The following commands show how to download the project, create the ZIP, and send any changes back to GitHub. They are instructions for reproducing the workflow; run them in a terminal with Git and Python 3 installed.

### Clone the repository

```bash
git clone https://github.com/ianjam658/team-website.git
cd team-website
```

### Create the ZIP archive

```bash
python3 create_zip.py
```

On Windows, if `python3` is not recognized, try:

```powershell
py create_zip.py
```

The script creates `team-website.zip` in the repository's top-level folder. It includes the project and documentation, but excludes Git's internal `.git` directory and the generated archive itself.

### Save and upload edits

After editing or adding files, use these commands from the repository folder:

```bash
git status
git add .
git commit -m "Update team website"
git push origin main
```

`git status` lets you review the changes before staging them. The commit command records the changes locally, and `git push` uploads them to GitHub. GitHub may ask you to authenticate.

## Downloading a ZIP from GitHub

GitHub also provides a ZIP of the committed source: open the repository page, choose **Code**, then **Download ZIP**. The terminal script above is useful when you want to make a fresh ZIP after local changes.
